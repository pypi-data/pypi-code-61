"""Base class for an object that has settings that can be loaded from ini and saved to json."""

__author__ = "Nikolai Dontschuk and Dan McCloskey"
__copyright__ = "Copyright 2020, Nikolai Dontschuk and Dan McCloskey"
__license__ = "Licensed under the Academic Free License version 3.0"

from pathlib import Path
import configparser
import json
import datetime
from numpyencoder import NumpyEncoder
from bandalyzer_app.utilities import ini_string_to_python
import bandalyzer_app

config_folder = Path(bandalyzer_app.CONFIG_PATH)
if not config_folder.exists():
    print(f"Could'nt find .config folder!!!  Install broken, you can fix by making the folder: {config_folder}")

default_settings_ini = config_folder / "default_settings.ini"

# make sure we have a default settings file
if not default_settings_ini.exists():
    print(f"Couldn't find .config folder, if you know what you are doing create {str(default_settings_ini)}")
#     with open(default_settings_ini, mode='x'):
#         pass
config_parser_args = {'comment_prefixes': ('#', ';'), 'inline_comment_prefixes': (';',)}

def update_from_ini(a_dict, ini_path, section=None):
    config_parser = configparser.ConfigParser(**config_parser_args)
    sections = []
    with open(ini_path) as f:
        config_parser.read_file(f)
    if section is None:
        sections = config_parser.sections()
    else:
        if config_parser.has_section(section):
            sections = [section]
    for section in sections:
        for k, v in config_parser.items(section):
            v = ini_string_to_python(v)
            if v is not None:
                a_dict[k] = v


def check_if_in_ini(a_dict, ini_path, section):
    config_parser = configparser.ConfigParser(**config_parser_args)
    with open(ini_path) as f:
        config_parser.read_file(f)
    for k, v in a_dict.items():
        if not config_parser.has_option(section, k):
            # TODO log as warning.
            print(f"Setting default '{k}' found in program defaults and not in {str(ini_path.absolute())}")


def __create_default_ini__(default_settings_dict):
    config_parser = configparser.ConfigParser(**config_parser_args)
    # with open(default_settings_ini) as f:
    #     config_parser.read_file(f)
    for section, settings in default_settings_dict.items():
        if not config_parser.has_section(section):
            config_parser.add_section(section)
        for k, v in settings.items():
            try:
                config_parser.set(section, k, str(v))
            except TypeError as e:
                print(f"Can't parse setting in section {section} named {k} with value: {v}")
                raise e
    with open(default_settings_ini, mode='w') as f:
        config_parser.write(f)


def load_from_jsoncache(cache_dir):
    cache_dir = Path(cache_dir)
    if cache_dir.exists():
        with open(cache_dir, mode='r') as f:
            return json.load(f)
    else:
        raise FileNotFoundError

class SettingsObject:
    """Manages setting for any class that needs settings.  In the form of a self.settings dict, where they keys are the
    setting names.  Supports saving to JSON, and loading from a deafult and specified ini file.

     In each child class provide a '_settings_heading_' class variable that will serve as the settings ini-section
     name for that class.  Optionally you can programmatically define default values with a class variable
     'default_settings' dict.

     These dict keys cannot be capitalised or they will be duplicated in lower case by the ini-config.
     You then need to call __add_default_settings(Class, **kwargs) so that these defaults get added to self.settings dict.

     eg.
     class MyClass(SettingsObject)
         _settings_heading_ = "GeneralSettings"
         default_settings = {'a_setting': None, 'another_setting': "."}

         __init__(self, **kwargs):
            super()__init__(**kwargs)
            self.__add_default_settings__(MyClass, **kwargs)

     Really thinking of just moving everything to JSON, the price for a pretty settings file is too damn high."""
    _settings_heading_ = "GeneralSettings"
    default_settings = {'settings_file': None, 'local_dir': "."}

    def __init__(self, *args, settings_file=None, local_dir=".", **kwargs):
        self.settings = {'settings_file': settings_file, 'local_dir': local_dir}
        if self.settings['settings_file'] is not None:
            settings_file = Path(self.settings['settings_file'])
            if not settings_file.is_file():
                settings_file = Path(local_dir) / settings_file
                if settings_file.is_file():
                    # TODO log as warning.
                    print(f"Could'nt find {self.settings['settings_file']}, using the found {str(settings_file)}.")
                    self.settings['settings_file'] = str(settings_file)
                else:
                    raise FileNotFoundError(f"Cannot find settings file at specified {self.settings['settings_file']},"
                                            f"or at {str(settings_file)}")

        self.__default_settings__ = {}
        self.__add_default_settings__(SettingsObject, **kwargs)

    def __add_default_settings__(self, obj, **kwargs):
        self.__default_settings__[obj._settings_heading_] = obj.default_settings
        self.update_settings(obj._settings_heading_, **kwargs)

    def update_settings(self, section, **kwargs):
        # Adds the class programmed, default and instance ini_file defaults.
        check_if_in_ini(self.__default_settings__[section], default_settings_ini, section)
        update_from_ini(self.__default_settings__[section], default_settings_ini, section)
        # This order is important, otherwise settings_file will be overwritten with default 'None'.
        self.settings = {**self.__default_settings__[section], **self.settings}
        # Update with instance specific ini if it exists.
        if self.settings['settings_file'] is not None:
            update_from_ini(self.settings, Path(self.settings['local_dir']) / self.settings['settings_file'], section=section)
        # update all the settings values with instance creation defined values.
        for setting_name, setting_value in kwargs.items():
            if setting_name in self.settings:  # Don't gunk up the settings dict with unused values.
                if setting_value is not None:
                    self.settings[setting_name] = setting_value

    def save_jsoncache(self, dump_to_file=True, dict_to_append={}):
        if dump_to_file:
            fname = datetime.datetime.now().strftime(f'%Y%m%d_%H%M.%S_{self._settings_heading_}_settings.jsonlock')
            fpath = Path(self.settings['local_dir']) / ".history"
            if not fpath.exists():
                fpath.mkdir()
            with open(fpath / fname, mode='x') as f:
                json.dump({**self.settings, **dict_to_append}, f, cls=NumpyEncoder)
        return self.settings
