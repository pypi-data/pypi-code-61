#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/11/20
# Desc: 

from datetime import datetime

from zxutils.pytime import str_to_date, ts_to_date


def test_ts_to_date():
    assert ts_to_date(1574232324) is not None
    assert ts_to_date(1574232316000) is not None


def test_text_to_date():
    assert str_to_date("2017-07-09") == datetime(2017, 7, 9)
