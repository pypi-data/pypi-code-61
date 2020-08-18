import os
import re
import shutil
from abc import ABC, abstractmethod

import pytz
import xlrd
from loguru import logger
from minio import Minio
from pathlib import Path
from datetime import datetime

# prefix components:
space = '    '
branch = '│   '
# pointers:
tee = '├── '
last = '└── '


class FileSystem(ABC):
    def __init__(self, **kwargs):
        self.__client__ = kwargs.get("client", None)

    @abstractmethod
    def lb(self):
        pass

    @abstractmethod
    def ls(self, path, recursive=False, grep=None):
        pass

    @abstractmethod
    def tree(self, path: Path, prefix: str = ''):
        pass

    @abstractmethod
    def stat(self):
        pass

    @abstractmethod
    def find(self):
        pass

    @abstractmethod
    def get_file(self):
        pass

    @abstractmethod
    def read_bytes(self):
        pass

    @abstractmethod
    def read_excel(self):
        pass

    def grep(self, iterable, regex):
        return [obj for obj in iterable if re.match(rf'{regex}', obj)]


class MinioFS(FileSystem):
    def __init__(self, hostname, access_key=None, secret_key=None, secure=True):
        client = Minio(hostname,
                       access_key=access_key,
                       secret_key=secret_key,
                       secure=secure)
        super().__init__(client=client)

    def lb(self, grep=None):
        """
        List all buckets.
        :return: list of tuples (name, creation date)
        """
        buckets = [bucket.name for bucket in self.__client__.list_buckets()]
        if grep:
            return self.grep(buckets, grep)
        else:
            return buckets

    def ls(self, path, recursive=False, grep=None):
        """

        :param path: <bucket>/path/to/folder/in/bucket
        :param recursive: To list recursively
        :param grep:
        :return:
        """
        bucket, prefix = self._process_path(path)
        objects = [object.object_name for object in self.__client__.list_objects(bucket,
                                                                                 prefix=prefix,
                                                                                 recursive=recursive)]
        if grep:
            return self.grep(objects, grep)
        else:
            return objects
        pass

    def tree(self, path):
        raise NotImplementedError("Tree list is not implemented for minio file system yet. Sorry ):")
        pass

    def stat(self, path):
        """

        :param path: path to directory or file. If directory, it will stat for all files in the directory.
        :return:
        """
        file_attributes = []
        bucket, prefix = self._process_path(path)
        for object in self.__client__.list_objects(bucket, prefix=prefix, recursive=False):
            file_attributes.append({
                "name": object.object_name,
                "type": "folder" if object.is_dir else "file",
                "modified": datetime.strftime(object.last_modified, "%Y-%m-%d %H:%M:%S"),
                "size": object.size,
            })
        return file_attributes
        pass

    def find(self, path, filename):
        """
        Recursively look for a file starting from given path. Match exact, case sensitive.
        :param path: Starting directory to start looking top down
        :param filename: name of file to search for
        :return: path to file
        """
        filepaths = []
        bucket, prefix = self._process_path(path)
        for object in self.__client__.list_objects(bucket, prefix=prefix, recursive=True):
            if filename in object.object_name:
                filepaths.append(object.object_name)

        return filepaths

    def get_file(self, source, destination):
        bucket, filename = self._process_path(source)
        self.__client__.fget_object(bucket, object_name=filename, file_path=destination)
        logger.info("Success")
        return

    def read_bytes(self, filename):
        data = self._stream_file(filename)
        return b''.join(data)

    def read_excel(self, filename):
        """
        returns xlrd workbook object
        :param filename:
        :return: An instance of the :class:`~xlrd.book.Book` class.
        """
        data = self._stream_file(filename)
        return xlrd.open_workbook(file_contents=b''.join(data))

    def _process_path(self, path):
        """
        Split path string into bucket and the prefix for usage in list_objects for the s3 api.
        :param path:
        :return:
        """
        bucket = path.split('/')[0]
        prefix = '/'.join(path.split('/')[1:])
        return bucket, prefix

    def _stream_file(self, filename):
        data = []
        bucket, filepath = self._process_path(filename)
        file = self.__client__.get_object(bucket_name=bucket, object_name=filepath)
        for data_stream in file.stream(32 * 1024):
            data.append(data_stream)
        return data


class LocalFS(FileSystem):
    def lb(self, grep=None):
        """
        Since local fs has no such thing as buckets, we will just do a ls on the pwd.
        :param grep: regex pattern that will be matched using re.match()
        """
        return self.ls(path='.', grep=grep)

    def ls(self, path, recursive=False, grep=None):
        """
        :param path: path to list directory
        :param tree: list directory tree
        :param grep: regex pattern that will be matched using re.match()
        :return: list of files & folders in directory
        """
        items = os.listdir(path)
        if grep:
            return self.grep(items, grep)
        else:
            return items

    def tree(self, path: Path, prefix: str = ''):
        """A recursive generator, given a directory Path object
        will yield a visual tree structure line by line
        with each line prefixed by the same characters

        example: fs.tree(Path()) to get tree for current working dir.
       for line in fs.tree(Path()):
            print(line)
        """
        contents = list(path.iterdir())
        # contents each get pointers that are ├── with a final └── :
        pointers = [tee] * (len(contents) - 1) + [last]
        for pointer, path in zip(pointers, contents):
            yield prefix + pointer + path.name
            if path.is_dir():  # extend the prefix and recurse:
                extension = branch if pointer == tee else space
                # i.e. space because last, └── , above so no more |
                yield from self.tree(path, prefix=prefix + extension)

    def stat(self, path):
        """
        Get file statistics for files in the directory
        :param path: path to directory
        :return: list of file statistics
        """
        file_attributes = []

        if Path(path).is_dir():
            for file in Path(path).iterdir():
                stats = file.stat()
                file_attributes.append({
                    "name": file.name,
                    "type": "folder" if file.is_dir() else "file",
                    "modified": datetime.strftime(datetime.fromtimestamp(stats.st_mtime, pytz.timezone("Asia/Singapore")), "%Y-%m-%d %H:%M:%S"),
                    "size": stats.st_size,
                })
        else:
            file = Path(path)
            stats = file.stat()
            file_attributes.append({
                "name": file.name,
                "type": "file",
                "modified":  datetime.strftime(datetime.fromtimestamp(stats.st_mtime, pytz.timezone("Asia/Singapore")), "%Y-%m-%d %H:%M:%S"),
                "size": stats.st_size,
            })

        return file_attributes

    def find(self, path, filename):
        filepaths = []
        for root, dirs, files in os.walk(path):
            if filename in files:
                filepaths.append(os.path.join(root, filename))
        return filepaths

    def get_file(self, source, destination):
        """
        Effectively the same as just copying a file from a source to destination.
        :param source:
        :param dest:
        :return:
        """
        logger.info(f"Getting file from {source} to {destination}")
        shutil.copy2(source, destination)
        logger.info(f"Success.")
        return

    def read_bytes(self, filename):
        """
        Read bytes of a file.
        :param filename: path to file to read.
        :return:
        """
        file = open(filename, "rb")
        return file.read()

    def read_excel(self, filename):
        """

        :param filename:
        :return: An instance of the :class:`~xlrd.book.Book` class.
        """
        return xlrd.open_workbook(filename)

