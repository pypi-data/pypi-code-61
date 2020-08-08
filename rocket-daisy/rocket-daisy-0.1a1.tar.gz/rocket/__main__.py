# +-------------------------------------------------------------------------------+
#
#      Program:    rocket-daisy
#
#      Purpose:    setup for remote open control - key enabling technology (Rocket)
#
#      Target:     ARMV61A
#
#      Author:     Martin Shishkov
#
#      License:    GPL 3
# +-------------------------------------------------------------------------------+
import os
import sys
from daisy.server import Server
from daisy.utils.loader import loadScript
from daisy.utils.logger import exception, setDebug, info, logToFile
from daisy.utils.version import VERSION_STRING
from daisy.utils.thread import runLoop, stop

def displayHelp():
    print("Daisy command-line usage")
    print("daisy [-h] [-c config] [-l log] [-s script] [-d] [port]")
    print("")
    print("Options:")
    print("  -h, --help           Display this help")
    print("  -c, --config file    Load config from file")
    print("  -l, --log file       Log to file")
    print("  -s, --script file    Load script from file")
    print("  -d, --debug          Enable DEBUG")
    print("")
    print("Arguments:")
    print("  port                 Port to bind the HTTP Server")
    exit()

def main(argv):
    port = 8000
    configfile = None
    scriptfile = None
    logfile = None
    
    i = 1
    while i < len(argv):
        if argv[i] in ["-c", "-C", "--config-file"]:
            configfile = argv[i+1]
            i+=1
        elif argv[i] in ["-l", "-L", "--log-file"]:
            logfile = argv[i+1]
            i+=1
        elif argv[i] in ["-s", "-S", "--script-file"]:
            scriptfile = argv[i+1]
            i+=1
        elif argv[i] in ["-h", "-H", "--help"]:
            displayHelp()
        elif argv[i] in ["-d", "--debug"]:
            setDebug()
        else:
            try:
                port = int(argv[i])
            except ValueError:
                displayHelp()
        i+=1
    
    if logfile:
        logToFile(logfile)

    info("Starting %s" % VERSION_STRING)
    server = Server(port=port, configfile=configfile, scriptfile=scriptfile)
    runLoop()
    server.stop()

if __name__ == "__main__":
    try:
        main(sys.argv)
    except Exception as e:
        exception(e)
        stop()