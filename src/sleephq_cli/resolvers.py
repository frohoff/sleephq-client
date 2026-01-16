from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Iterable

import typer

from sleephq.api.machines import get_v1_teams_team_id_machines
from sleephq.api.teams import get_v1_teams
from sleephq.types import UNSET

from .config import CLIConfig, save_config
from .output import serialize


def resolve_team_id(
    *,
    client,
    config: CLIConfig,
    config_path: Path,
    team_id: str | None = None,
    team_name: str | None = None,
    persist_default: bool = True,
) -> str:
    if team_id:
        return team_id

    env_team = os.environ.get("SLEEPHQ_TEAM_ID")
    if env_team:
        return env_team

    teams = None
    if team_name:
        teams = _list_teams(client)
        match = _match_by_name(teams, team_name)
        if match is None:
            available = ", ".join(_describe_team(team) for team in teams)
            raise typer.BadParameter(
                f"No team named '{team_name}'. Available teams: {available or 'none'}"
            )
        return match

    if config.default_team_id:
        name = config.default_team_name
        label = f'"{name}"' if name else config.default_team_id
        typer.echo(
            f"Using configured team {label} ({config.default_team_id}). Override with --team-id/--team-name.",
            err=True,
        )
        return config.default_team_id

    teams = teams or _list_teams(client)
    if not teams:
        raise typer.BadParameter("No teams available for this account")
    if len(teams) == 1:
        team = teams[0]
        team_id_value = str(_team_id(team))
        if persist_default:
            config.default_team_id = team_id_value
            config.default_team_name = _team_name(team)
            save_config(config, config_path)
            label = f'"{config.default_team_name}"' if config.default_team_name else team_id_value
            typer.echo(
                f"Configured single team {label} ({team_id_value}) as default.",
                err=True,
            )
        return team_id_value

    names = ", ".join(_describe_team(team) for team in teams)
    raise typer.BadParameter(
        f"Multiple teams available ({names}). Specify --team-id or --team-name."
    )


def resolve_machine_id(
    *,
    client,
    config: CLIConfig,
    config_path: Path,
    team_id: str,
    machine_id: str | None = None,
    machine_name: str | None = None,
    persist_default: bool = True,
) -> str:
    if machine_id:
        return machine_id

    env_machine = os.environ.get("SLEEPHQ_MACHINE_ID")
    if env_machine:
        return env_machine

    machines = None
    if machine_name:
        machines = _list_machines(client, team_id)
        match = _match_machine_by_name(machines, machine_name)
        if match is None:
            available = ", ".join(_describe_machine(machine) for machine in machines)
            raise typer.BadParameter(
                f"No machine named '{machine_name}'. Available: {available or 'none'}"
            )
        return match

    cached = config.default_machine_ids.get(team_id)
    if cached:
        label = _machine_name_from_config(config, cached)
        if not label:
            machines = machines or _list_machines(client, team_id)
            machine = _find_machine_by_id(machines, cached)
            label = _machine_name(machine) if machine else None
            if label and persist_default:
                if config.default_machine_names.get(cached) != label:
                    config.default_machine_names[cached] = label
                    save_config(config, config_path)
        quoted_label = f'"{label}"' if label else None
        typer.echo(
            f"Using configured machine {quoted_label or cached} ({cached}). Override with --machine-id/--machine-name.",
            err=True,
        )
        return cached

    machines = machines or _list_machines(client, team_id)
    if not machines:
        raise typer.BadParameter("No machines available for the selected team")
    if len(machines) == 1:
        machine = machines[0]
        machine_id_value = str(_machine_id(machine))
        machine_name_value = _machine_name(machine)
        if persist_default:
            config.default_machine_ids[team_id] = machine_id_value
            if machine_name_value:
                config.default_machine_names[machine_id_value] = machine_name_value
            save_config(config, config_path)
            label = f'"{machine_name_value}"' if machine_name_value else machine_id_value
            typer.echo(
                f"Configured single machine {label} ({machine_id_value}) as default.",
                err=True,
            )
        return machine_id_value

    names = ", ".join(_describe_machine(machine) for machine in machines)
    raise typer.BadParameter(
        f"Multiple machines available ({names}). Specify --machine-id or --machine-name."
    )


def _list_teams(client) -> list[Any]:
    response = get_v1_teams.sync(client=client)
    if not response or response.data is UNSET or response.data is None:
        return []
    return list(response.data)


def _list_machines(client, team_id: str) -> list[Any]:
    response = get_v1_teams_team_id_machines.sync(client=client, team_id=team_id)
    if not response or response.data is UNSET or response.data is None:
        return []
    return list(response.data)


def _match_by_name(teams: Iterable[Any], name: str) -> str | None:
    lowered = name.lower()
    matches = [team for team in teams if (_team_name(team) or "").lower() == lowered]
    if not matches:
        return None
    if len(matches) > 1:
        options = ", ".join(_describe_team(team) for team in matches)
        raise typer.BadParameter(
            f"Team name '{name}' is ambiguous. Matches: {options}. Use --team-id instead."
        )
    return str(_team_id(matches[0]))


def _match_machine_by_name(machines: Iterable[Any], name: str) -> str | None:
    lowered = name.lower()
    matches = [machine for machine in machines if (_machine_name(machine) or "").lower() == lowered]
    if not matches:
        return None
    if len(matches) > 1:
        options = ", ".join(_describe_machine(machine) for machine in matches)
        raise typer.BadParameter(
            f"Machine name '{name}' is ambiguous. Matches: {options}. Use --machine-id instead."
        )
    return str(_machine_id(matches[0]))


def _team_name(team: Any) -> str | None:
    data = serialize(team)
    attributes = data.get("attributes") or {}
    value = attributes.get("name")
    return str(value) if value is not None else None


def _team_id(team: Any) -> str:
    data = serialize(team)
    return str(data.get("id"))


def _machine_name(machine: Any) -> str | None:
    data = serialize(machine)
    attributes = data.get("attributes") or {}
    value = attributes.get("name")
    return str(value) if value is not None else None


def _machine_id(machine: Any) -> str:
    data = serialize(machine)
    return str(data.get("id"))


def _describe_team(team: Any) -> str:
    name = _team_name(team)
    team_id = _team_id(team)
    return f"{name or 'unnamed'} ({team_id})"


def _describe_machine(machine: Any) -> str:
    name = _machine_name(machine)
    machine_id = _machine_id(machine)
    data = serialize(machine)
    attributes = data.get("attributes") or {}
    brand = attributes.get("brand")
    parts = [part for part in (brand, name) if part]
    label = " ".join(parts) if parts else machine_id
    return f"{label} ({machine_id})"


def _machine_name_from_config(config: CLIConfig, machine_id: str | None) -> str | None:
    if not machine_id:
        return None
    return config.default_machine_names.get(machine_id)


def _find_machine_by_id(machines: Iterable[Any] | None, machine_id: str) -> Any | None:
    if not machines:
        return None
    for machine in machines:
        if str(_machine_id(machine)) == machine_id:
            return machine
    return None
