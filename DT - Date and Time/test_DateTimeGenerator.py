import DateTimeGenerator as DTG
from DateTimeGenerator import __is_leap

def test_standard_leap_year():
    assert __is_leap(1996)

def test_non_standard_leap_year():
    assert __is_leap(2000)

def test_non_leap_year():
    assert not __is_leap(1997)

def test_non_standart_non_leap_year():
    assert not __is_leap(1900)

