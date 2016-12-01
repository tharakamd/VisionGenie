from AbstractPreProcessor import AbstractPreProcessor
import numpy as np
import cv2

class EdgeMatchObjectDetector(AbstractPreProcessor):

    def update(self,frame):
        edges = cv2.Canny(frame,100,200)
        cv2.imshow('frame',edges)


