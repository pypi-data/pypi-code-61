import getpass
import pwd


def __virtual__(hub):
    return "posix" in hub.tool.grains._loaded or (False, "Not a posix system")


async def load_console_user(hub):
    hub.grains.GRAINS.console_username = getpass.getuser()
    hub.grains.GRAINS.console_user = pwd.getpwnam(
        hub.grains.GRAINS.console_username
    ).pw_uid
