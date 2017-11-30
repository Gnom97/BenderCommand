# -*- coding: utf-8 -*-
from commands.Command import command

def blue(connection):
	answer = command(connection, b'blue\n', None)
	print(answer)
