"""
    Threatstack microagent for Python.
"""

__title__ = 'threatstack'
__author__ = 'Threat Stack Inc'
__license__ = 'PROPRIETARY'
__copyright__ = 'Copyright 2019 Threat Stack'


version = '0.0'

try:
    from threatstack.buildVersion import buildVersion
except ImportError:
    buildVersion = 0

version_info = list(map(int, version.split('.'))) + [buildVersion]
version = '.'.join(map(str, version_info))
