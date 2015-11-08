from datetime import timedelta, datetime

from time_tracker.core.entities import Entry, Issue, Comment, User, Commit


class TestEntriesFromEntities:

    def test_entries_from_issue(self):
        author = User('user', 'email', 'url')
        comments = [Comment(':clock1: 1m', author)]
        issue = Issue(2, 'test', ':clock1: 5h12m', comments)
        valid_deltatimes = [
            timedelta(hours=5, minutes=12),
            timedelta(minutes=1)]
        entries = issue.get_entries()
        assert len(entries) == len(valid_deltatimes)
        for entry in entries:
            assert entry.time in valid_deltatimes

    def test_entries_from_commit(self):
        author = User('user', 'email', 'url')
        commit = Commit(author, ':clock1: 1m', datetime(2015, 6, 15))
        entries = commit.get_entries()
        assert len(entries) == 1
        assert entries[0].time == timedelta(minutes=1)


class TestEntryFromString:
    def test_time(self):
        time = lambda s: Entry.from_string(s).time
        assert time(':cLoCk1: 5M') == \
            timedelta(minutes=5), "Any case"
        assert time(':clock1: 1d2h5m') == \
            timedelta(days=1, hours=2, minutes=5), "Several units"
        assert time('  :clock1:  5m  ') == \
            timedelta(minutes=5), "Whitespace"
        assert time('  :clock1:  1d  2h  5m  ') == \
            timedelta(days=1, hours=2, minutes=5), "More whitespace"
        assert time(':clock1: 2h130m') == \
            timedelta(hours=4, minutes=10), "Overlapping units"
        assert time('This is a test\n'
                    '\n'
                    ':clock1: 5m') == \
            timedelta(minutes=5), "Can be anywhere"

    def test_comment(self):
        comment = lambda s: Entry.from_string(s).comment
        assert comment(':clock1: 5m') is None, "No comment"
        assert comment(':clock1: 5m Hello world') == \
            'Hello world', "Simple case"
        assert comment(':clock1: 5m | Hello world') == \
            'Hello world', "With pipe"
        assert comment(':clock1: 5m    |    Hello world') == \
            'Hello world', "Whitespace"
