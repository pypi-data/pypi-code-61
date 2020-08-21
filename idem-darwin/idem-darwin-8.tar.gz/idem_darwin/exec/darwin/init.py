import os


def __sub_virtual__(hub):
    uname = os.uname()
    return (
        hasattr(uname, "sysname") and uname.sysname == "Darwin",
        "idem-linux only runs on linux systems",
    )
