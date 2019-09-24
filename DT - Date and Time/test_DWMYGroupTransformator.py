import pandas as pd
import pytest

import DWMYGroupTransformator as T


def _get_ground_truth_day():
    ground_truth = pd.DataFrame()
    ground_truth["TIME_d"] = [20190101, 20190102, 20190103]
    ground_truth["VALUE"] = [1, 2, 3]

    return ground_truth


def _get_ground_truth_week():
    ground_truth = pd.DataFrame()
    ground_truth["TIME_w"] = [201901, 201902, 201903]
    ground_truth["VALUE"] = [1, 2, 3]

    return ground_truth

def _get_ground_truth_month():
    ground_truth = pd.DataFrame()
    ground_truth["TIME_m"] = [201901, 201902, 201903]
    ground_truth["VALUE"] = [1, 2, 3]

    return ground_truth


def _get_ground_truth_year():
    ground_truth = pd.DataFrame()
    ground_truth["TIME_y"] = [2019, 2020, 2021]
    ground_truth["VALUE"] = [1, 2, 3]

    return ground_truth


def _get_ts_df(time_type):
    ts_df = pd.DataFrame()
    if time_type == "d":
        ts_df["TIME" + "_" + time_type] = [20190101, 20190102, 20190102, 20190103, 20190103, 20190103]
    elif time_type == "w" or time_type == "m":
        ts_df["TIME" + "_" + time_type] = [201901, 201902, 201902, 201903, 201903, 201903]
    elif time_type == "y":
        ts_df["TIME" + "_" + time_type] = [2019, 2020, 2020, 2021, 2021, 2021]

    ts_df["VALUE"] = [1] * 6

    return ts_df


def _transform_ts_df(ts_df, transformation_type, time_type):
    t = T.DWMYGroupTransformator()

    if transformation_type == "f":
        transformed_data = t.fit(ts_df, time_type, ["TIME", "VALUE"], sum)
    elif transformation_type == "fp":
        transformed_data = t.fit_predict(ts_df, time_type, ["TIME", "VALUE"], sum)
    elif transformation_type == "p":
        transformed_data = t.predict(ts_df, time_type, ["TIME", "VALUE"], sum)

    return transformed_data


@pytest.mark.parametrize("transformation_type, time_type, ground_truth",
                         [
                             ("f", "d", _get_ground_truth_day()),
                             ("fp", "d", _get_ground_truth_day()),
                             ("p", "d", _get_ground_truth_day()),
                             ("f", "w", _get_ground_truth_week()),
                             ("fp", "w", _get_ground_truth_week()),
                             ("p", "w", _get_ground_truth_week()),
                             ("f", "m", _get_ground_truth_month()),
                             ("fp", "m", _get_ground_truth_month()),
                             ("p", "m", _get_ground_truth_month()),
                             ("f", "y", _get_ground_truth_year()),
                             ("fp", "y", _get_ground_truth_year()),
                             ("p", "y", _get_ground_truth_year())
                         ])
def test_conversion(transformation_type, time_type, ground_truth):
    ts_df = _get_ts_df(time_type)
    transformed_data = _transform_ts_df(ts_df, transformation_type, time_type)

    assert transformed_data.equals(ground_truth)
