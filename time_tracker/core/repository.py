
# -*- coding: utf-8 -*-
# author: Jakub Skałecki (jakub.skalecki@gmail.com)

import abc


class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_issues(self):
        """
        :rtype: list[time_tracker.core.entities.Issue]
        """

    @abc.abstractmethod
    def get_issue_by_id(self):
        """
        :rtype: time_tracker.core.entities.Issue | None
        """

    @abc.abstractmethod
    def get_commits(self):
        """
        :rtype: list[time_tracker.core.entities.Commit]
        """

    @abc.abstractmethod
    def get_commits_of_user(self):
        """
        :rtype: list[time_tracker.core.entities.Commit]
        """

    @abc.abstractmethod
    def get_commit_by_id(self):
        """
        :rtype: time_tracker.core.entities.Commit
        """

    @abc.abstractmethod
    def get_users(self):
        """
        :rtype: time_tracker.core.entities.Committer
        """
        pass
