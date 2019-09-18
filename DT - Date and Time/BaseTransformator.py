from abc import ABC, abstractmethod


class BaseTransformator(ABC):

    def __init__(self, name, data_type):
        self.name = name
        self.data_type = data_type

    @abstractmethod
    def fit(self):
        pass

    @abstractmethod
    def predict(self):
        pass

    @abstractmethod
    def fitpredict(self):
        pass
