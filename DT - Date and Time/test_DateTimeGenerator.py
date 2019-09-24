import random

import pytest

from DateTimeGenerator import DateTimeGenerator
from DateTimeGenerator import is_leap


@pytest.fixture
def dtg():
    return DateTimeGenerator()


def _compare_samples(fun, t_from, t_to, n_sample=200, seed=432):
    random.seed(seed)

    gen = set([fun(t_from, t_to) for i in range(n_sample)])
    test = set(range(t_from, t_to + 1))

    return gen == test


def test_year_generator(dtg):
    assert _compare_samples(dtg.generate_year, 2000, 2025)


def test_month_generator(dtg):
    assert _compare_samples(dtg.generate_month, 1, 12)


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


@pytest.mark.parametrize("year_from, year_to, month_from, month_to, n_days",
                         [(2020, 2020, 1, 1, 31),
                          (2020, 2020, 2, 2, 29),
                          (2020, 2020, 3, 3, 31),
                          (2020, 2020, 4, 4, 30),
                          (2020, 2020, 5, 5, 31),
                          (2020, 2020, 6, 6, 30),
                          (2020, 2020, 7, 7, 31),
                          (2020, 2020, 8, 8, 31),
                          (2020, 2020, 9, 9, 30),
                          (2020, 2020, 10, 10, 31),
                          (2020, 2020, 11, 11, 30),
                          (2020, 2020, 12, 12, 31),
                          (2019, 2019, 2, 2, 28)
                          ])
def test_generate_day(year_from, year_to, month_from, month_to, n_days):
    random.seed(87602)
    dsg = DateTimeGenerator()
    gen = set([dsg.generate_date(year_from, year_to, month_from, month_to) for i in range(150)])
    (y, m, d) = zip(*gen)
    assert set(y) == {year_from}
    assert set(m) == {month_from}
    assert set(d) == set(range(1, n_days + 1))


@pytest.mark.parametrize("triplet, result",
                         [
                             ((2019, 2, 29), 20190229),
                             ((2019, 12, 1), 20191201),
                             ((2019, 12, 12), 20191212),
                             ((2019, 3, 5), 20190305)
                         ])
def test_convert_triplet(triplet, result):
    dsg = DateTimeGenerator()
    assert dsg.convert_triplet(triplet) == result


def test_standard_leap_year():
    assert is_leap(1996)


def test_non_standard_leap_year():
    assert is_leap(2000)


def test_non_leap_year():
    assert not is_leap(1997)


def test_non_standart_non_leap_year():
    assert not is_leap(1900)
