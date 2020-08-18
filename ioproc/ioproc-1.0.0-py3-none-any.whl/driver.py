#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pathlib as pt

import click

from ioproc.config import configProvider
from ioproc.defaults import *
from ioproc.logger import mainlogger as log
from ioproc.datamanager import DataManager
from ioproc.actionmanager import getActionManager
from ioproc.tools import freeze, setupFolderStructure


__author__ = ["Benjamin Fuchs", "Judith Vesper", "Felix Nitsch"]
__copyright__ = "Copyright 2020, German Aerospace Center (DLR)"
__credits__ = ["Niklas Wulff", "Hedda Gardian", "Gabriel Pivaro", "Kai von Krbek"]

__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Felix Nitsch"
__email__ = "ioProc@dlr.de"
__status__ = "Production"


IOPROCINSTALLROOT = pt.Path(__file__).resolve().parent
SCHEMAPATH = pt.Path(IOPROCINSTALLROOT, "schema")
HOME = pt.Path.home()

defaultConfigContent = defaultConfigContent.format(IOPROCINSTALLROOT.as_posix())


@click.command()
@click.option('--setupproject', is_flag=True, help='generate default project setup')
@click.option('--userconfig', '-c', default=None, help='path to user.yaml')
@click.option('--setupfolders', is_flag=True, help='generate default folder structure')
@click.option('--projectname', default='project1', help='name of your project' )
def ioproc(setupproject, userconfig, setupfolders, projectname):
    _main(setupproject, userconfig, setupfolders, projectname)


def _main(setupproject=False, userconfig=None, setupfolders=False, projectname='project1'):
    """
    Main driver which triggers the setup of the required folder structure, if needed.
    It also sets the user config path and the project structure, if they are not set up already.
    If the project is already set up, the action manager and the data manager are initialized.
    Next and according to the provided user configuration, the workflow with its actions
    is executed, which can also be started from a checkpoint to resume a previously started run.
    """
    if setupfolders:
        setupFolderStructure(projectname)
        return

    userConfigPath = pt.Path(pt.Path.cwd(), 'user.yaml')

    if userconfig is not None:
        userConfigPath = pt.Path(userconfig)

    if setupproject and not userConfigPath.exists():
        if not userConfigPath.parent.exists():
            raise IOError(f"Path to user config not found: {userConfigPath.as_posix()}")

        with userConfigPath.open('w') as opf:
            opf.write(defaultUserContent)

        projectStartScript = userConfigPath / 'run.py'
        if not projectStartScript.exists():
            with projectStartScript.open('w') as opf:
                opf.write(defaultRunPyFile)

    configProvider.setPathes(ioprocSchema=SCHEMAPATH,
                             userConfigPath=userConfigPath,
                             )
    config = configProvider.get()

    if not setupproject:
        actionMgr = getActionManager()
        assert len(actionMgr) > 0
        dmgr = DataManager()

        log.info('starting workflow')

        log.debug('commencing action calling')

        FROMCHECKPOINT = config['user']['fromCheckPoint'] != 'start'

        for iActionInfo in config['user']['workflow']:
            iActionInfo = iActionInfo[list(iActionInfo.keys())[0]]
            if FROMCHECKPOINT and 'tag' in iActionInfo and iActionInfo['tag'] != config['user']['fromCheckPoint']:
                continue
            elif FROMCHECKPOINT and 'tag' in iActionInfo and iActionInfo['tag'] == config['user']['fromCheckPoint']:
                FROMCHECKPOINT = False
                dmgr.fromCache(config['user']['fromCheckPoint'])
                log.info('reading from cache for tag "{}"'.format(config['user']['fromCheckPoint']))
                continue
            elif FROMCHECKPOINT:
                continue

            log.debug('executing action "'+iActionInfo['call']+'"')
            dmgr.entersAction(iActionInfo['project']+'-'+iActionInfo['call'])
            try:
                actionMgr[iActionInfo['project']][iActionInfo['call']](dmgr, config, freeze(iActionInfo))
            except Exception as e:
                log.exception('Fatal error during execution of action "'+iActionInfo['call']+'":\nData manager log:\n'+dmgr.report())
                raise e
            dmgr.leavesAction()


if __name__ == '__main__':
    ioproc()
