#!/usr/bin/env python

import os
import sys
import readline
import atexit
#import socketio
#import subprocess
import time

import cnc.logging_config as logging_config
from cnc.gcode import GCode, GCodeException
from cnc.gmachine import GMachine, GMachineException

#modoprueba = 1
#soquete = socketio.Client()

#@soquete.event
#def message(data):
#    print('Mensaje Recibido!')

#@soquete.on('chat message')
#def on_message(data):
    #print('I received a message!')
    #do_line(data)
    #print(data)

#@soquete.on('GCODE Box Chat')
#def on_message(data):
    #global modoprueba
    #print('I received a message!')
    #comentada do_line(data)
    #if data[0]!='T':
        #print(data+'\n')
        #if modoprueba==1:
            #print("torno ->" + data + "\n")
            #do_line(data)
        #else:
            #print("prueba ->" + data + "\n")
            #soquete.emit('GCODE Box Chat', 'TOK ')
    #else:
        #if data=='TTORNO':
            #modoprueba = 1
            #soquete.emit('GCODE Box Chat', 'TSe entra en modo TORNO ')
        #if data=='TPRUEBA':
            #modoprueba = 0
            #soquete.emit('GCODE Box Chat', 'TSe entra en modo PRUEBA ')
        #soquete.emit('GCODE-Box-Chat-1', 'TOK ')

        #print('del torno\n')


#@soquete.on('GCODE STATUS TORNO')
#def on_message(data):
    #print('I received a message!')
    #comentada do_line(data)
    #if data[0]!='T':
    #    print(data+'\n')
    #soquete.emit('control message', 'Enc_Calibr')
        #print('del torno\n')

#@soquete.on('control message')
#def on_message(data):
    #print('I received a message!')
    #if (data=='prender_camara' & camara==0):
    #if (data=='prender_camara'):
        #print("prender la camara")
        #subprocess.run(['bash','./prender_camara.sh'])
        #soquete.emit('control message', 'camara_prendida')
    #if (data=='apagar_camara' & camara==1):
    #if (data=='apagar_camara'):
        #print("apagar la camara")
        #subprocess.run(['bash','./apagar_camara.sh'])
        #soquete.emit('control message', 'camara_apagada')

    #do_line(data)
    #print(data)

#@soquete.event
#def connect():
    #print("Conectado!")
    #soquete.emit('control message', 'Enc_SinCal')
    #time.sleep(2)
    #soquete.emit('control message', 'Calibrando')
    #time.sleep(1)
    #print("Voy a mandar el do line g28")
    #do_line("g91")
    #do_line("g1 x10 f300")
    #time.sleep(1)
    #do_line("g1 x20 f400")
    #time.sleep(0.1)
    #do_line("G28")
    #time.sleep(8)
    #print("Volvi del do_line bro ")
    #time.sleep(2)
    #soquete.emit('control message', 'Enc_Calibr')
    #time.sleep(1)

#@soquete.event
#def connect_error():
    #print("Falla de conexion!")

#@soquete.event
#def disconnect():
    #print("Desconectado!")


#print("Intentanto conectar")

#soquete.connect('http://66.97.46.179:3003/test')
#soquete.connect('http://66.97.46.179:3003/')

#print('El socket id es', soquete.sid)


try:  # python3 compatibility
    type(raw_input)
except NameError:
    # noinspection PyShadowingBuiltins
    raw_input = input

# configure history file for interactive mode
history_file = os.path.join(os.environ['HOME'], '.pycnc_history')
try:
    readline.read_history_file(history_file)
except IOError:
    pass
readline.set_history_length(1000)
atexit.register(readline.write_history_file, history_file)

machine = GMachine()


def do_line(line):
    try:
        #print('Line : ' + line + ' \n ')
        if line.find('\n') < 0:
            line = line + '\n'

        if line[0] == 'D' and line[1] == '1':
            g = GCode.parse_line(line)
            res = machine.do_command(g)
        else:
            g = GCode.parse_line(line)
            #print('EN g :  \n ')
            #print(vars(g))
            #print('voy a mandar el do command')
            res = machine.do_command(g)
            #print('volvi del do_comand')
    except (GCodeException, GMachineException) as e:
        print('ERROR ' + str(e))
        #soquete.emit('GCODE Box Chat', 'TERROR ' + str(e))
        return False
    if res is not None:
        #soquete.emit('GCODE Box Chat', 'TOK '+ res)
        print('OK ' + res)
    else:
        #soquete.emit('GCODE Box Chat', 'TOK ')
        print('OK')
    return True


def main():
    logging_config.debug_disable()
    try:
        if len(sys.argv) > 1:
            # Read file with gcode
            with open(sys.argv[1], 'r') as f:
                for line in f:
                    line = line.strip()
                    print('> ' + line)
                    #comentada
                    if not do_line(line):
                        #comentada
                        break
                    time.sleep(6)
        else:
            # Main loop for interactive shell
            # Use stdin/stdout, additional interfaces like
            # UART, Socket or any other can be added.
            print("*************** Bienvenido a UNTornoLaM! ***************")

            while True:
                line = raw_input('> ')
                if line == 'quit' or line == 'exit':
                    break
                do_line(line)
    except KeyboardInterrupt:
        pass
    print("\r\n Saliendo...")
    machine.release()


if __name__ == "__main__":
    main()
