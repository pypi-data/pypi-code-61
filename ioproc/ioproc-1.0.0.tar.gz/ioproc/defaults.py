#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = ["Benjamin Fuchs", "Judith Vesper", "Felix Nitsch"]
__copyright__ = "Copyright 2020, German Aerospace Center (DLR)"
__credits__ = ["Niklas Wulff", "Hedda Gardian", "Gabriel Pivaro", "Kai von Krbek"]

__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Felix Nitsch"
__email__ = "ioProc@dlr.de"
__status__ = "Production"


'''
This file features several default scripts for setting up and testing ioProc.
'''

defaultRunPyFile = """
#-*- coding:utf-8 -*-


import ioproc.runners as run

run.start()
"""

defaultSetupFoldersPyFile = """
#-*- coding:utf-8 -*-


import ioproc.runners as run

run.create_folders()
"""

defaultUserContent = """
actionFolder: actions

debug:
  timeit: False

fromCheckPoint: start

workflow:
  - action1:
      project: general
      call: readExcel
      fieldName: 'Bond'
      param1: 007
      param2: True

  - action2:
      project: general
      call: printData

  - actionCheck:
      project: general
      call: checkpoint
      tag: test
"""

defaultActions = r"""
#-*- coding:utf-8 -*-


from ioproc.tools import action
from ioproc.logger import mainlogger


@action('general')
def readExcel(dmgr, config, params):
    '''
    reads excel files

    :param fieldName: the name of the data manager field to store the data to
    :param param1: the data to be stored in the data manager
    :param param2: currently unused
    '''
    with dmgr.overwrite:
        dmgr[params['fieldName']] = params['param1']
        dmgr['data3'] = [1, 2, 3]


@action('general')
def printData(dmgr, config, params):
    '''
    simple debugging printing function. Prints all data in the data manager.

    Does not have any parameters.
    '''
    for k, v in dmgr.items():
        mainlogger.info(k+' = \n'+str(v))


@action('general')
def checkpoint(dmgr, config, params):
    '''
    creates a checkpoint file in the current working directory with name
    Cache_TAG while TAG is supplied by the action config.

    :param tag: the tag for this checkpoint, this can never be "start"
    '''
    assert params['tag'] != 'start', 'checkpoints can not be named start'
    dmgr.toCache(params['tag'])
    mainlogger.info('set checkpoint "{}"'.format(params['tag']))

"""

defaultConfigContent = """
userschema: schema/user_schema.yaml
"""