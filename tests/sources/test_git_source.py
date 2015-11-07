# -*- coding: utf-8 -*-
# author: Jakub Skałecki (jakub.skalecki@gmail.com)

import mock

from tests.sources.mock_models import CommitFactory, UserFactory, IssueFactory
from time_tracker.core.data_source import Repository
from time_tracker.core.entities import Commit, Committer, Issue
from time_tracker.sources.github_source import GithubDataSource, \
    GithubRepository


def test_get_repository():
    repository = GithubDataSource().get_repo("test_repo")
    assert isinstance(repository, Repository)
    assert repository.name == "test_repo"


@mock.patch('time_tracker.sources.github_source.Github')
def test_get_commits(mock_client):
    mock_commits = CommitFactory.create_batch(3)
    mock_client.return_value.get_repo.return_value.get_commits.return_value = \
        mock_commits
    repo = GithubRepository('test/test')
    commits = repo.get_commits()
    assert len(mock_commits) == len(commits)
    for mock_c, c in zip(mock_commits, commits):
        assert isinstance(c, Commit)
        assert mock_c.commit.message == c.message
        assert mock_c.committer.email == c.committer.email
        assert mock_c.committer.name == c.committer.name


@mock.patch('time_tracker.sources.github_source.Github')
def test_get_commits_by_author(mock_client):
    mock_commits = CommitFactory.create_batch(3)
    mock_client.return_value.get_repo.return_value.get_commits.return_value = \
        mock_commits
    repo = GithubRepository('test/test')
    commits = repo.get_commits_by_user_name('Test')
    assert len(mock_commits) == len(commits)
    for mock_c, c in zip(mock_commits, commits):
        assert isinstance(c, Commit)
        assert mock_c.commit.message == c.message
        assert mock_c.committer.email == c.committer.email
        assert mock_c.committer.name == c.committer.name


@mock.patch('time_tracker.sources.github_source.Github')
def test_get_commit_by_id(mock_client):
    mock_commit = CommitFactory()
    mock_client.return_value.get_repo.return_value.get_commit.return_value = \
        mock_commit
    repo = GithubRepository('test/test')
    commit = repo.get_commit_by_id('#123fdsf34f')

    assert isinstance(commit, Commit)
    assert mock_commit.commit.message == commit.message
    assert mock_commit.committer.email == commit.committer.email
    assert mock_commit.committer.name == commit.committer.name


@mock.patch('time_tracker.sources.github_source.Github')
def test_get_users(mock_client):
    mock_users = UserFactory.create_batch(3)
    mock_client.return_value.get_repo.return_value.get_contributors.return_value = \
        mock_users
    repo = GithubRepository('test/test')
    users = repo.get_users()
    assert len(mock_users) == len(users)
    for mock_u, u in zip(mock_users, users):
        assert isinstance(u, Committer)
        assert mock_u.email == u.email
        assert mock_u.name == u.name


@mock.patch('time_tracker.sources.github_source.Github')
def test_get_issues(mock_client):
    mock_issues = IssueFactory.create_batch(3)
    mock_client.return_value.get_repo.return_value.get_issues.return_value = \
        mock_issues
    repo = GithubRepository('test/test')
    issues = repo.get_issues()
    assert len(mock_issues) == len(issues)
    for mock_i, i in zip(mock_issues, issues):
        assert isinstance(i, Issue)
        assert mock_i.title == i.name
        assert mock_i.body == i.message
        assert mock_i.number == i.number


@mock.patch('time_tracker.sources.github_source.Github')
def test_get_issue(mock_client):
    mock_issue = IssueFactory()
    mock_client.return_value.get_repo.return_value.get_issue.return_value = \
        mock_issue
    repo = GithubRepository('test/test')
    issue = repo.get_issue_by_id(23)

    assert isinstance(issue, Issue)
    assert mock_issue.title == issue.name
    assert mock_issue.body == issue.message
    assert mock_issue.number == issue.number
