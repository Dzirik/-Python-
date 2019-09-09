import datetime

import pytest

import TimeSeries as TS
import TimeSeriesGenerator as TSG


def __get_ts_df():
    tsg = TSG.TimeSeriesGenerator()
    list_ts = tsg.generate_month_data()

    ts = TS.TimeSeries()
    ts.set_ts_list(list_ts, ["TIME", "VALUE"])

    df = ts.get_ts_df()

    return df


def __get_ts_series():
    tsg = TSG.TimeSeriesGenerator()
    list_ts = tsg.generate_month_data()

    ts = TS.TimeSeries()
    ts.set_ts_list(list_ts, ["TIME", "VALUE"])

    series = ts.get_ts_series()

    return series


def test_ts_series_shape():
    series = __get_ts_series()
    assert series.shape == (30,)


@pytest.mark.skip("WIP")
def test_ts_series_name():
    pass


def test_ts_df_shape():
    df = __get_ts_df()
    assert df.shape == (30, 2)


def test_ts_df_date_type():
    df = __get_ts_df()
    assert isinstance(df["TIME"][0], datetime.datetime)


@pytest.mark.skip("WIP")
def test_ts_df_names():
    pass
