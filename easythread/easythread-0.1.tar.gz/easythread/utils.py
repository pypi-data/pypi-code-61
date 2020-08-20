# -*- coding: utf-8 -*-
# @Author : Hcyang-NULL
# @Time   : 2020/8/20 11:35 上午
# - - - - - - - - - - -

from .custom_exception import *

def multi_split(target, num, show=False):
    """
    split target to a list which contains num list from target
    :param show: boolean -> show information
    :param target: list or set
    :param num: split number
    :return: list consists of num list
    """
    if isinstance(target, set):
        target = list(target)
    elif not isinstance(target, list):
        raise NotSupportException(target, [list, set])

    if isinstance(num, int):
        if num <= 0:
            raise MustPositiveException('split number')

    if num > len(target):
        print(f'>> Warning: split number > target length, change split number to target length!')
        num = len(target)
        
    unit_num = len(target) // num
    split_list = [target[i*unit_num:(i+1)*unit_num] for i in range(num)]

    if len(target) % num != 0:
        remain = target[num*unit_num:]
        for i in range(len(remain)):
            split_list[i % num].append(remain[i])

    if show:
        print(f'>> split target to {len(split_list)} list: ')
        length = [len(item) for item in split_list]
        print(length)

    return split_list
