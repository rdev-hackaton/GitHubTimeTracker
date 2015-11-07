# -*- coding: utf-8 -*-
# author: Jakub Skałecki (jakub.skalecki@gmail.com)

import mock

from github import Commit
from tests.sources.mock_models import CommitFactory

from time_tracker.core.data_source import Repository
from time_tracker.sources.github_source import GithubDataSource, GithubRepository


def test_get_repository():
    repository = GithubDataSource().get_repo("test_repo")
    assert isinstance(repository, Repository)
    assert repository.name == "test_repo"


@mock.patch('time_tracker.sources.github_source.Github')
def test_get_commits(mock_client):
    mock_commits = CommitFactory.create_batch(3)
    mock_client.get_repo.get_commits.return_value = mock_commits
    repo = GithubRepository('test/test')
    commits = repo.get_commits()

