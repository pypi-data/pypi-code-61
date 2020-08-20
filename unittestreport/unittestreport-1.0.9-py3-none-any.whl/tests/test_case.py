"""
============================
Author:柠檬班-木森
Time:2020/8/19   17:46
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
from unittestreport import ddt, data

import unittest
from unittestreport import rerun

import unittest
from unittestreport import rerun


class TestClass(unittest.TestCase):

    def test_case_01(self):
        a = 100
        b = 99
        assert a == b

    def test_case_02(self):
        a = 100
        b = 100
        assert a == b

    def test_case_03(self):
        a = 100
        b = 101
        assert a == b

    # @data(1, 2, 3, 4, 5)
    # def test_01case(self,i):
    #     assert 100 == 100
