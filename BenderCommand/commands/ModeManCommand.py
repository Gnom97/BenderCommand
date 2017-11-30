# -*- coding: utf-8 -*-
from commands.Command import command
import keyboard

forward = 'w'
backward = 's'
left = 'a'
right = 'd'
stop = 'esc'

forwardNewline = 'w\n'
backwardNewline = 's\n'
leftNewline = 'a\n'
rightNewline = 'd\n'

forward_byte = forwardNewline.encode("UTF-8")
backward_byte = backwardNewline.encode("UTF-8")
left_byte = leftNewline.encode("UTF-8")
right_byte = rightNewline.encode("UTF-8")

def modeMan(connection):
	answer = command(connection, b'man\n', None)
	answer = int(answer)
	print(answer)

	if answer == 0:
		print("Manueller Modus aktiviert")
	else:
		print("Manueller Modus wurde nicht aktiviert")

	while True:
		if keyboard.is_pressed(forward):
			command(connection, forward_byte, 0)
			print("gesendet w")
		elif keyboard.is_pressed(backward):
			command(connection, backward_byte, 0)
			print("gesendet s")
		elif keyboard.is_pressed(right):
			command(connection, right_byte, 0)
			print("gesendet d")
		elif keyboard.is_pressed(left):
			command(connection, left_byte, 0)
			print("gesendet a")
		elif keyboard.is_pressed(stop):
			print("break")
			break
		else:
			command(connection, b'0\n', 0)
