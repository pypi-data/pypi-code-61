#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 11:17:47 2017

@author: nick
"""

import numpy as np

def stats(data):

    if len(data[data==data]) > 0:

        med = np.median(data)
        uq = np.percentile(data, 75)
        lq = np.percentile(data, 25)
        
        iqr = uq - lq
        uw = data[data<=uq+1.5*iqr].max()
        lw = data[data>=lq-1.5*iqr].min()
    else:
        med = np.nan
        uq = np.nan
        lq = np.nan
        
        iqr = np.nan
        uw = np.nan
        lw = np.nan
        
    return(med,uq,lq,iqr,uw,lw)