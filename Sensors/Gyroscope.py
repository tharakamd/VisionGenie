from AbstractGyroscope import AbstractGyroscope

class Gyroscope(AbstractGyroscope):
    current_position = 0;

    def getCurrentVelocity(self):
        return 2
