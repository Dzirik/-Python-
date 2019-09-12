import numpy as np

import DWMYTransformator as T
import TimeSeries as TS
import TimeSeriesGenerator as TSG


def __get_ts_array(time_type):
    tsg = TSG.TimeSeriesGenerator()
    ts = TS.TimeSeries()

    if time_type == "d":
        ts.set_ts_list(tsg.generate_day_data(), ["TIME", "VALUE"])
    elif time_type == "w":
        ts.set_ts_list(tsg.generate_week_data(), ["TIME", "VALUE"])
    elif time_type == "m" or time_type == "y":
        ts.set_ts_list(tsg.generate_month_data(), ["TIME", "VALUE"])

    ts_d = ts.get_ts_df()

    return ts_d["TIME"].array


def __transform_ts_array(ts_array, transformation_type, time_type):
    t = T.DWMYTransformator()

    if transformation_type == "f":
        transformed_data = t.fit(ts_array, time_type)

    return transformed_data


def test_fit_day_conversion():
    time_array = __get_ts_array("d")
    transform_data = __transform_ts_array(time_array, "f", "d")
    ground_truth = np.array([20190801, 20190805, 20190809, 20190811, 20190813, 20190822, 20190824, 20190825,
                             20190826, 20190827, 20190827, 20190828, 20190829, 20190829, 20190901, 20190901, 20190903,
                             20190909, 20190909, 20190911, 20190912, 20190913, 20190917, 20190917, 20190922, 20190922,
                             20190923, 20190924, 20190929, 20190930])

    assert np.array_equal(transform_data, ground_truth)
