import os
import pytest

from time_tracker.config import BackendConfig, Backends, Config, ConfigFileDataError


class TestBackendConfig:

    # Helpers

    def assert_repo_name_pattern(self, config_dict, backend_config):
        pattern = config_dict.get('repo_name_pattern', None)
        if not pattern:
            assert backend_config.repo_name_pattern is None
        else:
            assert backend_config.repo_name_pattern
            assert backend_config.repo_name_pattern.pattern == pattern

    # Tests

    @pytest.mark.parametrize('config_dict', [
        {'name': 'Dummy'},
        {'module_path': 'dummy'},
        {}
    ])
    def test_creating_backend_config_fail(self, config_dict):
        with pytest.raises(ConfigFileDataError):
            BackendConfig(config_dict)

    @pytest.mark.parametrize('config_dict', [
        {'name': 'Dummy', 'module_path': 'tests.dummy_backend'},
        {'name': 'Dummy', 'module_path': 'tests.dummy_backend',
         'repo_name_pattern': ''},
        {'name': 'Dummy', 'module_path': 'tests.dummy_backend',
         'repo_name_pattern': 'dummy'},
        {'name': 'Dummy', 'module_path': 'tests.dummy_backend',
         'repo_name_pattern': '', 'default': True},
        {'name': 'Dummy', 'module_path': 'tests.dummy_backend.DummyBackend'}
    ])
    def test_creating_backend_config_success(self, config_dict):
        backend_config = BackendConfig(config_dict)
        assert config_dict['name'] == backend_config.name
        assert config_dict['module_path'] == backend_config.module_path
        self.assert_repo_name_pattern(config_dict, backend_config)
        assert config_dict.get('default', False) == backend_config.default
        assert backend_config.module

    @pytest.mark.parametrize('config_dict', [
        {'name': 'Dummy', 'module_path': 'tests.goofy_backend'},
        {'name': 'Dummy', 'module_path': 'tests.goofy_backend.GoofyClass'},
    ])
    def test_creating_backend_config_fail_import(self, config_dict):
        with pytest.raises(ImportError):
            BackendConfig(config_dict).module


class TestBackends:

    # Helpers

    def build_backends(self, backends_list):
        backends = Backends()
        for backend_dict in backends_list:
            backends.add(BackendConfig(backend_dict))
        return backends

    # Fixtures

    @pytest.fixture("class")
    def backends(self):
        backends_list = [
            {'name': 'Dummy', 'module_path': 'tests.dummy_backend'},
            {'name': 'Goofy', 'module_path': 'tests.dummy_backend'},
            {'name': 'Spooky', 'module_path': 'tests.dummy_backend'}
        ]
        return self.build_backends(backends_list)

    # Tests

    def test_backends_add_success(self):
        backends = Backends()
        backends.add(BackendConfig({'name': 'Aloha', 'module_path': 'dummy'}))
        assert backends.Aloha
        assert list(backends)

    @pytest.mark.parametrize("backend", [
        12,
        "asdasd",
        object(),
        {'name': 'Aloha', 'module_path': 'dummy'},
        ['name'],
        ('name', 'Aloha')
    ])
    def test_backends_add_fail(self, backend, backends):
        with pytest.raises(AssertionError):
            backends.add(backend)

    def test_backends_default_from_config(self):
        backends_list = [
            {'name': 'Dummy', 'module_path': 'tests.dummy_backend'},
            {'name': 'Goofy', 'module_path': 'tests.dummy_backend', 'default': True},
        ]
        backends = self.build_backends(backends_list)
        assert backends.Dummy
        assert backends.Goofy
        assert backends.default
        assert backends.default == backends.Goofy

    def test_backends_default_unset(self):
        backends_list = [
            {'name': 'Dummy', 'module_path': 'tests.dummy_backend'},
            {'name': 'Goofy', 'module_path': 'tests.dummy_backend'},
        ]
        backends = self.build_backends(backends_list)
        assert backends.Dummy
        assert backends.Goofy
        assert backends.default
        assert backends.default == backends.Dummy
        assert backends.default == backends._backends[0]

    def test_backends_default_none(self):
        backends = self.build_backends([])
        assert not list(backends)
        assert backends.default is None

    def test_backends_iter(self, backends):
        for backend in backends:
            assert backend == getattr(backends, backend.name)

    @pytest.mark.parametrize("backend", [
        12,
        "asdasd",
        object(),
        BackendConfig({'name': 'Hello', 'module_path': 'tests.dummy_backend'})
    ])
    def test_backends_set_default_fail(self, backends, backend):
        with pytest.raises(TypeError):
            backends.set_default(backend)

    @pytest.mark.parametrize("backend", [
        "Dummy",
        "Goofy",
        "Spooky"
    ])
    def test_backends_set_default_success_string(self, backends, backend):
        backends.set_default(backend)
        assert backends.default == getattr(backends, backend)

    @pytest.mark.parametrize("backend_index", [
        0, 1, 2
    ])
    def test_backends_set_default_success_backend(self, backends, backend_index):
        backend = backends._backends[backend_index]
        backends.set_default(backend)
        assert backends.default == backend

    @pytest.mark.parametrize("backend_name", [
        "Dummy",
        "Goofy",
        "Spooky"
    ])
    def test_get_backend_config_from_name(self, backends, backend_name):
        assert backends.get_backend_config(backend_name)

    def test_get_backend_config_default(self, backends):
        backend = backends.get_backend_config()
        assert backend
        assert backend == backends.default

    def test_get_backend_config_fail(self, backends):
        with pytest.raises(Backends.BackendDoesNotExist):
            backends.get_backend_config("Aloha")


class TestConfig:

    # Fixtures

    @pytest.fixture("class")
    def file_path(self):
        return os.path.dirname(os.path.realpath(__file__))

    # Tests

    @pytest.mark.parametrize("file_name", [
        "config.json",
        "configs/config.json"
    ])
    def test_config_create_and_get_backend(self, file_name, file_path):
        path = os.path.join(file_path, file_name)
        assert Config(path).get_backend("Goofy")

    def test_config_no_backends(self, file_path):
        path = os.path.join(file_path, "configs/config_no_backends.json")
        with pytest.raises(ConfigFileDataError):
            Config(path)

    def test_config_get_backend_fail(self, file_path):
        path = os.path.join(file_path, "config.json")
        with pytest.raises(Backends.BackendDoesNotExist):
            Config(path).get_backend("Aloha")