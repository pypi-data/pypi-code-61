"""
@author: zhangX
@license: (C) Copyright 1999-2019, NJ_LUCULENT Corporation Limited.
@contact: 494677221@qq.com
@file: storager.py
@time: 2020/4/15 15:47
@desc:
"""
import os
import shutil
from abc import ABCMeta, ABC
import abc
from hdfs.client import InsecureClient
from sushineAI.utils.file_operator import FileOperator


class Storager(metaclass=ABCMeta):

    def __init__(self, args):
        self._args = args

    @abc.abstractmethod
    def get(self, **kwargs):
        pass

    def send(self, **kwargs):
        pass


class Hdfs(Storager, ABC):

    def __init__(self, args: dict, file_type, model_type=None):
        super().__init__(args)
        self._host = args.get('host')
        self._port = args.get('port')
        self._user = args.get('userName')
        self._fs = InsecureClient(url='http://{0}:{1}'.format(self._host, self._port), user=self._user)
        self._file_type = file_type
        self._hdfs_path = args.get('filePath') + '/'
        self._local_path = 'cache' + args.get('filePath') + '/'
        self.model_type = model_type

    def get(self, **kwargs):
        if self._local_path == 'cache/':
            return None
        try:
            os.makedirs(self._local_path)
        except FileExistsError:
            pass
        data = FileOperator.read(self._fs, self._hdfs_path, self._local_path, self._file_type, self.model_type)
        shutil.rmtree(os.path.dirname(os.path.dirname(os.path.abspath(self._local_path))))
        return data

    def send(self, **kwargs):
        if kwargs.get('data') is None:
            return
        file_name = FileOperator.save(kwargs.get('data'), self._local_path+'{}/'.format(kwargs.get('key')), self._file_type, self.model_type)
        self._fs.makedirs(self._hdfs_path)
        self._fs.upload(self._hdfs_path+'{}/'.format(kwargs.get('key')) + file_name,
                        self._local_path + '{}/'.format(kwargs.get('key'))+file_name, overwrite=True)
        shutil.rmtree(os.path.dirname(os.path.abspath(self._local_path)))


class Kafka(Storager, ABC):

    def __init__(self, args):
        super().__init__(args)

    def get(self, **kwargs):
        pass

    def send(self, **kwargs):
        pass
