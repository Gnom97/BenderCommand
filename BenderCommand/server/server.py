# -*- coding: utf-8 -*-
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 80
SERVER_ADDRESS = ("", PORT)

class Server(BaseHTTPRequestHandler):
    def __init__(self, commandsdict):
        #Dictionary aller Kommandos
        self.commandsdict = commandsdict
        #HTTPServer
        self.http_server = HTTPServer(SERVER_ADDRESS, Server)

    def run(self):
        print("HTTP Server wird gestartet")
        self.http_server.serve_forever()

    def do_GET(self):
        pass
