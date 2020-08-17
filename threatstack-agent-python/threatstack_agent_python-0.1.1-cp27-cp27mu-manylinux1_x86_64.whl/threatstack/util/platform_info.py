""" Helper module for platform information
"""
import os 
import requests
from . import logger
_logger = logger.getLogger(__name__)

from ..config import CONF
from ..receiver import receiver_instance

def _isDocker():
    """ check if running in Docker """

    path = '/proc/self/cgroup'
    bReturn = False

    try:        
        bReturn = (os.path.exists('/.dockerenv') or
            os.path.isfile(path) and any('docker' in line for line in open(path)))
    except:
        _logger.debug("could not parse docker info")            
        pass            

    return bReturn
    

def get_os_info():
    """ OS and container specific info """

    _instance_receiver = receiver_instance()

    try:
        settings_os = {}
        import platform
        result = platform.uname()
        # (system, node, release, version, machine, processor)
        # ('Darwin', 'thefoolserrand.local', '17.7.0', 'Darwin Kernel Version 17.7.0: Thu Jun 21 22:53:14 PDT 2018; root:xnu-4570.71.2~1/RELEASE_X86_64', 'x86_64', 'i386')
        # ('Linux', 'dev4', '4.4.0-87-generic', '#110-Ubuntu SMP Tue Jul 18 12:55:35 UTC 2017', 'x86_64', 'x86_64')

        _instance_receiver.set_environment_info({'hostname': result[1]})
        settings_os['platform'] = result[0]
        settings_os['arch'] = result[4]
        settings_os['release'] = result[2]
        settings_os['type'] = result[0]
        settings_os['isdocker'] = _isDocker()

        settings_aws = get_AWSMetadata()

        _instance_receiver.set_environment_info({
            'os': settings_os,
            'aws': settings_aws
            })
    except ImportError:
        _logger.debug('Could not import platform')
        pass

def get_dependencies():
    """ get dependencies """

    _instance_receiver = receiver_instance()

    try:
        dependencies_set = {}
        import pkg_resources

        for package in pkg_resources.working_set:
            _logger.debug("Appending Dependency %s %s", package.key, package.version)
            dependencies_set[package.key] = package.version

        _instance_receiver.set_dependencies({'dependencies': dependencies_set})

    except ImportError:
        _logger.debug('Could not import pkg_resources')
        pass


def get_AWSMetadata():
    """ get AWS Metadata """
    metadata_aws = {}
    URL_METADATA = 'http://169.254.169.254/latest/dynamic/instance-identity/document'
    SEC_TIMEOUT = 0.5

    _instance_receiver = receiver_instance()

    try:
        r = requests.get(URL_METADATA, timeout=SEC_TIMEOUT)
        r.raise_for_status()
    except Exception as e:
        r = None
        _logger.debug('Unable to fetch AWS meta data from %r: %r', URL_METADATA, e)
        return metadata_aws

    try:
        j = r.json()
    except ValueError:
        _logger.debug('could not parse AWS Metadata %r', r.text)
        return metadata_aws

    metadata_aws = j
    return metadata_aws
