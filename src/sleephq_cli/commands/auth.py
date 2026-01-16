from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import typer

from sleephq.auth import get_token

from ..config import CLIConfig, DEFAULT_BASE_URL, DEFAULT_SCOPE, default_config_path, load_config, save_config
from ..options import CONTEXT_SETTINGS

app = typer.Typer(
    help="Manage authentication and saved credentials",
    no_args_is_help=True,
    context_settings=CONTEXT_SETTINGS,
)


def _format_timestamp(timestamp: int | None) -> str:
    if not timestamp:
        return "unknown"
    dt = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    return dt.isoformat()


@app.command("login")
def login(
    client_id: str | None = typer.Option(None, "--client-id", "-i", help="SleepHQ OAuth client ID"),
    client_secret: str | None = typer.Option(None, "--client-secret", "-s", help="SleepHQ OAuth client secret"),
    scope: str = typer.Option(DEFAULT_SCOPE, help="OAuth scope to request"),
    base_url: str = typer.Option(DEFAULT_BASE_URL, help="API base URL"),
    config_path: Path | None = typer.Option(None, help="Override config file path"),
) -> None:
    """Store credentials locally and fetch an access token."""

    path = config_path or default_config_path()
    existing = load_config(path)

    if not client_id:
        default_value = existing.client_id or ""
        client_id = typer.prompt("SleepHQ client ID", default=default_value if default_value else None, show_default=bool(default_value))

    if not client_secret:
        client_secret = typer.prompt(
            "SleepHQ client secret",
            default=existing.client_secret if existing.client_secret else None,
            hide_input=True,
            show_default=False,
        )

    client_id = client_id.strip()
    client_secret = client_secret.strip()
    if not client_id or not client_secret:
        raise typer.BadParameter("Client ID and secret are required")

    typer.echo("Requesting token from SleepHQ…")
    token = get_token(client_id=client_id, client_secret=client_secret, scope=scope)

    config = CLIConfig(
        client_id=client_id,
        client_secret=client_secret,
        scope=scope,
        base_url=base_url,
    )
    config.token = token.access_token
    config.token_expires_at = token.created_at + token.expires_in

    save_config(config, path)
    typer.echo("Credentials saved. Token expires at " + _format_timestamp(config.token_expires_at))


@app.command("status")
def status(
    config_path: Path | None = typer.Option(None, help="Override config file path"),
    json_output: bool = typer.Option(False, "--json", help="Emit JSON instead of text"),
) -> None:
    """Display stored credential information."""

    config = load_config(config_path or default_config_path())
    data = {
        "client_id": config.client_id,
        "base_url": config.base_url,
        "scope": config.scope,
        "token_present": bool(config.token),
        "token_expires_at": config.token_expires_at,
    }
    if json_output:
        import json

        typer.echo(json.dumps(data, indent=2))
        return

    typer.echo("Stored credentials:")
    typer.echo(f"  Client ID: {config.client_id or 'not set'}")
    typer.echo(f"  Base URL: {config.base_url}")
    typer.echo(f"  Scope: {config.scope}")
    if config.token:
        typer.echo(f"  Token expires at: {_format_timestamp(config.token_expires_at)}")
    else:
        typer.echo("  Token: not cached")


@app.command("logout")
def logout(config_path: Path | None = typer.Option(None, help="Override config file path")) -> None:
    """Remove cached access token (credentials remain)."""

    path = config_path or default_config_path()
    config = load_config(path)
    if not config.token:
        typer.echo("No cached token found", err=True)
        raise typer.Exit(code=1)

    config.token = None
    config.token_expires_at = None
    save_config(config, path)
    typer.echo("Cached token removed")
