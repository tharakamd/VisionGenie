from AbstractGyroscope import AbstractGyroscope

class Gyroscope(AbstractGyroscope):
    velocity =0;
    current_position = 0;
    def getCurrentVelocity(self,reading):
        self.velocity = reading;
        return 2

    def setStartPosition(self):
        global current_position
        current_position = 0

    def getDistanceFromCurrentPosition(self):
        return 2
