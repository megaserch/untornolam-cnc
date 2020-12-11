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
import subprocess

# standard Python
soquete = socketio.Client()


#modoprueba = 0

@soquete.event
def message(data):
    print('I received a message!')

@soquete.on('COMANDOS TORNO')
def on_message(data):
    #global modoprueba
    #print('I received a message!')
    #print(data)
    #print('I received a message!')
    #if (data=='prender_camara' & camara==0):
    if (data=='prender_torno'):
        #print("Prender Torno")
        subprocess.run(['bash','/home/pi/untornolam-cnc/untornolam-cnc/otros/app-torno.sh'])
        soquete.emit('control message', 'Torno Encendido')
        #if (data=='apagar_camara' & camara==1):
        return True

    if (data=='apagar_torno'):
        #print("Apagar Torno")
        subprocess.run(['bash','/home/pi/untornolam-cnc/untornolam-cnc/otros/apagar_torno.sh'])
        soquete.emit('control message', 'Torno Apagado')
        return True

    if (data=='actualizar_torno'):
        #print("Actualizar GIT Torno")
        subprocess.run(['bash','/home/pi/untornolam-cnc/untornolam-cnc/otros/actualizar.sh'])
        soquete.emit('control message', 'Torno Actualizado')
        return True

    if (data=='habilitar_ssh'):
        #print("Habilitar GIT Torno")
        subprocess.run(['bash','/home/pi/untornolam-cnc/untornolam-cnc/otros/habilitar_ssh.sh'])
        soquete.emit('control message', 'SSH Habilitado')
        return True

    if (data=='test'):
        #print("Test")
        subprocess.run(['bash','ps -aux'])
        return True

    print('Comando del Torno desconocido: ' + data)
    return True



#do_line(data)
#print(data)

#@soquete.on('control message')
#def on_message(data):
    #print('I received a message!')
    #if (data=='juan'):
    #    print("entro")
    #else:
    #print("no entro")

@soquete.event
def connect():
    print("Conectado al mundo UNtornoLaM!")

@soquete.event
def connect_error():
    print("Error de conexion!")

@soquete.event
def disconnect():
    print("Desconectado del mundo UNtornoLaM, vuelvas brontos!")


print("Intentanto conectar al mundo UNtornoLaM!")

#soquete.connect('http://66.97.46.179:3003/test')
soquete.connect('http://66.97.46.179:3003/')

print('El id de conexion es', soquete.sid)

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
        #soquete.emit('chat message', line)
        do_line(line)
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
