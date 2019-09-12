import random

import pytest

from DateTimeGenerator import DateTimeGenerator
from DateTimeGenerator import __is_leap


@pytest.fixture
def dtg():
    return DateTimeGenerator()


def test_year_generator(dtg):
    random.seed(321)
    year_from = 2000
    year_to = 2025
    years_gen = set([dtg.generate_year(year_from, year_to) for i in range(200)])
    years_test = set(range(year_from, year_to + 1))

    assert years_gen == years_test


def test_standard_leap_year():
    assert __is_leap(1996)


def test_non_standard_leap_year():
    assert __is_leap(2000)


def test_non_leap_year():
    assert not __is_leap(1997)


def test_non_standart_non_leap_year():
    assert not __is_leap(1900)
