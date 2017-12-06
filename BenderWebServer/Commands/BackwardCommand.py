# -*- coding: utf-8 -*-
from Commands.Command import command

def backward_cmd(connection):
    answer = command(connection, b"s\n", 0)
    return str(answer)
    