# -*- coding: utf-8 -*-
"""
TODO
"""
from commands.Command import command
import keyboard #pylint: disable=E0401

FORWARD = 'w'
BACKWARD = 's'
LEFT = 'a'
RIGHT = 'd'
STOP = 'esc'

FORWARD_NEWLINE = 'w\n'
BACKWARD_NEWLINE = 's\n'
LEFT_NEWLINE = 'a\n'
RIGHT_NEWLINE = 'd\n'

FORWARD_BYTE = FORWARD_NEWLINE.encode("UTF-8")
BACKWARD_BYTE = BACKWARD_NEWLINE.encode("UTF-8")
LEFT_BYTE = LEFT_NEWLINE.encode("UTF-8")
RIGHT_BYTE = RIGHT_NEWLINE.encode("UTF-8")

def mode_man(connection):
    """
    TODO
    """
    answer = command(connection, b'man\n', None)
    answer = int(answer)
    print(answer)

    if answer == 0:
        print("Manueller Modus aktiviert")
    else:
        print("Manueller Modus wurde nicht aktiviert")

    while True:
        if keyboard.is_pressed(FORWARD):
            command(connection, FORWARD_BYTE, 0)
            print("gesendet w")
        elif keyboard.is_pressed(BACKWARD):
            command(connection, BACKWARD_BYTE, 0)
            print("gesendet s")
        elif keyboard.is_pressed(RIGHT):
            command(connection, RIGHT_BYTE, 0)
            print("gesendet d")
        elif keyboard.is_pressed(LEFT):
            command(connection, LEFT_BYTE, 0)
            print("gesendet a")
        elif keyboard.is_pressed(STOP):
            print("break")
            break
        else:
            command(connection, b'0\n', 0)
