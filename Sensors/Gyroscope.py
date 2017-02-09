from AbstractGyroscope import AbstractGyroscope
import smbus
import math
import time

class Gyroscope():

    current_position = 0

    MAX_A = 0.8
    MIN_A = -0.8
    AVG_A = 0.2

    power_mgmt_1 = 0x6b
    power_mgmt_2 = 0x6c

    def __init__(self):
        self.bus = smbus.SMBus(1)  # or bus = smbus.SMBus(1) for Revision 2 boards
        self.address = 0x68  # This is the address value read via the i2cdetect command
        self.v = 0
        self.bus.write_byte_data(self.address, self.power_mgmt_1, 0)

    def read_byte(self,adr):
        return self.bus.read_byte_data(self.address, adr)

    def read_word(self,adr):
        high = self.bus.read_byte_data(self.address, adr)
        low = self.bus.read_byte_data(self.address, adr + 1)
        val = (high << 8) + low
        return val

    def read_word_2c(self,adr):
        val = self.read_word(adr)
        if (val >= 0x8000):
            return -((65535 - val) + 1)
        else:
            return val

    def dist(self,a, b):
        return math.sqrt((a * a) + (b * b))

    def get_y_rotation(self,x, y, z):
        radians = math.atan2(x, self.dist(y, z))
        return radians  # there was a - mark here !!!!

    def get_x_rotation(self,x, y, z):
        radians = math.atan2(y, self.dist(x, z))
        return math.degrees(radians)

    def getValidAcceleration(self,a):
        if(a >= self.MAX_A or a <= self.MIN_A ): # error !!! reset value
            a = self.AVG_A
            self.v = 0
        return a

    def getCurrentVelocity(self):

        accel_xout = self.read_word_2c(0x3b)
        accel_yout = self.read_word_2c(0x3d)
        accel_zout = self.read_word_2c(0x3f)

        accel_xout_scaled = accel_xout / 16384.0
        accel_yout_scaled = accel_yout / 16384.0
        accel_zout_scaled = accel_zout / 16384.0

        y_rotation = self.get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
        accel_xout_scaled -= (0.9807 * math.sin(y_rotation) * 10 + 1)
        accel_xout_scaled = self.getValidAcceleration(accel_xout_scaled) # final acceleration value


        self.v += accel_xout_scaled*0.5

        return self.v
