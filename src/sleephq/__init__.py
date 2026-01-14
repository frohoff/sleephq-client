"""A client library for accessing SleepHQ"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)

# Hand-written auth helpers (injected by generate.sh)
from sleephq.auth import create_client as create_client
from sleephq.auth import TokenResponse as TokenResponse
from sleephq.auth import get_token as get_token
