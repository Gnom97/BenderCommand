# -*- coding: utf-8 -*-
from Command import command

def blue(connection):
	answer = command(connection, b'blue\n', None)
	print(answer)
