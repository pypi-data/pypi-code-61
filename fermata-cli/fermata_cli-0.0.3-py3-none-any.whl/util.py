import sys
import os
import logging

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger("fermata.debug")


def load_app(path):

    if path is None:
        path = 'app'
    elif path[-3:] == '.py':
        path = path[:-3]

    path = path if '.' in path else f'{path}.app'
    sys.path.append(os.getcwd())
    mod, ins = path.rsplit('.', 1)
    module = __import__(mod, fromlist=[None])

    return getattr(module, ins), module
