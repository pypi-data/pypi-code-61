# -*- coding: utf-8 -*-
# @Author : Hcyang-NULL
# @Time   : 2020/8/20 12:18 下午
# - - - - - - - - - - -

class NotSupportException(Exception):
    def __init__(self, err, accept=[]):
        self.err_type = str(type(err))[8:-2]
        self.accept = []
        for item in accept:
            self.accept.append(str(type(item))[8:-2])

    def __str__(self):
        print(f'{self.err_type} is not support as input! ', end='')
        if len(self.accept) != 0:
            print(f'Accepted input type: {self.accept}')

class MustPositiveException(Exception):
    def __init__(self, name=''):
        self.info = f'{name} should > 0!' if name != '' else 'parameter of input should > 0!'

    def __str__(self):
        print(self.info)
