# -*- coding: utf-8 -*-
"""
TODO
"""
from http.server import HTTPServer #pylint: disable=E0401

from server.MyRequestHandler import MyRequestHander


def run(server_class=HTTPServer, handler_class=MyRequestHander, domain="", port=80):
    """
    TODO
    """
    server_address = (domain, port)
    http_server = server_class(server_address, handler_class)
    print("HTTP Server startet")
    http_server.serve_forever()
