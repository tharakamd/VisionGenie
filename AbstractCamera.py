from abc import  ABCMeta, abstractmethod
from AbstractSensor import AbstractSensor

class AbstractCamera(AbstractSensor):
    __metaclass__ = ABCMeta

    @abstractmethod
    def getVideo(self):
        return

    @abstractmethod
    def getFrames(self):
        return