import click

from time_tracker.core.usecases import get_entries_list, get_total_stats
from time_tracker.config import Config
from .pprint import pprint_entry, pprint_header, pprint_stats


@click.command()
@click.option('--token', '--login',
              prompt='GitHub login or personal access token',
              help='Your GitHub login or personal access token')
@click.option('--password',
              prompt='GitHub password (leave empty if token used)',
              hide_input=True, help='Your GitHub password', default='')
@click.option('--repo', prompt='Repo name', help='Repository.')
@click.option('--committer', default=None,
              help='Limit results to given committer.')
@click.option('--issue', default=None,
              help='Limit results to commits related to given issue.')
@click.option('--milestone', default=None,
              help='Limit results to commits related to given milestone.')
@click.option('--total/--non-total', default=False,
              help='Give total time/budget instead of a list of entries.')
def print_time_tracking_info(
        login, password, repo, committer, issue, milestone, total):
    """Print time/budget info"""

    if issue:
        try:
            issue = int(issue)
        except (ValueError, TypeError):
            raise SystemExit("Wrong issue number: {}".format(issue))

    pprint_header(repo_name=repo, issue=issue, milestone=milestone)

    config = Config()
    data_source = config.get_backend()(login, password)

    click.echo("Loading...")
    if total:
        result = get_total_stats(
            data_source, repo, committer, issue, milestone)
        pprint_stats(result)
    else:
        result = get_entries_list(
            data_source, repo, committer, issue, milestone)
        for entry in result['entries']:
            pprint_entry(entry, committer)


if __name__ == '__main__':
    print_time_tracking_info()
