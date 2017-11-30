# -*- coding: utf-8 -*-
"""
TODO
"""
import sys

def exit_func(connection):
    """
    TODO
    """
    connection.close()
    print("Serielle Verbindung geschlossen")
    print("Programm schließt sich")
    sys.exit(0)
