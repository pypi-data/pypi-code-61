# -*- coding: utf-8 -*-

import argparse
import traceback
import logging
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from .testpack import Test

def test1(path):
	ctest = Test()
	ctest.filelist(path)
	
test1("/")