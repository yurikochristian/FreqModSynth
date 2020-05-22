import librosa
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sn


def framing(signal, size, step):
    frame = []
    for i in range(0, len(signal), step):
        frame.append(signal[i:i + size])
    return frame

def hilbert1(signal):
    hil = []
    for i in range(len(signal)):
        hil.append(abs((1/np.pi*i)*signal[i]))
    return hil

def maf(signal):
    env = []
    point = 200
    for i in range(len(signal)):
        if(i<len(signal)-point):
            env.append((1/point)*sum(signal[i:i+point]))
    return env

def energy(signal):
    env = []
    frame = framing(signal,512,256)
    for i in range(len(frame)):
        f,t,Zxx = sn.stft(frame[i],44100,nperseg=512)
        env.append(sum(abs(Zxx)))
    return env



def hanning_window(frame):
    windowed = []
    for i in range(len(frame)):
        windowed.append([])
        for j in range(len(frame[i])):
            windowed[i].append(frame[i][j] * (0.5 - (0.5 * np.cos(2 * np.pi / len(frame[i]) * j))))
    return windowed

def note_build(windowed, length):
    note = []
    for i in range(len(windowed)-1):
        for j in range(length):
            if(j<256):
                note.append(windowed)

y, sr = librosa.load('Kalimba 4.wav')
L = 512
envelope = abs(sn.hilbert(y))
envelope = maf(envelope)
plt.plot(envelope)
plt.show()