from morse_converter import convertTextToMorse
import cv2
import pytesseract
import winsound
import time
import tempfile
import wave
import math
import struct
import numpy as np

time_unit = 0.1


def dot():
    winsound.Beep(600, int(time_unit*1000))
    print('dot')
    time.sleep(time_unit)


def dash():
    winsound.Beep(500, int(time_unit*1000*3))
    time.sleep(time_unit)
    print('dash')


def write_signal(wavef, duration, volume=0, rate=44100.0, frequency=1240.0):
    """
    rate = 44100.0 # Sample rate in Hertz
    duration = 0.1       # seconds
    frequency = 1240.0    # hertz
    """
    for i in range(int(duration * rate * duration)):
            # max volume 32767.0
            value = int(volume*math.sin(frequency*math.pi*float(i)/float(rate)))
            data = struct.pack('<h', value)
            wavef.writeframesraw(data)


def morse_to_wav(text, file_=None):

    char2signal = {'.': 0.2, '-': 0.4, '/': 0.5, ' ': 0.2}
    file_ = './morse.wav' #tempfile.mkstemp(".wav")

    wav = wave.open(file_, 'wb')
    wav.setnchannels(1) # mono
    wav.setsampwidth(2)
    rate = 44100.0
    wav.setframerate(rate)

    for char in text:
        write_signal(wav, char2signal[char], volume=32767.0)
        write_signal(wav, 0.3, volume=0)

    wav.writeframes(b'')
    wav.close()
    print('Saved')
    return file_


def morse_to_vid(text):

    time_unit = 0.1
    height = width = 300

    char2signal = {'.': 0.2, '-': 0.4, '/': 0.5, ' ': 0.2}

    out = cv2.VideoWriter('./morse.webm',cv2.VideoWriter_fourcc(*'VP90'), 20, (width, height))

    for char in text:
        frame = np.zeros((height,width,3), np.uint8)
        if char != ' ':
            frame[:, :] = (0, 0, 255)
        for _ in range(int(time_unit * char2signal[char] * 100)):
            out.write(frame)
        out.write(np.zeros((height,width,3), np.uint8))

    out.release()


def encode_image(image):

    text = pytesseract.image_to_string(image)

    s = [convertTextToMorse(i.lower()) for i in text]

    s = [i for i in s if i is not None]

    return text, s


def encode_text(text):
    
    s = [convertTextToMorse(i.lower()) for i in text]

    s = [i for i in s if i is not None]

    return text, s

def play(s):
    for word in s:
        for ch in word:
            for i in ch:
                if i=='.':
                    dot()
                elif i=='-':
                    dash()
            time.sleep(time_unit*3)
        time.sleep(time_unit*7)
