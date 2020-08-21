import argparse
import pathlib
import colorama


CHAR_EMPTY = '│'
CHAR_CHILD = '├'
CHAR_CHILD_END = '└'
CHAR_START = '┐'
CHAR_SUB_START = '┬'
CHAR_INDENT = '─'

COLOR_FILE = colorama.Fore.GREEN
COLOR_DIR = colorama.Fore.CYAN
COLOR_RESET = colorama.Style.RESET_ALL


def create_argparser():
    parser = argparse.ArgumentParser(
        prog='ppdir',
        description='Pretty print a directory structure as a tree',
    )

    parser.add_argument('-a, --all', dest='all', action='store_true', help='Include hidden files')
    parser.add_argument('-c, --color', dest='color', action='store_true', help='Colorize output')

    parser.add_argument('dir', metavar='DIR', type=str, nargs='?')

    return parser

def make_dir_output(path, args, depth=0, last=False):
    if path.name.startswith('.') and not args.all:
        return ''

    output = ''
    indent = CHAR_INDENT * depth
    empty = ' ' + (CHAR_EMPTY * (depth - 1))
    pre = CHAR_CHILD_END if last else CHAR_CHILD

    if path.is_file():
        output += f'{empty}{pre}{indent} {COLOR_FILE if args.color else ""}{path.name}{COLOR_RESET if args.color else ""}\n'
    else:
        if depth > 0:
            output += f'{empty}{pre}{CHAR_SUB_START}{indent} {COLOR_DIR if args.color else ""}{path.name}{COLOR_RESET if args.color else ""}\n'

        contents = sorted(list(path.iterdir()), key=lambda d: d.is_file())

        for index, elem in enumerate(contents):
            last = index == (len(contents) - 1)
            output += make_dir_output(elem, args, depth + 1, last=last)

    return output


def main():
    args_parser = create_argparser()
    args = args_parser.parse_args()

    if not args.dir:
        args_parser.print_help()
    else:
        if args.color:
            colorama.init()

        output = f'{CHAR_INDENT}{CHAR_START}\n{make_dir_output(pathlib.Path(args.dir), args)}'
        print(output)
    

if __name__ == '__main__':
    main()
