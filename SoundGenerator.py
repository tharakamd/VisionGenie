import math
import pyaudio

class SoundGenerator:

    def __init__(self):
        self.BITRATE = 16000
        self.FREQUENCY = 2000  # Hz
        PyAudio = pyaudio.PyAudio
        self.p = PyAudio();
        self.stream = self.p.open(format=p.get_format_from_width(1),
                        channels=1,
                        rate=self.BITRATE,
                        output=True)

    def updateDistance(self,new_distance):
        self.frequency = (1/new_distance)*5000

    def generateSound(self):
        c_distance = self.distance
