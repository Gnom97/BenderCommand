# -*- coding: utf-8 -*-
from Command import command
import keyboard

forward = 'w'
backward = 's'
left = 'a'
right = 'd'
stop = 'esc'

def modeMan(connection):
	answer = command(connection, b'man\n', None)
	answer = int(answer)
	print(answer)

	if answer == 0:
		print("Manueller Modus aktiviert")
	else:
		print("Manueller Modus wurde nicht aktiviert")

	while True:
		inputStr = ''

		if keyboard.is_pressed(forward):
			inputStr += forward
		if keyboard.is_pressed(backward):
			inputStr += backward
		if keyboard.is_pressed(right):
			inputStr += right
		if keyboard.is_pressed(left):
			inputStr += left
		if keyboard.is_pressed(stop):
			break

		inputStr += '\n'
		command(connection, inputStr.encode("UTF-8"), None)
