# -*- coding: utf-8 -*-
"""
TODO
"""

from commands.commandline_only.commanddict import COMMANDS_DICT
from connection.Connection import Connection

def commandline():
    """
    TODO
    """
    #Speichert das aktuelle Kommando als Bytearray
    command = None
    #Entgegennehmen von Kommandos
    while True:
        command = input(">>> ")
        #Finden des Kommandos in der Dictionary commands
        try:
            command_func = COMMANDS_DICT[command]
        except KeyError:
            print("main: Angegebenes Kommando existiert nicht")
            continue

        #Ausführen des Kommandos
        command_func(Connection.connection)
        