# -*- coding: utf-8 -*-
"""
TODO
"""
import sys
from serial import Serial, SerialException

class Connection(object):
    """
    TODO
    """
    connection = None

    @staticmethod
    def open_connection(port, baudrate):
        """
        TODO
        """
        if Connection.connection is not None:
            print("Ein Verbindung ist bereits offen, schließe diese zuerst")
        else:
            try:
                Connection.connection = Serial(port, baudrate, timeout=1, write_timeout=1)
            except SerialException as err:
                sys.exit(err)

    @staticmethod
    def close_connection():
        """
        TODO
        """
        if Connection.connection is not None:
            Connection.connection.close()
            Connection.connection = None
