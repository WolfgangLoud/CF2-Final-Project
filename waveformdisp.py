import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt

CHUNK = 1024 * 4  # 4096 samples per chunk
FORMAT = pyaudio.paInt16  # bytes per sample
CHANNELS = 1  # mono sound
RATE = 44100  # samples per second (44.1 kHz)

p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)


#possible method to implement synth input
#input_device_index = None
#for i in range(p.get_device_count()):
#    info = p.get_device_info_by_index(i)
#    if 'synthesizer' in info['name'].lower():  # Adjust this condition based on your synthesizer's name
#        input_device_index = i
#        break

#if input_device_index is None:
#    print("Synthesizer input device not found.")
#    exit()

fig, ax = plt.subplots()
x = np.arange(0, 2 * CHUNK, 2)
line, = ax.plot(x, np.random.rand(CHUNK))

ax.set_ylim(0, 255)
ax.set_xlim(0, 2 * CHUNK)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Intensity')
plt.title('Synthesizer Waveform Output Display')

while True:
    data = stream.read(CHUNK)
    data_int = np.array(struct.unpack(str(2 * CHUNK) + 'B', data), dtype='b')[::2] + 128
    line.set_ydata(data_int)
    plt.pause(0.01)  # Pause for a short time to update the plot
    plt.draw()
