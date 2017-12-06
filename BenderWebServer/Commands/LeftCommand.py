# -*- coding: utf-8 -*-
from Commands.Command import command

def left_cmd(connection):
    answer = command(connection, b"a\n", 0)
    return str(answer)
    