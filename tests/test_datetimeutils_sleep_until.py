"""
datetimeutils/sleep_until.py unit tests
"""

from datetimeutils import sleep_until


def test_convert_age_seconds():
    """Verify various age formats < 1m"""

    assert sleep_until.sleep_until(1) == 1
