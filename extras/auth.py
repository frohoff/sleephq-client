"""
OAuth2 authentication helper for SleepHQ API.

This module is injected into the generated SDK by generate.sh.

Example usage:
    from sleephq.auth import create_client
    from sleephq.api.teams import get_v1_teams

    client = create_client(client_id="...", client_secret="...")
    response = get_v1_teams.sync(client=client)
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

import httpx

if TYPE_CHECKING:
    from sleephq.client import AuthenticatedClient

_TOKEN_URL = "https://sleephq.com/oauth/token"
_BASE_URL = "https://sleephq.com/api"


@dataclass(frozen=True)
class TokenResponse:
    """OAuth2 token response from SleepHQ."""

    access_token: str
    token_type: str
    expires_in: int
    scope: str
    created_at: int

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> TokenResponse:
        return cls(
            access_token=str(data["access_token"]),
            token_type=str(data["token_type"]),
            expires_in=int(data["expires_in"]),
            scope=str(data["scope"]),
            created_at=int(data["created_at"]),
        )


def get_token(
    client_id: str,
    client_secret: str,
    *,
    scope: str = "read write delete",
    grant_type: str = "password",
) -> TokenResponse:
    """
    Obtain an OAuth2 access token from SleepHQ.

    Args:
        client_id: Your SleepHQ OAuth client ID.
        client_secret: Your SleepHQ OAuth client secret.
        scope: OAuth scopes to request. Defaults to "read write delete".
        grant_type: OAuth grant type. Defaults to "password".

    Returns:
        TokenResponse containing the access token and metadata.

    Raises:
        httpx.HTTPStatusError: If the token request fails.
    """
    response = httpx.post(
        _TOKEN_URL,
        data={
            "grant_type": grant_type,
            "client_id": client_id,
            "client_secret": client_secret,
            "scope": scope,
        },
    )
    response.raise_for_status()
    return TokenResponse.from_dict(response.json())


def create_client(
    client_id: str,
    client_secret: str,
    *,
    scope: str = "read write delete",
    grant_type: str = "password",
    base_url: str = _BASE_URL,
) -> AuthenticatedClient:
    """
    Create an authenticated SleepHQ API client.

    This is a convenience function that obtains an OAuth token and creates
    an AuthenticatedClient in one step.

    Args:
        client_id: Your SleepHQ OAuth client ID.
        client_secret: Your SleepHQ OAuth client secret.
        scope: OAuth scopes to request. Defaults to "read write delete".
        grant_type: OAuth grant type. Defaults to "password".
        base_url: API base URL. Defaults to "https://sleephq.com/api".

    Returns:
        An AuthenticatedClient ready to use with API functions.

    Example:
        from sleephq.auth import create_client
        from sleephq.api.teams import get_v1_teams

        client = create_client(client_id="...", client_secret="...")
        teams = get_v1_teams.sync(client=client)
    """
    from sleephq.client import AuthenticatedClient

    token = get_token(client_id, client_secret, scope=scope, grant_type=grant_type)
    return AuthenticatedClient(base_url=base_url, token=token.access_token)
