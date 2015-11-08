from github import Github

from time_tracker.core.data_source import DataSource, Repository
from time_tracker.core.entities import Commit, Committer, Issue, Comment


class GithubDataSource(DataSource):

    def get_repo(self, name):
        return GithubRepository(name, self.login, self.password)


class GithubRepository(Repository):

    def __init__(self, name, login=None, password=None):
        Repository.__init__(self, name)
        self._repo = Github(login, password).get_repo(self.name)

    def get_commits_by_user_name(self, username):
        commits = self._repo.get_commits(author=username)
        return [self._commit_to_model(c) for c in commits]

    def get_contributors(self):
        users = self._repo.get_contributors()
        return [self._committer_to_model(u) for u in users]

    def get_issues(self):
        issues = self._repo.get_issues()
        return [self._issue_to_model(i) for i in issues]

    def get_commits(self):
        commits = self._repo.get_commits()
        return [self._commit_to_model(c) for c in commits]

    def get_commit(self, commit_id):
        commit = self._repo.get_commit(commit_id)
        return self._commit_to_model(commit)

    def get_issue(self, number):
        issue = self._repo.get_issue(number)
        return self._issue_to_model(issue)

    @staticmethod
    def _committer_to_model(commiter):
        return Committer(commiter.name, commiter.email, 'dupa')

    @staticmethod
    def _commit_to_model(commit):
        user = GithubRepository._committer_to_model(commit.committer)
        return Commit(user, commit.commit.message, None, None)

    @staticmethod
    def _issue_to_model(issue):
        comments = [GithubRepository._comment_to_model(c)
                    for c in issue.get_comments()]
        return Issue(issue.number, issue.title, issue.body, comments)

    @staticmethod
    def _comment_to_model(comment):
        user = GithubRepository._committer_to_model(comment.user)
        return Comment(comment.body, user)
