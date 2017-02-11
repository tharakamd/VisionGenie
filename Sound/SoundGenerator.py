import math
import pyaudio

class SoundGenerator:


    def __init__(self):
        self.BITRATE = 44100 #this is the value for my usb sound card
        self.LENGTH = 0.1 # seconds to play sound
        PyAudio = pyaudio.PyAudio
        self.paudio = PyAudio()
        self.stream = self.paudio.open(format=self.paudio.get_format_from_width(1),
                        channels=1,
                        output_device_index=2,
                        rate=self.BITRATE,
                        output=True)

    def updateDistance(self,new_distance):
        frequency = (1/new_distance)*5000
        # the frequency would be in the range of 50 - 5000 Hz
        if frequency > self.BITRATE:
            bitrate = frequency + 100
        else:
            bitrate = self.BITRATE
        number_of_frames = int(bitrate * self.LENGTH)
        rest_frames = number_of_frames % bitrate
        wavedata = ''
        for x in xrange(number_of_frames):
            wavedata = wavedata + chr(int(math.sin(x / ((bitrate / frequency) / math.pi)) * 127 + 128))
        rest_frames = int(rest_frames)
        for x in xrange(rest_frames):
            wavedata = wavedata + chr(128)
        self.stream.write(wavedata)
        # self.stop_stream()
