import time
import socketserver

morseAlphabet ={
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

reverse_morse = dict((v,k) for (k,v) in morseAlphabet.items())

class DecoderHandler(socketserver.BaseRequestHandler):
    def handle(self):
        t1 = time.time()
        self.timings = []
        while True:
            self.data = self.request.recv(1024).decode('utf-8')
            if self.data == 'END':
                break

            t2 = time.time()
            self.timings.append(t2-t1)
            t1 = t2

        morse = ''
        del self.timings[0]
        for t in self.timings:
            if t < 0.3:
                morse += '.'
            elif t < 0.5:
                morse += '-'
            elif t < 0.7:
                morse += '/'
            else:
                morse += ' '

        decoded = ''.join(reverse_morse.get(i) for i in morse.split())
        print(morse)
        print(decoded)
        #self.shutdown()

if __name__ == '__main__':
    server = socketserver.TCPServer(('localhost', 2525), DecoderHandler)
    server.serve_forever()