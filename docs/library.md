# SleepHQ Python Client Library

## Installation

```bash
pip install git+https://github.com/frohoff/sleephq-client.git
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv add git+https://github.com/frohoff/sleephq-client.git
```

## Quick Start

```python
from sleephq import create_client
from sleephq.api.teams import get_v1_teams
from sleephq.api.machines import get_v1_teams_team_id_machines

client = create_client(
    client_id="your_client_id",
    client_secret="your_client_secret"
)

teams = get_v1_teams.sync(client=client)
for team in teams.data:
    machines = get_v1_teams_team_id_machines.sync(client=client, team_id=team.id)
    print(team.id, len(machines.data or []))
```

## Authentication

### `create_client()` (Recommended)

```python
from sleephq import create_client

client = create_client(
    client_id="your_client_id",
    client_secret="your_client_secret"
)
```

### `get_token()`

```python
from sleephq import get_token
from sleephq.client import AuthenticatedClient

token = get_token(client_id="...", client_secret="...")
client = AuthenticatedClient(base_url="https://sleephq.com/api", token=token.access_token)
```

### Existing Tokens

```python
from sleephq.client import AuthenticatedClient

client = AuthenticatedClient(
    base_url="https://sleephq.com/api",
    token="your_access_token"
)
```

## Running Tests

```bash
export SLEEPHQ_CLIENT_ID="your_client_id"
export SLEEPHQ_CLIENT_SECRET="your_client_secret"
uv run pytest tests/test_integration.py -v
```

## Type Checking

```bash
uv run mypy src/sleephq
```
