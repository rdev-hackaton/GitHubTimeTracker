import click
from time_tracker.core.usecases import get_entries_list, get_total_stats
from time_tracker.config import Config


@click.command()
@click.option('--token', '--login',
              prompt='GitHub login or personal access token',
              help='Your GitHub login or personal access token')
@click.option('--password',
              prompt='GitHub password (leav empty if token used)',
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
    click.echo('\nRepository: ' + repo)

    def pretty_print_entry(entry):
        output_string = ''
        if committer:
            output_string += 'Committer: ' + committer + ' '
        output_string += 'Time: %s Cost: %s' % (entry['time'], entry['cost'])
        output_string += ' Commit: ' + str(entry['commit'])
        click.echo(output_string)

    def pretty_print_stats(stats):
        # FIXME
        click.echo(stats['result'])

    if issue:
        click.echo('    Results limited to issue: ' + issue)
    if milestone:
        click.echo('    Results limited to milestone: ' + milestone)

    config = Config()
    data_source = config.get_backend()(login, password)

    if total:
        pretty_print_stats(get_total_stats(data_source, repo, committer,
                                           issue, milestone))
    else:
        for entry in get_entries_list(data_source, repo, committer,
                                      issue, milestone):
            pretty_print_entry(entry)


if __name__ == '__main__':
    print_time_tracking_info()
