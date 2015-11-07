# -*- coding: utf-8 -*-
# author: Jakub Skałecki (jakub.skalecki@gmail.com)
from time_tracker.core.data_source import Repository

from time_tracker.sources.github_source import GithubDataSource
import mock

@mock.patch('time_tracker.source.github_source.Github')
def test_get_repository(github_client):
    repository = GithubDataSource().get_repo("test_repo")
    assert isinstance(repository, Repository)
