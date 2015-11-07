# -*- coding: utf-8 -*-
# author: Jakub Skałecki (jakub.skalecki@gmail.com)

import abc


class DataSource(metaclass=abc.ABCMeta):

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
    def get_issue_by_id(self, issue_id):
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
    def get_commit_by_id(self, commit_id):
        """
        :type commit_id: int
        :rtype: time_tracker.core.entities.Commit | None
        """

    @abc.abstractmethod
    def get_users(self):
        """
        :rtype: time_tracker.core.entities.Commiter
        """
        pass
