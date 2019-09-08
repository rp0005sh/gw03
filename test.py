# coding: utf-8

import pyaudio
import numpy as np
import matplotlib.pyplot as plt

import RPi.GPIO as GPIO
import time


CHUNK = 1024
RATE = 44100

P = pyaudio.PyAudio()

stream = P.open(format=pyaudio.paInt16, channels=1, rate=RATE, frames_per_buffer=CHUNK, input=True, output=False)
a = []
for i in range(0, int(RATE / CHUNK * 3)):
    data = stream.read(CHUNK, exception_on_overflow=False)
    a.append(data)

stream.stop_stream()
stream.close()
P.terminate()

a = b''.join(a)

GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.OUT)
GPIO.output(15, GPIO.HIGH)
time.sleep(1)
GPIO.output(15, GPIO.LOW)


x = np.frombuffer(a,dtype="int16") / 32768.0
plt.figure(figsize=(15,3))
plt.plot(x)
plt.show()

