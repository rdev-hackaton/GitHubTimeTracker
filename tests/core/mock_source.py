from tests.core.factories import CommitFactory, IssueFactory, UserFactory
from time_tracker.core.data_source import DataSource, Repository


class MockSource(DataSource):

    def get_repo(self, name):
        return MockRepository(name)


class MockRepository(Repository):

    def get_commits(self):
        return CommitFactory.create_batch(5)

    def get_issues(self):
        return IssueFactory.create_batch(5)

    def get_commits_by_user_name(self, name):
        return CommitFactory.create_batch(5, committer__name=name)

    def get_issue(self, issue_id):
        return IssueFactory(number=issue_id)

    def get_contributors(self):
        return UserFactory.create_batch(4)

    def get_commit(self, sha):
        return CommitFactory()
