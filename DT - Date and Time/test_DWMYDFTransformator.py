import numpy as np
import pandas as pd
import pytest

import DWMYDFTransformator as T
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
ground_truth_week = np.array([201801, 201801, 201801, 201803, 201805, 201806, 201807, 201845, 201845,
                              201847, 201848, 201849, 201850, 201901, 201901, 201902, 201903, 201903,
                              201907, 201908, 201908, 201909, 201909, 201944, 201944, 201947, 201948,
                              201948, 201949, 201950])
ground_truth_year = np.array([2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018,
                              2018, 2018, 2018, 2018, 2019, 2019, 2019, 2019, 2019, 2019,
                              2019, 2019, 2019, 2019, 2019, 2019, 2019, 2019, 2019,
                              2019, 2019])


def __get_ts_df(time_type):
    tsg = TSG.TimeSeriesGenerator()
    ts = TS.TimeSeries()

    if time_type == "d":
        ts.set_ts_list(tsg.generate_day_data(), ["TIME", "VALUE"])
    elif time_type == "w":
        ts.set_ts_list(tsg.generate_week_data(), ["TIME", "VALUE"])
    elif time_type == "m" or time_type == "y":
        ts.set_ts_list(tsg.generate_month_data(), ["TIME", "VALUE"])

    ts_df = ts.get_ts_df()
    ts_df["VALUE"] = [1] * ts_df.shape[0]

    return ts_df


def __transform_ts_df(ts_df, transformation_type, time_type):
    t = T.DWMYDFTransformator()

    if transformation_type == "f":
        transformed_data = t.fit(ts_df, time_type, ["TIME", "VALUE"])
    elif transformation_type == "fp":
        transformed_data = t.fit_predict(ts_df, time_type, ["TIME", "VALUE"])
    elif transformation_type == "p":
        transformed_data = t.predict(ts_df, time_type, ["TIME", "VALUE"])

    return transformed_data


@pytest.mark.parametrize("transformation_type, time_type, ground_truth",
                         [
                             ("f", "d", ground_truth_day),
                             ("fp", "d", ground_truth_day),
                             ("p", "d", ground_truth_day),
                             ("f", "w", ground_truth_week),
                             ("fp", "w", ground_truth_week),
                             ("p", "w", ground_truth_week),
                             ("f", "m", ground_truth_month),
                             ("fp", "m", ground_truth_month),
                             ("p", "m", ground_truth_month),
                             ("f", "y", ground_truth_year),
                             ("fp", "y", ground_truth_year),
                             ("p", "y", ground_truth_year)
                         ])
def test_conversion(transformation_type, time_type, ground_truth):
    df_ground_truth = pd.DataFrame()
    df_ground_truth["VALUE"] = [1] * len(ground_truth)
    df_ground_truth["TIME" + "_" + time_type] = ground_truth

    ts_df = __get_ts_df(time_type)
    transform_data = __transform_ts_df(ts_df, transformation_type, time_type)

    assert transform_data.equals(df_ground_truth)
