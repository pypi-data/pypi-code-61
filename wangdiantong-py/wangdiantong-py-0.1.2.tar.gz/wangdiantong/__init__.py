import six

if six.PY2:
    __import__('pkg_resources').declare_namespace(__name__)


__author__ = """Ranger Huang"""
__email__ = 'ranger_huang@yeah.net'
__version__ = '0.1.2'
VERSION = __version__.split('.')
