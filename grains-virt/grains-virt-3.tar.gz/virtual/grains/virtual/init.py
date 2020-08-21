def __sub_virtual__(hub):
    return "cmd" in hub.exec, "cmdmod not available in hub.exec"
