"""This file houses the primary entrypoint, and main business logic of ahd.

Module Variables
----------------

usage (str):
    Used by docopt to setup argument parsing;
    Defines the actual command line interface

config(dict):
    The dictionary containing the current configuration
    once deserialized from CONFIG_FILE_PATH

CONFIG_FILE_PATH(str):
    The path to the configuration file

CURRENT_PATH(str):
    Used to keep track of users current directory
    to cd back into it after script execution


Documentation
-------------
Docs website: https://ahd.readthedocs.io
"""

# Standard lib dependencies
import os                             # Used primarily to validate paths
import sys                            # Used to check length of input arguments
import glob                           # Used to preprocess wildcard paths
import logging                        # Used to log valueable logging info
import webbrowser                     # Used to auto-launch the documentation link
import subprocess                     # Used to run the dispatched commands


# Internal dependencies
from .configuration import migrate_config, configure, register

# Third-party dependencies
import colored                        # Used to colour terminal output
import yaml                           # Used to handle configuration serialization/deserialization
from docopt import docopt             # Used to parse arguments and setup POSIX compliant usage info

usage = """Add-hoc dispatcher

Create ad-hoc commands to be dispatched within their own namespace.

Usage: 
    ahd list [-l]
    ahd [-h] [-v] [-d]
    ahd docs [-a] [-o]
    ahd config [-e] [-i CONFIG_FILE_PATH]
    ahd register <name> [<command>] [<paths>]
    ahd <name> [<command>] [<paths>]

Options:
    -h, --help            show this help message and exit
    -v, --version         show program's version number and exit
    -l, --long            Shows all commands in configuration with paths and commands
    -a, --api             shows the local API docs
    -o, --offline         shows the local User docs instead of live ones
    -e, --export          exports the configuration file
    -i CONFIG_FILE_PATH, --import CONFIG_FILE_PATH 
                        imports the configuration file
    """

config = {}  # The dictionary containing the current configuration once deserialized from CONFIG_FILE_PATH

CONFIG_FILE_PATH = f"{os.path.dirname(__file__)}{os.sep}ahd.yml"  # The path to the configuration file

CURRENT_PATH = os.curdir # Keeps track of current directory to return to after executing commands

def main() -> None:
    """The primary entrypoint for the ahd script.

    All primary business logic is within this function."""

    # Setup arguments for parsing
    arguments = docopt(usage, version="ahd V 0.4.0")

    if len(sys.argv) == 1:
        print("\n", usage)
        sys.exit()

    # Checks if a legacy config is available and if it is migrates to new standard
    migrate_config()  # TODO: Remove in V0.6.0

    if os.path.exists(CONFIG_FILE_PATH): # If the file already exists
        with open(CONFIG_FILE_PATH, "r") as config_file:
            config = yaml.safe_load(config_file)
            config = dict(config)

    else: # If a file does not exist create one
        print(f"{colored.fg(1)}Could not locate valid config file creating new one at {CONFIG_FILE_PATH} {colored.fg(15)}")
        with open(CONFIG_FILE_PATH, "w") as config_file:
            config_file.write("macros:")
            sys.exit()

    # Begin argument parsing

    if arguments["list"]:
        list_macros(arguments["--long"], config)
        sys.exit()

    # ========= Docs argument parsing =========
    if arguments["docs"]:
        docs(arguments["--api"], arguments["--offline"])
        sys.exit()

    # ========= config argument parsing =========
    if arguments["config"]:
        configure(arguments["--export"], arguments["--import"], config)
        sys.exit()

    # ========= preprocessing commands and paths =========
    if not arguments["<paths>"]:
        logging.debug("No paths argument registered setting to \'\'")
        arguments["<paths>"] = ""
    else:
        arguments["<paths>"] = _preprocess_paths(arguments["<paths>"])

    if not arguments["<command>"]:
        logging.debug("No command argument registered setting to \'\'")
        arguments["<command>"] = ""

    if "." == arguments["<command>"]: # If <command> is . set to specified value
        logging.debug(f". command registered, setting to {config['macros'][arguments['<name>']]['command']}")
        arguments["<command>"] = config["macros"][arguments["<name>"]]["command"]

    # ========= register argument parsing =========
    if arguments["register"]:
        register(arguments["<name>"], arguments["<command>"], arguments["<paths>"], config)

    # ========= User command argument parsing =========

    if arguments['<name>']:
        if not arguments['<paths>'] and not arguments['<command>']:
            dispatch(arguments['<name>'], config=config)

        else:
            if arguments['<paths>'] and not arguments['<command>']: 
                # Process inputted paths
                arguments['<paths>'] = _preprocess_paths(arguments['<paths>'])
                arguments['<paths>'] = _postprocess_paths(arguments['<paths>'])
                dispatch(arguments['<name>'], paths = arguments['<paths>'], config=config)

            if arguments['<command>'] and not arguments['<paths>']:
                dispatch(arguments['<name>'], command = arguments['<command>'], config=config)

            else:
                # Process inputted paths
                arguments['<paths>'] = _preprocess_paths(arguments['<paths>'])
                arguments['<paths>'] = _postprocess_paths(arguments['<paths>'])
                dispatch(arguments['<name>'], paths = arguments['<paths>'], command = arguments['<command>'], config=config)

def list_macros(verbose:bool = False, config:dict={}) -> None:
    """Lists commands currently in config

    Parameters
    ----------
    verbose: (bool)
        When specified will print both the command name and
        associated commands + paths. Additionally the dictionary
        will only return when this flag is specified.

    config: (dict)
        The dict that contains the current config
    """

    # Iterate over the config, and pull information about the macros
    count = 0
    for count, macro in enumerate(config["macros"]):
        if verbose:
            print(f"{colored.fg(6)}{macro}\n")
            print(f"{colored.fg(100)}\tCommand = {config['macros'][macro]['command']}")
            print(f"\tPaths = {config['macros'][macro]['paths']}{colored.fg(15)}")
        else:
            print(f"\n{colored.fg(6)}{macro}{colored.fg(15)}")
    print(f"\n\n{count+1} macros detected")

def docs(api:bool = False, offline:bool = False) -> None:
    """Processes incoming arguments when the docs command is invoked

    Parameters
    ----------
    api: (bool)
        When specified, shows API docs as opposed to user docs.

    offline: (bool)
        When specified will build local copy of docs instead of going to website

    Notes
    -----
    - By Default user documentation is selected
    - By default the online documentation is selected
    """
    if not api and not offline:
        webbrowser.open_new("https://ahd.readthedocs.io")
    else:
        if offline and not api:
            # TODO Implement build local user docs.
            print("Not yet implemented")

        elif api:
            if not offline:
                webbrowser.open_new("https://kieranwood.ca/ahd")
            else:
                # TODO Implement build local user docs.
                print("Not yet implemented")

def dispatch(name, command:str=False, paths:str=False, config:dict={}) -> None:
    """Controls the dispatching of macros

    Parameters
    ----------
    name: (str)
        The name of the macro to dispatch

    command: (str)
        Used to override the macros configured command
        when set to False, will pull from configuration

    paths: (str)
        Used to override the macros configured paths
        when set to False, will pull from configuration

    config: (dict)
        The dict that contains the current config"""
    if "register" == name:
                print(usage)
                sys.exit()
    logging.info(f"Beggining execution of {name}")

    try: # Accessing stored information on the command
        config["macros"][name]

    except KeyError: # TODO Find a way to suggest a similar command
        print(f"{colored.fg(1)}Command not found in configuration validate spelling is correct.")
        sys.exit()
    
    if not command or command == ".":
        command = config["macros"][name]['command']
    
    if not paths:
        paths = _postprocess_paths(config["macros"][name]['paths'])

    if len(paths) > 1:
        for current_path in paths:
            if os.name == "nt":
                current_path = current_path.replace("/", f"{os.sep}")
                current_path = current_path.replace("~", os.getenv('USERPROFILE'))
            print(f"Running: cd {current_path} && {command} ".replace("\'",""))
            subprocess.Popen(f"cd {current_path} && {command} ".replace("\'",""), shell=True)

    else: # if only a single path is specified instead of a 'list' of them
        print(f"Running: cd {paths[0]} && {command} ".replace("\'",""))
        subprocess.Popen(f"cd {paths[0]} && {command} ".replace("\'",""), shell=True)
    pass

def _preprocess_paths(paths:str) -> str:
    """Preprocesses paths from input and splits + formats them
    into a useable list for later parsing.

    Example
    -------
    ```
    paths = '~/Desktop/Development/Canadian Coding/SSB, C:\\Users\\Kieran\\Desktop\\Development\\*, ~\\Desktop\\Development\\Personal\\noter, .'

    paths = _preprocess_paths(paths)

    print(paths) # Prints: '~/Desktop/Development/Canadian Coding/SSB,~/Desktop/Development/*,~/Desktop/Development/Personal/noter,.'
    ```
    """
    logging.info(f"Beginning path preprocessing on {paths}")
    result = paths.split(",")
    for index, directory in enumerate(result):
        directory = directory.strip()
        logging.debug(f"Directory: {directory}")
        if directory.startswith(".") and (len(directory) > 1):
            directory = os.path.abspath(directory)
        if not "~" in directory:
            if os.name == "nt":
                directory = directory.replace(os.getenv('USERPROFILE'),"~")

            else:
                directory = directory.replace(os.getenv('HOME'),"~")
            directory = directory.replace("\\", "/")
            result[index] = directory
        else:
            directory = directory.replace("\\", "/")
            result[index] = directory

    logging.debug(f"Result: {result}")
    result = ",".join(result)

    return result

def _postprocess_paths(paths:str) -> list:
    """Postprocesses existing paths to be used by dispatcher.

    This means things like expanding wildcards, and processing correct path seperators.

    Example
    -------
    ```
    paths = 'C:\\Users\\Kieran\\Desktop\\Development\\Canadian Coding\\SSB, C:\\Users\\Kieran\\Desktop\\Development\\Canadian Coding\\website, ~/Desktop/Development/Personal/noter, C:\\Users\\Kieran\\Desktop\\Development\\*'

    paths = _preprocess_paths(paths)

    print(_postprocess_paths(paths)) 
    # Prints: ['C:/Users/Kieran/Desktop/Development/Canadian Coding/SSB', ' C:/Users/Kieran/Desktop/Development/Canadian Coding/website', ' C:/Users/Kieran/Desktop/Development/Personal/noter', 'C:/Users/Kieran/Desktop/Development/Canadian Coding', 'C:/Users/Kieran/Desktop/Development/Personal', 'C:/Users/Kieran/Desktop/Development/pystall', 'C:/Users/Kieran/Desktop/Development/python-package-template', 'C:/Users/Kieran/Desktop/Development/Work']
    ```
    """
    logging.info(f"Beginning path postprocessing on {paths}")

    paths = paths.split(",")
    result = []
    for directory in paths:
        directory = directory.strip()

        if os.name == "nt":
            directory = directory.replace("/", "\\")

        if directory.startswith("."):
            try:
                if directory[1] == "/" or directory[1] == "\\":
                    directory = f"{os.curdir}{directory[1::]}"
            except IndexError:
                directory = os.path.abspath(".")

        if "~" in directory:
            if os.name == "nt":
                directory = directory.replace("~",f"{os.getenv('USERPROFILE')}")
            else:
                directory = directory.replace("~", f"{os.getenv('HOME')}")

        if "*" in directory:

            wildcard_paths = glob.glob(directory.strip())

            for wildcard_directory in wildcard_paths:
                wildcard_directory = wildcard_directory.replace("\\", "/")
                result.append(wildcard_directory)
        else:
            result.append(directory)

    logging.debug(f"Result: {result}")
    return result


if __name__ == "__main__":
    main()
