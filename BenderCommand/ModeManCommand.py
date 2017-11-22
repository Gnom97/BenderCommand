# -*- coding: utf-8 -*-
from Command import command

def modeMan(connection):
	answer = command(connection, b'man\n', 1)
	answer = int(answer)

	if answer == 0:
		print("Manueller Modus aktiviert")
	else:
		print("Manueller Modus wurde nicht aktiviert")
