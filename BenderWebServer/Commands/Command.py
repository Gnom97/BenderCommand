# -*- coding: utf-8 -*-
"""
TODO
"""

def command(connection, command_str, answer_size):
    """
    TODO
    """
    #Ob gültige Parameter gesetzt sind
    if connection is None:
        print("command: connection ist None")
        return -1
    if command_str is None or not command_str: #not command_str -> len(command_str) == 0
        print("command: commandStr ist None")
        return -1

    #Schreiben der Nachricht
    byte_count = connection.write(command_str)
    #Überprüfung ob genug Bytes geschickt wurden
    if byte_count < len(command_str):
        print("command: Es konnten nicht alle Bytes geschrieben")

    #Lesen der Antwort
    answer = None
    if answer_size is None:
        answer = connection.readline()
    elif answer_size > 0:
        answer = connection.read(answer_size)

    return answer
