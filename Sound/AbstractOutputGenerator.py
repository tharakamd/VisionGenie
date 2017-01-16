from abc import  ABCMeta, abstractmethod

from ImageProcessors.AbstractAlgo import AbstractAlgo


class AbstractOurputGenerator(AbstractAlgo):

    __metaclass__ = ABCMeta

    @abstractmethod
    def convertDetailToSound(self):
        return