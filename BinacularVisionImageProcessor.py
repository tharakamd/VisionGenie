import numpy as np
import cv2
from AbstractImageProcessor import AbstractImageProcessor

class BinacularVisionImageProcessor(AbstractImageProcessor):

    def update(self,frame):
        cv2.imshow('frame',frame)