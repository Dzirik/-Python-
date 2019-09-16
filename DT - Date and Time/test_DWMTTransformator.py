import numpy as np
import pytest

import DWMYTransformator as T
import TimeSeries as TS
import TimeSeriesGenerator as TSG

ground_truth_day = np.array([20190801, 20190805, 20190809, 20190811, 20190813, 20190822, 20190824, 20190825,
                             20190826, 20190827, 20190827, 20190828, 20190829, 20190829, 20190901, 20190901, 20190903,
                             20190909, 20190909, 20190911, 20190912, 20190913, 20190917, 20190917, 20190922, 20190922,
                             20190923, 20190924, 20190929, 20190930])
ground_truth_month = np.array([201801, 201803, 201803, 201805, 201806, 201809, 201809, 201810, 201810,
                               201811, 201811, 201812, 201812, 201901, 201901, 201901, 201901, 201904, 201904,
                               201905, 201906, 201906, 201907, 201908, 201909, 201909, 201909, 201909,
                               201911, 201911])


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
    elif transformation_type == "fp":
        transformed_data = t.fitpredict(ts_array, time_type)
    elif transformation_type == "p":
        transformed_data = t.predict(ts_array, time_type)

    return transformed_data


@pytest.mark.parametrize("transformation_type, time_type, ground_truth",
                         [
                             ("f", "d", ground_truth_day),
                             ("fp", "d", ground_truth_day),
                             ("p", "d", ground_truth_day),
                             ("f", "m", ground_truth_month),
                             ("fp", "m", ground_truth_month),
                             ("p", "m", ground_truth_month)
                         ])
def test_fit_day_conversion(transformation_type, time_type, ground_truth):
    time_array = __get_ts_array(time_type)
    transform_data = __transform_ts_array(time_array, transformation_type, time_type)

    assert np.array_equal(transform_data, ground_truth)
