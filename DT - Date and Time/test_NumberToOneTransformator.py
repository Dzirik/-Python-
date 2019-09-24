import pandas as pd
import pytest

import NumberToOneTransformator as T


def _generate_data():
    df_val = pd.DataFrame()
    df_ground_true = pd.DataFrame()

    df_val["ID"] = [10, 20, 30, 40]
    df_ground_true["ID"] = df_val["ID"]

    df_val["VALUES"] = [40, 43, 890, 10]
    df_ground_true["VALUES"] = [1, 1, 1, 1]

    return df_val, df_ground_true


def _transform_df(df, transformation_type):
    t = T.NumberToOneTransformator()

    if transformation_type == "f":
        transformed_data = t.fit(df, ["ID", "VALUE"])
    elif transformation_type == "fp":
        transformed_data = t.fit_predict(df, ["ID", "VALUE"])
    elif transformation_type == "p":
        transformed_data = t.predict(df, ["ID", "VALUE"])

    return transformed_data


@pytest.mark.parametrize("transformation_type", ["f", "fp", "p"])
def test_transform(transformation_type):
    df_val, df_ground_truth = _generate_data()
    df_test = _transform_df(df_val, transformation_type)

    return df_test.equals(df_ground_truth)
