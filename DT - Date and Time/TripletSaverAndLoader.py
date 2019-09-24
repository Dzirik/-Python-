"""
Data frames are too large to save. Converting to arrays seems to work.
The goal is to convert it from df to array, save and opposite.
"""

import os
import pickle

import pandas as pd

from ConfigHandler import ConfigHandler
from Timerer import Timerer


class TripletSaverAndLoader(ConfigHandler):

    def __init__(self, config):
        super(TripletSaverAndLoader, self).__init__(config)
        self.t = Timerer()
        self.t.set_initial_timestamp(False)

    def save_triplet(self, df, file_name, atr_groupby, atr_value, where_to_store="raw"):
        """
        Saves a data frame into Raw or Final folder.

        :param df: DataFrame. DF to save.        
        :param file_name: String. File name without .pkl.
        :param atr_groupby: String. Name of index.
        :param atr_value: String. Name of values in time series.
        :param where_to_store: String. Within a folder strucutre "raw" or "final"
        """
        self.t.set_meantime(print_results=False)

        idx = df[atr_groupby].to_list()
        ts = df["TS_" + atr_value].to_list()
        for_save = [idx, ts]

        path = self.__get_path(file_name, where_to_store)

        with open(path, 'wb') as handle:
            pickle.dump(for_save, handle, protocol=pickle.HIGHEST_PROTOCOL)

        self.t.set_meantime(label="Saving Triplet Duration: ", print_results=True)

    def load_triplet(self, file_name, atr_groupby, atr_value, where_to_store="raw"):
        """
        Loads a pickle data frame from Raw or Final folder.
        
        :param file_name: String. File  name without .pkl.
        :param atr_groupby: String. Name of index.
        :param atr_value: String. Name of values in time series.
        :param where_to_store: String. Within a folder strucutre "raw" or "final"
        
        :return: DataFrame
        """
        self.t.set_meantime(print_results=False)

        path = self.__get_path(file_name, where_to_store)
        with open(path, 'rb') as handle:
            loaded = pickle.load(handle)

        df = pd.DataFrame()
        df[atr_groupby] = loaded[0]
        df["TS_" + atr_value] = loaded[1]

        self.t.set_meantime(label="Loading Triplet Duration: ", print_results=True)

        return df

    def __get_path(self, file_name, where_to_store="raw"):
        """
        Returns path of a file for Raw or Final data folder.
        
        :param file_name: String. File  name without .pkl.
        :param where_to_store: String. Within a folder strucutre "raw" or "final"
        :return: String. Path.
        """
        if where_to_store == "raw":
            # dir_path = os.path.join(os.getcwd(),"../../RawData")
            dir_path = self.config.get("path", "raw_data")
        elif where_to_store == "final":
            # dir_path = os.path.join(os.getcwd(),"../../FinalData")
            dir_path = self.config.get("path", "final_data")

        return os.path.abspath(os.path.join(
            dir_path, file_name + ".pkl"
        ))
