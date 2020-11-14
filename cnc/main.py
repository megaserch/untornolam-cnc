#!/usr/bin/env python

import os
import sys
import readline
import atexit
import socketio

import cnc.logging_config as logging_config
from cnc.gcode import GCode, GCodeException
from cnc.gmachine import GMachine, GMachineException

soquete = socketio.Client()

@soquete.event
def message(data):
    print('I received a message!')

#@soquete.on('chat message')
#def on_message(data):
    #print('I received a message!')
    #do_line(data)
    #print(data)

@soquete.on('control message')
def on_message(data):
    #print('I received a message!')
    if (data=='prender_camara'):
    #do_line(data)
        print("prender camara")

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
soquete.connect('http://66.97.46.179:3003/')

print('El sid es', soquete.sid)

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
        g = GCode.parse_line(line)
        res = machine.do_command(g)
    except (GCodeException, GMachineException) as e:
        print('ERROR ' + str(e))
        soquete.emit('chat message', 'ERROR ' + str(e))
        return False
    if res is not None:
        soquete.emit('chat message', 'OK '+ res)
        print('OK ' + res)
    else:
        soquete.emit('chat message', 'OK ')
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
    machine.release()


if __name__ == "__main__":
    main()
