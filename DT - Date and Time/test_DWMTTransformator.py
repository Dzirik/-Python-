import numpy as np

import DWMYTransformator as T
import TimeSeries as TS
import TimeSeriesGenerator as TSG


def __get_ts_array(type):
    tsg = TSG.TimeSeriesGenerator()
    ts = TS.TimeSeries()
    t = T.DWMYTransformator()

    if type == "d":
        ts.set_ts_list(tsg.generate_day_data(), ["TIME", "VALUE"])
    elif type == "w":
        ts.set_ts_list(tsg.generate_week_data(), ["TIME", "VALUE"])
    elif type == "m" or type == "y":
        ts.set_ts_list(tsg.generate_month_data(), ["TIME", "VALUE"])

    ts_d = ts.get_ts_df()
    transformed_data = t.fit(ts_d["TIME"].array, type)

    return transformed_data


def test_day_conversion():
    days = __get_ts_array("d")
    results = np.array([20190801, 20190805, 20190809, 20190811, 20190813, 20190822, 20190824, 20190825,
                        20190826, 20190827, 20190827, 20190828, 20190829, 20190829, 20190901, 20190901, 20190903,
                        20190909, 20190909, 20190911, 20190912, 20190913, 20190917, 20190917, 20190922, 20190922,
                        20190923, 20190924, 20190929, 20190930])

    assert np.array_equal(days, results)
