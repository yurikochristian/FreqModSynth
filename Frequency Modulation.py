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
root.title("Kalimba Gecko")


carrier_frequency = [265.0,291.0,327.0,338.0,381.0,426.0,493.0,508.0,587.0,643.0,688.0,772.0,865.0,984.0,1045.0,1160.0,1312.0]
# modulator_frequency = 1079.0/265.0*carrier_frequency[3]
# modulator_frequency = 1.0/7.0*carrier_frequency[3]
# modulator_frequency2 = 1695.0/1079.0*carrier_frequency[3]
modulation_index = 0.05
# modulation_index2 = 0.05

y, sr = librosa.load('Kalimba 4.wav')
envelope = abs(sn.hilbert(y))
envelope = maf(envelope)
for i in range(len(envelope)):
    envelope[i] = envelope[i]*25

time = np.arange(len(envelope)) / sr
# carrier = np.sin(2.0 * np.pi * carrier_frequency[3] * time)
# modulator = np.sin(2.0 * np.pi * modulator_frequency * time) * modulation_index
# product = envelope*np.sin((carrier + modulator))
product = []
for i in range(17):
    modulator_frequency = 1079.0/265.0 * carrier_frequency[i]
    carrier = np.sin(2.0 * np.pi * carrier_frequency[i] * time)
    modulator = np.sin(2.0 * np.pi * modulator_frequency * time) * modulation_index
    product.append(envelope * np.sin((carrier + modulator)))

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

# sf.write('Frequency Modulation.wav', product, sr, subtype='PCM_16')
sf.write('FM Carrier.wav', carrier, sr, subtype='PCM_16')
for i in range(17):
    sf.write('Modulated '+str(i+1)+'.wav', product[i], sr, subtype='PCM_16')

def play_1():
    mx.init()
    mx.music.load('Modulated 1.wav')
    mx.music.play()

def play_2():
    mx.init()
    mx.music.load('Modulated 2.wav')
    mx.music.play()

def play_3():
    mx.init()
    mx.music.load('Modulated 3.wav')
    mx.music.play()

def play_4():
    mx.init()
    mx.music.load('Modulated 4.wav')
    mx.music.play()

def play_5():
    mx.init()
    mx.music.load('Modulated 5.wav')
    mx.music.play()

def play_6():
    mx.init()
    mx.music.load('Modulated 6.wav')
    mx.music.play()

def play_7():
    mx.init()
    mx.music.load('Modulated 7.wav')
    mx.music.play()

def play_8():
    mx.init()
    mx.music.load('Modulated 8.wav')
    mx.music.play()

def play_9():
    mx.init()
    mx.music.load('Modulated 9.wav')
    mx.music.play()

def play_10():
    mx.init()
    mx.music.load('Modulated 10.wav')
    mx.music.play()

def play_11():
    mx.init()
    mx.music.load('Modulated 11.wav')
    mx.music.play()

def play_12():
    mx.init()
    mx.music.load('Modulated 12.wav')
    mx.music.play()

def play_13():
    mx.init()
    mx.music.load('Modulated 13.wav')
    mx.music.play()

def play_14():
    mx.init()
    mx.music.load('Modulated 14.wav')
    mx.music.play()

def play_15():
    mx.init()
    mx.music.load('Modulated 15.wav')
    mx.music.play()

def play_16():
    mx.init()
    mx.music.load('Modulated 16.wav')
    mx.music.play()

def play_17():
    mx.init()
    mx.music.load('Modulated 17.wav')
    mx.music.play()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

label1 = Label(topFrame,text="Frequency Modulation Kalimba Gecko")
label1.pack(side=TOP)

button1 = Button(topFrame,
                 text="1",
                 bg="grey",
                 fg="black",command=play_1)
button2 = Button(topFrame,
                 text="2",
                 bg="grey",
                 fg="black",command=play_2)
button3 = Button(topFrame,
                 text="3",
                 bg="grey",
                 fg="black",command=play_3)
button4 = Button(topFrame,
                 text="4",
                 bg="grey",
                 fg="black",command=play_4)
button18 = Button(topFrame,
                 text="5",
                 bg="grey",
                 fg="black",command=play_5)
button6 = Button(topFrame,
                 text="6",
                 bg="grey",
                 fg="black",command=play_6)
button7 = Button(topFrame,
                 text="7",
                 bg="grey",
                 fg="black",command=play_7)
button8 = Button(topFrame,
                 text="8",
                 bg="grey",
                 fg="black",command=play_8)
button9 = Button(topFrame,
                 text="9",
                 bg="grey",
                 fg="black",command=play_9)
button10 = Button(topFrame,
                 text="10",
                 bg="grey",
                 fg="black",command=play_10)
button11 = Button(topFrame,
                 text="11",
                 bg="grey",
                 fg="black",command=play_11)
button12 = Button(topFrame,
                 text="12",
                 bg="grey",
                 fg="black",command=play_12)
button13 = Button(topFrame,
                 text="13",
                 bg="grey",
                 fg="black",command=play_13)
button14 = Button(topFrame,
                 text="14",
                 bg="grey",
                 fg="black",command=play_14)
button15 = Button(topFrame,
                 text="15",
                 bg="grey",
                 fg="black",command=play_15)
button16 = Button(topFrame,
                 text="16",
                 bg="grey",
                 fg="black",command=play_16)
button17 = Button(topFrame,
                 text="17",
                 bg="grey",
                 fg="black",command=play_17)
button5 = Button(bottomFrame,
                 text="EXIT",
                 command=root.destroy)

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
button18.pack(side=LEFT)
button6.pack(side=LEFT)
button7.pack(side=LEFT)
button8.pack(side=LEFT)
button9.pack(side=LEFT)
button10.pack(side=LEFT)
button11.pack(side=LEFT)
button12.pack(side=LEFT)
button13.pack(side=LEFT)
button14.pack(side=LEFT)
button15.pack(side=LEFT)
button16.pack(side=LEFT)
button17.pack(side=LEFT)
button5.pack()

root.mainloop()