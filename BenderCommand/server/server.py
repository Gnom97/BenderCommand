# -*- coding: utf-8 -*-
"""
TODO
"""
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 80
SERVER_ADDRESS = ("", PORT)

class Server(BaseHTTPRequestHandler):
    """
    TODO
    """

    def __init__(self, commandsdict):
        """
        TODO
        """
        #Dictionary aller Kommandos
        self.commandsdict = commandsdict
        #HTTPServer
        self.http_server = HTTPServer(SERVER_ADDRESS, Server)

    def run(self):
        """
        TODO
        """

        print("HTTP Server wird gestartet")
        self.http_server.serve_forever()

    def do_GET(self):
        """
        TODO
        """
        pass
