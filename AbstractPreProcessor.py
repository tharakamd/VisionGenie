from abc import ABCMeta,abstractmethod
from AbstractSensor import AbstractSensor

class AbstractPreProcessor(AbstractSensor):
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self,frame):
        return