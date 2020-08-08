#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Formula Helpers for reading dimacs

Copyright (C) 2012-2020 Massimo Lauria <massimo.lauria@uniroma1.it>
https://massimolauria.net/cnfgen/
"""

import argparse
from cnfgen.utils.parsedimacs import readCNF

from cnfgen.clitools import redirect_stdin
from cnfgen.clitools import interactive_msg
from cnfgen.clitools import msg_prefix

from .formula_helpers import FormulaHelper

usage_string = """Dimacs reader

This is not a real formula construction. The formula is built by
reading a DIMACS file. This command is particularly useful to apply
some transformations to that file.

examples:
 {0}           --- read dimacs CNF from standard input
 {0} file.cnf  --- read dimacs CNF from file.cnf
"""


class DimacsCmdHelper(FormulaHelper):
    """Command line helper for the Pigeonhole principle CNF"""

    name = 'dimacs'
    description = 'Read dimacs file'

    @staticmethod
    def setup_command_line(parser):
        """Setup the command line options for pigeonhole principle formula

        Arguments:
        - `parser`: parser to load with options.
        """
        parser.usage = usage_string.format(parser.prog)
        parser.add_argument('input',
                            nargs='?',
                            help=argparse.SUPPRESS,
                            type=argparse.FileType('r'),
                            default='-')

    @staticmethod
    def build_cnf(args):

        msg = """Waiting for a DIMACS formula on <stdin>.
Alternatively you can feed a formula to <stdin>
with piping or giving a filename on the command line."""

        with redirect_stdin(args.input):
            with msg_prefix("INPUT: "):
                interactive_msg(msg, filltext=70)

            F = readCNF()

        return F
