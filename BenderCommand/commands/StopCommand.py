# -*- coding: utf-8 -*-
from commands.Command import command

def stop(connection):
    answer = command(connection, b'stop\n', None)
    answer = int(answer)
    print(answer)

    if answer == 0:
        print("Im Defaultmodus")
    else:
        print("Nicht im Defaultmodus")
