from __future__ import annotations

import typer

from functools import partial

from sleephq.api.import_files import (
    get_v1_imports_files_id,
    get_v1_imports_import_id_files,
    get_v1_teams_team_id_files,
)
from sleephq.types import UNSET

from .. import output, session
from ..options import (
    ALL_OPTION,
    CONTEXT_SETTINGS,
    LIMIT_OPTION,
    PAGE_OPTION,
    PAGE_SIZE_OPTION,
    TEAM_ID_OPTION,
    TEAM_NAME_OPTION,
)
from ..output import OutputFormat
from ..pagination import (
    collect_paginated,
    print_pagination_hint,
    resolve_pagination_options,
)
from ..resolvers import resolve_team_id
from ..utils import coerce_int, parse_fields

app = typer.Typer(help="File helpers", no_args_is_help=True, context_settings=CONTEXT_SETTINGS)

DEFAULT_PAGE_SIZE = 100


def _file_row(item: object) -> dict[str, object | None]:
    data = output.serialize(item)
    attributes = data.get("attributes") or {}
    return {
        "id": str(data.get("id")),
        "name": attributes.get("name"),
        "size": attributes.get("size"),
        "content_hash": attributes.get("content_hash"),
        "created_at": attributes.get("created_at"),
    }


@app.command("list")
def list_files(
    import_id: str | None = typer.Option(None, "--import-id", help="List files attached to a specific import"),
    team_id: str | None = TEAM_ID_OPTION,
    team_name: str | None = TEAM_NAME_OPTION,
    page: int = PAGE_OPTION,
    page_size: int | None = PAGE_SIZE_OPTION,
    limit: int | None = LIMIT_OPTION,
    fetch_all: bool = ALL_OPTION,
    format: OutputFormat = typer.Option(OutputFormat.TABLE, "--format", case_sensitive=False, help="Output format"),
    fields: str = typer.Option(
        "id,name,size,content_hash",
        help="Comma separated list of columns to include in table output",
    ),
) -> None:
    """List import files for a team or a specific import."""

    client, config, config_path = session.get_authenticated_client()

    if import_id and (team_id or team_name):
        raise typer.BadParameter("When --import-id is specified, omit team filters")

    options = resolve_pagination_options(
        page=page,
        page_size=page_size,
        default_page_size=DEFAULT_PAGE_SIZE,
        limit=limit,
        fetch_all=fetch_all,
    )

    if import_id:
        fetcher = partial(
            get_v1_imports_import_id_files.sync_detailed,
            client=client,
            import_id=coerce_int(import_id, "import-id"),
        )
    else:
        resolved_team_id = resolve_team_id(
            client=client,
            config=config,
            config_path=config_path,
            team_id=team_id,
            team_name=team_name,
        )
        fetcher = partial(
            get_v1_teams_team_id_files.sync_detailed,
            client=client,
            team_id=resolved_team_id,
        )

    result = collect_paginated(fetcher, options=options)

    rows = []
    if result.items:
        rows = [_file_row(item) for item in result.items]

    if not rows:
        typer.echo("No files found")
        return

    output.echo_list(rows, format=format, columns=parse_fields(fields), title="Files")
    print_pagination_hint(options, result)


@app.command("show")
def show_file(
    file_id: str = typer.Argument(..., help="File ID"),
    format: OutputFormat = typer.Option(OutputFormat.TABLE, "--format", case_sensitive=False, help="Output format"),
) -> None:
    """Display details for a single import file."""

    client, _, _ = session.get_authenticated_client()
    response = get_v1_imports_files_id.sync(client=client, id=coerce_int(file_id, "file_id"))
    if response is None:
        typer.echo("File not found", err=True)
        raise typer.Exit(code=1)

    payload = output.serialize(response)
    output.echo_item(payload, format=format, title=f"File {file_id}")
