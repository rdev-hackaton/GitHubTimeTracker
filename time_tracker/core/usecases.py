from .results import Result

from .parsers import IssueParser, CommiterParser


def get_entries_list(data_source, repo_name, author, issue, milestone):
    repo = data_source.get_repo(repo_name)
    if not repo:
        return {
            'result': Result.REPO_NOT_FOUND
        }
    commiter = repo.get_by_commiter(commiter_id)
    if not commiter:
        return {
            'result': Result.COMMITER_NOT_FOUND
        }
    entries = CommiterParser(commiter)
    return {
        'result': Result.OK,
        'entries': entries
    }


def get_total_stats(data_source, repo_name, author, issue, milestone):
    repo = data_source.get_repo(repo_name)
    if not repo:
        return {
            'result': Result.REPO_NOT_FOUND
        }
