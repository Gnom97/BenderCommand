# -*- coding: utf-8 -*-
from Commands.Command import command
from Commands.Returncodes import TIMEOUT

def right_cmd(connection):
    answer = command(connection, b"d\n", 0)
    return str(answer)
    