# -*- coding: utf-8 -*-
import abc


class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_issues(self):
        """
        :rtype: list[time_tracker.core.entities.Issue]
        """

    @abc.abstractmethod
    def get_issue(self, id):
        """
        :param id:
        :rtype: time_tracker.core.entities.Issue | None
        """

    @abc.abstractmethod
    def get_commits(self):
        """
        :rtype: list[time_tracker.core.entities.Commit]
        """

    @abc.abstractmethod
    def get_commits_of_user(self, user):
        """
        :param user:
        :rtype: list[time_tracker.core.entities.Commit]
        """

    @abc.abstractmethod
    def get_commit(self, hash):
        """
        :param hash:
        :rtype: time_tracker.core.entities.Commit
        """

    @abc.abstractmethod
    def get_users(self):
        """
        :rtype: time_tracker.core.entities.Committer
        """
        pass
