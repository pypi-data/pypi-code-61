"""Fermata cli.

Usage:
  fermata init
  fermata complete [<app>]
  fermata debug [<app>] [--host=<host>] [--port=<port>]

Options:
  -h --help     Show this screen.
  --host=<host>      [default: 127.0.0.1]
  --port=<port>  [default: 8000]

"""
from docopt import docopt

from .initializer import init
from .completor import complete
from .debugger import debug


def main():
    args = docopt(__doc__)
    if args['init']:
        init()
    elif args['complete']:
        complete(args['<app>'])
    elif args['debug']:
        debug(args['<app>'], args['--host'], args['--port'])

