import random

import pytest

from DateTimeGenerator import DateTimeGenerator
from DateTimeGenerator import __is_leap


@pytest.fixture
def dtg():
    return DateTimeGenerator()


def __compare_samples(fun, t_from, t_to, n_sample=200, seed=432):
    random.seed(seed)

    gen = set([fun(t_from, t_to) for i in range(n_sample)])
    test = set(range(t_from, t_to + 1))

    return gen == test


def test_year_generator(dtg):
    assert __compare_samples(dtg.generate_year, 2000, 2025)


def test_month_generator(dtg):
    assert __compare_samples(dtg.generate_month, 1, 12)


def test_standard_leap_year():
    assert __is_leap(1996)


def test_non_standard_leap_year():
    assert __is_leap(2000)


def test_non_leap_year():
    assert not __is_leap(1997)


def test_non_standart_non_leap_year():
    assert not __is_leap(1900)
