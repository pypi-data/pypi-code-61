#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains Artella loader implementation for Plot Twist
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"


import os
import logging.config

from artellapipe import loader
import artellapipe.register
import plottwist.register

from plottwist.core import asset
from plottwist.managers import ocio, menu
from plottwist.widgets import window

# =================================================================================

PACKAGE = 'plottwist'

# =================================================================================


def init(dev=False):
    """
    Initializes Plot Twist library
    """

    # Without default_integrations=False, PyInstaller fails during launcher generation
    if not dev:
        import sentry_sdk
        try:
            sentry_sdk.init("https://d71a4ba272374d7fb845269bb2aebf37@sentry.io/1816355")
        except (RuntimeError, ImportError):
            sentry_sdk.init("https://d71a4ba272374d7fb845269bb2aebf37@sentry.io/1816355", default_integrations=False)
    else:
        plottwist.register.cleanup()
        register_classes()

    logger = create_logger()
    plottwist.register.register_class('logger', logger)

    from plottwist.core import project

    loader.set_project(project.PlotTwist)


def create_logger(dev=False):
    """
    Returns logger of current module
    """

    logger_directory = os.path.normpath(os.path.join(os.path.expanduser('~'), PACKAGE, 'logs'))
    if not os.path.isdir(logger_directory):
        os.makedirs(logger_directory)

    logging_config = os.path.normpath(os.path.join(os.path.dirname(__file__), '__logging__.ini'))
    logging.config.fileConfig(logging_config, disable_existing_loggers=False)
    logger = logging.getLogger(PACKAGE)
    if dev:
        logger.setLevel(logging.DEBUG)
        for handler in logger.handlers:
            handler.setLevel(logging.DEBUG)

    return logger


def register_classes():
    artellapipe.register.register_class('Asset', asset.PlotTwistAsset)
    artellapipe.register.register_class('Window', window.PlotTwistWindow)
    artellapipe.register.register_class('OCIOMgr', ocio.PlotTwistOCIOManager)
    artellapipe.register.register_class('MenusMgr', menu.PlotTwistMenu)


register_classes()
