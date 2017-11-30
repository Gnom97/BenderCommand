# -*- coding: utf-8 -*-
"""
TODO
"""

from commands.BlueCommand import blue
from commands.ExitCommand import exit_func
from commands.HelpCommand import help_func
from commands.ModeAutoCommand import mode_auto
from commands.ModeManCommand import mode_man
from commands.StopCommand import stop

COMMANDS_DICT = {
    "blue" : blue,
    "modeauto" : mode_auto,
    "modeman" : mode_man,
    "exit" : exit_func,
    "stop" : stop,
    "help" : help_func
}
