import os


def __virtual__(hub):
    if os.name == "posix":
        return True
    else:
        return False, "idem-posix only runs on posix systems"
