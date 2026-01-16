# SleepHQ CLI

The `sleephq` command-line interface wraps the Python SDK with Typer-based ergonomics.

## Installation

Installing the package exposes the CLI:

```bash
pip install git+https://github.com/frohoff/python-sleephq-client.git
# or
uv add git+https://github.com/frohoff/python-sleephq-client.git
```

## Usage

```bash
$ sleephq auth login
SleepHQ client ID: your_client_id
SleepHQ client secret: ********
Requesting token from SleepHQ…
Credentials saved. Token expires at 2024-05-01T12:34:56+00:00

$ sleephq me show
╭──────────────┬────────────────────────────╮
│ Field        │ Value                      │
├──────────────┼────────────────────────────┤
│ id           │ 12345                      │
│ email        │ you@example.com            │
│ name         │ Example User               │
│ timezone     │ Australia/Sydney           │
╰──────────────┴────────────────────────────╯

$ sleephq teams list --format json
[
  {"id": "team_123", "name": "SleepHQ Home", "timezone": "Australia/Sydney"}
]
```

### Key Command Groups

- `sleephq auth login|status|logout`
- `sleephq me show`
- `sleephq teams list`
- `sleephq devices list`
- `sleephq machines list|show|sleep`
- `sleephq imports list|show --watch --watch-interval N|upload`
- `sleephq files list|show`
- `sleephq journals list|show`
- `sleephq patients list`

### Common Flags

- Pagination: `--page`, `--page-size`, `--limit`, `--all`
- Output format: `--format table|json`
- Entity selection: `--team-id/--team-name`, `--machine-id/--machine-name`
- Watching imports: `--watch [--watch-interval N]`

### Imports Workflow

```bash
# Upload every file under ./oscar-export, trigger processing, and watch until complete
sleephq imports upload --team-id <team-id> --files ./oscar-export --process --watch --watch-interval 2 --yes

# Inspect the files that were attached
sleephq files list --import-id <import-id> --limit 5 --format json

# Check final status later
sleephq imports show <import-id> --watch --watch-interval 5
```

`imports upload` accepts a single `--files PATH` (directory or `.zip`) or direct PATH arguments (files or directories, each walked recursively) to upload. When `--files` is set you can pass relative PATH filters to limit which files under that directory are sent; filters may omit or include the root directory name (as long as they still resolve under the source). Without `--files`, the positional PATH arguments resolve relative to the current working directory. The CLI prints a confirmation list (bypass via `--yes/-y`), computes the required content hashes, mirrors the relative directory structure under an optional `--base-path`, and can automatically call `--process/--skip-process` plus `--watch/--watch-interval` to monitor completion.

### Configuration

Credentials and defaults are stored in `~/.config/sleephq/config.toml` (POSIX) or `%APPDATA%\SleepHQ\config.toml` (Windows). Environment variables (`SLEEPHQ_CLIENT_ID`, `SLEEPHQ_CLIENT_SECRET`, `SLEEPHQ_TOKEN`, etc.) override config values. Use `sleephq auth logout` to clear tokens without removing stored credentials.

## Testing the CLI

Mocked tests (no real API calls):

```bash
uv run python -m pytest tests/test_cli.py -v
```

Optional end-to-end mode:

```bash
export SLEEPHQ_CLIENT_ID="your_client_id"
export SLEEPHQ_CLIENT_SECRET="your_client_secret"
export SLEEPHQ_CLI_E2E=1
uv run python -m pytest tests/test_cli.py -v
```

## Rate Limiting & Pagination

The CLI retries automatically on HTTP 429 responses (respecting `Retry-After` with configurable retries via `SLEEPHQ_RATE_LIMIT_RETRIES`). All list commands support `--limit` and `--all`, and table output emits hints when more pages are available.
