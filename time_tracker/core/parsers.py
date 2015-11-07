import re
from datetime import timedelta


_time_re = re.compile(
    r'''\s*
    :clock\d+:\s*                   # The clock emoji
    (?:(?P<days>\d+)d)?             # Days
    (?:(?P<hours>\d+)h)?            # Hours
    (?:(?P<minutes>\d+)m)?          # Minutes
    (?:\s*(\|\s*)?(?P<comment>.+))? # Comment
    \s*''', re.VERBOSE | re.IGNORECASE)


def entry_from_string(s):
    """Given a string, return spent time as a timedelta object.

    >>> entry_from_string(':clock1: 5m')
    (datetime.timedelta(0, 300), '')
    """
    for part in s.split('\n'):
        match = _time_re.match(part.strip())
        if match:
            results = match.groupdict()
            comment = results.pop('comment') or ''

            kwargs = {k: int(v or 0) for k, v in results.items()}
            time = timedelta(**kwargs)

            return time, comment


class IssueParser:
    pass  # TODO


class CommiterParser:
    pass  # TODO
