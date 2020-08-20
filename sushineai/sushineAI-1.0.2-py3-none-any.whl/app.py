"""
@author: zhangX
@license: (C) Copyright 1999-2019, NJ_LUCULENT Corporation Limited.
@contact: 494677221@qq.com
@file: app.py
@time: 2020/4/10 22:27
@desc:
"""

import argparse
import traceback

import requests


def scheduler(args, status, message):  # 0:开始运行   1:正常结束  2:异常结束
    json = {"nodeId": args.node, "status": status, "message": message}
    requests.post(url=args.api, json=json)


class App:

    @staticmethod
    def run(func, **kwargs):
        parser = argparse.ArgumentParser()
        parser.add_argument("--node", type=str)
        parser.add_argument("--api", type=str)
        args = parser.parse_known_args()[0]

        scheduler(args, 0, "")
        try:
            func(**kwargs)
        except Exception:
            error_msg = traceback.format_exc()
            scheduler(args, 2, error_msg)
            raise Exception(error_msg)
        else:
            scheduler(args, 1, "")
