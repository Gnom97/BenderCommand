# -*- coding: utf-8 -*-
from flask import Flask
from Connections.Connection import Connection
from Commands.ModeAutoCommand import mode_auto
from Commands.StopCommand import stop

app = Flask(__name__)
Connection.open_connection('/dev/ttyUSB0', 115200)

@app.route("/")
def index():
    return "Hallo Welt"

@app.route("/auto")
def auto():
    return mode_auto(Connection.connection)

@app.route("/stop")
def halt():
    return stop(Connection.connection)

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1")

Connection.close_connection()
print("Connection geschlossen")
