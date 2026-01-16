from __future__ import annotations

import typer

from .commands import auth, devices, files, imports, journals, machines, me, patients, teams
from .options import CONTEXT_SETTINGS

app = typer.Typer(
    help="SleepHQ command-line interface",
    no_args_is_help=True,
    context_settings=CONTEXT_SETTINGS,
)
app.add_typer(auth.app, name="auth")
app.add_typer(me.app, name="me")
app.add_typer(teams.app, name="teams")
app.add_typer(devices.app, name="devices")
app.add_typer(machines.app, name="machines")
app.add_typer(imports.app, name="imports")
app.add_typer(files.app, name="files")
app.add_typer(journals.app, name="journals")
app.add_typer(patients.app, name="patients")


@app.callback()
def main() -> None:
    """SleepHQ CLI entry point."""
    # Currently no global options, but this allows future expansion.
    return None
