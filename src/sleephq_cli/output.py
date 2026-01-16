from __future__ import annotations

import json
from enum import Enum
from typing import Any, Iterable, Mapping, Sequence

import typer
from rich.console import Console
from rich.table import Table

console = Console()


class OutputFormat(str, Enum):
    TABLE = "table"
    JSON = "json"


def serialize(value: Any) -> Any:
    if value is None:
        return None
    if isinstance(value, (str, int, float, bool)):
        return value
    if hasattr(value, "to_dict"):
        return value.to_dict()
    if isinstance(value, Mapping):
        return {key: serialize(val) for key, val in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [serialize(item) for item in value]
    return str(value)


def echo_item(data: Mapping[str, Any], *, format: OutputFormat, title: str | None = None) -> None:
    payload = {key: serialize(value) for key, value in data.items()}
    if format == OutputFormat.JSON:
        typer.echo(json.dumps(payload, indent=2, sort_keys=True))
        return

    table = Table(show_header=False, title=title, title_justify="left")
    table.add_column("Field", style="bold")
    table.add_column("Value")
    for key, value in _flatten_rows(payload):
        table.add_row(str(key), _stringify(value))
    console.print(table)


def echo_list(
    items: Sequence[Mapping[str, Any]],
    *,
    format: OutputFormat,
    columns: Iterable[str],
    title: str | None = None,
) -> None:
    serialised = [{key: serialize(value) for key, value in item.items()} for item in items]
    if format == OutputFormat.JSON:
        typer.echo(json.dumps(serialised, indent=2))
        return

    table = Table(title=title, title_justify="left")
    normalized_columns = list(columns)
    for column in normalized_columns:
        table.add_column(column)

    for row in serialised:
        values = [_stringify(row.get(column, "")) for column in normalized_columns]
        table.add_row(*values)

    console.print(table)


def _stringify(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, float):
        text = f"{value:.3f}".rstrip("0").rstrip(".")
        return text or "0"
    if isinstance(value, (str, int)):
        return str(value)
    return json.dumps(serialize(value), ensure_ascii=False)


def _flatten_rows(payload: Mapping[str, Any]) -> list[tuple[str, Any]]:
    rows: list[tuple[str, Any]] = []
    for key, value in payload.items():
        rows.extend(_flatten_value(str(key), value))
    return rows


def _flatten_value(prefix: str, value: Any) -> list[tuple[str, Any]]:
    if isinstance(value, Mapping):
        items: list[tuple[str, Any]] = []
        for sub_key, sub_value in value.items():
            dotted = f"{prefix}.{sub_key}"
            items.extend(_flatten_value(dotted, sub_value))
        return items or [(prefix, "")]
    if isinstance(value, list):
        if not value:
            return [(prefix, [])]
        if all(isinstance(item, Mapping) and "id" in item for item in value):
            ids = ", ".join(str(item.get("id")) for item in value)
            return [(prefix, ids)]
        return [(prefix, value)]
    return [(prefix, value)]
