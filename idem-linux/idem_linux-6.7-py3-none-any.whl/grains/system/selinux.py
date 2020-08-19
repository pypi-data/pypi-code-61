import shutil


def __virtual__(hub):
    return "linux" in hub.tool.grains._loaded or (False, "Not a linux system")


async def load_selinux(hub):
    if shutil.which("selinuxenabled"):
        hub.grains.GRAINS.selinux.enabled = (await hub.exec.cmd.run("selinuxenabled"))[
            "retcode"
        ] == 0

        if shutil.which("getenforce"):
            hub.grains.GRAINS.selinux.enforced = (await hub.exec.cmd.run("getenforce"))[
                "stdout"
            ].strip()
