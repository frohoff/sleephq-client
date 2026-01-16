# sleephq

SleepHQ is an online platform for CPAP users to view, share, and analyze therapy data. This repo provides both a Typer-based CLI (`sleephq`) and a typed Python client library so you can automate authentication, machine management, import processing, and data retrieval.

## Getting Started

### Installation

```bash
pip install git+https://github.com/frohoff/python-sleephq-client.git
# or
uv add git+https://github.com/frohoff/python-sleephq-client.git
```

### CLI

```bash
# 1. Authenticate (stores credentials + token)
sleephq auth login

# 2. List registered machines (team auto-resolved when only one exists)
sleephq machines list --format table --limit 5

# 3. Create/upload files into an import and watch processing
sleephq imports upload --team-id <team-id> --files ./oscar-export --process --watch --watch-interval 2 --yes
sleephq files list --import-id <import-id-from-upload> --limit 5 --format json

# 4. Retrieve machine medical analysis data (machine_dates)
sleephq machines sleep --machine-id <machine-id> --limit 5 --format json
```

Highlights:
- Shared authentication config plus environment overrides (`SLEEPHQ_CLIENT_ID`, etc.).
- Pagination helpers on every list command (`--page`, `--page-size`, `--limit`, `--all`) with hints when more data exists.
- `sleephq imports upload` creates imports from local directories/archives via `--files` (or explicit PATH arguments for files/directories, with recursive walking—even when filters include the `--files` root name), confirms the exact files to send, and can trigger processing + watch status.
- Entity lookups (`--team-name`, `--machine-name`) auto-resolve IDs and cache single-choice defaults.
- Import monitoring uses `--watch/--watch-interval` to poll until the API reports `complete`/`failed`.

See [docs/cli.md](docs/cli.md) for the full command tree, optional end-to-end tests (`SLEEPHQ_CLI_E2E=1`), and configuration details.

### Library

```python
from pathlib import Path

from sleephq import create_client
from sleephq.api.machines import get_v1_teams_team_id_machines
from sleephq.api.machine_dates import get_v1_machines_machine_id_machine_dates
from sleephq.api.imports import (
    post_v1_teams_team_id_imports,
    post_v1_imports_id_process_files,
)
from sleephq.api.import_files import post_v1_imports_import_id_files
from sleephq.types import File

# 1. Authenticate
client = create_client(client_id="your_client_id", client_secret="your_client_secret")

# 2. List machines for a team
team_id = 12345
machines = get_v1_teams_team_id_machines.sync(client=client, team_id=team_id)
first_machine = machines.data[0].id if machines.data else None

# 3. Import and process files
import_resp = post_v1_teams_team_id_imports.sync(client=client, team_id=team_id)
import_id = import_resp.data.id
with Path("night.zip").open("rb") as fh:
    post_v1_imports_import_id_files.sync(
        client=client,
        import_id=import_id,
        files={"file": File(payload=fh, file_name="night.zip")},
    )
post_v1_imports_id_process_files.sync(client=client, id=import_id)

# 4. Retrieve machine medical analysis data (machine_dates)
if first_machine:
    dates = get_v1_machines_machine_id_machine_dates.sync(
        client=client, machine_id=int(first_machine), per_page=5
    )
```

Highlights:
- `create_client()` handles OAuth token exchange; use `get_token()` + `AuthenticatedClient` for manual control.
- Every SleepHQ endpoint is available under `sleephq.api.*` with sync/async variants and typed models.
- Integration tests (`uv run pytest tests/test_integration.py -v`) exercise the live API via `SLEEPHQ_CLIENT_ID/SECRET`.

See [docs/library.md](docs/library.md) for more authentication patterns, endpoint examples, and testing instructions.
