from __future__ import annotations

import typer

from sleephq.api.patients import get_v1_teams_team_id_patients
from sleephq.types import UNSET

from .. import output, session
from ..options import CONTEXT_SETTINGS
from ..output import OutputFormat
from ..resolvers import resolve_team_id
from ..utils import parse_fields
from ..pagination import (
    collect_paginated,
    print_pagination_hint,
    resolve_pagination_options,
)

app = typer.Typer(help="Patient helpers", no_args_is_help=True, context_settings=CONTEXT_SETTINGS)


def _patient_row(item: object) -> dict[str, object | None]:
    data = output.serialize(item)
    attributes = data.get("attributes") or {}
    return {
        "id": str(data.get("id")),
        "name": attributes.get("name"),
        "created_at": attributes.get("created_at"),
    }


@app.command("list")
def list_patients(
    team_id: str | None = typer.Option(None, "--team-id", help="Team identifier"),
    team_name: str | None = typer.Option(None, "--team-name", help="Team name"),
    page: int = typer.Option(1, help="Page number"),
    page_size: int | None = typer.Option(None, "--page-size", help="Page size (defaults to 50 or SLEEPHQ_PAGE_SIZE)"),
    limit: int | None = typer.Option(None, "--limit", help="Maximum number of patients to list"),
    fetch_all: bool = typer.Option(False, "--all", help="Fetch every available page"),
    format: OutputFormat = typer.Option(OutputFormat.TABLE, "--format", case_sensitive=False, help="Output format"),
    fields: str = typer.Option(
        "id,name,created_at",
        help="Comma separated list of columns to include in table output",
    ),
) -> None:
    """List patients for the selected team."""

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
        default_page_size=50,
        limit=limit,
        fetch_all=fetch_all,
    )
    result = collect_paginated(
        lambda current_page, per_page_value: get_v1_teams_team_id_patients.sync_detailed(
            client=client,
            team_id=resolved_team_id,
            page=current_page,
            per_page=per_page_value,
        ),
        options=options,
    )

    rows = []
    if result.items:
        rows = [_patient_row(item) for item in result.items]

    if not rows:
        typer.echo("No patients found")
        return

    output.echo_list(rows, format=format, columns=parse_fields(fields), title="Patients")
    print_pagination_hint(options, result)
