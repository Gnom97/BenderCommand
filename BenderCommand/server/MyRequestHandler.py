# -*- coding: utf-8 -*-
"""
TODO
"""
from http.server import BaseHTTPRequestHandler
from commands.commanddict import COMMANDS_DICT

class MyRequestHander(BaseHTTPRequestHandler):
    """
    TODO
    """

    def do_GET(self):
        """
        TODO
        """
        print("Request empfangen")

    def do_POST(self):
        """
        TODO
        """
        pass
