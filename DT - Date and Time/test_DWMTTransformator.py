import TimeSeries as TS
import TimeSeriesGenerator as TSG


def __get_ts_array(type):
    tsg = TSG.TimeSeriesGenerator()
    ts = TS.TimeSeries()

    if type == "d":
        ts.set_ts_list(tsg.generate_day_data(), ["TIME", "VALUE"])
    elif type == "w":
        ts.set_ts_list(tsg.generate_week_data(), ["TIME", "VALUE"])
    elif type == "m" or type == "y":
        ts.set_ts_list(tsg.generate_month_data(), ["TIME", "VALUE"])

    ts_d = ts.get_ts_df()

    return ts_d["TIME"].array


def test_day_conversion():
    assert True
