# -*- coding: utf-8 -*-
# author: Jakub Skałecki (jakub.skalecki@gmail.com)

import abc


class DataSource(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_issues(self):
        """
        :rtype: list[time_tracker.core.entities.Issue]
        """

    @abc.abstractmethod
    def get_issue_by_id(self, issue_id):
        """
        :rtype: time_tracker.core.entities.Issue | None
        """

    @abc.abstractmethod
    def get_commits(self):
        """
        :rtype: list[time_tracker.core.entities.Commit]
        """

    @abc.abstractmethod
    def get_commits_of_user(self, user_id):
        """
        :rtype: list[time_tracker.core.entities.Commit]
        """

    @abc.abstractmethod
    def get_commit_by_id(self, commit_id):
        """
        :rtype: time_tracker.core.entities.Commit
        """

    @abc.abstractmethod
    def get_users(self):
        """
        :rtype: time_tracker.core.entities.Commiter
        """
        pass
