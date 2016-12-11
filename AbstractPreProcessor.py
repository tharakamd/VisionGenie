from abc import ABCMeta,abstractmethod
from AbstractSensor import AbstractSensor

class AbstractPreProcessor(AbstractSensor):
    __metaclass__ = ABCMeta
    image1 = null;
    image2 = null;
    @abstractmethod
    def update(self,frame):
        return


    def readImage(self):
        self.image1 =Image.open("location1");
        self.image2 =Image.open("location2");