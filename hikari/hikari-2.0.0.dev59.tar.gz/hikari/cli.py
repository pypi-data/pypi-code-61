# -*- coding: utf-8 -*-
# cython: language_level=3
# Copyright (c) 2020 Nekokatt
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""Provides the `python -m hikari` and `hikari` commands to the shell."""
from __future__ import annotations

import inspect
import os
import platform
import sys
import typing

from hikari import _about
from hikari.utilities import art


def main() -> None:
    """Print package info and exit."""
    # noinspection PyTypeChecker
    if "--pretty" in sys.argv[1:] or "-p" in sys.argv[1:]:
        sys.stdout.write(art.get_banner() + "\n")
    else:
        sourcefile = typing.cast(str, inspect.getsourcefile(_about))
        path: typing.Final[str] = os.path.abspath(os.path.dirname(sourcefile))
        branch: typing.Final[str] = _about.__git_branch__
        sha1: typing.Final[str] = _about.__git_sha1__
        date: typing.Final[str] = _about.__git_when__
        version: typing.Final[str] = _about.__version__
        py_impl: typing.Final[str] = platform.python_implementation()
        py_ver: typing.Final[str] = platform.python_version()
        py_compiler: typing.Final[str] = platform.python_compiler()
        sys.stderr.write(f"hikari v{version} {branch}@{sha1}, released on {date}\n")
        sys.stderr.write(f"located at {path}\n")
        sys.stderr.write(f"{py_impl} {py_ver} {py_compiler}\n")
