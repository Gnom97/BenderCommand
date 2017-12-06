# -*- coding: utf-8 -*-
"""
Main Modul
TODO
"""
import sys
from getopt import GetoptError, getopt
from commandline.Commandline import commandline
from connection.Connection import Connection


class Main(object):
    """
    Main Klasse
    TODO
    """

    def __init__(self):
        """
        Konstruktor
        TODO
        """
        #Der serielle Port an den das Kommando geht
        self.port = None
        #Ubertragungsgeschwindigkeit in bits pro sekunde
        self.baudrate = 0

    def parse_options(self):
        """
        parse methode
        TODO
        """
        #Optionen
        #p - Portname - Wert muss angegeben werden
        #b - Bautrate - Wert muss angegeben werden
        short_options = "p:b:"

        #Parsen der Übergabeoptionen
        try:
            opts, args = getopt(sys.argv[1:], short_options)
            print("Überflüssige Argumente: ")
            for arg in args:
                print(arg)
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
        if self.port is None:
            sys.exit("Die Option für den Port wurde nicht übergeben (-p)")

        if self.baudrate is None:
            sys.exit("Die Option für die Baudrate wurde nicht übergeben (-b)")



    def main(self):
        """
        TODO
        """
        self.parse_options()
        Connection.open_connection(self.port, self.baudrate)

        commandline()

M_OBJ = Main()
M_OBJ.main()
