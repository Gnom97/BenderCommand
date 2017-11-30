# -*- coding: utf-8 -*-
"""
TODO
"""
from http.server import BaseHTTPRequestHandler #pylint: disable=E0401
from commands.commanddict import COMMANDS_DICT

class MyRequestHander(BaseHTTPRequestHandler):
    """
    TODO
    """

    def do_GET(self): #pylint: disable=C0103
        """
        TODO
        """
        print("Request empfangen")

    def do_POST(self): #pylint: disable=C0103
        """
        TODO
        """
        pass
