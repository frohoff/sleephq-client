from __future__ import annotations

import typer

from functools import partial

from sleephq.api.teams import get_v1_teams
from sleephq.types import UNSET

from .. import output, session
from ..options import ALL_OPTION, LIMIT_OPTION, PAGE_OPTION, PAGE_SIZE_OPTION, CONTEXT_SETTINGS
from ..output import OutputFormat
from ..pagination import (
    collect_paginated,
    print_pagination_hint,
    resolve_pagination_options,
)

app = typer.Typer(help="Team utilities", no_args_is_help=True, context_settings=CONTEXT_SETTINGS)

DEFAULT_PAGE_SIZE = 50


def _team_row(team) -> dict[str, str | None]:
    attributes = team.attributes.to_dict() if team.attributes is not UNSET else {}
    return {
        "id": getattr(team, "id", None),
        "name": attributes.get("name"),
        "timezone": attributes.get("time_zone"),
        "type": getattr(team, "type_", None),
    }


@app.command("list")
def list_teams(
    page: int = PAGE_OPTION,
    page_size: int | None = PAGE_SIZE_OPTION,
    limit: int | None = LIMIT_OPTION,
    fetch_all: bool = ALL_OPTION,
    format: OutputFormat = typer.Option(OutputFormat.TABLE, "--format", case_sensitive=False, help="Output format"),
    fields: str = typer.Option(
        "id,name,timezone",
        help="Comma separated list of columns to include in table output",
    ),
) -> None:
    """List accessible teams."""

    client, _, _ = session.get_authenticated_client()
    options = resolve_pagination_options(
        page=page,
        page_size=page_size,
        default_page_size=DEFAULT_PAGE_SIZE,
        limit=limit,
        fetch_all=fetch_all,
    )

    fetcher = partial(get_v1_teams.sync_detailed, client=client)
    result = collect_paginated(fetcher, options=options)

    teams = []
    if result.items:
        teams = [_team_row(team) for team in result.items]

    if not teams:
        typer.echo("No teams found")
        return

    columns = [column.strip() for column in fields.split(",") if column.strip()]
    output.echo_list(teams, format=format, columns=columns, title="Teams")
    print_pagination_hint(options, result)
