# -*- coding: utf-8 -*-
from datetime import datetime


def current_datetime(fmt=False):
    """
    返回当前日期
    :param fmt: 若为True：%Y-%m-%d %H:%M:%S
    :return:
    """
    if fmt:
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return datetime.now()


def str_to_datetime(str_time):
    """
    返回格式化日期
    :param str_time: '2019-12-04 16:08:22'
    :return:
    """
    return datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S')
