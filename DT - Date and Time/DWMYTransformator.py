from BaseTransformator import BaseTransformator


class DWMYTransformator(BaseTransformator):

    def __init__(self):
        super(BaseTransformator, self).__init__("DWMY", "array")

    def __transform(self, X, type):
        """

        :param X:
        :param type:
        :return:
        """
        if type == "d":
            return ((X.year + X.month / 100 + X.day / 10000) * 10000).astype(int)
        elif type == "w":
            return ((X.year + X.week / 100) * 100).astype(int)
        elif type == "m":
            return ((X.year + X.month / 100) * 100).astype(int)
        elif type == "y":
            return (X.year).astype(int)

    def fit(self, X, type):
        """
        :param X:
        :param type:
        :return:
        """
        return self.__transform(X, type)

    def fitpredict(self, X, type):
        return self.__transform(X, type)

    def predict(self, X, type):
        return self.__transform(X, type)
