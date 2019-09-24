import datetime
import random

import numpy as np
import pandas as pd


class TimeSeriesGenerator():

    def __init__(self):
        self.seed = 123

    def set_seed_number(self, seed_number):
        self.seed = seed_number

    def __set_seed(self):
        random.seed(self.seed)
        np.random.seed(self.seed)

    def generate_sample_ts_df(self, ts_lengths=[20, 30, 40, 50], int_data=False):
        df = pd.DataFrame()
        id_list = []
        data_list = []
        i = 10
        for n in ts_lengths:
            id_list.append(i)
            i = i + 10
            data_list.append(self.generate_day_data(int_data=int_data, n=n))

        df["ID"] = id_list
        df["TS_DATA"] = data_list

        return df

    def generate_day_data(self, int_data=True, n=30):
        self.__set_seed()
        if int_data:
            upper = 100
        else:
            upper = 1
        data = [(datetime.datetime(
            year=2019,
            month=random.randint(8, 9),
            day=random.randint(1, 30)
        ), random.randint(1, upper)) for i in range(0, n)]

        return data

    def generate_week_data(self, int_data=True, n=30):
        self.__set_seed()
        if int_data:
            upper = 100
        else:
            upper = 1
        data = [(datetime.datetime(
            year=random.randint(2018, 2019),
            month=random.choice([11, 12, 1, 2]),
            day=random.randint(1, 30)
        ), random.randint(1, upper)) for i in range(0, n)]

        return data

    def generate_month_data(self, int_data=True, n=30):
        self.__set_seed()
        if int_data:
            upper = 100
        else:
            upper = 1
        data = [(datetime.datetime(
            year=random.randint(2018, 2019),
            month=random.randint(1, 12),
            day=random.randint(1, 30)
        ), random.randint(1, upper)) for i in range(0, n)]

        return data
