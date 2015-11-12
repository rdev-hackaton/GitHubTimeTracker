import mock

from tests.backends.sources.mock_models import CommitFactory, UserFactory, \
    IssueFactory
from time_tracker.core.data_source import Repository
from time_tracker.core.entities import Commit, Committer, Issue, Comment
from time_tracker.backends.sources.github_source import GithubDataSource, \
    GithubRepository

mock_login = mock.patch('time_tracker.backends.sources.github_source.login')


@mock_login
def test_get_repository(mock_login):
    repository = GithubDataSource(token='c0ff33').get_repo("test_repo")
    assert isinstance(repository, Repository)
    assert repository.name == "test_repo"


@mock_login
def test_get_commits(mock_login):
    mock_commits = CommitFactory.create_batch(3)
    mock_login.return_value \
        .repository.return_value \
        .iter_commits.return_value = \
        mock_commits
    repo = GithubRepository('test/test')
    commits = repo.get_commits()
    assert len(mock_commits) == len(commits)
    for mock_c, c in zip(mock_commits, commits):
        assert isinstance(c, Commit)
        assert mock_c.commit.message == c.message
        assert mock_c.committer.email == c.committer.email
        assert mock_c.committer.name == c.committer.name


@mock_login
def test_get_commits_by_author(mock_login):
    mock_commits = CommitFactory.create_batch(3)
    mock_login.return_value \
        .repository.return_value \
        .iter_commits.return_value = \
        mock_commits
    repo = GithubRepository('test/test')
    commits = repo.get_commits_by_user_name('Test')
    assert len(mock_commits) == len(commits)
    for mock_c, c in zip(mock_commits, commits):
        assert isinstance(c, Commit)
        assert mock_c.commit.message == c.message
        assert mock_c.committer.email == c.committer.email
        assert mock_c.committer.name == c.committer.name


@mock_login
def test_get_commit_by_id(mock_login):
    mock_commit = CommitFactory()
    mock_login.return_value \
        .repository.return_value \
        .commit.return_value = \
        mock_commit
    repo = GithubRepository('test/test')
    commit = repo.get_commit('#123fdsf34f')

    assert isinstance(commit, Commit)
    assert mock_commit.commit.message == commit.message
    assert mock_commit.committer.email == commit.committer.email
    assert mock_commit.committer.name == commit.committer.name


@mock_login
def test_get_users(mock_login):
    mock_users = UserFactory.create_batch(3)
    mock_login.return_value \
        .repository.return_value \
        .iter_contributors.return_value = \
        mock_users
    repo = GithubRepository('test/test')
    users = repo.get_contributors()
    assert len(mock_users) == len(users)
    for mock_u, u in zip(mock_users, users):
        assert isinstance(u, Committer)
        assert mock_u.email == u.email
        assert mock_u.name == u.name


@mock_login
def test_get_issues(mock_login):
    mock_issues = IssueFactory.create_batch(3)
    mock_login.return_value \
        .repository.return_value \
        .iter_issues.return_value = \
        mock_issues
    repo = GithubRepository('test/test')
    issues = repo.get_issues()
    assert len(mock_issues) == len(issues)
    for mock_i, i in zip(mock_issues, issues):
        assert isinstance(i, Issue)
        assert mock_i.title == i.name
        assert mock_i.body == i.message
        assert mock_i.number == i.number
        for mock_comment, comment in zip(mock_i.iter_comments(), i.comments):
            assert isinstance(comment, Comment)
            assert mock_comment.user.name == comment.author.name
            assert mock_comment.body == comment.message


@mock_login
def test_get_issue(mock_login):
    mock_issue = IssueFactory()
    mock_login.return_value \
        .repository.return_value \
        .issue.return_value = \
        mock_issue
    repo = GithubRepository('test/test')
    issue = repo.get_issue(23)

    assert isinstance(issue, Issue)
    assert mock_issue.title == issue.name
    assert mock_issue.body == issue.message
    assert mock_issue.number == issue.number
    for mock_c, comment in zip(mock_issue.iter_comments(), issue.comments):
        assert isinstance(comment, Comment)
        assert mock_c.user.name == comment.author.name
        assert mock_c.body == comment.message
