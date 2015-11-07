from datetime import timedelta

from time_tracker.core.entities import Entry


class TestEntryFromString:
    def test_time(self):
        time = lambda s: Entry.from_string(s).time
        assert time(':cLoCk1: 5M') == \
            timedelta(minutes=5), "Any case"
        assert time('  :clock1:  5m  ') == \
            timedelta(minutes=5), "Whitespace"
        assert time(':clock1: 1d2h5m') == \
            timedelta(days=1, hours=2, minutes=5), "Several units"
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
