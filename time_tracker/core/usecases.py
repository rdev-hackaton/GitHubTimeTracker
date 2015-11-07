from .results import Result

from ..config import Config
from .parsers import IssueParser, CommiterParser


def get_all_entries_for_issue(repo_name, issue_id):
    """All entries for issue"""
    issue_repo = Config.get_repo(repo_name)
    if not issue_repo:
        return {
            'result': Result.REPO_NOT_FOUND
        }
    issue = issue_repo.get_by_id(issue_id)
    if not issue:
        return {
            'result': Result.ISSUE_NOT_FOUND
        }
    entries = IssueParser(issue)
    return {
        'result': Result.OK,
        'entries': entries
    }


def get_all_entries_of_commiter(repo_name, commiter_id):
    """All entries of commiter"""
    issue_repo = Config.from_config(repo_name)
    if not issue_repo:
        return {
            'result': Result.REPO_NOT_FOUND
        }
    commiter = issue_repo.get_by_commiter(commiter_id)
    if not commiter:
        return {
            'result': Result.COMMITER_NOT_FOUND
        }
    entries = CommiterParser(commiter)
    return {
        'result': Result.OK,
        'entries': entries
    }


def get_project_budget(repo_name):
    """Project budget"""
    issue_repo = Config.get_repo(repo_name)
    if not issue_repo:
        return {
            'result': Result.REPO_NOT_FOUND
        }


def get_project_time(repo_name):
    """Get overall time spent at project"""
    return True


def get_issue_developers(repo_name, issue_id):
    """Get issue developers"""
    return True


def get_developer_time_at_project(repo_name):
    """Get time spent by developer at project"""
    return True
