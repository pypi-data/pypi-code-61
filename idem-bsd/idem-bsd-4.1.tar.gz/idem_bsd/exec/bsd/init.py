import os


def __sub_virtual__(hub):
    uname = os.uname()
    return (
        hasattr(uname, "sysname") and uname.sysname.upper().endswith("BSD"),
        "idem-bsd is only intended for BSD systems",
    )
