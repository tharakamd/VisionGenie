from abc import  ABCMeta, abstractmethod
from AbstractAlgo import AbstractAlgo

class AbstractImageProcessor(AbstractAlgo):

    __metaclass__ = ABCMeta

    @abstractmethod
    def getDistanceToOnject(self):
        return