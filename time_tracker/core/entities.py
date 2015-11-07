class Issue:
    def __init__(self, number, name, message, comments=None):
        self.number = number
        self.name = name
        self.message = message
        self.comments = comments or []


class Commit:
    def __init__(self, committer, message, time, issue=None):
        self.committer = committer
        self.message = message
        self.issue = issue
        self.time = time


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
