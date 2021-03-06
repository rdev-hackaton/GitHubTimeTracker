import importlib
import json
import os
import re


class ConfigFileDataError(Exception):
    """
    There are some error with data in config file i.e. bad structure.
    """


class BackendConfig:
    """
    Class representing config of single Backend
    """

    def __init__(self, conf_dict):
        try:
            self.name = conf_dict['name']
            self.module_path = conf_dict['module_path']
        except KeyError as e:
            raise ConfigFileDataError(
                "Backend definition in config file must have {}!"
                .format(e)
            )
        pattern = conf_dict.get('repo_name_pattern', None)
        self.repo_name_pattern = re.compile(pattern) if pattern else None
        self.default = conf_dict.get('default', False)
        self._module = None

    @property
    def module(self):
        """
        Returns backend module
        """
        if not self._module:
            try:
                self._module = importlib.import_module(self.module_path)
            except ImportError:
                try:
                    module_name, attr_name = self.module_path.rsplit('.', 1)
                    module = importlib.import_module(module_name)
                    self._module = getattr(module, attr_name)
                except (AttributeError, ImportError, ValueError):
                    raise ImportError(
                        "Can't import '{}'."
                        " Maybe module_path of {} backend"
                        " in config file is invalid?"
                        .format(self.module_path, self.name)
                    )
        return self._module


class Backends:
    """
    Class representing collection of backends
    """

    class BackendDoesNotExist(Exception):
        pass

    def __init__(self):
        self._backends = []
        self._default_name = ''

    def __iter__(self):
        for backend in self._backends:
            yield backend

    @property
    def default(self):
        """
        Returns default backend or - if there is
        no default specified - first in collection
        """
        if not self._default_name:
            try:
                return self._backends[0]
            except IndexError:
                return None
        return getattr(self, self._default_name)

    def add(self, backend):
        """
        Adds backend to collection,
        set default if backend is default
        """
        assert isinstance(backend, BackendConfig), \
            "Backend should be instance of BackendConfig"
        self._backends.append(backend)
        setattr(self, backend.name, backend)
        if backend.default:
            self.set_default(backend)

    def set_default(self, backend):
        """
        Sets default using backend name or backend config object
        """
        if isinstance(backend, str) and hasattr(self, backend):
            self._default_name = backend
        elif isinstance(backend, BackendConfig) and backend in self._backends:
            self._default_name = backend.name
        else:
            raise TypeError(
                "Default backend need to be"
                " string or BackendConfig instance"
                " and must be already registered backend."
            )

    def get_backend_config(self, backend_name=None):
        """
        Returns backend config object.
        If no backend_name specified returns default.
        Raises exception if backend does not exist in collection.
        """
        if not backend_name:
            return self.default

        for backend in self._backends:
            if backend.name == backend_name:
                return backend
            elif backend.repo_name_pattern and \
                    backend.repo_name_pattern.match(backend_name):
                return backend

        raise self.BackendDoesNotExist(
            "Backend '{}' does not exist".format(backend_name))


class Config:
    """
    Class representing config
    """

    def __init__(self, file_name=None):
        file_name = file_name or os.path.join(
            os.path.dirname(os.path.realpath(__file__)), 'config.json')
        self.backends = Backends()
        self._process_config_file(file_name)

    def _process_config_file(self, file_name):
        """
        Gets config file and process it
        """
        with open(file_name) as config_file:
            config_dict = json.load(config_file)
        self._process_config_dict(config_dict)

    def _process_config_dict(self, config_dict):
        """
        Processes dict loaded from json file
        """
        try:
            self._process_backends(config_dict['BACKENDS'])
        except KeyError:
            raise ConfigFileDataError(
                "Config file should have BACKENDS list specified.")

    def _process_backends(self, backends):
        """
        Processes backends list.
        Adds every backend on the list to the backends collection.
        """
        for backend in backends:
            self.backends.add(BackendConfig(backend))

    def get_backend(self, backend_name=None):
        """
        Returns specified backend module.
        """
        return self.backends.get_backend_config(backend_name).module
