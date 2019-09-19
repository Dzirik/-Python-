"""
input is not tested
"""

import pandas as pd


class TimeSeries():
    def __init__(self):
        self.ts_list = None
        self.col_names = None

    def set_ts_list(self, ts_list, col_names):
        """
        Set the time series.

        :param ts_list: List. List of tuples (timestamp, value).
        :param col_names: List. Name of time column and name of data column.
        """
        # TODO - add tests of the structure and type + tests
        self.ts_list = ts_list
        self.col_names = col_names

    def get_ts_series(self):
        """
        Get ts as pandas.Series.

        :returns: pandas.series.
        """
        ts = pd.Series(dict(self.ts_list))
        ts.rename(self.col_names[1], inplace=True)
        ts.sort_index()

        return ts

    def get_ts_df(self):
        """
        Get ts as pandas.DataFrame sorted by time.

        :returns: pandas.DataFrame.
        """
        df = pd.DataFrame(self.ts_list)
        df.columns = self.col_names
        df.sort_values(by=self.col_names[0], inplace=True)
        df.reset_index(drop=True, inplace=True)

        return df
