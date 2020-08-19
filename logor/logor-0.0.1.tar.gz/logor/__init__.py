import sys

from core.entry import *


def withFields(fields: dict) -> Entry:
    entry = EntryMap.get()
    entry.setFields(fields)
    return entry


def getLogger(module) -> Entry:
    return EntryMap().get(module)


def setLevel(level: int):
    assert level in level_map, "please ensure your level valid"
    GlobalManager.level = level


def log_serve(server: socket.socket):
    o = sys.stdout
    while True:
        try:
            msg = decode_msg(server)
            o.write(f"{msg}\n")
            o.flush()
        except:
            break
    o.write("logor serve stop\n")
    o.flush()


class Logor:

    def __init__(self, module="", process=False):
        if process and module == "__main__":
            self.start_process = True
        else:
            self.start_process = False

    def __enter__(self):
        server = GlobalManager.get_server()
        if self.start_process:
            p = multiprocessing.Process(target=log_serve, args=(server,), daemon=False)
            p.start()
            thread_or_process.append(p)
        else:
            t = threading.Thread(target=log_serve, args=(server,), daemon=True)
            t.start()
            thread_or_process.append(t)

    def __exit__(self, exc_type, exc_val, exc_tb):
        client = GlobalManager.get_client()
        for top in thread_or_process:
            if hasattr(top, "terminate"):
                client.send(b"close")
