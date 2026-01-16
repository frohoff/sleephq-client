from __future__ import annotations

import json
import os
import hashlib
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

import pytest
from typer.testing import CliRunner

from sleephq_cli.app import app
from sleephq_cli.pagination import PaginationResult

runner = CliRunner()
E2E_MODE = os.getenv("SLEEPHQ_CLI_E2E") == "1"


def invoke_cli(*args: str):
    return runner.invoke(app, args)


if not E2E_MODE:
    @pytest.fixture(autouse=True)
    def mock_session(monkeypatch):  # type: ignore[no-redef]
        client = mock.Mock(name="client")
        config = SimpleNamespace(
            default_team_id=None,
            default_team_name=None,
            default_machine_ids={},
            default_machine_names={},
        )
        path = Path("/tmp/config")

        def fake_get_authenticated_client(*_args, **_kwargs):
            return client, config, path

        monkeypatch.setattr(
            "sleephq_cli.session.get_authenticated_client",
            fake_get_authenticated_client,
        )
        yield


def make_team(name: str = "Team 1") -> SimpleNamespace:
    class Attrs:
        def to_dict(self):
            return {"name": name, "time_zone": "UTC"}

    return SimpleNamespace(id="team_1", attributes=Attrs(), type_="team")


def make_import(status: str) -> dict[str, object]:
    return {
        "data": {
            "attributes": {
                "status": status,
                "created_at": "2024-01-01T00:00:00Z",
                "team_id": 1,
                "machine_id": 2,
                "progress": 50,
            },
            "id": "import_1",
        }
    }


def test_teams_list_uses_limit(monkeypatch):
    team = make_team()
    if E2E_MODE:
        pytest.skip("mocked pagination test")

    pagination_result = PaginationResult(items=[team], has_more=False, last_page=1)

    mock_collect = mock.MagicMock(return_value=pagination_result)
    monkeypatch.setattr(
        "sleephq_cli.commands.teams.collect_paginated",
        mock_collect,
    )
    monkeypatch.setattr(
        "sleephq_cli.commands.teams.print_pagination_hint",
        lambda *_args, **_kwargs: None,
    )

    result = invoke_cli("teams", "list", "--format", "json", "--limit", "1")

    assert result.exit_code == 0
    options = mock_collect.call_args.kwargs["options"]
    assert options.limit == 1
    assert "Team 1" in result.stdout


def test_import_show_watch_default_interval(monkeypatch):
    if E2E_MODE:
        pytest.skip("mocked watch behavior")

    responses = [make_import("pending"), make_import("complete")]

    def fake_call_with_backoff(func):
        _ = func  # unused
        payload = responses.pop(0)
        return SimpleNamespace(parsed=payload)

    monkeypatch.setattr(
        "sleephq_cli.commands.imports.call_with_backoff",
        fake_call_with_backoff,
    )

    result = invoke_cli("imports", "show", "123", "--format", "json", "--watch")

    assert result.exit_code == 0
    assert "poll every 5" in result.stderr
    assert "Status: pending" in result.stderr
    assert '"status": "complete"' in result.stdout


def test_import_show_watch_custom_interval(monkeypatch):
    if E2E_MODE:
        pytest.skip("mocked watch behavior")
    responses = [make_import("processing"), make_import("complete")]

    monkeypatch.setattr(
        "sleephq_cli.commands.imports.call_with_backoff",
        lambda func: SimpleNamespace(parsed=responses.pop(0)),
    )

    result = invoke_cli(
        "imports", "show", "123", "--format", "json", "--watch", "--watch-interval", "2"
    )

    assert result.exit_code == 0
    assert "poll every 2" in result.stderr
    assert "Status: processing" in result.stderr


def test_import_show_watch_requires_positive_interval():
    if E2E_MODE:
        pytest.skip("mocked watch behavior")
    with mock.patch(
        "sleephq_cli.commands.imports.call_with_backoff",
        return_value=SimpleNamespace(parsed=make_import("pending")),
    ):
        result = invoke_cli(
            "imports",
            "show",
            "123",
            "--watch",
            "--watch-interval",
            "0",
        )
    assert result.exit_code != 0
    assert "must be positive" in result.stderr


def test_import_upload_requires_input():
    result = invoke_cli("imports", "upload", "--team-id", "1")
    assert result.exit_code != 0
    assert "Provide --files or at least one PATH" in result.stderr


def test_import_upload_single_file(tmp_path: Path, monkeypatch):
    if E2E_MODE:
        pytest.skip("mocked upload behavior")

    file_path = tmp_path / "foo.edf"
    file_path.write_text("hello world")

    monkeypatch.setattr(
        "sleephq_cli.commands.imports.resolve_team_id",
        lambda **_kwargs: "1",
    )

    import_mock = mock.MagicMock(
        return_value=SimpleNamespace(data=SimpleNamespace(id="42"))
    )
    monkeypatch.setattr(
        "sleephq_cli.commands.imports.post_v1_teams_team_id_imports.sync",
        import_mock,
    )

    upload_mock = mock.MagicMock()
    monkeypatch.setattr(
        "sleephq_cli.commands.imports.post_v1_imports_import_id_files.sync",
        upload_mock,
    )

    process_mock = mock.MagicMock()
    monkeypatch.setattr(
        "sleephq_cli.commands.imports.post_v1_imports_id_process_files.sync",
        process_mock,
    )

    watch_mock = mock.MagicMock()
    monkeypatch.setattr(
        "sleephq_cli.commands.imports._watch_import_status",
        watch_mock,
    )

    result = invoke_cli(
        "imports",
        "upload",
        "--team-id",
        "1",
        "--files",
        str(tmp_path),
        "--device-id",
        "17",
        "--name",
        "CLI Import",
        "--skip-process",
        "--yes",
    )

    assert result.exit_code == 0

    import_body = import_mock.call_args.kwargs["body"]
    assert import_body.device_id == 17
    assert import_body.name == "CLI Import"

    upload_body = upload_mock.call_args.kwargs["body"]
    assert upload_body.name == file_path.name
    assert upload_body.path == "./"
    expected_hash = hashlib.md5()
    expected_hash.update(file_path.read_bytes())
    expected_hash.update(file_path.name.encode("utf-8"))
    assert upload_body.content_hash == expected_hash.hexdigest()

    process_mock.assert_not_called()
    watch_mock.assert_not_called()


def test_import_upload_positional_paths(monkeypatch, tmp_path: Path):
    if E2E_MODE:
        pytest.skip("mocked upload behavior")

    root = tmp_path / "workspace"
    root.mkdir()
    file_path = root / "nested" / "night.edf"
    file_path.parent.mkdir()
    file_path.write_text("hello world")

    monkeypatch.chdir(root)
    monkeypatch.setattr(
        "sleephq_cli.commands.imports.resolve_team_id",
        lambda **_kwargs: "1",
    )

    import_mock = mock.MagicMock(
        return_value=SimpleNamespace(data=SimpleNamespace(id="42"))
    )
    monkeypatch.setattr(
        "sleephq_cli.commands.imports.post_v1_teams_team_id_imports.sync",
        import_mock,
    )
    upload_mock = mock.MagicMock()
    monkeypatch.setattr(
        "sleephq_cli.commands.imports.post_v1_imports_import_id_files.sync",
        upload_mock,
    )
    process_mock = mock.MagicMock()
    monkeypatch.setattr(
        "sleephq_cli.commands.imports.post_v1_imports_id_process_files.sync",
        process_mock,
    )
    watch_mock = mock.MagicMock()
    monkeypatch.setattr(
        "sleephq_cli.commands.imports._watch_import_status",
        watch_mock,
    )

    result = invoke_cli(
        "imports",
        "upload",
        "--team-id",
        "1",
        "nested/night.edf",
        "--skip-process",
        "--yes",
    )

    assert result.exit_code == 0
    upload_body = upload_mock.call_args.kwargs["body"]
    assert upload_body.name == "night.edf"
    assert upload_body.path == "./nested/"


def test_import_upload_directory_argument(monkeypatch, tmp_path: Path):
    if E2E_MODE:
        pytest.skip("mocked upload behavior")

    root = tmp_path / "payload"
    (root / "sub").mkdir(parents=True)
    (root / "sub" / "night.edf").write_text("hello")
    (root / "sub" / "notes.txt").write_text("ignore")

    monkeypatch.chdir(root.parent)
    monkeypatch.setattr(
        "sleephq_cli.commands.imports.resolve_team_id",
        lambda **_kwargs: "1",
    )
    import_mock = mock.MagicMock(
        return_value=SimpleNamespace(data=SimpleNamespace(id="42"))
    )
    monkeypatch.setattr(
        "sleephq_cli.commands.imports.post_v1_teams_team_id_imports.sync",
        import_mock,
    )
    upload_mock = mock.MagicMock()
    monkeypatch.setattr(
        "sleephq_cli.commands.imports.post_v1_imports_import_id_files.sync",
        upload_mock,
    )
    process_mock = mock.MagicMock()
    monkeypatch.setattr(
        "sleephq_cli.commands.imports.post_v1_imports_id_process_files.sync",
        process_mock,
    )
    watch_mock = mock.MagicMock()
    monkeypatch.setattr(
        "sleephq_cli.commands.imports._watch_import_status",
        watch_mock,
    )

    result = invoke_cli(
        "imports",
        "upload",
        "--team-id",
        "1",
        "payload/sub",
        "--skip-process",
        "--yes",
    )

    assert result.exit_code == 0
    assert upload_mock.call_count == 2
    uploaded_paths = sorted(
        (
            call.kwargs["body"].name,
            call.kwargs["body"].path,
        )
        for call in upload_mock.call_args_list
    )
    assert uploaded_paths == [
        ("night.edf", "./payload/sub/"),
        ("notes.txt", "./payload/sub/"),
    ]


def test_import_upload_filters_with_files(monkeypatch, tmp_path: Path):
    if E2E_MODE:
        pytest.skip("mocked upload behavior")

    root = tmp_path / "export"
    (root / "keep").mkdir(parents=True)
    (root / "drop").mkdir()
    keep_file = root / "keep" / "first.edf"
    keep_file.write_text("hello")
    (root / "drop" / "second.edf").write_text("ignored")

    monkeypatch.setattr(
        "sleephq_cli.commands.imports.resolve_team_id",
        lambda **_kwargs: "1",
    )
    import_mock = mock.MagicMock(
        return_value=SimpleNamespace(data=SimpleNamespace(id="42"))
    )
    monkeypatch.setattr(
        "sleephq_cli.commands.imports.post_v1_teams_team_id_imports.sync",
        import_mock,
    )
    upload_mock = mock.MagicMock()
    monkeypatch.setattr(
        "sleephq_cli.commands.imports.post_v1_imports_import_id_files.sync",
        upload_mock,
    )
    process_mock = mock.MagicMock()
    monkeypatch.setattr(
        "sleephq_cli.commands.imports.post_v1_imports_id_process_files.sync",
        process_mock,
    )
    watch_mock = mock.MagicMock()
    monkeypatch.setattr(
        "sleephq_cli.commands.imports._watch_import_status",
        watch_mock,
    )

    result = invoke_cli(
        "imports",
        "upload",
        "--team-id",
        "1",
        "--files",
        str(root),
        "keep",
        "--skip-process",
        "--yes",
    )

    assert result.exit_code == 0
    assert upload_mock.call_count == 1
    upload_body = upload_mock.call_args.kwargs["body"]
    assert upload_body.name == "first.edf"
    assert upload_body.path == "./keep/"


def test_import_upload_filters_with_files_using_prefixed_path(monkeypatch, tmp_path: Path):
    if E2E_MODE:
        pytest.skip("mocked upload behavior")

    root = tmp_path / "export"
    (root / "keep").mkdir(parents=True)
    keep_file = root / "keep" / "first.edf"
    keep_file.write_text("hello")

    monkeypatch.setattr(
        "sleephq_cli.commands.imports.resolve_team_id",
        lambda **_kwargs: "1",
    )
    import_mock = mock.MagicMock(
        return_value=SimpleNamespace(data=SimpleNamespace(id="42"))
    )
    monkeypatch.setattr(
        "sleephq_cli.commands.imports.post_v1_teams_team_id_imports.sync",
        import_mock,
    )
    upload_mock = mock.MagicMock()
    monkeypatch.setattr(
        "sleephq_cli.commands.imports.post_v1_imports_import_id_files.sync",
        upload_mock,
    )
    process_mock = mock.MagicMock()
    monkeypatch.setattr(
        "sleephq_cli.commands.imports.post_v1_imports_id_process_files.sync",
        process_mock,
    )
    watch_mock = mock.MagicMock()
    monkeypatch.setattr(
        "sleephq_cli.commands.imports._watch_import_status",
        watch_mock,
    )

    # Run the CLI from the parent directory so the filter includes the root name
    monkeypatch.chdir(root.parent)
    prefixed = root.name + "/keep"

    result = invoke_cli(
        "imports",
        "upload",
        "--team-id",
        "1",
        "--files",
        str(root),
        prefixed,
        "--skip-process",
        "--yes",
    )

    assert result.exit_code == 0
    assert upload_mock.call_count == 1
    upload_body = upload_mock.call_args.kwargs["body"]
    assert upload_body.name == "first.edf"
    assert upload_body.path == "./keep/"


def test_files_list_does_not_resolve_team_when_import_specified(monkeypatch):
    if E2E_MODE:
        pytest.skip("mocked pagination test")

    pagination_result = PaginationResult(
        items=[{"id": "file_1", "attributes": {"name": "foo", "size": 1, "content_hash": "abc"}}],
        has_more=False,
        last_page=1,
    )
    mock_collect = mock.MagicMock(return_value=pagination_result)
    monkeypatch.setattr(
        "sleephq_cli.commands.files.collect_paginated",
        mock_collect,
    )
    mock_resolve_team = mock.MagicMock()
    monkeypatch.setattr("sleephq_cli.commands.files.resolve_team_id", mock_resolve_team)

    result = invoke_cli(
        "files", "list", "--import-id", "5", "--limit", "1", "--format", "json"
    )

    assert result.exit_code == 0
    options = mock_collect.call_args.kwargs["options"]
    assert options.limit == 1
    mock_resolve_team.assert_not_called()


@pytest.mark.skipif(not E2E_MODE, reason="requires SLEEPHQ_CLI_E2E=1 and valid SleepHQ credentials")
def test_e2e_me_show_json():
    result = invoke_cli("me", "show", "--format", "json")
    assert result.exit_code == 0
    data = json.loads(result.stdout)
    assert "id" in data


@pytest.mark.skipif(not E2E_MODE, reason="requires SLEEPHQ_CLI_E2E=1 and valid SleepHQ credentials")
def test_e2e_teams_list_limit():
    result = invoke_cli("teams", "list", "--format", "json", "--limit", "1")
    assert result.exit_code == 0
    teams = json.loads(result.stdout)
    assert isinstance(teams, list)
    assert teams
