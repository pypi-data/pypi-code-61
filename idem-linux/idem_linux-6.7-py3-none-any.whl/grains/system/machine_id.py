import aiofiles
import os


def __virtual__(hub):
    return "linux" in hub.tool.grains._loaded or (False, "Not a linux system")


async def load_machine_id(hub):
    """
    Provide the machine-id for machine/virtualization combination
    """
    # Provides:
    #   machine-id
    locations = ["/etc/machine-id", "/var/lib/dbus/machine-id"]
    existing_locations = [loc for loc in locations if os.path.exists(loc)]
    if existing_locations:
        async with aiofiles.open(existing_locations[0]) as machineid:
            hub.grains.GRAINS.machine_id = (await machineid.read()).strip()
