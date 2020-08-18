#!/bin/env python
# -*- coding:utf-8 -*-
# _author:ken

import os
import sys


class Path(object):
    def get_current_path(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        p = sys.path.append(BASE_DIR)
        print(BASE_DIR)
        return BASE_DIR
