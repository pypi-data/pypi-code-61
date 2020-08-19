import os


def __virtual__(hub):
    return "posix" in hub.tool.grains._loaded or (False, "Not a posix system")


async def load_pid(hub):
    hub.grains.GRAINS.pid = os.getpid()
