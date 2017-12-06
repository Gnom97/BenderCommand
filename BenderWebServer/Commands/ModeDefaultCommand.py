# -*- coding: utf-8 -*-
"""
TODO
"""
from Commands.Command import command
from Commands.Returncodes import TIMEOUT

def mode_default_cmd(connection):
    """
    TODO
    """
    answer = command(connection, b'stop\n', None)

    if answer == b'':
        answer = TIMEOUT

    return str(answer)