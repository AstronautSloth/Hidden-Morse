import time
import sys
from socket import *

morseAlphabet = {
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",
    " " : "/"
}

if __name__ == '__main__':
    msg = sys.argv[1].upper()

    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('127.0.0.1', 2525))

    morse_msg = ''
    for char in msg:
        morse_msg += morseAlphabet[char] + ' '

    print(morse_msg)

    for c in morse_msg:
        s.send(' '.encode('utf-8'))
        if c == '.':
            time.sleep(0.1)
        elif c == '-':
            time.sleep(0.3)
        elif c == '/':
            time.sleep(0.5)
        else:
            time.sleep(0.7)

    s.send('END'.encode('utf-8'))
    s.close()