import abc


class DataSource(metaclass=abc.ABCMeta):

    def __init__(self, token=None, login=None, password=None):
        self.token = token
        self.password = password
        self.login = login

    @abc.abstractmethod
    def get_repo(self, name):
        """
        :type name: str
        :rtype: Repository
        """


class Repository(metaclass=abc.ABCMeta):

    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def get_issues(self):
        """
        :rtype: list[time_tracker.core.entities.Issue]
        """

    @abc.abstractmethod
    def get_issue(self, issue_id):
        """
        :type issue_id: int
        :rtype: time_tracker.core.entities.Issue | None
        """

    @abc.abstractmethod
    def get_commits(self):
        """
        :rtype: list[time_tracker.core.entities.Commit]
        """

    @abc.abstractmethod
    def get_commits_by_user_name(self, name):
        """
        :type name: str
        :rtype: list[time_tracker.core.entities.Commit]
        """

    @abc.abstractmethod
    def get_commit(self, sha):
        """
        :type sha: str
        :rtype: time_tracker.core.entities.Commit | None
        """

    @abc.abstractmethod
    def get_contributors(self):
        """
        :rtype: time_tracker.core.entities.Commiter
        """
