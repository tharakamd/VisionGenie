import  cv2
from PreProcessors.AbstractPreProcessor import AbstractPreProcessor

class GBRtoGRAYpreProcessor(AbstractPreProcessor)
    def update(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_resized = cv2.resize(gray,(100,50))
        self.updateObservers(gray)