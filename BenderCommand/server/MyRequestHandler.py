# -*- coding: utf-8 -*-
"""
TODO
"""
from commands.server_only.commanddict import COMMANDS_DICT
from http.server import BaseHTTPRequestHandler  # pylint: disable=E0401
from urllib.parse import parse_qs, urlparse  # pylint: disable=E0611,E0401

from connection.Connection import Connection

CMD_PARAM_NAME = "cmd"

class MyRequestHandler(BaseHTTPRequestHandler):
    """
    TODO
    """

    def do_GET(self): #pylint: disable=C0103
        """
        TODO
        """
        url_components = urlparse(self.path)
        param_dict = parse_qs(url_components.query)
        command_name = None
        cmd_is_set = True

        try:
            command_name = param_dict[CMD_PARAM_NAME]
        except KeyError:
            print("Parameter " + CMD_PARAM_NAME + " nicht gesetzt")
            cmd_is_set = False

        if cmd_is_set is True:
            try:
                COMMANDS_DICT[command_name[0]](Connection.connection)
            except KeyError:
                print("Unbekanntes Kommando " + command_name[0])


    def do_POST(self): #pylint: disable=C0103
        """
        TODO
        """
        pass
