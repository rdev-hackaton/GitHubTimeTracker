from .parsers import entry_from_string


class Issue:
    def __init__(self, number, name, message, comments=None):
        self.number = number
        self.name = name
        self.message = message
        self.comments = comments or []

    def get_entries(self):
        entries = [entry_from_string(self.message)] + [
            entry_from_string(comment) for comment in self.comments
        ]
        return filter(None, entries)


class Commit:
    def __init__(self, committer, message, time, issue=None):
        self.committer = committer
        self.message = message
        self.issue = issue
        self.time = time

    def get_entries(self):
        entry = [entry_from_string(self.message)]
        return filter(None, entry)

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
        from .parsers import entry_from_string
        return entry_from_string(string)
