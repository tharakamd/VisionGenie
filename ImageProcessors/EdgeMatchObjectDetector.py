import cv2

from PreProcessors.AbstractPreProcessor import AbstractPreProcessor


class EdgeMatchObjectDetector(AbstractPreProcessor):

    def update(self,frame):
        edges = cv2.Canny(frame,100,200)
        self.updateObservers(edges)



