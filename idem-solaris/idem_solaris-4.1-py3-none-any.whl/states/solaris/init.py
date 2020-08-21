import os


def __sub_virtual__(hub):
    uname = os.uname()
    return (
        hasattr(uname, "sysname") and uname.sysname == "SunOS",
        "idem-solaris is only intended for SunOs systems",
    )
