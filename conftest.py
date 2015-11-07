import pytest

from time_tracker.config import Config


@pytest.fixture
def test_config():
    return Config
