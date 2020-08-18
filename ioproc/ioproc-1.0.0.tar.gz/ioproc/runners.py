#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import pathlib as pt

from ioproc.driver import _main


__author__ = ["Benjamin Fuchs"]
__copyright__ = "Copyright 2020, German Aerospace Center (DLR)"
__credits__ = ["Felix Nitsch", "Judith Vesper", "Niklas Wulff", "Hedda Gardian", "Gabriel Pivaro", "Kai von Krbek"]

__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Felix Nitsch"
__email__ = "ioProc@dlr.de"
__status__ = "Production"


envPath = pt.Path()

pathvar = os.environ['PATH']
elem = pathvar.split(';')

for ielem in elem:
    if 'Scripts' in ielem:
        envPath = pt.Path(ielem).parent
        break


def create_folders(projectName='yourTestProject'):
    '''
    Creates the required folder structure.
    '''
    _main(setupproject=False, userconfig=None, setupfolders=True, projectname=projectName)

def create_project(projectName='yourTestProject'):
    '''
    Creates a new project in the current work directory.
    '''
    # REMINDER: currently not used. Could be interfaced in the future.
    _main(setupproject=True, userconfig=None, setupfolders=False, projectname=projectName)

def start(userconfig=None):
    '''
    Executes the workflow manager.
    '''
    _main(setupproject=False, userconfig=userconfig, setupfolders=False, projectname=None)
