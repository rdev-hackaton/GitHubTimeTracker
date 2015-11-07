from .results import Result

CommitterParser = object()  # TODO


def get_entries_list(data_source, repo_name, committer, issue, milestone):
    repo = data_source.get_repo(repo_name)
    if not repo:
        return {
            'result': Result.REPO_NOT_FOUND
        }
    entries = []
    if issue:
        issue = repo.get_issue(issue)
        entries.extend(issue.get_entries())
    else:
        issues = repo.get_issues()
        entries.extend([
            issue.get_entries()
            for issue in issues
        ])
    for commit in repo.get_commits():
        entry = commit.get_entry()
        if entry:
            entries.append(entry)
    # TODO filter by committer & milestone
    return {
        'result': Result.OK,
        'entries': entries
    }


def get_total_stats(data_source, repo_name, committer, issue, milestone):
    # TODO sum up results
    return get_entries_list(
        data_source, repo_name, committer, issue, milestone)
