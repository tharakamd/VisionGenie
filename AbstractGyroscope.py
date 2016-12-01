from abc import  ABCMeta, abstractmethod
from AbstractSensor import AbstractSensor

class AbstractGyroscope(AbstractSensor):
    __metaclass__ = ABCMeta
    @abstractmethod
    def getCurrentVelocity(self):
        return