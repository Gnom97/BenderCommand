# -*- coding: utf-8 -*-
import sys
from getopt import GetoptError, getopt

from serial import Serial, SerialException

from BenderCommand.commands.BlueCommand import blue
from BenderCommand.commands.ExitCommand import exit_func
from BenderCommand.commands.HelpCommand import help_func
from BenderCommand.commands.ModeAutoCommand import mode_auto
from BenderCommand.commands.ModeManCommand import mode_man
from BenderCommand.commands.StopCommand import stop
from BenderCommand.server.server import Server


class Main(object):
    def __init__(self):
        #Der serielle Port an den das Kommando geht
        self.port = None
        #Ubertragungsgeschwindigkeit in bits pro sekunde
        self.baudrate = 0
        #Das Objekt mit für die serielle Verbindung
        self.connection = None
        #Ob die Anwendung mit einem Server oder der Kommandozeile läuft
        self.server_flag = False
        #Dictionary aller Kommandos
        self.commandsdict = {
            "blue" : blue,
            "modeauto" : mode_auto,
            "modeman" : mode_man,
            "exit" : exit_func,
            "stop" : stop,
            "help" : help_func
        }

    def parse_options(self):
        #Optionen
        #p - Portname - Wert muss angegeben werden
        #b - Bautrate - Wert muss angegeben werden
        short_options = "p:b:w"

        #Parsen der Übergabeoptionen
        try:
            opts, args = getopt(sys.argv[1:], short_options)
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
            elif opt == "-w":
                self.server_flag = True
            else:
                print("Unbekannte Option: " + opt)

		#Ob Pflichtoptionen gesetzt wurden
        if self.port is None:
            sys.exit("Die Option für den Port wurde nicht übergeben (-p)")

        if self.baudrate is None:
            sys.exit("Die Option für die Baudrate wurde nicht übergeben (-b)")

    def open_connection(self):
        #Öffnen der seriellen Verbindung
        try:
            self.connection = Serial(self.port, self.baudrate)
        except SerialException as err:
            sys.exit(err)

        print(self.connection.name)

    def main(self):
        self.parse_options()
        self.open_connection()

        if self.server_flag is True:
            ser_obj = Server(self.commandsdict)
            ser_obj.run()
        else:
            self.commandline()

    def commandline(self):
        #Speichert das aktuelle Kommando als Bytearray
        command = None
        #Entgegennehmen von Kommandos
        while True:
            command = input(">>> ")
            #Finden des Kommandos in der Dictionary commands
            try:
                command_func = self.commandsdict[command]
            except KeyError:
                print("main: Angegebenes Kommando existiert nicht")
                continue

            #Ausführen des Kommandos
            command_func(self.connection)

M_OBJ = Main()
M_OBJ.main()
