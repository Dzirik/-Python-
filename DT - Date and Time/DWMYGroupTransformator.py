from BaseTransformator import BaseTransformator


class DWMYGroupTransformator(BaseTransformator):

    def __init__(self):
        BaseTransformator.__init__(self, name="DWMYGroup", data_type="df")

    def __transform(self, X, time_type, atr_names, fun):
        """

        :param X:
        :param time_type:
        :param col_names:
        :return:
        """
        atr_time = atr_names[0] + "_" + time_type

        df_res = X.groupby(by=atr_time, as_index=True).apply(fun)
        df_res.drop([atr_time], axis=1, inplace=True)
        df_res.reset_index(level=0, inplace=True)

        return df_res

    def fit(self, X, time_type, atr_names, fun):
        """
        :param X:
        :param time_type:
        :return:
        """
        return self.__transform(X, time_type, atr_names, fun)

    def fit_predict(self, X, time_type, atr_names, fun):
        return self.__transform(X, time_type, atr_names, fun)

    def predict(self, X, time_type, atr_names, fun):
        return self.__transform(X, time_type, atr_names, fun)
