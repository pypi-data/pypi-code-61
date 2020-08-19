import argparse
from . import version


def entry_point():
    parser = argparse.ArgumentParser(
        description='This is for ... Data models',
        epilog='''Shows the optional arguments to view the version and verbosity.''')
    parser.add_argument('--verbose', '-v', action='count',
                        help='increase verbosity.  Specify multiple times '
                             'for increased diagnostic output')
    parser.add_argument('--version', action='version',
                        version='%(prog)s {}'.format(version),
                        help='show the version number and exit')

    parser.parse_args()
    # do stuff here

if __name__ == '__main__':
    entry_point()