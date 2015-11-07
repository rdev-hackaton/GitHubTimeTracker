from itertools import chain
import re
from datetime import timedelta


_time_re = re.compile(
    r'''\s*
    :clock\d+:\s*          # The clock emoji
    (?:(?P<days>\d+)d)?    # Days
    (?:(?P<hours>\d+)h)?   # Hours
    (?:(?P<minutes>\d+)m)? # Minutes
    \s*''', re.VERBOSE | re.IGNORECASE)


def time_from_string(s):
    """Given a string, return spent time as a timedelta object."""
    parts = (p.split('|') for p in s.split('\n'))
    for part in chain(*parts):
        match = _time_re.match(part.strip())
        if match:
            kwargs = {k: int(v or 0) for k, v in match.groupdict().items()}
            return timedelta(**kwargs)
