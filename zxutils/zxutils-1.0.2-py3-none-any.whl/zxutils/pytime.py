#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/11/20
# Desc: 

import math
import time
from datetime import datetime


def ts_to_date(timestamp):
    """
    Timestamp to datetime
    :param timestamp:
    :return:
    """
    digits = int(math.log10(timestamp)) + 1
    if digits == 13:
        timestamp /= 1000

    # TODO Different time zone servers have different calculated dates
    time_local = time.localtime(timestamp)

    return time.strftime("%Y-%m-%d %X", time_local)


def ts(level=1.0):
    return int(time.time() * level)


def get_ms_timestamp():
    """
    Get current timestamp (ms)
    :return:
    """
    return ts(1e3)


def get_timestamp():
    """
    Get current timestamp (seconds)
    :return:
    """
    return ts()


def str_to_date(detester):
    """
    String to time
    :param detester:
    :return:
    """
    return datetime.strptime(detester, '%Y-%m-%d')
