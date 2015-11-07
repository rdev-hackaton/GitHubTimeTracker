from time_tracker.core.data_source import DataSource


class GithubDataSource(DataSource):

    def __init__(self, github_wrapper):
        self.github = github_wrapper

    def get_commits_of_user(self, user_id):
        pass

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
