from .results import Result


def get_entries_list(data_source, repo_name, committer=None, issue=None,
                     milestone=None):
    repo = data_source.get_repo(repo_name)
    if not repo:
        return {
            'result': Result.REPO_NOT_FOUND
        }
    entries = []
    if issue:
        issue = repo.get_issue(issue)
        entries.extend(issue.get_entries())
    if committer:
        for commit in repo.get_commits_by_user_name(committer):
            entries.extend(commit.get_entries())
    if not issue and not commiter:
        entries_set = set()
        for issue in repo.get_issues():
            entries_set.update(issue.get_entries())
        for commit in repo.get_commits():
            entries_set.update(commit.get_entries())
            issue_entries = issue.get_entries()
        entries = list(entries_set)
    return {
        'result': Result.OK,
        'entries': entries
    }


def get_total_stats(data_source, repo_name, committer=None, issue=None,
                    milestone=None):
    """Return a summary of time entries data for given queries."""
    data = get_entries_list(
        data_source, repo_name, committer, issue, milestone)
    if data['result'] == Result.OK:
        return {
            'result': Result.OK,
            'time': sum(e.time for e in data['entries']),
            'entries': len(data['entries']),
        }
    else:
        return data  # Forward the error
