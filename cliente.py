#!/usr/bin/env python

'''from socketIO_client import SocketIO, BaseNamespace

class Namespace(BaseNamespace):

    def on_connect(self):
        print('[Connected]')

    def on_reconnect(self):
        print('[Reconnected]')

    def on_disconnect(self):
        print('[Disconnected]')

socketIO = SocketIO('66.97.46.179', 3003, Namespace)
socketIO.wait(seconds=1)'''

import os
import sys
import readline
import atexit
import socketio

# standard Python
soquete = socketio.Client()

print("intentanto conectar")

soquete.connect('http://66.97.46.179:3003/test')

print('El sid es', soquete.sid)

#soquete.emit('test', {'probando': 'desde python'})


try:
    if len(sys.argv) > 1:
        # Read file with gcode
        with open(sys.argv[1], 'r') as f:
            for line in f:
                line = line.strip()
                print('> ' + line)
                if not do_line(line):
                    break
    else:
        # Main loop for interactive shell
        # Use stdin/stdout, additional interfaces like
        # UART, Socket or any other can be added.
        print("*************** Welcome to PyCNC! ***************")
        while True:
            line = raw_input('> ')
            if line == 'quit' or line == 'exit':
                break
            do_line(line)
except KeyboardInterrupt:
    pass
print("\r\nExiting...")






soquete.emit('test', 'ESTE MENSAJE VIENE DE PYTHON! ah y juan se la come')
#soquete.emit()

print("conectado")
print("saliendo")


soquete.disconnect()


#@soquete.event
#def my_event(sid, data):
    # handle the message
#    print("el dato es:" + data)
#    return "OK", 123

@soquete.event
def message(data):
    print('I received a message!')

@soquete.event
def connect():
    print("I'm connected!")

@soquete.event
def connect_error():
    print("The connection failed!")

@soquete.event
def disconnect():
    print("I'm disconnected!")
