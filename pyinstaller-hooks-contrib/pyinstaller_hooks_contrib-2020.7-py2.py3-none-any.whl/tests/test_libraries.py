# ------------------------------------------------------------------
# Copyright (c) 2020 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE.GPL.txt, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------

from PyInstaller.compat import is_darwin
from PyInstaller.utils.tests import importorskip, xfail, skipif_win


@importorskip('jinxed')
def test_jinxed(pyi_builder):
    pyi_builder.test_source(
        '''
        import jinxed
        jinxed.setupterm('xterm')
        assert jinxed._terminal.TERM.terminfo is jinxed.terminfo.xterm
        '''
    )


@importorskip('tensorflow')
def test_tensorflow(pyi_builder):
    pyi_builder.test_source(
        """
        from tensorflow import *
        """
    )


@importorskip('trimesh')
def test_trimesh(pyi_builder):
    pyi_builder.test_source(
        """
        import trimesh
        """
    )


@importorskip('boto')
@xfail(reason='boto does not fully support Python 3')
def test_boto(pyi_builder):
    pyi_builder.test_script('pyi_lib_boto.py')


@xfail(reason='Issue #1844.')
@importorskip('boto3')
def test_boto3(pyi_builder):
    pyi_builder.test_source(
        """
        import boto3
        session = boto3.Session(region_name='us-west-2')

        # verify all clients
        for service in session.get_available_services():
            session.client(service)

        # verify all resources
        for resource in session.get_available_resources():
            session.resource(resource)
        """)


@xfail(reason='Issue #1844.')
@importorskip('botocore')
def test_botocore(pyi_builder):
    pyi_builder.test_source(
        """
        import botocore
        from botocore.session import Session
        session = Session()
        # verify all services
        for service in session.get_available_services():
            session.create_client(service, region_name='us-west-2')
        """)


@xfail(is_darwin, reason='Issue #1895.')
@importorskip('enchant')
def test_enchant(pyi_builder):
    pyi_builder.test_script('pyi_lib_enchant.py')


@importorskip('zmq')
def test_zmq(pyi_builder):
    pyi_builder.test_source(
        """
        import zmq
        print(zmq.__version__)
        print(zmq.zmq_version())
        # This is a problematic module and might cause some issues.
        import zmq.utils.strtypes
        """)


@importorskip('pylint')
def test_pylint(pyi_builder):
    pyi_builder.test_source(
        """
        # The following more obvious test doesn't work::
        #
        #   import pylint
        #   pylint.run_pylint()
        #
        # because pylint will exit with 32, since a valid command
        # line wasn't given. Instead, provide a valid command line below.

        from pylint.lint import Run
        Run(['-h'])
        """)


@importorskip('markdown')
def test_markdown(pyi_builder):
    # Markdown uses __import__ed extensions. Make sure these work by
    # trying to use the 'toc' extension..
    pyi_builder.test_source(
        """
        import markdown
        print(markdown.markdown('testing',
            extensions=['markdown.extensions.toc']))
        """)


@importorskip('lxml')
def test_lxml_isoschematron(pyi_builder):
    pyi_builder.test_source(
        """
        # The import of this module triggers the loading of some
        # required XML files.
        from lxml import isoschematron
        """)


@importorskip('openpyxl')
def test_openpyxl(pyi_builder):
    pyi_builder.test_source(
        """
        # Test the hook to openpyxl
        from openpyxl import __version__
        """)


@importorskip('pyodbc')
def test_pyodbc(pyi_builder):
    pyi_builder.test_source(
        """
        # pyodbc is a binary Python module. On Windows when installed with easy_install
        # it is installed as zipped Python egg. This binary module is extracted
        # to PYTHON_EGG_CACHE directory. PyInstaller should find the binary there and
        # include it with frozen executable.
        import pyodbc
        """)


@importorskip('pyttsx')
def test_pyttsx(pyi_builder):
    pyi_builder.test_source(
        """
        # Basic code example from pyttsx tutorial.
        # http://packages.python.org/pyttsx/engine.html#examples
        import pyttsx
        engine = pyttsx.init()
        engine.say('Sally sells seashells by the seashore.')
        engine.say('The quick brown fox jumped over the lazy dog.')
        engine.runAndWait()
        """)


@importorskip('pycparser')
def test_pycparser(pyi_builder):
    pyi_builder.test_script('pyi_lib_pycparser.py')


@importorskip('Crypto')
def test_pycrypto(pyi_builder):
    pyi_builder.test_source(
        """
        import binascii
        from Crypto.Cipher import AES
        BLOCK_SIZE = 16
        print('AES null encryption, block size', BLOCK_SIZE)
        # Just for testing functionality after all
        print('HEX', binascii.hexlify(
            AES.new(b"\\0" * BLOCK_SIZE, AES.MODE_ECB).encrypt(b"\\0" * BLOCK_SIZE)))
        from Crypto.PublicKey import ECC
        """)


@importorskip('Cryptodome')
def test_cryptodome(pyi_builder):
    pyi_builder.test_source(
        """
        from Cryptodome import Cipher
        from Cryptodome.PublicKey import ECC
        print('Cryptodome Cipher Module:', Cipher)
        """)


@importorskip('h5py')
def test_h5py(pyi_builder):
    pyi_builder.test_source("""
        import h5py
        """)


@importorskip('unidecode')
def test_unidecode(pyi_builder):
    pyi_builder.test_source("""
        from unidecode import unidecode

        # Unidecode should not skip non-ASCII chars if mappings for them exist.
        assert unidecode(u"kožušček") == "kozuscek"
        """)


@importorskip('pinyin')
def test_pinyin(pyi_builder):
    pyi_builder.test_source("""
        import pinyin
        """)


@importorskip('uvloop')
@skipif_win
def test_uvloop(pyi_builder):
    pyi_builder.test_source("import uvloop")


@importorskip('web3')
def test_web3(pyi_builder):
    pyi_builder.test_source("import web3")


@importorskip('phonenumbers')
def test_phonenumbers(pyi_builder):
    pyi_builder.test_source("""
        import phonenumbers

        number = '+17034820623'
        parsed_number = phonenumbers.parse(number)

        assert(parsed_number.country_code == 1)
        assert(parsed_number.national_number == 7034820623)
        """)


@importorskip('pendulum')
def test_pendulum(pyi_builder):
    pyi_builder.test_source("""
        import pendulum

        print(pendulum.now().isoformat())
        """)


@importorskip('argon2')
def test_argon2(pyi_builder):
    pyi_builder.test_source("""
        from argon2 import PasswordHasher

        ph = PasswordHasher()
        hash = ph.hash("s3kr3tp4ssw0rd")
        ph.verify(hash, "s3kr3tp4ssw0rd")
        """)


@importorskip('pytest')
def test_pytest_runner(pyi_builder):
    """
    Check if pytest runner builds correctly.
    """
    pyi_builder.test_source(
        """
        import pytest
        import sys
        sys.exit(pytest.main(['--help']))
        """)


@importorskip('eel')
def test_eel(pyi_builder):
    pyi_builder.test_source("import eel")


@importorskip('sentry_sdk')
def test_sentry(pyi_builder):
    pyi_builder.test_source(
        """
        import sentry_sdk
        sentry_sdk.init()
        """)
