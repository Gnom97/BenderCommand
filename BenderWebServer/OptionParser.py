# -*- coding: utf-8 -*-
import sys
from getopt import GetoptError, getopt

def parse_options(argv):
    short_options = "p:b:"
    port = None
    baudrate = None

    #Parse der Übergabeoptionen
    try:
        opts, args = getopt(argv, short_options)
        print("Unbekannte Argumente: ")
        for arg in args:
            print(arg)
    except GetoptError as err:
        print(err)
        sys.exit()

    #Setzen der Werte
    for opt, val in opts:
        if opt == "-p":
            print("Portname: " + val)
            port = val
        elif opt == "-b":
            print("Baudrate: " + val)
            baudrate = int(val)
        elif opt == "-h":
            print("Parameter: -p Portname -b Baudrate")
        else:
            print("Unbekannte Option: " + opt)

    if port is None:
        sys.exit("Pflichtparameter -p fehlt")
    if baudrate is None:
        sys.exit("Pflichtparameter -b fehlt")

    return port, baudrate
