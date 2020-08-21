import os


def __sub_virtual__(hub):
    uname = os.uname()
    if hasattr(uname, "sysname") and uname.sysname == "Linux":
        return True
    else:
        return False, "idem-linux only runs on linux systems"
