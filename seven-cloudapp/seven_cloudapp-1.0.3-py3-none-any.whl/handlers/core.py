# -*- coding: utf-8 -*-
"""
@Author: HuangJingCan
@Date: 2020-05-26 14:45:44
@LastEditTime: 2020-08-13 16:04:05
@LastEditors: HuangJingCan
@Description: 通用Handler
"""
from handlers.seven_base import *


class IndexHandler(SevenBaseHandler):
    """
    @description: 默认页
    @return: str
    @last_editors: HuangJingCan
    """
    def get_async(self):
        self.write("盲盒接口站")