from __future__ import annotations

import typer

from functools import partial

from sleephq.api.machine_dates import get_v1_machines_machine_id_machine_dates
from sleephq.api.machines import get_v1_machines_id, get_v1_teams_team_id_machines
from sleephq.types import UNSET

from .. import output, session
from ..output import OutputFormat
from ..options import (
    ALL_OPTION,
    CONTEXT_SETTINGS,
    LIMIT_OPTION,
    MACHINE_ID_OPTION,
    MACHINE_NAME_OPTION,
    PAGE_OPTION,
    PAGE_SIZE_OPTION,
    TEAM_ID_OPTION,
    TEAM_NAME_OPTION,
)
from ..pagination import (
    collect_paginated,
    print_pagination_hint,
    resolve_pagination_options,
)
from ..resolvers import resolve_machine_id, resolve_team_id
from ..utils import coerce_int, parse_fields

app = typer.Typer(help="Machine utilities", no_args_is_help=True, context_settings=CONTEXT_SETTINGS)

MACHINE_LIST_PAGE_SIZE = 50
MACHINE_DATES_PAGE_SIZE = 30


def _machine_row(item: object) -> dict[str, object | None]:
    data = output.serialize(item)
    attributes = data.get("attributes") or {}
    return {
        "id": str(data.get("id")),
        "name": attributes.get("name"),
        "brand": attributes.get("brand"),
        "model": attributes.get("model"),
        "serial_number": attributes.get("serial_number"),
    }


def _machine_date_row(item: object) -> dict[str, object | None]:
    data = output.serialize(item)
    attributes = data.get("attributes") or {}
    ahi_summary = attributes.get("ahi_summary") or {}
    leak_summary = attributes.get("leak_rate_summary") or {}

    def _summary_value(summary: dict[str, Any], keys: list[str]) -> Any | None:
        for key in keys:
            if key in summary and summary[key] not in (None, ""):
                return summary[key]
        return None

    return {
        "id": data.get("id"),
        "date": attributes.get("date"),
        "usage_minutes": attributes.get("usage"),
        "ahi": _summary_value(ahi_summary, ["ahi", "total", "value", "score"]),
        "score": ahi_summary.get("score"),
        "leak_median": _summary_value(leak_summary, ["median", "average", "av", "value", "score"]),
    }


@app.command("list")
def list_machines(
    team_id: str | None = TEAM_ID_OPTION,
    team_name: str | None = TEAM_NAME_OPTION,
    page: int = PAGE_OPTION,
    page_size: int | None = PAGE_SIZE_OPTION,
    limit: int | None = LIMIT_OPTION,
    fetch_all: bool = ALL_OPTION,
    format: OutputFormat = typer.Option(OutputFormat.TABLE, "--format", case_sensitive=False, help="Output format"),
    fields: str = typer.Option(
        "id,name,brand,model",
        help="Comma separated list of columns to include in table output",
    ),
) -> None:
    """List machines for a team."""

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
        default_page_size=MACHINE_LIST_PAGE_SIZE,
        limit=limit,
        fetch_all=fetch_all,
    )

    fetcher = partial(get_v1_teams_team_id_machines.sync_detailed, client=client, team_id=resolved_team_id)
    result = collect_paginated(fetcher, options=options)

    rows = []
    if result.items:
        rows = [_machine_row(machine) for machine in result.items]

    if not rows:
        typer.echo("No machines found for the selected team")
        return

    output.echo_list(rows, format=format, columns=parse_fields(fields), title="Machines")
    print_pagination_hint(options, result)


@app.command("show")
def show_machine(
    machine_id: str | None = MACHINE_ID_OPTION,
    machine_name: str | None = MACHINE_NAME_OPTION,
    team_id: str | None = TEAM_ID_OPTION,
    team_name: str | None = TEAM_NAME_OPTION,
    format: OutputFormat = typer.Option(OutputFormat.TABLE, "--format", case_sensitive=False, help="Output format"),
) -> None:
    """Show details for a single machine."""

    if machine_id and machine_name:
        raise typer.BadParameter("Use either --machine-id or --machine-name, not both")

    client, config, config_path = session.get_authenticated_client()

    resolved_team_id: str | None = team_id
    resolved_machine_id: str | None = machine_id
    if resolved_machine_id is None:
        resolved_team_id = resolve_team_id(
            client=client,
            config=config,
            config_path=config_path,
            team_id=team_id,
            team_name=team_name,
        )
        resolved_machine_id = resolve_machine_id(
            client=client,
            config=config,
            config_path=config_path,
            team_id=resolved_team_id,
            machine_id=None,
            machine_name=machine_name,
        )

    machine_int = coerce_int(resolved_machine_id, "machine-id")
    response = get_v1_machines_id.sync(client=client, id=machine_int)
    if response is None:
        typer.echo("Machine not found", err=True)
        raise typer.Exit(code=1)

    payload = output.serialize(response)
    output.echo_item(payload, format=format, title=f"Machine {resolved_machine_id}")


@app.command("sleep")
def list_machine_dates(
    machine_id: str | None = MACHINE_ID_OPTION,
    machine_name: str | None = MACHINE_NAME_OPTION,
    team_id: str | None = TEAM_ID_OPTION,
    team_name: str | None = TEAM_NAME_OPTION,
    page: int = PAGE_OPTION,
    page_size: int | None = PAGE_SIZE_OPTION,
    limit: int | None = LIMIT_OPTION,
    fetch_all: bool = ALL_OPTION,
    format: OutputFormat = typer.Option(OutputFormat.TABLE, "--format", case_sensitive=False, help="Output format"),
    fields: str = typer.Option(
        "date,usage_minutes,ahi,score,leak_median",
        help="Comma separated list of columns to include in table output",
    ),
) -> None:
    """List sleep records (`machine_dates`) for a machine."""

    if machine_id and machine_name:
        raise typer.BadParameter("Use either --machine-id or --machine-name, not both")

    client, config, config_path = session.get_authenticated_client()

    resolved_machine_id = machine_id
    if resolved_machine_id is None:
        resolved_team_id = resolve_team_id(
            client=client,
            config=config,
            config_path=config_path,
            team_id=team_id,
            team_name=team_name,
        )
        resolved_machine_id = resolve_machine_id(
            client=client,
            config=config,
            config_path=config_path,
            team_id=resolved_team_id,
            machine_id=None,
            machine_name=machine_name,
        )

    machine_int = coerce_int(resolved_machine_id, "machine-id")
    options = resolve_pagination_options(
        page=page,
        page_size=page_size,
        default_page_size=MACHINE_DATES_PAGE_SIZE,
        limit=limit,
        fetch_all=fetch_all,
    )
    fetcher = partial(
        get_v1_machines_machine_id_machine_dates.sync_detailed,
        client=client,
        machine_id=machine_int,
    )
    result = collect_paginated(fetcher, options=options)

    rows = []
    if result.items:
        rows = [_machine_date_row(item) for item in result.items]

    if not rows:
        typer.echo("No sleep records found for the selected machine")
        return

    output.echo_list(rows, format=format, columns=parse_fields(fields), title="Machine Dates")
    print_pagination_hint(options, result)
