from __future__ import annotations

import typer
from click import get_current_context


def parse_fields(field_string: str) -> list[str]:
    return [field.strip() for field in field_string.split(",") if field.strip()]


def coerce_int(value: str, label: str) -> int:
    try:
        return int(value)
    except ValueError as exc:  # pragma: no cover - defensive
        raise typer.BadParameter(f"{label} must be numeric, got '{value}'") from exc


def usage_error(message: str) -> None:
    ctx = get_current_context()
    typer.echo(f"Error: {message}\n", err=True)
    typer.echo(ctx.get_help(), err=True)
    raise typer.Exit(code=2)
