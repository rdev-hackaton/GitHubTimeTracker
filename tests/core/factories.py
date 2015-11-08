import factory

from datetime import datetime
from time_tracker.core import entities


class UserFactory(factory.Factory):

    class Meta:
        model = entities.User

    name = factory.Faker('name')
    email = factory.Faker('email')
    url = factory.Faker('url')


class CommitterFactory(factory.Factory):

    class Meta:
        model = entities.Committer

    message = factory.Faker('sentence')
    email = factory.Faker('email')
    user = factory.SubFactory(UserFactory)


class CommentFactory(factory.Factory):

    class Meta:
        model = entities.Comment

    message = factory.Faker('sentence')
    author = factory.SubFactory(UserFactory)


class IssueFactory(factory.Factory):

    class Meta:
        model = entities.Issue

    number = factory.Sequence(lambda x: x)
    name = factory.Faker('name')
    message = factory.Faker('sentence')
    comments = factory.List([CommentFactory() for _ in range(4)])


class CommitFactory(factory.Factory):

    class Meta:
        model = entities.Commit

    committer = factory.SubFactory(UserFactory)
    message = factory.Faker('sentence')
    issue = factory.SubFactory(IssueFactory)
    time = datetime.utcnow()
