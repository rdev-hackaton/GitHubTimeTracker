from .results import Result

from ..core import Config
from ..parsers import IssueParser


def get_all_entries_for_issue(repo_name, issue_id):
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


def get_all_entries_for_commiter(repo_name, commiter_id):
    issue_repo = Config.get_repo(repo_name)
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
    issue_repo = Config.get_repo(repo_name)
    if not issue_repo:
        return {
            'result': Result.REPO_NOT_FOUND
        }
