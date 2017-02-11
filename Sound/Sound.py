import math
import pyaudio



PyAudio = pyaudio.PyAudio

#See http://en.wikipedia.org/wiki/Bit_rate#Audio
BITRATE = 44100 #number of frames per second/frameset.

FREQUENCY = 2000 #Hz, waves per second, 261.63=C4-note.
LENGTH = 0.1 #seconds to play sound

if FREQUENCY > BITRATE:
    BITRATE = FREQUENCY+100

NUMBEROFFRAMES = int(BITRATE * LENGTH)
RESTFRAMES = NUMBEROFFRAMES % BITRATE
WAVEDATA = ''

for x in xrange(NUMBEROFFRAMES):
 WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))

for x in xrange(RESTFRAMES):
 WAVEDATA = WAVEDATA+chr(128)



p = PyAudio()
print BITRATE
stream = p.open(format = p.get_format_from_width(1),
                channels = 1,
                rate = BITRATE,
		output_device_index = 2,
                output = True)

stream.write(WAVEDATA)
stream.stop_stream()
stream.close()
p.terminate()
