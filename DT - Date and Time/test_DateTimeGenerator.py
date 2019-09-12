import random

import pytest

from DateTimeGenerator import DateTimeGenerator
from DateTimeGenerator import is_leap


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


@pytest.mark.parametrize("year, month, n_days",
                         [(2020, 1, 31),
                          (2020, 2, 29),
                          (2020, 3, 31),
                          (2020, 4, 30),
                          (2020, 5, 31),
                          (2020, 6, 30),
                          (2020, 7, 31),
                          (2020, 8, 31),
                          (2020, 9, 30),
                          (2020, 10, 31),
                          (2020, 11, 30),
                          (2020, 12, 31),
                          (2021, 2, 28)
                          ])
def test_day_generator(year, month, n_days):
    random.seed(5498)
    dsg = DateTimeGenerator()
    gen = set([dsg.generate_day(year, month) for i in range(300)])
    test = set(range(1, n_days + 1))
    assert gen == test


def test_month_generator(dtg):
    assert __compare_samples(dtg.generate_month, 1, 12)


def test_standard_leap_year():
    assert is_leap(1996)


def test_non_standard_leap_year():
    assert is_leap(2000)


def test_non_leap_year():
    assert not is_leap(1997)


def test_non_standart_non_leap_year():
    assert not is_leap(1900)
