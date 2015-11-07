from .results import Result

from .parsers import IssueParser, CommiterParser


def get_all_entries_for_issue(data_source, repo_name, issue_id):
    """All entries for issue"""
    repo = data_source.get_repo(repo_name)
    if not repo:
        return {
            'result': Result.REPO_NOT_FOUND
        }
    issue = repo.get_issue_by_id(issue_id)
    if not issue:
        return {
            'result': Result.ISSUE_NOT_FOUND
        }
    entries = IssueParser(issue)
    return {
        'result': Result.OK,
        'entries': entries
    }


def get_all_entries_of_commiter(data_source, repo_name, commiter_id):
    """All entries of commiter"""
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


def get_project_budget(data_source, repo_name):
    """Project budget"""
    repo = data_source.get_repo(repo_name)
    if not repo:
        return {
            'result': Result.REPO_NOT_FOUND
        }


def get_project_time(data_source, repo_name):
    """Get overall time spent at project"""
    return True


def get_issue_developers(data_source, repo_name, issue_id):
    """Get issue developers"""
    return True


def get_developer_time_at_project(data_source, repo_name):
    """Get time spent by developer at project"""
    return True
