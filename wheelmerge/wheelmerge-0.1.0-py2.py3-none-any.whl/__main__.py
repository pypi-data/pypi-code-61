import sys
import re

import entrypoints


def main():
    entry_points = entrypoints.get_group_all("console_scripts", sys.path[:2])

    sys.argv = sys.argv[1:]
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])

    if len(sys.argv) > 0:
        for entry_point in entry_points:
            if entry_point.name == sys.argv[0]:
                return entry_point.load()()
        else:
            sys.stderr.write("No such console script '{}'\n".format(sys.argv[0]))
    else:
        sys.stderr.write("Console script is missing!")


if __name__ == '__main__':
    sys.exit(main())
