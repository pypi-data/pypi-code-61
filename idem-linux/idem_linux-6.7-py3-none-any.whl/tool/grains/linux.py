import os


def __virtual__(hub):
    uname = os.uname()
    if hasattr(uname, "sysname") and uname.sysname == "Linux":
        return True
    else:
        return False, "idem-linux only runs on linux systems"
