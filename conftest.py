import pytest

from config import Config


@pytest.fixture
def test_config():
    return Config
