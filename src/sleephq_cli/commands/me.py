from __future__ import annotations

from typing import Any

import typer

from sleephq.api.current_user import get_v1_me
from sleephq.types import UNSET

from .. import output, session
from ..options import CONTEXT_SETTINGS
from ..output import OutputFormat

app = typer.Typer(help="Current user helpers", no_args_is_help=True, context_settings=CONTEXT_SETTINGS)


def _extract_user_details(payload: dict[str, Any]) -> dict[str, Any]:
    data = payload.get("data") or {}
    attributes = data.get("attributes") or {}
    return {
        "id": data.get("id"),
        "email": attributes.get("email"),
        "name": attributes.get("name"),
        "timezone": attributes.get("time_zone"),
    }


@app.command("show")
def show(
    format: OutputFormat = typer.Option(OutputFormat.TABLE, "--format", case_sensitive=False, help="Output format"),
) -> None:
    """Display the current authenticated user."""

    client, _, _ = session.get_authenticated_client()
    response = get_v1_me.sync(client=client)
    if response is None or response is UNSET:
        typer.echo("No response from API", err=True)
        raise typer.Exit(code=1)

    payload = output.serialize(response)
    details = _extract_user_details(payload)
    output.echo_item(details, format=format, title="Current User")
