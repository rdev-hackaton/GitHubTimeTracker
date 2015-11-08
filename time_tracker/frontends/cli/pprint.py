import click


def pprint_header(repo_name, issue, milestone):
    click.echo('\nRepository: ' + repo_name)
    if issue:
        click.echo('    Results limited to issue: ' + str(issue))
    if milestone:
        click.echo('    Results limited to milestone: ' + milestone)


def pprint_entry(entry, committer=None):
    output = [
        "    Time: {}".format(entry.time),
        "    Comment: {}".format(entry.comment)
    ]
    if committer:
        output.append("    Committer: " + committer)
    click.echo("".join(output))


def pprint_stats(stats):
    click.echo("    Total time: {}".format(stats['time']))
    click.echo("    Total entries: {}".format(stats['entries']))
