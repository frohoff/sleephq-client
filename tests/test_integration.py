"""
Integration tests for SleepHQ API client.

These tests require valid credentials in environment variables:
- SLEEPHQ_CLIENT_ID
- SLEEPHQ_CLIENT_SECRET

Run with: uv run pytest tests/test_integration.py -v
"""

from __future__ import annotations

import os

import pytest

from sleephq import create_client
from sleephq.api.current_user import get_v1_me
from sleephq.api.devices import get_v1_devices
from sleephq.api.imports import get_v1_teams_team_id_imports
from sleephq.api.machine_dates import get_v1_machines_machine_id_machine_dates
from sleephq.api.machines import get_v1_teams_team_id_machines
from sleephq.api.teams import get_v1_teams
from sleephq.client import AuthenticatedClient


@pytest.fixture(scope="module")
def client() -> AuthenticatedClient:
    """Create an authenticated client using environment credentials."""
    client_id = os.environ.get("SLEEPHQ_CLIENT_ID")
    client_secret = os.environ.get("SLEEPHQ_CLIENT_SECRET")

    if not client_id or not client_secret:
        pytest.skip("SLEEPHQ_CLIENT_ID and SLEEPHQ_CLIENT_SECRET required")

    return create_client(client_id=client_id, client_secret=client_secret)


@pytest.fixture(scope="module")
def team_id(client: AuthenticatedClient) -> str:
    """Get the first team ID for the authenticated user."""
    teams = get_v1_teams.sync(client=client)
    assert teams is not None
    assert teams.data is not None
    assert len(teams.data) > 0
    team = teams.data[0]
    assert team.id is not None
    return team.id


@pytest.fixture(scope="module")
def machine_id(client: AuthenticatedClient, team_id: str) -> str | None:
    """Get the first machine ID for the team."""
    machines = get_v1_teams_team_id_machines.sync(client=client, team_id=team_id)
    if machines and machines.data and len(machines.data) > 0:
        return machines.data[0].id
    return None


class TestCurrentUser:
    """Tests for /v1/me endpoint."""

    def test_get_current_user(self, client: AuthenticatedClient) -> None:
        """Can retrieve current user information."""
        result = get_v1_me.sync(client=client)
        assert result is not None
        assert result.data is not None


class TestDevices:
    """Tests for /v1/devices endpoint."""

    def test_list_device_types(self, client: AuthenticatedClient) -> None:
        """Can list available device types."""
        result = get_v1_devices.sync(client=client)
        assert result is not None
        assert result.data is not None
        assert len(result.data) > 0


class TestTeams:
    """Tests for /v1/teams endpoint."""

    def test_list_teams(self, client: AuthenticatedClient) -> None:
        """Can list user's teams."""
        result = get_v1_teams.sync(client=client)
        assert result is not None
        assert result.data is not None
        assert len(result.data) > 0

    def test_team_has_attributes(self, client: AuthenticatedClient) -> None:
        """Teams have expected attributes."""
        result = get_v1_teams.sync(client=client)
        assert result is not None
        assert result.data is not None
        team = result.data[0]
        assert team.id is not None
        assert team.attributes is not None
        assert team.attributes.name is not None


class TestMachines:
    """Tests for /v1/teams/{team_id}/machines endpoint."""

    def test_list_machines(
        self, client: AuthenticatedClient, team_id: str
    ) -> None:
        """Can list machines for a team."""
        result = get_v1_teams_team_id_machines.sync(client=client, team_id=team_id)
        assert result is not None
        # May or may not have machines, but should not error


class TestImports:
    """Tests for /v1/teams/{team_id}/imports endpoint."""

    def test_list_imports(
        self, client: AuthenticatedClient, team_id: str
    ) -> None:
        """Can list imports for a team."""
        result = get_v1_teams_team_id_imports.sync(
            client=client, team_id=team_id, per_page=5
        )
        assert result is not None


class TestMachineDates:
    """Tests for /v1/machines/{machine_id}/machine_dates endpoint."""

    def test_list_machine_dates(
        self, client: AuthenticatedClient, machine_id: str | None
    ) -> None:
        """Can list sleep data for a machine."""
        if machine_id is None:
            pytest.skip("No machine available for testing")

        result = get_v1_machines_machine_id_machine_dates.sync(
            client=client, machine_id=machine_id, per_page=5
        )
        assert result is not None
