from abc import ABC, abstractmethod


class BaseTransformator(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fit(self):
        pass

    @abstractmethod
    def predict(self):
        pass

    @abstractmethod
    def fitpredict(self):
        pass
