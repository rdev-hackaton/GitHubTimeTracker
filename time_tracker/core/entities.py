from time_tracker.utils import parse_time_entry


class Issue:
    def __init__(self, number, name, message, author, comments=None):
        self.author = author
        self.number = number
        self.name = name
        self.message = message
        self.comments = comments or []

    def get_entries(self):
        entries = []
        comments_messages = [(c.author, c.message) for c in self.comments]
        for author, comment in [(self.author, self.message)] \
                + comments_messages:
            entry = Entry.from_string(comment, author)
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
        entry = Entry.from_string(self.message, self.committer)
        return [entry] if entry else []


class Committer:
    def __init__(self, name, email, user=None):
        self.name = name
        self.email = email
        self.user = user


class User:
    def __init__(self, name, email, url):
        self.name = name
        self.email = email
        self.url = url


class Comment:
    def __init__(self, message, author):
        self.message = message
        self.author = author


class Entry:
    """Represents a time entry."""

    def __init__(self, time, author, comment=None):
        self.author = author
        self.time = time
        self.comment = comment

    @classmethod
    def from_string(cls, string, author):
        """Initialize an Entry object from string.

        >>> entry = Entry.from_string(':clock1: 5m | Initial commit')
        >>> entry.time
        datetime.timedelta(0, 300)
        >>> entry.comment
        'Initial commit'
        >>> Entry.from_string('Invalid') is None
        True
        """
        args = parse_time_entry(string)
        if args:
            return cls(args[0], author, args[1])
