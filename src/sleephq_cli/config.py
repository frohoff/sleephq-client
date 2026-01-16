from __future__ import annotations

from dataclasses import asdict, dataclass, field
from pathlib import Path
import os
import sys
from typing import Any

try:  # Python 3.11+
    import tomllib  # type: ignore[attr-defined]
except ModuleNotFoundError:  # pragma: no cover - fallback for Python 3.10
    import tomli as tomllib  # type: ignore[no-redef]

import tomli_w

DEFAULT_SCOPE = "read write delete"
DEFAULT_BASE_URL = "https://sleephq.com/api"


@dataclass
class CLIConfig:
    client_id: str | None = None
    client_secret: str | None = None
    token: str | None = None
    token_expires_at: int | None = None
    scope: str = DEFAULT_SCOPE
    base_url: str = DEFAULT_BASE_URL
    default_team_id: str | None = None
    default_team_name: str | None = None
    default_machine_ids: dict[str, str] = field(default_factory=dict)
    default_machine_names: dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        # Drop None values to keep the config tidy
        return {key: value for key, value in data.items() if value is not None}

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "CLIConfig":
        return cls(
            client_id=data.get("client_id"),
            client_secret=data.get("client_secret"),
            token=data.get("token"),
            token_expires_at=data.get("token_expires_at"),
            scope=data.get("scope", DEFAULT_SCOPE),
            base_url=data.get("base_url", DEFAULT_BASE_URL),
            default_team_id=data.get("default_team_id"),
            default_team_name=data.get("default_team_name"),
            default_machine_ids=data.get("default_machine_ids", {}) or {},
            default_machine_names=data.get("default_machine_names", {}) or {},
        )


def default_config_path() -> Path:
    if sys.platform.startswith("win"):
        base = os.environ.get("APPDATA")
        base_path = Path(base) if base else Path.home() / "AppData" / "Roaming"
        return base_path / "SleepHQ" / "config.toml"

    base = os.environ.get("XDG_CONFIG_HOME")
    base_path = Path(base) if base else Path.home() / ".config"
    return base_path / "sleephq" / "config.toml"


def load_config(path: Path | None = None) -> CLIConfig:
    config_path = path or default_config_path()
    if not config_path.exists():
        return CLIConfig()
    with config_path.open("rb") as handle:
        data = tomllib.load(handle)
    return CLIConfig.from_dict(data)


def save_config(config: CLIConfig, path: Path | None = None) -> None:
    config_path = path or default_config_path()
    config_path.parent.mkdir(parents=True, exist_ok=True)
    payload = config.to_dict()
    with config_path.open("wb") as handle:
        handle.write(tomli_w.dumps(payload).encode("utf-8"))
