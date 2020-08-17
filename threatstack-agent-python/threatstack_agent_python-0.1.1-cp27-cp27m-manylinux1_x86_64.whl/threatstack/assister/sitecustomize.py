import os
import sys
import traceback
import time

# from ..util import logger
# from ..config import Config
import threatstack.util.logger
import threatstack.config

env = threatstack.config.Config()
_logger = threatstack.util.logger.getLogger(__name__)

# _logger.debug('03 sys.path %s', sys.path)
# We need to import the original sitecustomize.py file if it exists. We
# can't just try and import the existing one as we will pick up
# ourselves again. Even if we remove ourselves from sys.modules and
# remove the bootstrap directory from sys.path, still not sure that the
# import system will not have cached something and return a reference to
# ourselves rather than searching again. What we therefore do is use the
# imp module to find the module, excluding the bootstrap directory from
# the search, and then load what was found.

import imp

boot_directory = os.path.dirname(__file__)
root_directory = os.path.dirname(os.path.dirname(boot_directory))

# traceback.print_stack()

_logger.debug('root_directory = %r', root_directory)
_logger.debug('boot_directory = %r', boot_directory)


path = list(sys.path)

if boot_directory in path:
    _logger.debug('deleting boot_directory %s from path', boot_directory)
    del path[path.index(boot_directory)]

try:
    (file, pathname, description) = imp.find_module('sitecustomize', path)
    _logger.debug('file = %s, pathname = %s', file, pathname)
except ImportError:
    pass
else:
    _logger.info('sitecustomize = %r', (file, pathname, description))
    imp.load_module('sitecustomize', file, pathname, description)

# Because the PYTHONPATH environment variable has been amended and the
# bootstrap directory added, if a Python application creates a sub
# process which runs a different Python interpreter, then it will still
# load this sitecustomize.py. If that is for a different Python version
# it will cause problems if we then try and import and initialize the
# agent. We therefore need to try our best to verify that we are running
# in the same Python installation as the original threatstackctl script
# which was run and only continue if we are.

expected_python_prefix = env.read_str('PYTHON_PREFIX')
actual_python_prefix = os.path.realpath(os.path.normpath(sys.prefix))

expected_python_version = env.read_str('PYTHON_VERSION')
actual_python_version = '.'.join(map(str, sys.version_info[:2]))

python_prefix_matches = expected_python_prefix == actual_python_prefix
python_version_matches = expected_python_version == actual_python_version

if python_prefix_matches and python_version_matches:
    # We also need to skip agent initialisation if neither the license
    # key or config file environment variables are set. We do this as
    # some people like to use a common startup script which always uses
    # the wrapper script, and which controls whether the agent is
    # actually run based on the presence of the environment variables.

    license_key = env.read_str('LICENSE_KEY', None)
    config_file = env.read_str('CONFIG_FILE', None)
    environment = env.read_str('ENVIRONMENT', None)

    disable_appsec_agent = env.read_truthy('DISABLED', False)

    _logger.debug('04 sys.path %s', sys.path)
    if root_directory not in sys.path:
        _logger.debug('going to insert root_directory %s', root_directory)
        sys.path.insert(0, root_directory)

    if disable_appsec_agent:
        _logger.debug('THREATSTACK_DISABLED is True, going to disable the agent')
    else:
        _logger.debug("About to import agent")

        try:
            import threatstack.agent
        except ImportError:
            traceback.print_exc(file=sys.stdout)
        except Exception as e: 
            print(e)
            raise

        # Finally initialize the agent.
        _logger.debug("About to initialize agent")
        _logger.debug('05 sys.path %s', sys.path)

        try:
            threatstack.agent.initialize(config_file, environment)
        except:
            _logger.error("Couldn't initialize agent")        
            traceback.print_exc(file=sys.stdout)
