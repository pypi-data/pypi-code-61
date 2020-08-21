#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains initialization module for artellapipe-libs-kitsu
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"


def init(*args, **kwargs):
    import artellapipe.register
    from artellapipe.libs.kitsu.core import tracking

    artellapipe.register.register_class('Tracker', tracking.KitsuTrackingManager)
