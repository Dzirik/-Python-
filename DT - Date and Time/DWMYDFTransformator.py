# TODO - refactor transform
from DWMYTransformator import DWMYTransformator


class DWMYDFTransformator(DWMYTransformator):

    def __init__(self):
        DWMYTransformator.__init__(self)
        self.name = "DWMY"
        self.data_type = "df"

    def transform(self, X, time_type, atr_names):
        """

        :param X:
        :param time_type:
        :return:
        """
        # X[atr_names[0] + "_" + time_type] = super(DWMYDFTransformator, self).fit(X[atr_names[0]].array, time_type)
        # X[atr_names[0] + "_" + time_type] = DWMYTransformator.fit(self, X[atr_names[0]].array, time_type)
        X[atr_names[0] + "_" + time_type] = super().fit(X[atr_names[0]].array, time_type)
        X.drop([atr_names[0]], axis=1, inplace=True)
        X.reset_index(drop=True, inplace=True)

        return X

    def fit(self, X, time_type, atr_names):
        """
        :param X:
        :param time_type:
        :return:
        """
        return self.transform(X, time_type, atr_names)

    def fit_predict(self, X, time_type, atr_names):
        return self.transform(X, time_type, atr_names)

    def predict(self, X, time_type, atr_names):
        return self.transform(X, time_type, atr_names)
