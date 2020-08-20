# coding: utf-8
from logor.interface import IHook


class FileHook(IHook):

    def __init__(self):
        self.o = open("logor.log", "aw", encoding="utf-8")

    def process_msg(self, msg: str) -> None:
        self.o.write(msg)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.o.close()
