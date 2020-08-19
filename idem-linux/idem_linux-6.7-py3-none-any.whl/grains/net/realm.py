import shutil


def __virtual__(hub):
    return "linux" in hub.tool.grains._loaded or (False, "Not a linux system")


async def load_windows_domain(hub):
    if shutil.which("realm"):
        realms = (await hub.exec.cmd.run(["realm", "list", "--name-only"]))[
            "stdout"
        ].splitlines()
        if realms:
            hub.grains.GRAINS.windowsdomain = realms[0]
            hub.grains.GRAINS.windowsdomaintype = "Domain"
