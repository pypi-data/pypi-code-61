import aiofiles
import glob


def __virtual__(hub):
    return "linux" in hub.tool.grains._loaded or (False, "Not a linux system")


async def load_wwn(hub):
    """
    Return Fibre Channel port WWNs from a Linux host.
    """
    fc_wwn = []
    for fc_file in glob.glob("/sys/class/fc_host/*/port_name"):
        async with aiofiles.open(fc_file, "r") as _wwn:
            content = await _wwn.read()
            for line in content.splitlines():
                fc_wwn.append(line.rstrip()[2:])

    if fc_wwn:
        hub.grains.GRAINS.fc_wwn = fc_wwn
