import factory


"""
Classes used to mock data received from github library
"""


class Issue(object):

    def __init__(self, title, assignee, body, number, comments):
        self.comments = comments
        self.number = number
        self.title = title
        self.assignee = assignee
        self.body = body

    def iter_comments(self):
        return iter(self.comments)


class Commit(object):

    def __init__(self, author, committer, url, commit):
        self.author = author
        self.committer = committer
        self.url = url
        self.commit = commit


class User(object):

    def __init__(self, name, login, email, html_url):
        self.html_url = html_url
        self.name = name
        self.login = login
        self.email = email


class GitCommit(object):

    def __init__(self, author, committer, message, url):
        self.author = author
        self.committer = committer
        self.message = message
        self.url = url


class IssueComment(object):

    def __init__(self, body, url, user):
        self.url = url
        self.body = body
        self.user = user


"""
Factories to fake data received from github library
"""


class UserFactory(factory.Factory):

    class Meta:
        model = User

    name = factory.Faker('first_name')
    login = factory.Faker('name')
    email = factory.Faker('email')
    html_url = factory.Faker('url')


class GitCommitFactory(factory.Factory):

    class Meta:
        model = GitCommit

    author = factory.SubFactory(UserFactory)
    committer = factory.SubFactory(UserFactory)
    message = factory.Faker('word')
    url = factory.Faker('url')


class CommitFactory(factory.Factory):

    class Meta:
        model = Commit

    commit = factory.SubFactory(GitCommitFactory)
    author = factory.SubFactory(UserFactory)
    committer = factory.SubFactory(UserFactory)
    url = factory.Faker('url')


class IssueCommentFactory(factory.Factory):

    class Meta:
        model = IssueComment

    body = factory.Faker('sentence')
    url = factory.Faker('url')
    user = factory.SubFactory(UserFactory)


class IssueFactory(factory.Factory):

    class Meta:
        model = Issue

    assignee = factory.SubFactory(UserFactory)
    title = factory.Faker('word')
    body = factory.Faker('sentence')
    number = factory.Sequence(lambda x: x)
    comments = factory.List([IssueCommentFactory() for _ in range(4)])
