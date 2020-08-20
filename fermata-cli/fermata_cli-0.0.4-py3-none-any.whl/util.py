import sys
import os
import logging

import coloredlogs

logger = logging.getLogger("fermata.debug")


def init_logger(fmt='%(levelname)7s %(message)s'):
    logging.getLogger('meinheld.access').handlers = []
    logging.getLogger('meinheld.error').handlers = []
    coloredlogs.install(fmt=fmt)


def load_app(path):

    if path is None:
        path = 'app'
    elif path[-3:] == '.py':
        path = path[:-3]

    path = path if '.' in path else f'{path}.app'
    sys.path.append(os.getcwd())
    mod, ins = path.rsplit('.', 1)
    module = __import__(mod, fromlist=[None])

    init_logger()

    return getattr(module, ins), module
