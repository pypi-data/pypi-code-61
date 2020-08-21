async def load_kernel(hub):
    hub.grains.GRAINS.kernel = "Windows"

    # Hard coded grainss for windows systems
    hub.grains.GRAINS.init = "Windows"
    hub.grains.GRAINS.os_family = "Windows"
    hub.grains.GRAINS.ps = "tasklist.exe"
