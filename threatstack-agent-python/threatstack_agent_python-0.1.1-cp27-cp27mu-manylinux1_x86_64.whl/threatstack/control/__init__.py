from __future__ import print_function

import sys
from ..util import logger

_commands = {}

def command(name, options='', description='', hidden=False,
        log_intercept=True):
    def wrapper(callback):
        callback.name = name
        callback.options = options
        callback.description = description
        callback.hidden = hidden
        callback.log_intercept = log_intercept
        _commands[name] = callback
        return callback
    return wrapper

def usage(name):
    details = _commands[name]
    print('Usage: threatstackctl %s %s' % (name, details.options))

@command('help', '[command]', hidden=True)
def help(args):
    if not args:
        print('Usage: threatstackctl command [options]')
        print()
        print("Type 'threatstackctl help <command>'", end='')
        print("for help on a specific command.")
        print()
        print("Available commands are:")

        commands = sorted(_commands.keys())
        for name in commands:
            details = _commands[name]
            if not details.hidden:
                print(' ', name)

    else:
        name = args[0]

        if name not in _commands:
            print("Unknown command '%s'." % name, end=' ')
            print("Type 'threatstackctl help' for usage.")

        else:
            details = _commands[name]

            print('Usage: threatstackctl %s %s' % (name, details.options))
            if details.description:
                print()
                print(details.description)

def main():
    try:
        if len(sys.argv) > 1:
            command = sys.argv[1]
        else:
            command = 'help'

        callback = _commands[command]

    except Exception:
        print("Unknown command '%s'." % command, end='')
        print("Type 'threatstackctl help' for usage.")
        sys.exit(1)

    callback(sys.argv[2:])

module_name = '%s.%s' % (__name__, 'execProgram')
__import__(module_name)    


if __name__ == '__main__':
    main()
