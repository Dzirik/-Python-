from BaseTransformator import BaseTransformator


class NumberToOneTransformator(BaseTransformator):

    def __init__(self):
        BaseTransformator.__init__(self, name="NumberToOne", data_type="df")

    def __transform(self, X, atr_names):
        """

        :param X:
        :param atr_names:
        :return:
        """
        X[atr_names[1]] = [1] * X.shape[0]

        return X

    def fit(self, X, atr_names):
        """
        :param X:
        :param time_type:
        :return:
        """
        return self.__transform(X, atr_names)

    def fitpredict(self, X, atr_names):
        return self.__transform(X, atr_names)

    def predict(self, X, atr_names):
        return self.__transform(X, atr_names)
