from .results import Result

from ..config import Config
from .parsers import IssueParser, CommiterParser


def get_entries_list(repo_name, author, issue, milestone):
    repo = Config.get_repo(repo_name)
    if not repo:
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


def get_total_stats(repo_name, author, issue, milestone):
    repo = Config.get_repo(repo_name)
    if not issue_repo:
        return {
            'result': Result.REPO_NOT_FOUND
        }
