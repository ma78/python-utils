"""
datetimeutils/age.py unit tests
"""

from datetime import timedelta

from datetimeutils import age


def test_convert_age_seconds():
    """Verify various age formats < 1m"""

    seconds_9 = timedelta(seconds=9)
    assert age.convert_age(seconds_9, always_show_minutes=False) == "9s"
    assert age.convert_age(seconds_9, always_show_minutes=True) == "0m9s"

    seconds_33 = timedelta(seconds=33)
    assert age.convert_age(seconds_33, always_show_minutes=False) == "33s"
    assert age.convert_age(seconds_33, always_show_minutes=True) == "0m33s"


def test_convert_age_minutes():
    """Verify various age formats < 1h"""

    less_than_1h = timedelta(minutes=10, seconds=15)
    assert age.convert_age(less_than_1h, always_show_minutes=False) == "10m15s"
    assert age.convert_age(less_than_1h, always_show_minutes=True) == "10m15s"


def test_convert_age_hours():
    """Verify various age formats < 1d"""
    less_than_1d = timedelta(minutes=195)
    assert age.convert_age(less_than_1d, always_show_minutes=False) == "3h15m"
    assert age.convert_age(less_than_1d, always_show_minutes=True) == "3h15m"


def test_convert_age_days():
    """Verify various age formats > 1d"""
    more_than_1d = timedelta(days=2, minutes=195)
    assert age.convert_age(more_than_1d, always_show_minutes=False) == "2d3h"
    assert age.convert_age(more_than_1d, always_show_minutes=True) == "2d3h15m"

    # Verify > 9d (only show days)
    more_than_9d = timedelta(days=11, minutes=195)
    assert age.convert_age(more_than_9d, always_show_minutes=False) == "11d"
    assert age.convert_age(more_than_9d, always_show_minutes=True) == "11d"
