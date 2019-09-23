import numpy as np

from BaseTransformator import BaseTransformator


def entropy(labels, base=None):
    # TODO - think a bit about it
    # TODO - create a tests for it
    """ Computes entropy of label distribution. """

    n_labels = len(labels)

    if n_labels <= 1:
        return 0

    value, counts = np.unique(labels, return_counts=True)
    probabilities = counts / n_labels
    n_classes = np.count_nonzero(probabilities)

    if n_classes <= 1:
        return 0

    ent = 0.

    # Compute entropy
    if base is None:
        divisor = 1
    else:
        divisor = np.log(base)
    for i in probabilities:
        ent -= i * np.log(i) / divisor

    return ent / (np.log(n_classes) / divisor)


class TSToIndexTransformator(BaseTransformator):

    def __init__(self):
        BaseTransformator.__init__(self, name="TSToIndex", data_type="array")

    def __transform(self, X, fun_type):
        if fun_type == "entropy":
            return entropy(X)

    def fit(self, X, fun_type="entropy"):
        return self.__transform(X, fun_type)

    def fitpredict(self, X, fun_type="entropy"):
        return self.__transform(X, fun_type)

    def predict(self, X, fun_type="entropy"):
        return self.__transform(X, fun_type)
