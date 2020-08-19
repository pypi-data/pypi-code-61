# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ICollectiveTestimonyLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ICollectiveTestimonyMosaicLayer(ICollectiveTestimonyLayer):
    """Marker interface that defines a browser layer."""
