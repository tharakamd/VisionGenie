from AbstractGyroscope import AbstractGyroscope

class Gyroscope(AbstractGyroscope):
    current_position = 0;
    def getCurrentVelocity(self):
        return 2

    def setStartPosition(self):
        global current_position
        current_position = 0

    def getDistanceFromCurrentPosition(self):
        return 2
