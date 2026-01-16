from __future__ import annotations

import typer

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}

TEAM_ID_OPTION = typer.Option(None, "--team-id", help="Numeric team ID")
TEAM_NAME_OPTION = typer.Option(None, "--team-name", help="Team name to match")

MACHINE_ID_OPTION = typer.Option(None, "--machine-id", help="Numeric machine ID")
MACHINE_NAME_OPTION = typer.Option(None, "--machine-name", help="Machine name to match")

PAGE_OPTION = typer.Option(1, "--page", help="Page number")
PAGE_SIZE_OPTION = typer.Option(None, "--page-size", help="Page size (defaults to command-specific value or SLEEPHQ_PAGE_SIZE)")
LIMIT_OPTION = typer.Option(None, "--limit", help="Maximum number of records to return")
ALL_OPTION = typer.Option(False, "--all", help="Fetch every available page")

WATCH_FLAG = typer.Option(False, "--watch", help="Poll until the resource reaches a terminal status")
WATCH_INTERVAL_OPTION = typer.Option(5.0, "--watch-interval", help="Seconds between polls when using --watch")
