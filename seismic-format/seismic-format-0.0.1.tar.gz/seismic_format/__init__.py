# -*- coding: utf-8 -*-
from __future__ import print_function
#from ._version import get_versions

__author__ = 'Mike Hagerty'
__email__ = 'mhagerty@isti.com'
__version__ = '0.0.1'
#__version__ = get_versions()['version']
#del get_versions

import os
def get_format_dir():
    this_dir = os.path.abspath(os.path.dirname(__file__))
    formats_dir = os.path.join(this_dir, "formats")
    return formats_dir

