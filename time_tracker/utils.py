import re
from datetime import timedelta


_entry_re = re.compile(
    r'''\s*
    :clock\d+:\s*                   # The clock emoji
    (?:(?P<days>\d+)d)?             # Days
    (?:(?P<hours>\d+)h)?            # Hours
    (?:(?P<minutes>\d+)m)?          # Minutes
    (?:\s*(\|\s*)?(?P<comment>.+))? # Comment
    \s*''', re.VERBOSE | re.IGNORECASE)


def parse_time_entry(string):
    """Return a (time, comment) tuple from string if available."""
    for part in string.split('\n'):
        match = _entry_re.match(part.strip())
        if match:
            results = match.groupdict()
            comment = results.pop('comment')
            kwargs = {k: int(v or 0) for k, v in results.items()}
            time = timedelta(**kwargs)
            return time, comment
