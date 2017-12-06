# -*- coding: utf-8 -*-
"""
TODO
"""
from Commands.Command import command
from Connections.Connection import Connection

def mode_auto(connection):
    """
    TODO
    """
    answer = command(connection, b'auto\n', None)
    answer = int(answer)
    print(answer)

    if answer == 0:
        return "Automatischer Modus aktiviert"
    else:
        return "Automatischer Modus wurde nicht aktiviert"
