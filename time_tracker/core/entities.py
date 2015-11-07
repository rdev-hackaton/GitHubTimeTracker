class Issue:
    def __init__(self, number, name, msg):
        self.number = number
        self.name = name
        self.msg = msg


class Commit:
    def __init__(self, author, msg, issue, time, src):
        self.author = author
        self.msg = msg
        self.issue = issue
        self.time = time
        self.src = src


class Commiter:
    def __init__(self, name, email, user=None):
        self.name = name
        self.email = email
        self.user = user


class Entry:
    """Represents a time entry."""

    def __init__(self, time, comment):
        self.time = time
        self.comment = comment
