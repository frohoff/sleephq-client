from __future__ import annotations

import typer

from functools import partial

from sleephq.api.journals import get_v1_journals_id, get_v1_teams_team_id_journals
from sleephq.types import UNSET

from .. import output, session
from ..options import CONTEXT_SETTINGS
from ..output import OutputFormat
from ..resolvers import resolve_team_id
from ..pagination import (
    collect_paginated,
    print_pagination_hint,
    resolve_pagination_options,
)
from ..utils import coerce_int, parse_fields

app = typer.Typer(help="Journal helpers", no_args_is_help=True, context_settings=CONTEXT_SETTINGS)


def _journal_row(item: object) -> dict[str, object | None]:
    data = output.serialize(item)
    attributes = data.get("attributes") or {}
    return {
        "id": str(data.get("id")),
        "date": attributes.get("date"),
        "feeling_score": attributes.get("feeling_score"),
        "notes": attributes.get("notes"),
    }


@app.command("list")
def list_journals(
    team_id: str | None = typer.Option(None, "--team-id", help="Team identifier"),
    team_name: str | None = typer.Option(None, "--team-name", help="Team name"),
    page: int = typer.Option(1, help="Page number"),
    page_size: int | None = typer.Option(None, "--page-size", help="Page size (defaults to 20 or SLEEPHQ_PAGE_SIZE)"),
    limit: int | None = typer.Option(None, "--limit", help="Maximum number of journals to list"),
    fetch_all: bool = typer.Option(False, "--all", help="Fetch every available page"),
    format: OutputFormat = typer.Option(OutputFormat.TABLE, "--format", case_sensitive=False, help="Output format"),
    fields: str = typer.Option(
        "id,date,feeling_score",
        help="Comma separated list of columns to include in table output",
    ),
) -> None:
    """List journal entries for a team."""

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
        default_page_size=20,
        limit=limit,
        fetch_all=fetch_all,
    )
    fetcher = partial(
        get_v1_teams_team_id_journals.sync_detailed,
        client=client,
        team_id=resolved_team_id,
    )

    result = collect_paginated(fetcher, options=options)

    rows = []
    if result.items:
        rows = [_journal_row(item) for item in result.items]

    if not rows:
        typer.echo("No journals found")
        return

    output.echo_list(rows, format=format, columns=parse_fields(fields), title="Journals")
    print_pagination_hint(options, result)


@app.command("show")
def show_journal(
    journal_id: str = typer.Argument(..., help="Journal ID"),
    format: OutputFormat = typer.Option(OutputFormat.TABLE, "--format", case_sensitive=False, help="Output format"),
) -> None:
    """Display a specific journal entry."""

    client, _, _ = session.get_authenticated_client()
    response = get_v1_journals_id.sync(client=client, id=coerce_int(journal_id, "journal_id"))
    if response is None:
        typer.echo("Journal not found", err=True)
        raise typer.Exit(code=1)

    payload = output.serialize(response)
    output.echo_item(payload, format=format, title=f"Journal {journal_id}")
