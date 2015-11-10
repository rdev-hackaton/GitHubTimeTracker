import click
import pytest

from click.testing import CliRunner
from mock import Mock

from tests.core.mock_source import MockSource

from time_tracker.frontends.cli.tracker import print_time_tracking_info, \
    run_cli
from time_tracker.frontends.cli.options import DependentOption


@pytest.fixture(autouse=True)
def monkeypatch_config(monkeypatch):
    monkeypatch.setattr('time_tracker.config.Config.__init__', lambda *a: None)
    monkeypatch.setattr('time_tracker.config.Config.get_backend',
                        lambda *a: MockSource)


def test_cli():
    runner = CliRunner()
    result = runner.invoke(
        print_time_tracking_info,
        ['--token', 'dummy', '--repo', 'dummy']
    )
    assert not result.exception


def test_cli_total():
    runner = CliRunner()
    result = runner.invoke(
        print_time_tracking_info,
        ['--token', 'dummy', '--repo', 'dummy', '--total']
    )
    assert not result.exception


def test_cli_issue():
    runner = CliRunner()
    result = runner.invoke(
        print_time_tracking_info,
        ['--token', 'dummy', '--repo', 'dummy', '--issue', '1']
    )
    assert not result.exception


def test_cli_milestone():
    runner = CliRunner()
    result = runner.invoke(
        print_time_tracking_info,
        ['--token', 'dummy', '--repo', 'dummy', '--milestone', 'dummy']
    )
    assert not result.exception


def test_cli_committer():
    runner = CliRunner()
    result = runner.invoke(
        print_time_tracking_info,
        ['--token', 'dummy', '--repo', 'dummy', '--committer', 'dummy']
    )
    assert not result.exception


def test_cli_fail():
    runner = CliRunner()
    result = runner.invoke(
        print_time_tracking_info,
        ['--token', 'dummy', '--repo', 'dummy', '--issue', 'a']
    )
    assert result.exception


def test_run_cli(monkeypatch):
    mocked_cli = Mock()
    monkeypatch.setattr(
        'time_tracker.frontends.cli.tracker.print_time_tracking_info',
        mocked_cli)

    run_cli('__main__')
    assert mocked_cli.called


# Options tests

def test_dependent_option_prompt():
    @click.command()
    @click.option('--option', cls=DependentOption, prompt=True,
                  prompt_depends_on=('another', False))
    def test_comm(option):
        pass

    runner = CliRunner()
    result = runner.invoke(
        test_comm,
        input='a'
    )
    assert not result.exception


@pytest.mark.parametrize('value', [1, 'a', [], {}])
def test_dependent_option_create_fail(value):
    with pytest.raises(TypeError):
        DependentOption('--option', prompt_depends_on=value)
