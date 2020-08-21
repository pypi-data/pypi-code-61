#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains implementation for Solstice Artella project
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import os

from artellapipe.core import project as artella_project


class PlotTwist(artella_project.ArtellaProject, object):
    def __init__(self):
        super(PlotTwist, self).__init__(name='PlotTwist')

    def init(self, force_skip_hello=False):
        super(PlotTwist, self).init(force_skip_hello=force_skip_hello)

    def get_toolsets_paths(self):
        """
        Overrides base ArtellaProject get_toolsets_paths
        Returns path where project toolsets are located
        :return: list(str)
        """

        import plottwist.toolsets

        return [os.path.dirname(os.path.abspath(plottwist.toolsets.__file__))]

    def get_resources_paths(self):
        """
        Overrides base ArtellaProject get_resources_paths
        Returns path where project resources are located
        :return: dict(str, str)
        """

        resources_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'resources')
        return {
            'project': resources_path,
            'shelf': os.path.join(resources_path, 'icons', 'shelf')
        }
