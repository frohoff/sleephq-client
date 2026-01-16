from __future__ import annotations

import os
import time
from dataclasses import dataclass
from http import HTTPStatus
from typing import Any, Callable

import typer

from sleephq.types import Response, UNSET

DEFAULT_RATE_LIMIT_RETRIES = int(os.environ.get("SLEEPHQ_RATE_LIMIT_RETRIES", 3))
DEFAULT_PAGE_SIZE_ENV = os.environ.get("SLEEPHQ_PAGE_SIZE")


@dataclass
class PaginationOptions:
    page: int
    page_size: int
    limit: int | None
    fetch_all: bool


@dataclass
class PaginationResult:
    items: list[Any]
    has_more: bool
    last_page: int


def resolve_pagination_options(
    *,
    page: int,
    page_size: int | None,
    default_page_size: int,
    limit: int | None,
    fetch_all: bool,
) -> PaginationOptions:
    if limit is not None and limit <= 0:
        raise typer.BadParameter("--limit must be a positive integer")
    if fetch_all and limit is not None:
        raise typer.BadParameter("Use either --limit or --all, not both")
    if page <= 0:
        raise typer.BadParameter("--page must be positive")

    resolved_page_size = page_size
    if resolved_page_size is None:
        if DEFAULT_PAGE_SIZE_ENV:
            try:
                resolved_page_size = int(DEFAULT_PAGE_SIZE_ENV)
            except ValueError as exc:  # pragma: no cover - defensive
                raise typer.BadParameter(
                    f"Invalid SLEEPHQ_PAGE_SIZE value: {DEFAULT_PAGE_SIZE_ENV}"
                ) from exc
    if resolved_page_size is None:
        resolved_page_size = default_page_size

    if resolved_page_size <= 0:
        raise typer.BadParameter("Page size must be positive")

    return PaginationOptions(
        page=page,
        page_size=resolved_page_size,
        limit=limit,
        fetch_all=fetch_all,
    )


def call_with_backoff(
    fetch: Callable[[], Response[Any]],
    *,
    retries: int | None = None,
) -> Response[Any]:
    max_attempts = retries if retries is not None else DEFAULT_RATE_LIMIT_RETRIES
    attempts = 0
    while True:
        response = fetch()
        if response.status_code != HTTPStatus.TOO_MANY_REQUESTS:
            return response
        attempts += 1
        if attempts > max_attempts:
            typer.echo("Exceeded rate limit retries", err=True)
            raise typer.Exit(code=1)
        retry_after = response.headers.get("Retry-After")
        try:
            wait_seconds = int(retry_after) if retry_after else None
        except ValueError:  # pragma: no cover - defensive
            wait_seconds = None
        if wait_seconds is None:
            wait_seconds = min(60, 2**attempts)
        typer.echo(
            f"Rate limited (HTTP 429). Retrying in {wait_seconds}s...",
            err=True,
        )
        time.sleep(wait_seconds)


def collect_paginated(
    fetch_page: Callable[..., Response[Any]],
    *,
    options: PaginationOptions,
) -> PaginationResult:
    current_page = options.page
    remaining = options.limit
    collected: list[Any] = []
    has_more = False

    while True:
        response = call_with_backoff(
            lambda: fetch_page(page=current_page, per_page=options.page_size)
        )
        parsed = response.parsed
        raw_items: list[Any]
        if parsed is None:
            raw_items = []
        else:
            data = getattr(parsed, "data", UNSET)
            raw_items = [] if data in (UNSET, None) else list(data)

        count = len(raw_items)
        more_available = count == options.page_size
        has_more = more_available

        if remaining is not None:
            to_take = min(count, remaining)
            collected.extend(raw_items[:to_take])
            remaining -= to_take
        else:
            collected.extend(raw_items)

        if remaining is not None and remaining <= 0:
            has_more = more_available or options.fetch_all
            break

        if not options.fetch_all and options.limit is None:
            # Single-page mode
            break

        if not more_available:
            has_more = False
            break

        current_page += 1
        # Continue fetching further pages for --all or --limit
        continue

    return PaginationResult(items=collected, has_more=has_more, last_page=current_page)


def print_pagination_hint(options: PaginationOptions, result: PaginationResult) -> None:
    if options.fetch_all or options.limit is not None:
        return
    if not result.has_more:
        return
    next_page = options.page + 1
    typer.echo(
        f"Page {options.page} complete. Use --page {next_page} or --all for more results.",
        err=True,
    )
