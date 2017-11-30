# -*- coding: utf-8 -*-
from commands.Command import command

def mode_auto(connection):
    answer = command(connection, b'auto\n', None)
    answer = int(answer)
    print(answer)

    if answer == 0:
        print("Automatischer Modus aktiviert")
    else:
        print("Automatischer Modus wurde nicht aktiviert")
