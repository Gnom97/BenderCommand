# -*- coding: utf-8 -*-
"""
TODO
"""
import sys
from connection.Connection import Connection

def exit_func(connection):
    """
    TODO
    """
    Connection.close_connection()
    print("Serielle Verbindung geschlossen")
    print("Programm schließt sich")
    sys.exit(0)
