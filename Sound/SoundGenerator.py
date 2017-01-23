import math
import pyaudio

class SoundGenerator:


    def __init__(self):
        self.BITRATE = 16000 #number of frames per second/frameset.
        self.LENGTH = 0.5  # seconds to play sound
        PyAudio = pyaudio.PyAudio
        self.paudio = PyAudio()
        self.stream = self.paudio.open(format=self.paudio.get_format_from_width(1),
                        channels=1,
                        rate=self.BITRATE,
                        output=True)

    def updateDistance(self,new_distance):
        frequency = (1/new_distance)*5000
        if frequency > self.BITRATE:
            bitrate = frequency + 100
        else:
            bitrate = self.BITRATE

        number_of_frames = int(bitrate * self.LENGTH)
        rest_frames = number_of_frames % bitrate
        wavedata = ''
        for x in xrange(number_of_frames):
            wavedata = wavedata + chr(int(math.sin(x / ((bitrate / frequency) / math.pi)) * 127 + 128))

        for x in xrange(rest_frames):
            wavedata = wavedata + chr(128)

        self.stream.write(wavedata)
        # self.stop_stream()
