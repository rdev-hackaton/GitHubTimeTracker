# -*- coding: utf-8 -*-
# author: Jakub Skałecki (jakub.skalecki@gmail.com)

import factory

class Commit(object):

    def __init__(self, author, commiter, url, commit):
        self.author = author
        self.commiter = commiter
        self.url = url
        self.commit = commit


class User(object):

    def __init__(self, name, login, email):
        self.name = name
        self.login = login
        self.email = email


class GitCommit(object):

    def __init__(self, author, commiter, message, url):
        self.author = author
        self.commiter = commiter
        self.message = message
        self.url = url


class UserFactory(factory.Factory):

    class Meta:
        model = User

    name = factory.Faker('first_name')
    login = factory.Faker('name')
    email = factory.Faker('email')


class GitCommitFactory(factory.Factory):

    class Meta:
        model = GitCommit

    author = factory.SubFactory(UserFactory)
    commiter = factory.SubFactory(UserFactory)
    message = factory.Faker('word')
    url = factory.Faker('url')


class CommitFactory(factory.Factory):

    class Meta:
        model = Commit

    commit = factory.SubFactory(GitCommitFactory)
    author = factory.SubFactory(UserFactory)
    commiter = factory.SubFactory(UserFactory)
    url = factory.Faker('url')

