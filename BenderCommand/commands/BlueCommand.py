# -*- coding: utf-8 -*-
"""
TODO
"""
from commands.Command import command

def blue(connection):
    """
    TODO
    """
    answer = command(connection, b'blue\n', None)
    print(answer)
