import os


def __sub_virtual__(hub):
    uname = os.uname()
    return (
        hasattr(uname, "sysname") and uname.sysname == "Linux",
        "idem-linux only runs on linux systems",
    )
