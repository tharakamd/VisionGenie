import  cv2
from PreProcessors.AbstractPreProcessor import AbstractPreProcessor

class GBRtoGRAYpreProcessor(AbstractPreProcessor)
    def update(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        self.updateObservers(gray)