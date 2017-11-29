# -*- coding: utf-8 -*-

def exit(connection):
	connection.close()
	print("Serielle Verbindung geschlossen")
	print("Programm schließt sich")
	sys.exit(0)
