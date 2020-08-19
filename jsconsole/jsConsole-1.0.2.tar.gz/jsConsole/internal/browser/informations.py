"""
All of the informations about the current pyJsConsole instance.

© Anime no Sekai - 2020
"""

drivername = ''
connected = False
areClassesInitialized = False

def set_connection_status(status):
    global connected
    connected = status
    return connected

def set_drivername(name):
    global drivername
    drivername = name
    return drivername

def set_classes_status(status):
    global areClassesInitialized
    areClassesInitialized = status
    return areClassesInitialized