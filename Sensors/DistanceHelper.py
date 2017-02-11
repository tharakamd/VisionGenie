from Gyroscope import Gyroscope
class DistanceHelper:
    MAX_SPEED = 0.8
    AVERAGE_SPEED = 0.55

    def __init__(self):
        self.gyro = Gyroscope()

    def getCurrentVelocity(self):
        current_speed = self.gyro.getCurrentVelocity();
        if(current_speed > self.MAX_SPEED): # error in speed, then give average speed
            return self.AVERAGE_SPEED
        return current_speed - 0.1

