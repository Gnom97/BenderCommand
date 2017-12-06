# -*- coding: utf-8 -*-
from Commands.Command import command
from Commands.Returncodes import SUCCESS

def forward_cmd(connection):
    answer = command(connection, b"w\n", 0)

    if answer is None:
        answer = SUCCESS

    return str(answer)
