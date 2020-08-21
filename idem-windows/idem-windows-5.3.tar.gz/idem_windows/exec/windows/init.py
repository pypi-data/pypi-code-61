import sys


def __sub_virtual__(hub):
    return (
        sys.platform.startswith("win"),
        "Idem-Windows is only intended for Windows systems",
    )
