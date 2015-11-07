import re
from datetime import timedelta

from .entities import Entry


_entry_re = re.compile(
    r'''\s*
    :clock\d+:\s*                   # The clock emoji
    (?:(?P<days>\d+)d)?             # Days
    (?:(?P<hours>\d+)h)?            # Hours
    (?:(?P<minutes>\d+)m)?          # Minutes
    (?:\s*(\|\s*)?(?P<comment>.+))? # Comment
    \s*''', re.VERBOSE | re.IGNORECASE)


def entry_from_string(s):
    """Given a string, return an Entry object.

    >>> entry = entry_from_string(':clock1: 5m | Initial commit')
    >>> entry.time
    datetime.timedelta(0, 300)
    >>> entry.comment
    'Initial commit'
    """
    for part in s.split('\n'):
        match = _entry_re.match(part.strip())
        if match:
            results = match.groupdict()
            comment = results.pop('comment')

            kwargs = {k: int(v or 0) for k, v in results.items()}
            time = timedelta(**kwargs)

            return Entry(time, comment)


class IssueParser:
    pass  # TODO


class CommiterParser:
    pass  # TODO
