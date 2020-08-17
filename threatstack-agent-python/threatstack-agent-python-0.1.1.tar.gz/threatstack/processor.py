import os
import sys
import time
import threading
import traceback
import uuid
import six

if six.PY3:
    get_ident = threading.get_ident
elif six.PY2:
    import thread
    get_ident = thread.get_ident

import threatstack
from .config import CONF
from .util import logger

_logger = logger.getLogger(__name__)

class Processor(object):
    """
    Takes care of eventing
    """

    _instance = None
    _instance_lock = threading.Lock()
    _instance_receiver = None

    def __init__(self):
        self._creation_time = time.time()
        self._process_id = os.getpid()

        self._lock = threading.Lock()
        self._collector_thread = threading.Thread(
            target=self._collector_loop,
            name='Threatstack-Collector-Thread')
        self._collector_thread.setDaemon(True)
        self._collector_shutdown = threading.Event()

        self._collection_count = 0
        self._last_collection = 0.0
        self._collection_duration = 0.0
        self._next_collection = 0.0

        self._process_shutdown = False   

        #TODO: get other information from config file
        self.agent = {}
        self.set_agent_info()

        _logger.info("Processor init complete")

    def set_agent_info(self):
        """Sets agent information as part of init"""
        self.agent['agent_id'] = CONF['AGENT_ID']
        self.agent['agent_instance_id'] = CONF['AGENT_INSTANCE_ID']
        self.agent['agent_version'] = CONF['AGENT_VERSION']
        self.agent['license_key'] = 'LICENSE_KEY_NOT_SET'

    # TODO: make this a property decorator
    def get_agent_info(self):
        """Gets agent dict"""
        return self.agent

    @staticmethod
    def reset_processor():
        """Reset processor"""
        if Processor._instance:
            Processor._instance.stop_collector()
            Processor._instance = None

        _logger.debug('Creating Threatstack processor in pid=%d, threadid=%d', os.getpid(), get_ident())

        instance = Processor()

        Processor._instance = instance

        if instance:
            _logger.debug('Begin bootstrap pid=%d, threadid=%d', os.getpid(), get_ident())
            instance.bootstrap()


    @staticmethod
    def processor_singleton():
        """Access the singleton processor"""

        if Processor._instance:
            return Processor._instance

        _logger.info('Threatstack Processor (%s)' % threatstack.version)

        instance = None

        # with Processor._instance_lock:
        if not Processor._instance:
            _logger.debug('Creating Threatstack processor in pid %d, threadid=%d', os.getpid(), get_ident())
            # _logger.debug('Processor was initialized from: %r',''.join(traceback.format_stack()[:-1]))

            instance = Processor()

            Processor._instance = instance

        if instance:
            _logger.debug('Begin bootstrap in pid %d, threadid=%d', os.getpid(), get_ident())
            instance.bootstrap()

        return Processor._instance


    def bootstrap(self):
        """Now bootstrap the processor."""        
        self._instance_receiver = threatstack.receiver.receiver_instance()
         # If background thread is already running, no need to initiate
        if self._collector_thread.isAlive():
            _logger.debug('self._collector_thread.isAlive, os.getpid=%d', os.getpid())
            return

        _logger.debug('Starting Threatstack Processor thread os.pid=%d, threading.id=%d', os.getpid(), get_ident())
        self._collector_thread.start()

    def _collector_loop(self):
        """Collector loop that runs every 60 seconds collecting metrics and sending to the backend."""
        _logger.debug('starting collector loop.')
        self._next_collector_time = time.time()
        try:
            while True:
                if self._collector_shutdown.isSet():
                    self._run_collector(stop_collection=True)
                    return

                time_now = time.time()
                while self._next_collector_time <= time_now:
                    self._next_collector_time += int(CONF['COLLECTOR_INTERVAL'])
                
                delay = self._next_collector_time - time_now
                self._collector_shutdown.wait(delay)

                if self._collector_shutdown.isSet():
                    # Before shutting down, get a final collection of metrics
                    self._run_collector(stop_collection=True)
                    return

                # Kick off the collection
                self._run_collector(stop_collection=False)


        except Exception:
            if self._process_shutdown:
                _logger.exception('Unknown exception in the collector_loop, after shutdown initiated')
            else:
                _logger.exception('Unknown exception in the collector_loop')               

    def _run_collector(self, stop_collection=False):
        """Collection and Reporting functions"""
        # _logger.debug('running collector loop %s', self._process_id)
        if stop_collection:
            _logger.debug('final collection before halt')
        #else:
        #    _logger.debug('Beginning collection')        

        self._collection_count += 1
        self._last_collection = time.time()

        # send events to the backend
        if self._instance_receiver:
            _logger.debug('Sending events time=%s, processid=%d, os.pid=%d',time.time(), self._process_id, os.getpid())        
            self._instance_receiver.send_metrics()

        self._collection_duration = time.time() - self._last_collection
        # _logger.debug('Collection completed in %.2f seconds.', self._collection_duration)
        
    def stop_collector(self):
        """Stop the collector"""
        _logger.debug('stop_collector os.getpid=%d', os.getpid())
        self._collector_shutdown.set()

            
def processor_instance():
    """Get the singleton instance of the processor"""
    _logger.debug("calling processor_instance, os.pid=%d", os.getpid())
    return Processor.processor_singleton()


def reset_processor():
    """Get the singleton instance of the processor"""
    return Processor.reset_processor()
