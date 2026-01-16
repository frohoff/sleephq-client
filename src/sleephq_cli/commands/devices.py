from __future__ import annotations

import typer

from sleephq.api.devices import get_v1_devices

from .. import output, session
from ..options import CONTEXT_SETTINGS
from ..output import OutputFormat

app = typer.Typer(help="Device utilities", no_args_is_help=True, context_settings=CONTEXT_SETTINGS)


def _device_row(item: object) -> dict[str, str | int | None]:
    data = output.serialize(item)
    attributes = data.get("attributes") or {}
    return {
        "id": str(attributes.get("id") or data.get("id")),
        "name": attributes.get("name"),
        "brand": attributes.get("brand"),
        "device_type": attributes.get("device_type"),
    }


@app.command("list")
def list_devices(
    limit: int | None = typer.Option(None, "--limit", help="Maximum number of devices to show"),
    format: OutputFormat = typer.Option(OutputFormat.TABLE, "--format", case_sensitive=False, help="Output format"),
    fields: str = typer.Option(
        "id,name,brand,device_type",
        help="Comma separated list of columns to include in table output",
    ),
) -> None:
    """List available SleepHQ device types."""

    client, _, _ = session.get_authenticated_client()
    response = get_v1_devices.sync(client=client)
    devices = []
    if response and response.data:
        devices = [_device_row(item) for item in response.data]

    if limit is not None:
        if limit <= 0:
            raise typer.BadParameter("--limit must be positive")
        devices = devices[:limit]

    if not devices:
        typer.echo("No devices returned from API")
        return

    columns = [column.strip() for column in fields.split(",") if column.strip()]
    output.echo_list(devices, format=format, columns=columns, title="Devices")
