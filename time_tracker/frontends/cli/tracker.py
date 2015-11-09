import click

from time_tracker.core.usecases import get_entries_list, get_total_stats
from time_tracker.config import Config
from .pprint import pprint_entry, pprint_header, pprint_stats
from .options import DependentOption


@click.command()
@click.option('--token', default=None,
              help='Your GitHub personal access token')
@click.option('--login',
              prompt='GitHub login', default=None,
              help='Your GitHub login (use this or token, not both)',
              cls=DependentOption, prompt_depends_on=('token', False))
@click.option('--password',
              prompt='GitHub password', default=None,
              hide_input=True, help='Your GitHub password',
              cls=DependentOption, prompt_depends_on=('login', True))
@click.option('--repo', prompt='Repo name', help='Repository.')
@click.option('--committer', default=None,
              help='Limit results to given committer.')
@click.option('--issue', default=None, type=int,
              help='Limit results to commits related to given issue.')
@click.option('--milestone', default=None,
              help='Limit results to commits related to given milestone.')
@click.option('--total/--non-total', default=False,
              help='Give total time/budget instead of a list of entries.')
def print_time_tracking_info(
        token, login, password, repo, committer, issue, milestone, total):
    """Print time/budget info"""

    pprint_header(repo_name=repo, issue=issue, milestone=milestone)

    config = Config()
    data_source = config.get_backend()(token or login, password)

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
