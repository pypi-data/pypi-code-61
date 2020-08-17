"""Custom ThreatStack logger

"""

import sys
import logging

from ..config import CONF

# COLORS = {
#     'regular': {'prefix': '\e[00m', 'suffix': '\e[0m'},
#     'bright': {'prefix': '\e[01m', 'suffix': '\e[0m'},
#     'black': {'prefix': '\e[30m', 'suffix': '\e[0m'},
#     'red': {'prefix': '\e[31m', 'suffix': '\e[0m'},
#     'green': {'prefix': '\e[32m', 'suffix': '\e[0m'},
#     'yellow': {'prefix': '\e[33m', 'suffix': '\e[0m'},
#     'blue': {'prefix': '\e[34m', 'suffix': '\e[0m'},
#     'magenta': {'prefix': '\e[35m', 'suffix': '\e[0m'},
#     'cyan': {'prefix': '\e[36m', 'suffix': '\e[0m'},
#     'gray': {'prefix': '\e[37m', 'suffix': '\e[0m'}
# }

# def color_text(text, color):
#     if not COLORS[color]:
#         return text
#     return COLORS[color]['prefix'] + text + COLORS[color]['suffix']



# # The background is set with 40 plus the number of the color, and the foreground with 30
# BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)
#
# # These are the sequences need to get colored ouput
# RESET_SEQ = "\033[0m"
# COLOR_SEQ = "\033[1;%dm"
# BOLD_SEQ = "\033[1m"
# COLORS = {
#     'DEBUG': WHITE,
#     'INFO': CYAN,
#     'WARNING': YELLOW,
#     'ERROR': RED,
#     'CRITICAL': RED
# }
#
# class ThreatstackLogFormatter(logging.Formatter):
#     def __init__(self, msg, use_color = False):
#         logging.Formatter.__init__(self, msg)
#         self.use_color = use_color
#
#     def format(self, record):
#         levelname = record.levelname
#         if self.use_color and levelname in COLORS:
#             levelname_color = COLOR_SEQ % (30 + COLORS[levelname]) + levelname + RESET_SEQ
#             record.levelname = levelname_color
#         return logging.Formatter.format(self, record)

def getLogger(name):
    logger = logging.getLogger(name)
    try:
        level = logging.getLevelName(CONF['LOG_LEVEL'])
        if CONF['LOG_COLORS']:
            from colorlog import ColoredFormatter
            formatter = ColoredFormatter(
                "[%(asctime)s] %(thread)d - %(log_color)s%(levelname)-5.5s%(reset)s %(name)s: %(message)s",
                datefmt=None,
                reset=True,
                log_colors={
                    'DEBUG': 'cyan',
                    'INFO': 'green',
                    'WARNING': 'yellow',
                    'ERROR': 'red',
                    'CRITICAL': 'red,bg_white',
                },
                secondary_log_colors={},
                style='%'
            )
        else:
            formatter = logging.Formatter("[%(asctime)s] %(thread)d - %(levelname)-5.5s %(name)s: %(message)s")
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(formatter)
        handler.setLevel(level)
        logger.handlers = []
        logger.propagate = False
        logger.addHandler(handler)
    except:
        print('Logger setup error', sys.exc_info()[0])
        logger.setLevel(logging.CRITICAL)
    return logger

