"""
@author: zhangX
@license: (C) Copyright 1999-2019, NJ_LUCULENT Corporation Limited.
@contact: 494677221@qq.com
@file: component.py
@time: 2020/4/26 12:21
@desc:
"""
from .argument import Argument, PreModel


class Component:

    @staticmethod
    def inputs(*arguments: Argument):

        def decorator(func):
            def _warp(**kwargs):
                geters = {}
                for argument in arguments:
                    geters[argument.argument_keys] = argument.run('input')
                for key, geter in geters.items():
                    geters[key] = geter.get()
                kwargs.update(geters)
                return func(**kwargs)

            return _warp

        return decorator

    @staticmethod
    def params(argument: Argument):

        def decorator(func):
            def _warp(**kwargs):
                param = argument.run('params')
                kwargs.update(param)
                func(**kwargs)

            return _warp

        return decorator
        pass

    @staticmethod
    def columns(*arguments: Argument):

        def decorator(func):
            def _warp(**kwargs):
                column_name = {}
                for argument in arguments:
                    column_name[argument.argument_keys] = argument.run('columns')
                kwargs.update(column_name)
                return func(**kwargs)

            return _warp

        return decorator

    @staticmethod
    def premodel(argument: Argument):

        def decorator(func):
            def _warp(**kwargs):
                if isinstance(argument, PreModel):
                    assert ValueError("invaild argument type, PreModel is required!")

                geter = argument.run('preModel')
                if geter is None:
                    pre_train_model = {argument.argument_keys: None}
                else:
                    pre_train_model = {argument.argument_keys: geter.get()}
                kwargs.update(pre_train_model)
                return func(**kwargs)

            return _warp

        return decorator

    @staticmethod
    def outputs(*arguments: Argument):

        def decorator(func):

            def _warp(**kwargs):
                senders = []
                keys = []
                for argument in arguments:
                    senders.append(argument.run('output'))
                    keys.append(argument.argument_keys)
                outputs = func(**kwargs)
                for sender, key in zip(senders, keys):
                    sender.send(data=outputs.get(key, None), key=key)

            return _warp

        return decorator
