#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pathlib as pt
import inspect
import pprint

import yaml
import cerberus


__author__ = ["Benjamin Fuchs", "Judith Vesper"]
__copyright__ = "Copyright 2020, German Aerospace Center (DLR)"
__credits__ = ["Felix Nitsch", "Niklas Wulff", "Hedda Gardian", "Gabriel Pivaro", "Kai von Krbek"]

__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Felix Nitsch"
__email__ = "ioProc@dlr.de"
__status__ = "Production"


class ConfigurationError(Exception):
    """
    Error raised by the configuration process.
    """
    pass


class ConfigDict(dict):

    def __getitem__(self, fieldname):
        """
        Access the config dictionary and retrieve data set by field name.
        If an KeyError is raised and the actionName is None, a ConfigurationError
        is raised, warning the user of an unsuccessful configuration.
        :param field name
        :return data from config dictionary which is accessed using the field name
        """
        try:
            return super().__getitem__(fieldname)
        except KeyError as e:
            s = inspect.stack()

            actionName = None
            lineno = s[0].lineno
            filename = pt.Path(s[0].filename).name

            for idx, iframe in enumerate(s):
                if iframe.function == '__actionwrapper__':
                    last = s[idx - 1]
                    actionName = last.function
                    lineno = last.lineno
                    filename = pt.Path(last.filename).name
                    break

            if actionName is None:
                out = '\n      config field "{}" unavailable\n'\
                      '      in file "{}" in line {}'.format(fieldname, filename, lineno)
            else:
                out = '\n      config field "{}" unavailable\n'\
                      '      requested by action "{}" in line {}\n'\
                      '      in file "{}"'.format(fieldname, actionName, lineno, filename)
            raise ConfigurationError(out)

    def print(self):
        pprint.pprint(self)


class ConfigList(list):
    def __getitem__(self, fieldname):
        """
        Access the config list and retrieve data set by field name.
        If an KeyError is raised and the actionName is None, a ConfigurationError
        is raised, warning the user of an unsuccessful configuration.
        :param field name
        :return data from config list which is accessed using the field name
        """
        try:
            return super().__getitem__(fieldname)
        except (TypeError, IndexError) as e:
            s = inspect.stack()

            actionName = None
            lineno = s[0].lineno
            filename = pt.Path(s[0].filename).name

            for idx, iframe in enumerate(s):
                if iframe.function == '__actionwrapper__':
                    last = s[idx - 1]
                    actionName = last.function
                    lineno = last.lineno
                    filename = pt.Path(last.filename).name
                    break

            if actionName is None:
                out = '\n      element at position {} unavailable\n'\
                      '      in file "{}" in line {}'.format(fieldname, filename, lineno)
            else:
                out = '\n      element at position {} unavailable\n'\
                      '      requested by action "{}" in line {}\n'\
                      '      in file "{}"'.format(fieldname, actionName, lineno, filename)

            raise ConfigurationError(out)


def convertList(d):
    '''
    When loading the .yaml, the user defined workflow is stored in a dictionary.
    This method converts the dictionary to a list.
    :return list with actions to execute in workflow
    '''
    if not isinstance(d, ConfigDict):
        for ikey, ivalue in d.items():
            if hasattr(ivalue, 'keys'):
                d[ikey] = convertList(ivalue)
            elif not hasattr(ivalue, 'strip') and hasattr(ivalue, '__iter__'):
                d[ikey] = ConfigList(ivalue)
    return d


def loadAndValidate(confPath, schema):
    """
    Loads the config file from a path provided and validates it against a provided schema. If the config file is
    empty, an empty dictionary is returned in order to comply with the following interfaces.
    :param confPath: path to config, schema: validation schema which ensure certain standards of configuration
    :return config dictionary which is validated against a provided schema
    """
    conf = yaml.load(open(confPath), Loader=yaml.Loader)

    if conf is None:
        return {}

    dirs = {}
    if 'directives' in conf:
        dirs = conf['directives']
        del conf['directives']

    v = cerberus.Validator(schema)

    v.require_all = True
    v.allow_unknown = True

    if not v.validate(conf):
        raise ConfigurationError('in config file "{}":\n{}'.format(confPath, v.errors))

    conf = convertList(conf)

    for idir in dirs:
        for itag, ival in idir.items():
            if itag == 'config':
                isubConfigTag, isubConfigPath = ival
                if isubConfigTag in conf:
                    raise KeyError(f'sub config with name "{isubConfigTag}" already exists. Rename subconfig')
                conf[isubConfigTag] = yaml.load(open(isubConfigPath), Loader=yaml.Loader)
    return conf


class ConfigProvider:
    """
    The ConfigProvider triggers the reading and validation of the config file.
    For this purpose it sets the pathes, parses the config file for a user schema
    and triggers the validation process.
    """
    def __init__(self):
        self.config = None
        self.ioprocSchema = None
        self.userConfigPath = None
        self.ioprocProjectRoot = None

    def setPathes(self, ioprocSchema, userConfigPath):
        self.ioprocSchema = ioprocSchema
        self.userConfigPath = userConfigPath

    def parse(self):
        self.config = ConfigDict()

        self.config['ioproc'] = {}
        self.config['ioproc']['userschema'] = self.ioprocSchema/'user_schema.yaml'

        p = self.config['ioproc']['userschema']
        if not p.exists():
            raise IOError(f'Schema file at \n"{p}"\n does not exist!')

        schema = yaml.load(open(p), Loader=yaml.SafeLoader)
        self.config["user"] = loadAndValidate(self.userConfigPath, schema)

        return self.config

    def get(self):
        if self.config is None:
            self.parse()
        return self.config

configProvider = ConfigProvider()
