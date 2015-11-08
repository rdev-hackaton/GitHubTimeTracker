import re
from datetime import timedelta


_entry_re = re.compile(
    r'''\s*
    :clock\d+:                # The clock emoji
    \s*                       # - Whitespace
    (?:(?P<days>\d+)d)?       # Days
    \s*                       # - Whitespace
    (?:(?P<hours>\d+)\s*h)?   # Hours
    \s*                       # - Whitespace
    (?:(?P<minutes>\d+)\s*m)? # Minutes
    \s*(\|\s*)?               # - Whitespace and optional pipe
    (?P<comment>.+)?          # Comment
    \s*''', re.VERBOSE | re.IGNORECASE)


def parse_time_entry(string):
    """Return a (time, comment) tuple from string if available."""
    for part in string.split('\n'):
        match = _entry_re.match(part)
        if match:
            results = match.groupdict()
            comment = results.pop('comment')
            kwargs = {k: int(v or 0) for k, v in results.items()}
            time = timedelta(**kwargs)
            return time, comment
