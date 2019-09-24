from BaseTransformator import BaseTransformator


class DWMYTransformator(BaseTransformator):

    def __init__(self):
        BaseTransformator.__init__(self, name="DWMY", data_type="array")

    def _transform(self, X, time_type):
        """

        :param X:
        :param time_type:
        :return:
        """
        if time_type == "d":
            return ((X.year + X.month / 100 + X.day / 10000) * 10000).astype(int)
        elif time_type == "w":
            return ((X.year + X.week / 100) * 100).astype(int)
        elif time_type == "m":
            return ((X.year + X.month / 100) * 100).astype(int)
        elif time_type == "y":
            return (X.year).astype(int)

    def fit(self, X, time_type):
        """
        :param X:
        :param time_type:
        :return:
        """
        return self._transform(X, time_type)

    def fit_predict(self, X, time_type):
        return self._transform(X, time_type)

    def predict(self, X, time_type):
        return self._transform(X, time_type)
