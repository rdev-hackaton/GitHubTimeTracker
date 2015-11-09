import pytest
from click.testing import CliRunner

from tests.core.mock_source import MockSource

from time_tracker.frontends.cli.tracker import print_time_tracking_info


@pytest.fixture(autouse=True)
def monkeypatch_config(monkeypatch):
    monkeypatch.setattr('time_tracker.config.Config.__init__', lambda *a: None)
    monkeypatch.setattr('time_tracker.config.Config.get_backend',
                        lambda *a: MockSource)


def test_cli():
    runner = CliRunner()
    result = runner.invoke(
        print_time_tracking_info,
        ['--token', 'dummy', '--password', '', '--repo', 'dummy']
    )
    assert not result.exception


def test_cli_total():
    runner = CliRunner()
    result = runner.invoke(
        print_time_tracking_info,
        ['--token', 'dummy', '--password', '', '--repo', 'dummy', '--total']
    )
    assert not result.exception


def test_cli_fail():
    runner = CliRunner()
    result = runner.invoke(
        print_time_tracking_info,
        ['--token', 'dummy', '--password', '', '--repo', 'dummy', '--total',
         '--issue', 'a']
    )
    assert result.exception
