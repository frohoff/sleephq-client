# ruff: noqa: E402
"""
OAuth2 authentication helper for SleepHQ API.

This module is injected into the generated SDK by generate.sh.
"""

from __future__ import annotations

import urllib.parse
import urllib.request
import json
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sleephq.api.active_storage_api import ActiveStorageApi
    from sleephq.api.current_user_api import CurrentUserApi
    from sleephq.api.devices_api import DevicesApi
    from sleephq.api.import_files_api import ImportFilesApi
    from sleephq.api.imports_api import ImportsApi
    from sleephq.api.journals_api import JournalsApi
    from sleephq.api.machine_dates_api import MachineDatesApi
    from sleephq.api.machines_api import MachinesApi
    from sleephq.api.patients_api import PatientsApi
    from sleephq.api.teams_api import TeamsApi


_TOKEN_URL = "https://sleephq.com/oauth/token"


@dataclass(frozen=True)
class TokenResponse:
    """OAuth2 token response from SleepHQ."""

    access_token: str
    token_type: str
    expires_in: int
    scope: str
    created_at: int

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> TokenResponse:
        return cls(
            access_token=str(data["access_token"]),
            token_type=str(data["token_type"]),
            expires_in=int(data["expires_in"]),  # type: ignore[arg-type]
            scope=str(data["scope"]),
            created_at=int(data["created_at"]),  # type: ignore[arg-type]
        )


def get_token(
    client_id: str,
    client_secret: str,
    *,
    scope: str = "read write delete",
    grant_type: str = "password",
) -> TokenResponse:
    """
    Obtain an OAuth2 access token using the password grant type.

    Args:
        client_id: Your SleepHQ OAuth client ID.
        client_secret: Your SleepHQ OAuth client secret.

    Returns:
        TokenResponse containing the access token and metadata.

    Raises:
        urllib.error.HTTPError: If the token request fails.
    """
    data = urllib.parse.urlencode({
        "grant_type": grant_type,
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": scope,
    }).encode("utf-8")

    request = urllib.request.Request(
        _TOKEN_URL,
        data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )

    with urllib.request.urlopen(request) as response:
        return TokenResponse.from_dict(json.loads(response.read().decode("utf-8")))


class Client:
    """
    Authenticated SleepHQ API client.

    Provides typed access to all API endpoints with automatic OAuth2 authentication.

    Example:
        client = Client.from_credentials(
            client_id="your_client_id",
            client_secret="your_client_secret"
        )
        teams = client.teams.get_v1_teams()
    """

    def __init__(self, access_token: str) -> None:
        """
        Create a client with an existing access token.

        Args:
            access_token: A valid OAuth2 access token.
        """
        # Import here to avoid circular imports
        from sleephq.api_client import ApiClient
        from sleephq.configuration import Configuration

        self._config = Configuration()
        self._config.access_token = access_token
        self._api_client = ApiClient(self._config)

        # Lazy-initialized API instances
        self._active_storage: ActiveStorageApi | None = None
        self._current_user: CurrentUserApi | None = None
        self._devices: DevicesApi | None = None
        self._import_files: ImportFilesApi | None = None
        self._imports: ImportsApi | None = None
        self._journals: JournalsApi | None = None
        self._machine_dates: MachineDatesApi | None = None
        self._machines: MachinesApi | None = None
        self._patients: PatientsApi | None = None
        self._teams: TeamsApi | None = None

    @classmethod
    def from_credentials(cls, client_id: str, client_secret: str) -> Client:
        """
        Create an authenticated client using OAuth2 credentials.

        Args:
            client_id: Your SleepHQ OAuth client ID.
            client_secret: Your SleepHQ OAuth client secret.

        Returns:
            An authenticated Client instance.
        """
        token = get_token(client_id, client_secret)
        return cls(token.access_token)

    @property
    def active_storage(self) -> ActiveStorageApi:
        """Access the ActiveStorage API."""
        if self._active_storage is None:
            from sleephq.api.active_storage_api import ActiveStorageApi
            self._active_storage = ActiveStorageApi(self._api_client)
        return self._active_storage

    @property
    def current_user(self) -> CurrentUserApi:
        """Access the CurrentUser API."""
        if self._current_user is None:
            from sleephq.api.current_user_api import CurrentUserApi
            self._current_user = CurrentUserApi(self._api_client)
        return self._current_user

    @property
    def devices(self) -> DevicesApi:
        """Access the Devices API."""
        if self._devices is None:
            from sleephq.api.devices_api import DevicesApi
            self._devices = DevicesApi(self._api_client)
        return self._devices

    @property
    def import_files(self) -> ImportFilesApi:
        """Access the ImportFiles API."""
        if self._import_files is None:
            from sleephq.api.import_files_api import ImportFilesApi
            self._import_files = ImportFilesApi(self._api_client)
        return self._import_files

    @property
    def imports(self) -> ImportsApi:
        """Access the Imports API."""
        if self._imports is None:
            from sleephq.api.imports_api import ImportsApi
            self._imports = ImportsApi(self._api_client)
        return self._imports

    @property
    def journals(self) -> JournalsApi:
        """Access the Journals API."""
        if self._journals is None:
            from sleephq.api.journals_api import JournalsApi
            self._journals = JournalsApi(self._api_client)
        return self._journals

    @property
    def machine_dates(self) -> MachineDatesApi:
        """Access the MachineDates API."""
        if self._machine_dates is None:
            from sleephq.api.machine_dates_api import MachineDatesApi
            self._machine_dates = MachineDatesApi(self._api_client)
        return self._machine_dates

    @property
    def machines(self) -> MachinesApi:
        """Access the Machines API."""
        if self._machines is None:
            from sleephq.api.machines_api import MachinesApi
            self._machines = MachinesApi(self._api_client)
        return self._machines

    @property
    def patients(self) -> PatientsApi:
        """Access the Patients API."""
        if self._patients is None:
            from sleephq.api.patients_api import PatientsApi
            self._patients = PatientsApi(self._api_client)
        return self._patients

    @property
    def teams(self) -> TeamsApi:
        """Access the Teams API."""
        if self._teams is None:
            from sleephq.api.teams_api import TeamsApi
            self._teams = TeamsApi(self._api_client)
        return self._teams
