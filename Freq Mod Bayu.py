from tkinter import *
from pygame import mixer
import numpy as np
from scipy.io.wavfile import write
import matplotlib.pyplot as plt


root = Tk()
root.title('FM Modulation')
root.geometry('300x300')
mixer.init()


def plotting():
    framerate = 44100
    carrier_Hz = float(entryCarrier.get())
    modulator_Hz = float(entryModulator.get())

    # modulation index adalah berapa banyak energi dari gelombang pembawa,
    modulation_index = float(entryIndex.get())
    t = np.linspace(0, 1, framerate)  # membuat titik sampel

    modulator = np.sin(2.0 * np.pi * modulator_Hz * t) * modulation_index

    carrier = np.sin(2.0 * np.pi * carrier_Hz * t)
    # membuat array signal yang berukuran sama dengan signal modulator namun memiliki value 0
    modulated = np.zeros_like(modulator)
    # modulated = np.cos(2* np.pi *carrier_Hz * t + modulation_index * np.sin(2 * np.pi * modulator_Hz * t))

    #lalu pada array tersebut diisi dengan rumus eFM = Vc sin ( ωc t + mf sin ωm t )
    for i, t in enumerate(t):
        modulated[i] = np.sin(2. * np.pi * (carrier_Hz * t + modulator[i]))

    #memasukkan data signal untuk di simpan pada file wav
    # 32767 adalah rentang maksimum integer yang bisa ditaruk di data 16Bit, karena 16 bit = 2^15 - 1 = 32767
    carrier_signal = np.int16(carrier * 32767)
    modulator_signal = np.int16(modulator * 32767)
    modulated_signal = np.int16(modulated * 32767)

    write('sine.wav', framerate, carrier_signal)
    write('modulator.wav', framerate, modulator_signal)
    write('modulated.wav', framerate, modulated_signal)

    plt.subplot(3, 1, 1)
    plt.plot(carrier, 'g')
    plt.xlim(0, int(entryxlimit.get()))
    plt.ylabel('Amplitude')
    plt.xlabel('Carrier signal')

    plt.subplot(3, 1, 2)
    plt.plot(modulator, 'b')
    plt.ylabel('Amplitude')
    plt.xlabel('Modulator signal')
    plt.xlim(0, int(entryxlimit.get()))

    plt.subplot(3, 1, 3)
    plt.plot(modulated, 'r')
    plt.ylabel('Amplitude')
    plt.xlabel('Modulated signal')
    plt.xlim(0, int(entryxlimit.get()))

    plt.subplots_adjust(hspace=1)
    plt.rc('font', size=15)
    plt.show()


def playCarrier():
    mixer.music.load('sine.wav')
    mixer.music.play()


def playModulator():
    mixer.music.load('modulator.wav')
    mixer.music.play()


def playModulated():
    mixer.music.load('modulated.wav')
    mixer.music.play()


def stopWav():
    mixer.music.stop()


entryCarrier = Entry(root, width=5, border=5)
labelCarrier = Label(root, text='F Carrier (Hz)')
labelCarrier.grid(row=0, sticky='W')
entryCarrier.grid(row=0, column=1)

entryModulator = Entry(root, width=5, border=5)
labelModulator = Label(root, text='F Modulator (Hz)')
labelModulator.grid(row=1, sticky='W')
entryModulator.grid(row=1, column=1)

entryIndex = Entry(root, width=5, border=5)
labelIndex = Label(root, text='Index Modulation (0 - 1)')
labelIndex.grid(row=2, sticky='W')
entryIndex.grid(row=2, column=1)

entryxlimit = Entry(root, width=5, border=5)
labelxlimit = Label(root, text='xlimit')
labelxlimit.grid(row=3, sticky='W')
entryxlimit.grid(row=3, column=1)


plotButton = Button(root, text='Plot & Calculate', command=plotting).grid(
    row=4, sticky='W', padx=5, pady=5)
playCarrier = Button(root, text='play Carrier', command=playCarrier).grid(
    row=5, sticky='W', padx=5, pady=5)
playModulator = Button(root, text='play Modulator', command=playModulator).grid(
    row=6, sticky='W', padx=5, pady=5)
playModulated = Button(root, text='play Modulated', command=playModulated).grid(
    row=7, sticky='W', padx=5, pady=5)
stopButton = Button(root, text='stop', command=stopWav).grid(
    row=8, sticky='W', padx=5, pady=5)


root.mainloop()