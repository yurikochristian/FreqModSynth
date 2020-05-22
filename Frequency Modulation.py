import numpy as np
import librosa
import matplotlib.pyplot as plt
from tkinter import *
import pygame.mixer as mx
import soundfile as sf
from scipy import signal as sn

def maf(signal):
    env = []
    point = 200
    for i in range(len(signal)):
        if(i<len(signal)-point):
            env.append((1/point)*sum(signal[i:i+point]))
    return env

root = Tk()

sr = 44100
duration = 4

carrier_frequency = [265.0,291.0,327.0,338.0,381.0,426.0,493.0,508.0,587.0,643.0,688.0,772.0,865.0,984.0,1045.0,1160.0,1312.0]
modulator_frequency = 1079.0/265.0*carrier_frequency[8]
modulator_frequency2 = 1695.0/1079.0*carrier_frequency[8]
modulation_index = 0.05
modulation_index2 = 0.05

y, sr = librosa.load('Kalimba 4.wav')
envelope = abs(sn.hilbert(y))
envelope = maf(envelope)
for i in range(len(envelope)):
    envelope[i] = envelope[i]*25

time = np.arange(len(envelope)) / 44100.0
carrier = np.sin(2.0 * np.pi * carrier_frequency[8] * time)
modulator = np.sin(2.0 * np.pi * modulator_frequency * time) * modulation_index
modulator2 = np.sin(2.0 * np.pi * modulator_frequency2 * time) * modulation_index2
product = envelope*np.sin((carrier + modulator + modulator2))

def plot():
    plt.subplot(3,1,1)
    plt.title('Frequency Modulation')
    plt.plot(modulator[:3000],'g')
    plt.ylabel('Amplitude')
    plt.xlabel('Modulator signal')

    plt.subplot(3,1,2)
    plt.plot(carrier[:3000], 'r')
    plt.ylabel('Amplitude')
    plt.xlabel('Carrier signal')

    plt.subplot(3,1,3)
    plt.plot(product[:3000], color="purple")
    plt.ylabel('Amplitude')
    plt.xlabel('FM signal')

    plt.subplots_adjust(hspace=1)
    plt.rc('font', size=15)
    plt.show()

sf.write('Frequency Modulation.wav', product, sr, subtype='PCM_16')
sf.write('FM Carrier.wav', carrier, sr, subtype='PCM_16')
sf.write('FM Modulator.wav', modulator, sr, subtype='PCM_16')

def play_modulated():
    mx.init()
    mx.music.load('Frequency Modulation.wav')
    mx.music.play()

def play_carrier():
    mx.init()
    mx.music.load('FM Carrier.wav')
    mx.music.play()

def play_modulator():
    mx.init()
    mx.music.load('FM Modulator.wav')
    mx.music.play()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

label1 = Label(topFrame,text="Frequency Modulation")
label1.pack(side=TOP)

button1 = Button(topFrame,
                 text="Show Waveform",
                 bg="blue",
                 fg="white",command=plot)
button2 = Button(topFrame,
                 text="Play Modulated Signal",
                 bg="green",
                 fg="white",command=play_modulated)
button3 = Button(topFrame,
                 text="Play Carrier",
                 bg="green",
                 fg="white",command=play_carrier)
button4 = Button(topFrame,
                 text="Play Modulator",
                 bg="green",
                 fg="white",command=play_modulator)
button5 = Button(bottomFrame,
                 text="EXIT",
                 command=root.destroy)

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
button5.pack()

root.mainloop()