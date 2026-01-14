# sleephq

Python SDK for the [SleepHQ](https://sleephq.com) API.

SleepHQ is an online platform for CPAP users to view, share and analyse their sleep therapy data.

## Installation

```bash
pip install git+https://github.com/frohoff/python-sleephq-client.git
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv add git+https://github.com/frohoff/python-sleephq-client.git
```

## Quick Start

```python
from sleephq import create_client
from sleephq.api.teams import get_v1_teams
from sleephq.api.machines import get_v1_teams_team_id_machines

# Create an authenticated client
client = create_client(
    client_id="your_client_id",
    client_secret="your_client_secret"
)

# Get your teams
teams = get_v1_teams.sync(client=client)
for team in teams.data:
    print(f"Team: {team.attributes.name}")

    # Get machines for each team
    machines = get_v1_teams_team_id_machines.sync(client=client, team_id=team.id)
    for machine in machines.data:
        print(f"  - {machine.attributes.brand} {machine.attributes.name}")
```

## Authentication

### Using `create_client()` (Recommended)

The simplest way to authenticate is using `create_client()`, which handles OAuth token acquisition automatically:

```python
from sleephq import create_client

client = create_client(
    client_id="your_client_id",
    client_secret="your_client_secret"
)
```

### Using `get_token()` Separately

If you need more control over token management:

```python
from sleephq import get_token
from sleephq.client import AuthenticatedClient

# Get token
token = get_token(client_id="...", client_secret="...")
print(f"Token expires in {token.expires_in} seconds")

# Create client with token
client = AuthenticatedClient(
    base_url="https://sleephq.com/api",
    token=token.access_token
)
```

### Using an Existing Token

If you already have an access token:

```python
from sleephq.client import AuthenticatedClient

client = AuthenticatedClient(
    base_url="https://sleephq.com/api",
    token="your_access_token"
)
```

## API Usage

All API endpoints are available as functions in `sleephq.api.*` modules. Each endpoint has:
- `sync()` - Synchronous call, returns parsed response
- `sync_detailed()` - Synchronous call, returns full Response object
- `asyncio()` - Async call, returns parsed response
- `asyncio_detailed()` - Async call, returns full Response object

### Examples

```python
from sleephq import create_client
from sleephq.api.current_user import get_v1_me
from sleephq.api.teams import get_v1_teams
from sleephq.api.machines import get_v1_teams_team_id_machines
from sleephq.api.machine_dates import get_v1_machines_machine_id_machine_dates
from sleephq.api.devices import get_v1_devices

client = create_client(client_id="...", client_secret="...")

# Get current user
me = get_v1_me.sync(client=client)

# List available device types
devices = get_v1_devices.sync(client=client)

# List teams
teams = get_v1_teams.sync(client=client)

# List machines for a team
machines = get_v1_teams_team_id_machines.sync(client=client, team_id="12345")

# Get sleep data for a machine (with pagination)
sleep_data = get_v1_machines_machine_id_machine_dates.sync(
    client=client,
    machine_id="67890",
    page=1,
    per_page=30
)
```

### Async Usage

```python
import asyncio
from sleephq import create_client
from sleephq.api.teams import get_v1_teams

async def main():
    client = create_client(client_id="...", client_secret="...")
    teams = await get_v1_teams.asyncio(client=client)
    for team in teams.data:
        print(team.attributes.name)

asyncio.run(main())
```

## Available Endpoints

### Current User (`sleephq.api.current_user`)
| Function | HTTP | Description |
|----------|------|-------------|
| `get_v1_me` | `GET /v1/me` | Get current user |
| `post_v1_me` | `POST /v1/me` | Update current user |

### Teams (`sleephq.api.teams`)
| Function | HTTP | Description |
|----------|------|-------------|
| `get_v1_teams` | `GET /v1/teams` | List user's teams |

### Machines (`sleephq.api.machines`)
| Function | HTTP | Description |
|----------|------|-------------|
| `get_v1_teams_team_id_machines` | `GET /v1/teams/{team_id}/machines` | List machines for a team |
| `get_v1_machines_id` | `GET /v1/machines/{id}` | Get a specific machine |

### Machine Dates / Sleep Data (`sleephq.api.machine_dates`)
| Function | HTTP | Description |
|----------|------|-------------|
| `get_v1_machines_machine_id_machine_dates` | `GET /v1/machines/{machine_id}/machine_dates` | List sleep data |
| `get_v1_machines_machine_id_machine_dates_date` | `GET /v1/machines/{machine_id}/machine_dates/{date}` | Get sleep data for specific date |
| `get_v1_machine_dates_id` | `GET /v1/machine_dates/{id}` | Get specific sleep data record |
| `put_v1_machine_dates_id` | `PUT /v1/machine_dates/{id}` | Update sleep data record |

### Devices (`sleephq.api.devices`)
| Function | HTTP | Description |
|----------|------|-------------|
| `get_v1_devices` | `GET /v1/devices` | List available device types |

### Imports (`sleephq.api.imports`)
| Function | HTTP | Description |
|----------|------|-------------|
| `get_v1_teams_team_id_imports` | `GET /v1/teams/{team_id}/imports` | List imports for a team |
| `post_v1_teams_team_id_imports` | `POST /v1/teams/{team_id}/imports` | Create a new import |
| `get_v1_imports_id` | `GET /v1/imports/{id}` | Get specific import |
| `delete_v1_imports_id` | `DELETE /v1/imports/{id}` | Delete an import |
| `post_v1_imports_id_process_files` | `POST /v1/imports/{id}/process_files` | Process import files |

### Import Files (`sleephq.api.import_files`)
| Function | HTTP | Description |
|----------|------|-------------|
| `get_v1_teams_team_id_files` | `GET /v1/teams/{team_id}/files` | List files for a team |
| `get_v1_imports_import_id_files` | `GET /v1/imports/{import_id}/files` | List files for an import |
| `post_v1_imports_import_id_files` | `POST /v1/imports/{import_id}/files` | Upload file to import |
| `get_v1_imports_files_id` | `GET /v1/imports/files/{id}` | Get specific file |
| `delete_v1_imports_files_id` | `DELETE /v1/imports/files/{id}` | Delete a file |
| `post_v1_imports_files_calculate_content_hash` | `POST /v1/imports/files/calculate_content_hash` | Calculate file content hash |

### Journals (`sleephq.api.journals`)
| Function | HTTP | Description |
|----------|------|-------------|
| `get_v1_teams_team_id_journals` | `GET /v1/teams/{team_id}/journals` | List journal entries |
| `post_v1_teams_team_id_journals` | `POST /v1/teams/{team_id}/journals` | Create journal entry |
| `get_v1_journals_id` | `GET /v1/journals/{id}` | Get specific journal entry |
| `put_v1_journals_id` | `PUT /v1/journals/{id}` | Update journal entry |

### Patients (`sleephq.api.patients`)
| Function | HTTP | Description |
|----------|------|-------------|
| `get_v1_teams_team_id_patients` | `GET /v1/teams/{team_id}/patients` | List patients for a team |

### Active Storage (`sleephq.api.active_storage`)
| Function | HTTP | Description |
|----------|------|-------------|
| `post_v1_active_storage_blobs` | `POST /v1/active_storage/blobs` | Create active storage blob |

See the [SleepHQ API documentation](https://sleephq.com/api-docs/index.html) for full details.

## Development

### Requirements

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

### Setup

```bash
git clone https://github.com/frohoff/python-sleephq-client.git
cd python-sleephq-client
uv sync
```

### Regenerating the SDK

The SDK is generated from the SleepHQ OpenAPI spec:

```bash
./generate.sh
uv sync
```

### Running Tests

```bash
# Set credentials
export SLEEPHQ_CLIENT_ID="your_client_id"
export SLEEPHQ_CLIENT_SECRET="your_client_secret"

# Run tests
uv run pytest tests/ -v
```

### Type Checking

```bash
uv run mypy src/sleephq
```

## License

MIT
