from Gyroscope import Gyroscope
from AbstractImageProcessor import AbstractImageProcessor
from Gyroscope import Gyroscope
from AbstractPreProcessor import AbstractPreProcessor

class BinacularVisionImageProcessor(AbstractImageProcessor):

    gyroscope = Gyroscope;
    velocity = gyroscope.velocity;


    def getDistanceToObject(self):

        preprocess = AbstractPreProcessor;
        image1 = preprocess.image1;
        image2 = preprocess.image2;
        return;