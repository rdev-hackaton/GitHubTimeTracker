from .results import Result

CommitterParser = object()  # TODO


def get_entries_list(data_source, repo_name, committer, issue, milestone):
    repo = data_source.get_repo(repo_name)
    if not repo:
        return {
            'result': Result.REPO_NOT_FOUND
        }
    commiter = repo.get_by_commiter(committer)
    if not commiter:
        return {
            'result': Result.COMMITER_NOT_FOUND
        }
    entries = CommitterParser(commiter)
    return {
        'result': Result.OK,
        'entries': entries
    }


def get_total_stats(data_source, repo_name, committer, issue, milestone):
    repo = data_source.get_repo(repo_name)
    if not repo:
        return {
            'result': Result.REPO_NOT_FOUND
        }
