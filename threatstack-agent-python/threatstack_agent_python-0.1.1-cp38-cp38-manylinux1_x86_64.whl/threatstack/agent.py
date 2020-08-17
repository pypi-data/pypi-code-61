import traceback
import sys

from .util import logger
from .processor import processor_instance
from .receiver import receiver_instance
from .util.common import get_process_cmdline,get_parent_cmdline

_logger = logger.getLogger(__name__)

try:
        from .instrumentation.django import wrap_django
        from .instrumentation.django_redis import wrap_django_redis
        from .instrumentation.flask_wrap import wrap_flask
        from .instrumentation.mysqldb import wrap_mysql
        from .instrumentation.pymysql import wrap_pymysql
        from .instrumentation.psycopg import wrap_pg
        from .instrumentation.os_wrap import wrap_os
        from .instrumentation.pty_wrap import wrap_pty
        from .instrumentation.subprocess_wrap import wrap_subprocess
        from .util.platform_info import get_os_info, get_dependencies
        from .instrumentation.global_wrap import wrap_global
except ImportError:
        traceback.print_exc(file=sys.stdout)

_instance_receiver = None
_instance_agent = None
_do_not_instrument_commands = ['newrelic-admin', 'manage.py shell']


def wrap_frameworks():
        """Called during agent initialization to instrument the Django framewort"""
        _logger.info('Instrumenting frameworks')
        wrap_global()
        wrap_pty()
        wrap_subprocess()
        wrap_flask()
        wrap_django_redis()
        wrap_django()
        wrap_mysql()
        wrap_pymysql()
        wrap_pg()
        wrap_os()
        _logger.info('Framework instrumentation complete')

def init_receiver():
        """Init Receiver"""
        _instance_receiver = receiver_instance()
        _logger.debug('Init Receiver complete')

def init_processor():
        """Init Processor"""
        _instance_agent = processor_instance()
        _logger.debug('Init processor complete')

def initialize(ignore_errors=None,log_file=None, log_level=None):
        """Main initializer for the agent

        """
        _logger.debug("Main initializer debug")

        # Retrieve the command used to launch the process
        
        if hasattr(sys, 'argv'):
                # _logger.info("sys.argv %s", sys.argv)
                command = get_process_cmdline()
                # _logger.info("command %s",command)

                # Retrieve the parent command
                parent_command = get_parent_cmdline()
                # _logger.info("parent_command %s",parent_command)

                # This can cause double instrumentation
                for item in _do_not_instrument_commands:
                        if item in command or item in parent_command:
                                _logger.info('Preventing Threatstack from running %s',item)
                                return

        # _logger.debug('Init wrap frameworks')
        wrap_frameworks()
        # _logger.debug('Init wrap frameworks complete') 

        init_receiver()
        init_processor()

        get_os_info()
        get_dependencies()

        _logger.info('ThreatStack agent initialized')
