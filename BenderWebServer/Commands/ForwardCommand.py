# -*- coding: utf-8 -*-
from Commands.Command import command

def forward_cmd(connection):
    answer = command(connection, b"w\n", 0)
    return str(answer)
