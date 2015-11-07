from github import Github
from time_tracker.core.data_source import DataSource, Repository


class GithubDataSource(DataSource):

    def get_repo(self, name):
        return GithubRepository(name)


class GithubRepository(Repository):

    def __init__(self, name):
        Repository.__init__(self, name)

    def get_commits_of_user(self, username):
        g = Github()
        commits = g.get_repo(self.name).get_commits(author=username)
        return

    def get_users(self):
        pass

    def get_issues(self):
        pass

    def get_commits(self):
        pass

    def get_commit_by_id(self, commit_id):
        pass

    def get_issue_by_id(self, commit_id):
        pass
