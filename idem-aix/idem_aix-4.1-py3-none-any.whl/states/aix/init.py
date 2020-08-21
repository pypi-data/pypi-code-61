import os


def __sub_virtual__(hub):
    uname = os.uname()
    if hasattr(uname, "sysname") and uname.sysname == "AIX":
        return True
    else:
        return False, "idem-aix only runs on AIX systems"
