import DWMYDFTransformator as DWMYDFT
import DWMYGroupTransformator as DWMYGgroup
import TSToIndexTransformator as TSToIndex
import TimeSeries as TS


class PipelineTSToIndex():

    def __init__(self):
        self.ts = TS.TimeSeries()
        self.dwmy_df_t = DWMYDFT.DWMYDFTransformator()
        self.dwmy_group_t = DWMYGgroup.DWMYGroupTransformator()
        self.ts_to_index_t = TSToIndex.TSToIndexTransformator()

    def execute(self, df, time_type, atr_names_df, atr_names_ts, group_fun, fun_type="entropy"):
        df_idx = df[atr_names_df[1]].apply(
            self._create_index_for_ts_list,
            args=(time_type, atr_names_ts, group_fun, fun_type)
        )
        df_idx = df_idx.to_frame()
        df_idx[atr_names_df[0]] = df[atr_names_df[0]]

        return df_idx

    def _group_ts_from_list(self, X, time_type, atr_names, group_fun):
        self.ts.set_ts_list(X, atr_names)
        df = self.ts.get_ts_df()

        df = self.dwmy_df_t.fitpredict(df, time_type, atr_names)
        df = self.dwmy_group_t.fitpredict(df, time_type, atr_names, group_fun)

        return df

    def _compute_index(self, X, atr_names, fun_type):
        return self.ts_to_index_t.fitpredict(X[atr_names[1]].array, fun_type)

    def _create_index_for_ts_list(self, X, time_type, atr_names, group_fun, fun_type="entropy"):
        df = self._group_ts_from_list(X, time_type, atr_names, group_fun)
        index = self._compute_index(df, atr_names, fun_type)

        return index