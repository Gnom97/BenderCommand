# -*- coding: utf-8 -*-
"""
TODO
"""

from commands.commandline_only.BlueCommand import blue
from commands.commandline_only.ModeAutoCommand import mode_auto
from commands.commandline_only.ModeManCommand import mode_man
from commands.commandline_only.ExitCommand import exit_func
from commands.commandline_only.StopCommand import stop
from commands.commandline_only.HelpCommand import help_func

COMMANDS_DICT = {
    "blue" : blue,
    "modeauto" : mode_auto,
    "modeman" : mode_man,
    "exit" : exit_func,
    "stop" : stop,
    "help" : help_func
}
