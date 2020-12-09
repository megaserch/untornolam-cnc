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
#import socketio
from socketIO_client import SocketIO

# standard Python
soquete = SocketIO('http://66.97.46.179',3003)


@soquete.event
def message(data):
    print('I received a message!')

@soquete.on('chat message')
def on_message(data):
    #print('I received a message!')
    print(data)

@soquete.event
def connect():
    print("I'm connected!")

@soquete.event
def connect_error():
    print("The connection failed!")

@soquete.event
def disconnect():
    print("I'm disconnected!")


print("intentanto conectar")

#soquete.connect('http://66.97.46.179:3003/test')
#soquete.connect('http://66.97.46.179:3003/')

print('El sid es', soquete.sid)

#soquete.emit('test', {'probando': 'desde python'})

try:  # python3 compatibility
    type(raw_input)
except NameError:
    # noinspection PyShadowingBuiltins
    raw_input = input

try:
    # Main loop for interactive shell
    # Use stdin/stdout, additional interfaces like
    # UART, Socket or any other can be added.
    print("*************** Welcome to PyCNC! ***************")
    while True:
        line = raw_input('> ')
        if line == 'quit' or line == 'exit':
            break
        #soquete.emit('test', line)
        soquete.emit('chat message', line)
        #do_line(line)
except KeyboardInterrupt:
    pass
print("\r\nExiting...")






#soquete.emit('test', 'ESTE MENSAJE VIENE DE PYTHON! ah y juan se la come')
#soquete.emit()

print("conectado")
print("saliendo")


soquete.disconnect()


#@soquete.event
#def my_event(sid, data):
    # handle the message
#    print("el dato es:" + data)
#    return "OK", 123
