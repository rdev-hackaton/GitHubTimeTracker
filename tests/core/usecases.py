import pytest

from tests.core.mock_source import MockSource
from time_tracker.core.results import Result
from time_tracker.core.usecases import get_entries_list, get_total_stats


# TODO - fix those tests to actually test anything
class TestUseCases(object):

    @pytest.mark.parametrize('input_data', [
        {},
        {'committer': 'test'},
        {'issue': '33'},
        {'milestone': 'stoneeed'}
    ])
    def test_get_entries_usecase(self, input_data):
        data_source = MockSource()
        result = get_entries_list(data_source, 'test', **input_data)
        assert result['result'] == Result.OK

    @pytest.mark.parametrize('input_data', [
        {},
        {'committer': 'test'},
        {'issue': '33'},
        {'milestone': 'stoneeed'}
    ])
    def test_get_total_usecase(self, input_data):
        data_source = MockSource()
        result = get_total_stats(data_source, 'test', **input_data)
        assert result['result'] == Result.OK
