from abc import  ABCMeta, abstractmethod

from Sensors.AbstractSensor import AbstractSensor


class AbstractGyroscope(AbstractSensor):
    __metaclass__ = ABCMeta
    @abstractmethod
    def getCurrentVelocity(self):
        return
    @abstractmethod
    def setStartPosition(self):
        return
    @abstractmethod
    def getDistanceFromCurrentPosition(self):
        return