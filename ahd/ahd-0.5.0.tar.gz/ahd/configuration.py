"""This file houses functions related to configuration management

Module Variables
----------------

CONFIG_FILE_PATH(str):
    The path to the configuration file

CURRENT_PATH(str):
    Used to keep track of users current directory
    to cd back into it after script execution

command_list(list[namedtuple]):
    A list of all the root commands baked into
    ahd for autocompletion generation

"""
import os                              # Used primarily to validate paths
import sys                             # Used to safely exit interpreter session
from configparser import ConfigParser  # Used to serialize and de-serialize legacy config files

# Internal dependencies
from .autocomplete import command, generate_bash_autocomplete

# Third-party dependencies
import colored                         # Used to colour terminal output
import yaml                            # Used to handle configuration serialization/deserialization

# The default (and currently only) path to the configuration file
CONFIG_FILE_PATH = f"{os.path.dirname(__file__)}{os.sep}ahd.yml"

CURRENT_PATH = os.curdir  # Keeps track of current directory to return to after executing commands

command_list = [  # Used for autocompletion generation
    command("docs", ["-a", "--api", "-o", "--offline"]),
    command("register", []),
    command("config", ["-e", "--export", "-i", "--import"])
]

def migrate_config() -> None:
    """Migrates pre V0.5.0 configs to the new standard"""
    OLD_CONFIG_FILE_PATH = f"{os.path.dirname(__file__)}{os.sep}.ahdconfig"
    if os.path.isfile(OLD_CONFIG_FILE_PATH):  # Validate whether a legacy config exists
        print(f"{colored.fg(1)}Old Configuration file found in {OLD_CONFIG_FILE_PATH} automatically migrating to version 0.5.0+{colored.fg(15)}")
        with open(OLD_CONFIG_FILE_PATH, "r") as old_config_file:
            old_config = ConfigParser()
            old_config.read_file(old_config_file)
            old_config = dict(old_config)
            del(old_config['DEFAULT'])
        for section in old_config:
            old_config[section] = {"command": old_config[section]["command"], "paths":old_config[section]["paths"]}
        new_config = {}
        new_config["macros"] = old_config
        with open(CONFIG_FILE_PATH, "w") as new_config_file:
            yaml.dump(new_config, new_config_file, default_flow_style=False)
        del old_config  # HACK: Clean up configparser reference since it screws with file access

        valid = False
        while not valid:
            remove_legacy = input("Would you like to remove the old configuration file (y or n)?")
            if remove_legacy.lower().startswith("y"):
                os.remove(OLD_CONFIG_FILE_PATH)
                return True
            elif remove_legacy.lower().startswith("n"):
                return True
            else:
                print("Please enter Y to remove config or N to not")
                continue

    else:  # If no legacy configs are present
        return False

def configure(export:bool=False, import_config:bool=False, config:dict={}) -> None:
    """Handles all the exporing and importing of configurations

    Parameters
    ----------
    export: (bool)
        When specified, shows API docs as opposed to user docs.

    import_config: (bool|str)
        False if no path, otherwise a string representation of path to config file.

    config: (dict)
        The dict that contains the current config

    Notes
    -----
    - If neither export or import_config are specified, then usage is printed.
    """

    if not export and not import_config:
        print("Please provide either the export (-e or --export) or import (-i or --import) flag")
        return
    if export:
        with open(CONFIG_FILE_PATH) as config_file:
            config = yaml.safe_load(config_file)
            with open(f"{os.path.abspath(CURRENT_PATH)}{os.sep}ahd.yml", "w") as export_file:
                yaml.dump(config, export_file, default_flow_style=False)

    if import_config:
        try:
            with open(import_config, "r") as config_file:  # Read new config file
                new_config = yaml.safe_load(config_file)
            print(f"Importing {os.path.abspath(import_config)} to {CONFIG_FILE_PATH}")
            os.remove(CONFIG_FILE_PATH)
            with open(CONFIG_FILE_PATH, "w") as config_file:
                yaml.dump(new_config, config_file, default_flow_style=False)
            
        except PermissionError:
            print(f"{colored.fg(1)} Unable to import configuration file, are you sudo?")
            print(f"{colored.fg(15)}\tTry running: sudo ahd config -i \"{import_config}\" ")

def register(macro_name:str, commands:str, paths:str, config:dict={}) -> None:
    """Handles registering of custom commands, and autocompletion generation.

    Parameters
    ----------
    macro_name: (str)
        The name used to call the commands.

    commands: (str)
        The set of commands to execute.
    
    paths: (str)
        A string representation of the paths to execute the command with.

    config: (dict)
        The dict that contains the current config

    Notes
    -----
    - When passing paths to this function make sure they are preprocessed.
    """
    print(f"Registering macro {macro_name} \n\tCommand: {commands} \n\tPaths: {paths}")
    try:
        config["macros"][macro_name] = {
            "command": commands,
            "paths": paths,
        }
    except TypeError:  # If the configuration is empty
        config["macros"] = {}
        config["macros"][macro_name] = {
            "command": commands,
            "paths": paths,
        }

    try:
        print(f"Begin writing config file to {CONFIG_FILE_PATH}")
        with open(CONFIG_FILE_PATH, "w") as config_file:
            yaml.dump(config, config_file, default_flow_style=False)
        print(f"Configuration file saved {macro_name} registered")
    except PermissionError:
        print(f"{colored.fg(1)}Unable to register command are you sudo?")
        print(f"{colored.fg(15)}\tTry running: sudo ahd register {macro_name} \"{commands}\" \"{paths}\" ")

    if not os.name == "nt":  # Generate bash autocomplete
        for custom_command in config["macros"]:
            command_list.append(command(custom_command, []))

        autocomplete_file_text = generate_bash_autocomplete(command_list)
        try:
            with open("/etc/bash_completion.d/ahd.sh", "w") as autocomplete_file:
                autocomplete_file.write(autocomplete_file_text)
            print("Bash autocompletion file written to /etc/bash_completion.d/ahd.sh \nPlease restart shell for autocomplete to update")
        except PermissionError:
            print(f"{colored.fg(1)}Unable to write bash autocompletion file are you sudo?")

    # Since executing commands requires changing directories, make sure to return after
    os.chdir(CURRENT_PATH)
    sys.exit()
