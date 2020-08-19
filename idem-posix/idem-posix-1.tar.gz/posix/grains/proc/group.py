import os
import grp


def __virtual__(hub):
    return "posix" in hub.tool.grains._loaded or (False, "Not a posix system")


async def load_group(hub):
    hub.grains.GRAINS.gid = os.getegid()
    try:
        hub.grains.GRAINS.groupname = grp.getgrgid(hub.grains.GRAINS.gid).gr_name
    except KeyError:
        hub.grains.GRAINS.groupname = None
