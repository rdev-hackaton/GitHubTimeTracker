from .results import Result

CommitterParser = object()  # TODO


def get_entries_list(data_source, repo_name, committer, issue, milestone):
    repo = data_source.get_repo(repo_name)
    if not repo:
        return {
            'result': Result.REPO_NOT_FOUND
        }
    committer = repo.get_by_committer(committer)
    if not committer:
        return {
            'result': Result.COMMITTER_NOT_FOUND
        }
    entries = CommitterParser(committer)
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
