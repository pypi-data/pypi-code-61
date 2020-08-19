import os
import pwd


def __virtual__(hub):
    return "posix" in hub.tool.grains._loaded or (False, "Not a posix system")


async def load_user(hub):
    hub.grains.GRAINS.uid = os.geteuid()
    hub.grains.GRAINS.username = pwd.getpwuid(hub.grains.GRAINS.uid).pw_name
