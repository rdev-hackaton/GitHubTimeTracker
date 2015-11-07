from datetime import timedelta

from time_tracker.core.parsers import time_from_string


def test_time_from_string():
    assert time_from_string(':cLoCk1: 5M') == \
        timedelta(minutes=5), "Any case"
    assert time_from_string('  :clock1:  5m  ') == \
        timedelta(minutes=5), "Whitespace"
    assert time_from_string(':clock1: 1d2h5m') == \
        timedelta(days=1, hours=2, minutes=5), "Several units"
    assert time_from_string(':clock1: 2h130m') == \
        timedelta(hours=4, minutes=10), "Overlapping units"
    assert time_from_string('This is a test\n'
                            '\n'
                            ':clock1: 5m') == \
        timedelta(minutes=5), "Can be anywhere"
