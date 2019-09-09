import datetime

import TimeSeries as TS
import TimeSeriesGenerator as TSG


def __get_ts_df():
    tsg = TSG.TimeSeriesGenerator()
    list_ts = tsg.generate_month_data()

    ts = TS.TimeSeries()
    ts.set_ts_list(list_ts, ["TIME", "VALUE"])

    df = ts.get_ts_df()

    return df


def test_ts_df_shape():
    df = __get_ts_df()
    assert df.shape == (30, 2)


def test_ts_df_date_type():
    df = __get_ts_df()
    assert isinstance(df["TIME"][0], datetime.datetime)
