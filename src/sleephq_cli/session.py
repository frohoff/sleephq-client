from __future__ import annotations

from dataclasses import replace
from datetime import datetime, timezone
import os
from pathlib import Path

import typer

from sleephq.auth import TokenResponse, get_token
from sleephq.client import AuthenticatedClient

from .config import CLIConfig, DEFAULT_BASE_URL, DEFAULT_SCOPE, default_config_path, load_config, save_config


def _timestamp() -> int:
    return int(datetime.now(timezone.utc).timestamp())


def _prompt_for(value_name: str, *, default: str | None = None, secret: bool = False) -> str:
    prompt_text = f"Enter {value_name}"
    if default:
        result = typer.prompt(prompt_text, default=default, show_default=True, hide_input=secret)
    else:
        result = typer.prompt(prompt_text, hide_input=secret)
    cleaned = result.strip()
    if not cleaned:
        raise typer.BadParameter(f"{value_name} is required")
    return cleaned


def _store_token(config: CLIConfig, token: TokenResponse) -> CLIConfig:
    expires_at = token.created_at + token.expires_in
    return replace(
        config,
        token=token.access_token,
        token_expires_at=expires_at,
    )


class CredentialError(RuntimeError):
    """Raised when credentials are missing and prompting is disabled."""


def get_authenticated_client(
    *,
    config_path: Path | None = None,
    allow_prompt: bool = True,
    persist_token: bool = True,
) -> tuple[AuthenticatedClient, CLIConfig, Path]:
    """Return an authenticated SleepHQ client, refreshing the token when needed."""

    path = config_path or default_config_path()
    config = load_config(path)

    base_url = os.environ.get("SLEEPHQ_BASE_URL") or config.base_url or DEFAULT_BASE_URL
    scope = os.environ.get("SLEEPHQ_SCOPE") or config.scope or DEFAULT_SCOPE

    env_token = os.environ.get("SLEEPHQ_TOKEN")
    if env_token:
        client = AuthenticatedClient(base_url=base_url, token=env_token)
        return client, config, path

    token = config.token
    expires_at = config.token_expires_at or 0
    if token and expires_at > _timestamp():
        client = AuthenticatedClient(base_url=base_url, token=token)
        return client, config, path

    client_id = os.environ.get("SLEEPHQ_CLIENT_ID") or config.client_id
    client_secret = os.environ.get("SLEEPHQ_CLIENT_SECRET") or config.client_secret

    if not client_id:
        if allow_prompt:
            client_id = _prompt_for("SleepHQ client ID", default=config.client_id)
        else:
            raise CredentialError("Client ID not configured. Run 'sleephq auth login'.")

    if not client_secret:
        if allow_prompt:
            client_secret = _prompt_for(
                "SleepHQ client secret",
                default=config.client_secret,
                secret=True,
            )
        else:
            raise CredentialError("Client secret not configured. Run 'sleephq auth login'.")

    token_response = get_token(client_id=client_id, client_secret=client_secret, scope=scope)
    config = replace(
        config,
        client_id=client_id,
        client_secret=client_secret,
        scope=scope,
    )
    config = _store_token(config, token_response)

    if persist_token:
        save_config(config, path)

    client = AuthenticatedClient(base_url=base_url, token=token_response.access_token)
    return client, config, path
