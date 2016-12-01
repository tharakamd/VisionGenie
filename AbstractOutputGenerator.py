from abc import  ABCMeta, abstractmethod
from AbstractAlgo import AbstractAlgo

class AbstractOurputGenerator(AbstractAlgo):

    __metaclass__ = ABCMeta

    @abstractmethod
    def convertDetailToSound(self):
        return