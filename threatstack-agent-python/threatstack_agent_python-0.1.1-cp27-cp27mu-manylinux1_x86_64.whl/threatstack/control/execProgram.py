from __future__ import print_function

from threatstack.control import command, usage

from ..util import logger

_logger = logger.getLogger(__name__)

@command('execProgram', '...',
"""Command line execution of the program that auto-initiates the Threatstack agent.

Setting the THREATSTACK_CONFIG_FILE environment variable is recommended for a configuration file. 
Alternatively, set the following
THREATSTACK_APP_KEY
THREATSTACK_APP_NAME
THREATSTACK_LOG""")
def execProgram(args):
    import os
    import sys
    import time

    #_logger.debug('01 sys.path %s', sys.path)

    if len(args) == 0:
        usage('execProgram')
        sys.exit(1)

    from threatstack import version, __file__ as root_directory

    root_directory = os.path.dirname(root_directory)
    boot_directory = os.path.join(root_directory, 'assister')

    python_path = boot_directory

    if 'PYTHONPATH' in os.environ:
        path = os.environ['PYTHONPATH'].split(os.path.pathsep)
        if not boot_directory in path:
            _logger.debug('boot_directory not in path, adding it now')
            python_path = "%s%s%s" % (boot_directory, os.path.pathsep,
                    os.environ['PYTHONPATH'])

    os.environ['PYTHONPATH'] = python_path
    #_logger.debug("python_path %s",python_path)
    #_logger.debug("02 sys_path %s",sys.path)

    os.environ['THREATSTACK_CONTROL_COMMAND'] = repr(sys.argv)

    os.environ['THREATSTACK_PYTHON_PREFIX'] = os.path.realpath(os.path.normpath(sys.prefix))
    os.environ['THREATSTACK_PYTHON_VERSION'] = '.'.join(map(str, sys.version_info[:2]))

    # If not an absolute or relative path, then we need to
    # see if program can be found in PATH. Note that can
    # be found in current working directory even though '.'
    # not in PATH.

    programRun_path = args[0]
    _logger.info('programRun_path %s', programRun_path)

    if not os.path.dirname(programRun_path):
        program_search_path = os.environ.get('PATH', '').split(os.path.pathsep)
        print('program_search_path %s',program_search_path)
        for path in program_search_path:
            path = os.path.join(path, programRun_path)
            if os.path.exists(path) and os.access(path, os.X_OK):
                programRun_path = path
                break

    os.execl(programRun_path, *args)
