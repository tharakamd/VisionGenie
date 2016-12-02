# from abc import  ABCMeta, abstractmethod
from AbstractCamera import AbstractCamera
import numpy as np
import cv2

class WebCamera(AbstractCamera):

    def start(self):
        cap = cv2.VideoCapture(0)
        while(True):
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Display the resulting frame
            # cv2.imshow('frame',gray)
            self.updateObservers(gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()
