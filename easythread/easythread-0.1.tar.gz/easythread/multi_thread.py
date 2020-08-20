# -*- coding: utf-8 -*-
# @Author : Hcyang-NULL
# @Time   : 2020/8/20 1:16 下午
# - - - - - - - - - - -

from threading import Thread
from .utils import multi_split

class MultiThread(Thread):
    def __init__(self, thread_id, func, task_list, *args):
        Thread.__init__(self)
        self.thread_id = thread_id
        self.task_list = task_list
        self.func = func
        self.args = args[0]

    def run(self):
        self.func(self.thread_id, self.task_list, self.args)

def multi_thread(all_list, thread_num, func, *args):
    thread_pool = []
    for index, task_list in enumerate(multi_split(all_list, thread_num), 1):
        thread_id = f'Thread-{index}'
        thread = MultiThread(thread_id, func, task_list, args)
        thread_pool.append(thread)
    for thread in thread_pool:
        thread.start()
    for thread in thread_pool:
        thread.join()
    print(f'>> All Thread Accomplished!')
