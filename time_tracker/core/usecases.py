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
