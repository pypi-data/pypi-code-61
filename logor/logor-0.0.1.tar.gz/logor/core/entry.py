import datetime

from utils import *
from .common import *


def check_log_level(level: int = None):
    def wrapper(*args, **kwargs):
        def _wrapper(entry, msg: str):
            basic_level = GlobalManager.level if entry.level is None else \
                entry.level
            if level < basic_level:
                return
            entry.text_msg(level, msg)

        return _wrapper

    return wrapper


class Entry:

    def __init__(self, module: str, level: int = None, sock: socket.socket = None):
        self.module = module
        self.level = level
        self.fields = dict()
        self.text_fields = ""
        self.sock = sock or GlobalManager.get_client()

    def setLevel(self, level: int):
        assert level in level_map, "ensure your log level validity"
        self.level = level

    def setFields(self, fields: dict) -> None:
        self.fields.update(fields)
        text_fields = ""
        for key, value in self.fields.items():
            text_fields += f"{key}={value} "
        self.text_fields = text_fields

    def send(self, msg: str):
        self.sock.send(encode_msg(msg))

    def text_msg(self, level: int, msg: str):
        text_msg = f'time="{datetime.datetime.now()}" level={level_map.get(level, "unknown")} msg="{msg}" {self.text_fields}'
        self.send(text_msg)

    @check_log_level(level=DEBUG)
    def debug(self, msg: str):
        raise NotImplementedError

    @check_log_level(level=INFO)
    def info(self, msg: str):
        raise NotImplementedError

    @check_log_level(level=WARNING)
    def warning(self, msg: str):
        raise NotImplementedError

    @check_log_level(level=ERROR)
    def error(self, msg: str):
        raise NotImplementedError

    @check_log_level(level=PANIC)
    def panic(self, msg: str):
        raise NotImplementedError


class EntryMap:
    entryMap = dict()

    @classmethod
    def get(cls, module: str = None) -> Entry:
        if module not in cls.entryMap:
            GlobalManager.init_socketpair()
            cls.entryMap[module] = Entry(module)
        return cls.entryMap[module]
