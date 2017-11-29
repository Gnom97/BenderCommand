# -*- coding: utf-8 -*-
from getopt import getopt, GetoptError
from serial import Serial, SerialException
from BlueCommand import blue
from ModeAutoCommand import modeAuto
from ModeManCommand import modeMan
from ExitCommand import exit
from HelpCommand import helpFunc
from StopCommand import stop

import sys

commands = {
	"blue" : blue,
	"modeauto" : modeAuto,
	"modeman" : modeMan,
	"exit" : exit,
	"stop" : stop,
	"help" : helpFunc
}

class Main: 
	def __init__(self):
		#Der serielle Port an den das Kommando geht
		self.port = None
		#Ubertragungsgeschwindigkeit in bits pro sekunde
		self.baudrate = 0
		#Das Objekt mit für die serielle Verbindung
		self.connection = None

	def parseOptions(self):
		#Optionen
		#p - Portname - Wert muss angegeben werden
		#b - Bautrate - Wert muss angegeben werden
		shortOptions = "p:b:"

		#Parsen der Übergabeoptionen
		try:
			opts, args = getopt(sys.argv[1:], shortOptions)
		except GetoptError as err:
			print(err)
			sys.exit()

		#Setzen aller übergebenen Werte
		for opt, val in opts:
			if opt == "-p":
				print("Portname: " + val)
				self.port = val
			elif opt == "-b":
				print("Baudrate: " + val)
				self.baudrate = int(val)
			elif opt == "-h":
				print("Parameter: -p Portname -b Bautrate")
			else:
				print("Unbekannte Option: " + opt)

		#Ob Pflichtoptionen gesetzt wurden
		if self.port == None:
			sys.exit("Die Option für den Port wurde nicht übergeben (-p)")

		if self.baudrate == None:
			sys.exit("Die Option für die Baudrate wurde nicht übergeben (-b)")
	#-----------------------------------------------------------------------------------

	def openConnection(self):
		#Öffnen der seriellen Verbindung
		try:
			self.connection = Serial(self.port, self.baudrate)
		except SerialException as err:
			sys.exit(err)

		print(self.connection.name)
	#-----------------------------------------------------------------------------------

	def main(self):
		self.parseOptions()
		self.openConnection()

		#Speichert das aktuelle Kommando als Bytearray
		command = None
		#Speichert die tatsächlich geschriebenen Bytes durch write
		count = 0	
		#Entgegennehmen von Kommandos
		while True:
			command = input(">>> ")

			#Finden des Kommandos in der Dictionary commands	
			try:
				commandFunc = commands[command]
			except KeyError:
				print("main: Angegebenes Kommando existiert nicht. Überprüfe ob die Funktion in der Map commands (main.py) gesetzt wurde")
				continue
	
			#Ausführen des Kommandos
			commandFunc(self.connection)
	#-----------------------------------------------------------------------------------

m = Main()
m.main()
