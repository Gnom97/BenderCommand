# -*- coding: utf-8 -*-
"""
TODO
"""
from http.server import HTTPServer #pylint: disable=E0401

from server.MyRequestHandler import MyRequestHandler
from connection.Connection import Connection

def run(server_class=HTTPServer, handler_class=MyRequestHandler, domain="", port=80):
    """
    TODO
    """
    server_address = (domain, port)
    http_server = server_class(server_address, handler_class)
    print("HTTP Server startet")
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()
        print("Serielle Verbindung wird geschlossen")
        Connection.close_connection()


