# -*- coding: utf-8 -*-
"""
TODO
"""
from Commands.Command import command

def stop(connection):
    """
    TODO
    """
    answer = command(connection, b'stop\n', None)
    answer = int(answer)
    print(answer)

    if answer == 0:
        return "Im Defaultmodus"
    else:
        return "Nicht im Defaultmodus"
