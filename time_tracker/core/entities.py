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


class Issue:
    def __init__(self, number, name, message, comments=None):
        self.number = number
        self.name = name
        self.message = message
        self.comments = comments or []

    def get_entries(self):
        entries = []
        for comment in [self.message] + self.comments:
            entry = Entry.from_string(comment)
            if entry:
                entries.append(entry)
        return entries


class Commit:
    def __init__(self, committer, message, time, issue=None):
        self.committer = committer
        self.message = message
        self.issue = issue
        self.time = time

    def get_entries(self):
        entry = Entry.from_string(self.message)
        return [entry] if entry else []


class Committer:
    def __init__(self, name, email, user=None):
        self.name = name
        self.email = email
        self.user = user


class Entry:
    """Represents a time entry."""

    def __init__(self, time, comment=None):
        self.time = time
        self.comment = comment

    @classmethod
    def from_string(cls, string):
        """Initialize an Entry object from string.

        >>> entry = Entry.from_string(':clock1: 5m | Initial commit')
        >>> entry.time
        datetime.timedelta(0, 300)
        >>> entry.comment
        'Initial commit'
        >>> Entry.from_string('Invalid') is None
        True
        """
        for part in string.split('\n'):
            match = _entry_re.match(part.strip())
            if match:
                results = match.groupdict()
                comment = results.pop('comment')
                kwargs = {k: int(v or 0) for k, v in results.items()}
                time = timedelta(**kwargs)
                return Entry(time, comment)
