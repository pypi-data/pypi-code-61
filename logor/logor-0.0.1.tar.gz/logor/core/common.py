import atexit
import socket
import threading
import multiprocessing

from typing import List

DEBUG = 10
INFO = 20
WARNING = 30
ERROR = 40
PANIC = 50
level_map = {
    DEBUG: "debug",
    INFO: "info",
    WARNING: "warning",
    ERROR: "error",
    PANIC: "panic",
}
thread_or_process = []  # type: List[multiprocessing.Process, threading.Thread]


def _python_exit():
    client = GlobalManager.get_client()
    client.send(b"close")
    for top in thread_or_process:
        top.join()


atexit.register(_python_exit)


class GlobalManager:
    server = None
    client = None
    level = INFO

    lock = threading.Lock()

    @classmethod
    def init_socketpair(cls) -> None:
        if cls.server or cls.client:
            return
        with cls.lock:
            if cls.server or cls.client:
                return
            cls.server, cls.client = socket.socketpair()

    @classmethod
    def clear(cls) -> None:
        cls.server = None
        cls.client = None

    @classmethod
    def get_server(cls) -> socket.socket:
        if not cls.server:
            cls.init_socketpair()
        return cls.server

    @classmethod
    def get_client(cls) -> socket.socket:
        if not cls.client:
            cls.init_socketpair()
        return cls.client
