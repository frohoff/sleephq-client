from __future__ import annotations

from pathlib import Path
from typing import Any, Iterable
import hashlib
import time
from functools import partial

import typer

from sleephq.api.import_files import post_v1_imports_import_id_files
from sleephq.api.imports import (
    get_v1_imports_id,
    get_v1_teams_team_id_imports,
    post_v1_imports_id_process_files,
    post_v1_teams_team_id_imports,
)
from sleephq.models.post_v1_imports_import_id_files_body import PostV1ImportsImportIdFilesBody
from sleephq.models.post_v1_teams_team_id_imports_body import PostV1TeamsTeamIdImportsBody
from sleephq.types import File, UNSET

from .. import output, session
from ..options import (
    ALL_OPTION,
    CONTEXT_SETTINGS,
    LIMIT_OPTION,
    PAGE_OPTION,
    PAGE_SIZE_OPTION,
    TEAM_ID_OPTION,
    TEAM_NAME_OPTION,
    WATCH_FLAG,
    WATCH_INTERVAL_OPTION,
)
from ..output import OutputFormat
from ..pagination import (
    call_with_backoff,
    collect_paginated,
    print_pagination_hint,
    resolve_pagination_options,
)
from ..resolvers import resolve_team_id
from ..utils import coerce_int, parse_fields, usage_error

app = typer.Typer(help="Import utilities", no_args_is_help=True, context_settings=CONTEXT_SETTINGS)

DEFAULT_PAGE_SIZE = 25


def _import_row(item: object) -> dict[str, object | None]:
    data = output.serialize(item)
    attributes = data.get("attributes") or {}
    return {
        "id": str(data.get("id")),
        "name": attributes.get("name"),
        "status": attributes.get("status"),
        "progress": attributes.get("progress"),
        "machine_id": attributes.get("machine_id"),
    }


def _fetch_import_payload(client: Any, import_id: int) -> dict[str, Any]:
    response = call_with_backoff(
        lambda: get_v1_imports_id.sync_detailed(client=client, id=import_id)
    )
    parsed = response.parsed
    if parsed is None:
        typer.echo("Import not found", err=True)
        raise typer.Exit(code=1)
    return output.serialize(parsed)


def _watch_import_status(
    client: Any,
    import_id: int,
    watch_interval: float,
) -> dict[str, Any]:
    if watch_interval <= 0:
        usage_error("--watch-interval must be positive seconds")

    typer.echo(
        f"Watching import {import_id} (poll every {watch_interval}s)...",
        err=True,
    )
    seen_statuses: set[str | None] = set()
    while True:
        payload = _fetch_import_payload(client, import_id)
        data = payload.get("data") or {}
        attrs = data.get("attributes") or {}
        status = attrs.get("status")
        if status not in seen_statuses:
            typer.echo(f"Status: {status}", err=True)
            seen_statuses.add(status)
        if status in {"complete", "failed", "error"}:
            return payload
        time.sleep(watch_interval)


def _normalize_base_path(base_path: str) -> str:
    value = base_path.strip()
    if not value or value == ".":
        value = "./"
    if value.startswith("/"):
        raise typer.BadParameter("--base-path must be relative (e.g. ./ or ./DATALOG/)")
    if not value.startswith("./"):
        value = "./" + value.lstrip("./")
    if not value.endswith("/"):
        value += "/"
    return value


def _append_relative_path(base_path: str, relative: Path) -> str:
    base = _normalize_base_path(base_path)
    if str(relative) in (".", ""):
        return base
    rel = relative.as_posix().strip("/")
    if not rel:
        return base
    return f"{base}{rel}/"


def _calculate_content_hash(path: Path, name: str) -> str:
    hasher = hashlib.md5()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8192), b""):
            hasher.update(chunk)
    hasher.update(name.encode("utf-8"))
    return hasher.hexdigest()


def _collect_upload_entries(
    *,
    source_root: Path | None,
    include_paths: list[Path],
    base_path: str,
) -> list[tuple[Path, str, str]]:
    normalized_base = _normalize_base_path(base_path)
    relative_files: list[tuple[Path, Path]] = []

    if source_root is not None:
        resolved_source = source_root.resolve()
        if resolved_source.is_dir():
            relative_files = _collect_from_directory(
                root=resolved_source,
                include_paths=include_paths,
                include_entire_root_when_empty=True,
                context="--files",
            )
        elif resolved_source.is_file():
            if resolved_source.suffix.lower() != ".zip":
                raise typer.BadParameter("--files must be a directory or a .zip archive")
            relative_files = _collect_from_single_file(
                file_path=resolved_source,
                include_paths=include_paths,
                context="--files",
            )
        else:
            raise typer.BadParameter(f"--files path not accessible: {source_root}")
    else:
        include_paths = include_paths or []
        if not include_paths:
            usage_error("Provide --files or at least one PATH argument")
        cwd = Path.cwd().resolve()
        relative_files = _collect_from_directory(
            root=cwd,
            include_paths=include_paths,
            include_entire_root_when_empty=False,
            context="current directory",
        )

    if not relative_files:
        return []

    entries: list[tuple[Path, str, str]] = []
    for absolute_path, relative_path in relative_files:
        parent = relative_path.parent
        remote_path = _append_relative_path(normalized_base, parent)
        entries.append((absolute_path, remote_path, relative_path.name))
    return entries


def _collect_from_directory(
    *,
    root: Path,
    include_paths: Iterable[Path] | None,
    include_entire_root_when_empty: bool,
    context: str,
) -> list[tuple[Path, Path]]:
    filters = list(include_paths or [])
    targets: list[Path] = []

    if not filters:
        if include_entire_root_when_empty:
            targets = [root]
        else:
            return []
    else:
        for filter_path in filters:
            target = _resolve_relative_target(root=root, relative_path=filter_path, context=context)
            targets.append(target)

    files: list[tuple[Path, Path]] = []
    seen: set[str] = set()
    for target in targets:
        if target.is_dir():
            for path in sorted(target.rglob("*")):
                if path.is_file():
                    relative = path.relative_to(root)
                    key = relative.as_posix()
                    if key not in seen:
                        seen.add(key)
                        files.append((path, relative))
        elif target.is_file():
            relative = target.relative_to(root)
            key = relative.as_posix()
            if key not in seen:
                seen.add(key)
                files.append((target, relative))
        else:
            raise typer.BadParameter(f"Path not found relative to {context}: {target}")

    if not files:
        raise typer.BadParameter("No files found for the provided paths")
    return files


def _collect_from_single_file(
    *,
    file_path: Path,
    include_paths: Iterable[Path] | None,
    context: str,
) -> list[tuple[Path, Path]]:
    filters = [path for path in (include_paths or []) if str(path) not in ("", ".")]
    if filters:
        allowed = {file_path.name}
        normalized = {filter_path.name for filter_path in filters}
        invalid = normalized - allowed
        if invalid:
            bad = ", ".join(sorted(invalid))
            raise typer.BadParameter(
                f"Path(s) {bad} do not exist within {context} source {file_path}"
            )
    return [(file_path, Path(file_path.name))]


def _resolve_relative_target(*, root: Path, relative_path: Path, context: str) -> Path:
    raw = Path(relative_path)
    candidates: list[Path] = []

    if raw.is_absolute():
        candidates.append(raw)
    else:
        candidates.append(root / raw)
        candidates.append(Path.cwd() / raw)

    tried: list[str] = []
    for candidate in candidates:
        resolved = candidate.resolve()
        key = str(resolved)
        if key in tried:
            continue
        tried.append(key)

        try:
            resolved.relative_to(root)
        except ValueError:
            continue

        if resolved.exists():
            return resolved

    raise typer.BadParameter(f"Path not found within {context}: {relative_path}")


def _confirm_upload(entries: list[tuple[Path, str, str]], assume_yes: bool) -> None:
    if assume_yes:
        return

    _echo_upload_entries(entries, title="Files to upload")

    if not typer.confirm("Proceed with upload?", default=True):
        typer.echo("Upload cancelled", err=True)
        raise typer.Exit(code=1)


def _echo_upload_entries(entries: Iterable[tuple[Path, str, str]], title: str) -> None:
    typer.echo(title)
    for local_path, remote_path, remote_name in entries:
        typer.echo(f" - {_format_upload_entry(local_path, remote_path, remote_name)}")


def _format_upload_entry(local_path: Path, remote_path: str, remote_name: str) -> str:
    return f"{local_path} -> {remote_path}{remote_name}"

@app.command("list")
def list_imports(
    team_id: str | None = TEAM_ID_OPTION,
    team_name: str | None = TEAM_NAME_OPTION,
    page: int = PAGE_OPTION,
    page_size: int | None = PAGE_SIZE_OPTION,
    limit: int | None = LIMIT_OPTION,
    fetch_all: bool = ALL_OPTION,
    format: OutputFormat = typer.Option(OutputFormat.TABLE, "--format", case_sensitive=False, help="Output format"),
    fields: str = typer.Option(
        "id,name,status,progress",
        help="Comma separated list of columns to include in table output",
    ),
) -> None:
    """List imports for a team."""

    client, config, config_path = session.get_authenticated_client()
    resolved_team_id = resolve_team_id(
        client=client,
        config=config,
        config_path=config_path,
        team_id=team_id,
        team_name=team_name,
    )
    options = resolve_pagination_options(
        page=page,
        page_size=page_size,
        default_page_size=DEFAULT_PAGE_SIZE,
        limit=limit,
        fetch_all=fetch_all,
    )

    fetcher = partial(
        get_v1_teams_team_id_imports.sync_detailed,
        client=client,
        team_id=resolved_team_id,
    )
    result = collect_paginated(fetcher, options=options)

    rows = []
    if result.items:
        rows = [_import_row(item) for item in result.items]

    if not rows:
        typer.echo("No imports found")
        return

    output.echo_list(rows, format=format, columns=parse_fields(fields), title="Imports")
    print_pagination_hint(options, result)


@app.command("show")
def show_import(
    import_id: str = typer.Argument(..., help="Import ID"),
    format: OutputFormat = typer.Option(OutputFormat.TABLE, "--format", case_sensitive=False, help="Output format"),
    watch: bool = WATCH_FLAG,
    watch_interval: float = WATCH_INTERVAL_OPTION,
) -> None:
    """Display details for a specific import (optionally waiting for completion)."""

    client, _, _ = session.get_authenticated_client()
    import_id_int = coerce_int(import_id, "import_id")
    if not watch:
        payload = _fetch_import_payload(client, import_id_int)
        output.echo_item(payload, format=format, title=f"Import {import_id_int}")
        return

    payload = _watch_import_status(client, import_id_int, watch_interval)
    output.echo_item(payload, format=format, title=f"Import {import_id_int}")


@app.command("upload")
def upload_import(
    team_id: str | None = TEAM_ID_OPTION,
    team_name: str | None = TEAM_NAME_OPTION,
    device_id: int | None = typer.Option(None, "--device-id", help="SleepHQ device ID (see 'sleephq devices list')"),
    name: str | None = typer.Option(None, "--name", help="Friendly name for the import"),
    files_source: Path | None = typer.Option(
        None,
        "--files",
        help="Directory or .zip archive to upload from",
        exists=True,
        file_okay=True,
        dir_okay=True,
        readable=True,
        resolve_path=True,
    ),
    paths: list[Path] | None = typer.Argument(
        None,
        metavar="[PATH]...",
        help="Relative files or directories to include (defaults to entire --files source or current directory)",
    ),
    base_path: str = typer.Option("./", "--base-path", help="Remote path prefix (default: ./)"),
    process_after: bool = typer.Option(True, "--process/--skip-process", help="Process the import once files finish uploading"),
    watch: bool = WATCH_FLAG,
    watch_interval: float = WATCH_INTERVAL_OPTION,
    format: OutputFormat = typer.Option(OutputFormat.TABLE, "--format", case_sensitive=False, help="Output format when watching"),
    yes: bool = typer.Option(False, "--yes", "-y", help="Skip the upload confirmation prompt"),
) -> None:
    """Create an import, upload files, optionally process + watch status."""

    include_paths = list(paths or [])

    entries = _collect_upload_entries(
        source_root=files_source,
        include_paths=include_paths,
        base_path=base_path,
    )
    if not entries:
        typer.echo("No files found to upload", err=True)
        raise typer.Exit(code=1)

    _confirm_upload(entries, assume_yes=yes)

    client, config, config_path = session.get_authenticated_client()
    resolved_team_id = resolve_team_id(
        client=client,
        config=config,
        config_path=config_path,
        team_id=team_id,
        team_name=team_name,
    )

    team_int = coerce_int(str(resolved_team_id), "team-id")
    import_body = PostV1TeamsTeamIdImportsBody(
        programatic=True,
        device_id=device_id if device_id is not None else UNSET,
        name=name if name else UNSET,
    )
    import_response = post_v1_teams_team_id_imports.sync(
        client=client,
        team_id=team_int,
        body=import_body,
    )
    import_id = getattr(getattr(import_response, "data", None), "id", None)
    if import_id is None:
        typer.echo("Failed to create import", err=True)
        raise typer.Exit(code=1)

    import_id_int = coerce_int(str(import_id), "import_id")
    typer.echo(f"Created import {import_id_int}")

    for path, remote_path, remote_name in entries:
        typer.echo(f"Uploading {_format_upload_entry(path, remote_path, remote_name)}")
        content_hash = _calculate_content_hash(path, remote_name)
        with path.open("rb") as handle:
            file_body = PostV1ImportsImportIdFilesBody(
                name=remote_name,
                path=remote_path,
                content_hash=content_hash,
                file=File(payload=handle, file_name=remote_name),
            )
            post_v1_imports_import_id_files.sync(
                client=client,
                import_id=import_id_int,
                body=file_body,
            )

    typer.echo(f"Uploaded {len(entries)} file(s) to import {import_id_int}")

    if process_after:
        post_v1_imports_id_process_files.sync(client=client, id=import_id_int)
        typer.echo("Triggered import processing")

    if watch:
        payload = _watch_import_status(client, import_id_int, watch_interval)
        output.echo_item(payload, format=format, title=f"Import {import_id_int}")
    else:
        typer.echo(
            f"Use 'sleephq imports show {import_id_int}' to monitor processing",
            err=True,
        )
