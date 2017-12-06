# -*- coding: utf-8 -*-
import sys

from flask import Flask, render_template

from Commands.ModeAutoCommand import mode_auto_cmd
from Commands.ModeDefaultCommand import mode_default_cmd
from Commands.ModeManCommand import mode_man_cmd
from Commands.ForwardCommand import forward_cmd
from Commands.BackwardCommand import backward_cmd
from Commands.LeftCommand import left_cmd
from Commands.RightCommand import right_cmd
from Commands.StopCommand import stop_cmd
from Connections.Connection import Connection
from OptionParser import parse_options

APP = Flask(__name__)

BENDER_PORT, BAUDRATE = parse_options(sys.argv[1:])

Connection.open_connection(BENDER_PORT, BAUDRATE)

@APP.route("/")
def index():
    """
    Ruft die Startseite auf
    """
    return render_template("index.html")

#Wechseln zwischen den Modi von Bender
@APP.route("/auto")
def auto():
    """
    Lässt Bender in den Automatikmodus wechseln
    """
    return mode_auto_cmd(Connection.connection)

@APP.route("/default")
def defaul():
    """
    Lässt Bender in den Defaultmodus wechseln
    """
    return mode_default_cmd(Connection.connection)

@APP.route("/man")
def man():
    """
    Lässt Bender in den Manuellenmodus wechseln
    """
    return mode_man_cmd(Connection.connection)

#Befehle für den Manuellen Modus
@APP.route("/forward")
def forward():
    """
    Lässt Bender im Manuellenmodus vorwärts fahren"
    """
    return forward_cmd(Connection.connection)

@APP.route("/backward")
def backward():
    """
    Lässt Bender im Manuellenmodus rückwärts fahren"
    """
    return backward_cmd(Connection.connection)

@APP.route("/left")
def left():
    """
    Lässt Bender im Manuellenmodus links fahren"
    """
    return left_cmd(Connection.connection)

@APP.route("/right")
def right():
    """
    Lässt Bender im Manuellenmodus rechts fahren"
    """
    return right_cmd(Connection.connection)

@APP.route("/stop")
def stop():
    """
    Lässt Bender im Manuellenmodus anhalten"
    """
    return stop_cmd(Connection.connection)

#Starten des WebServers
APP.run(debug=True, host="127.0.0.1")

#Schließen der Verbindung zu Bender
Connection.close_connection()
print("Connection geschlossen")
