import os
import threading
import traceback
import json
import six

if six.PY3:
    get_ident = threading.get_ident
elif six.PY2:
    import thread
    get_ident = thread.get_ident

from .models.event import Event
from .models.event import EventEncoder
from .models.environmentinfoevent import EnvironmentInfoEvent
from .models.attackevent import AttackEvent
from .models.dependenciesevent import DependenciesEvent
import threatstack
import requests
import sys
from .config import CONF
from .util import logger
from inspect import currentframe, getframeinfo

_logger = logger.getLogger(__name__)

class Receiver(object):
    """Communicates with the backend"""

    # singleton
    _instance = None
    _instance_lock = threading.Lock()

    _bucket_event = []
    _bucket_event_length = 0    
    _bucket_environment = {}
    _bucket_dependency = {}
    _sent_environment_info = False
    _sent_dependency_info = False
    _pid = None

    _http_session = requests.Session()

    def __init__(self):
        _logger.info("Receiver init complete")
        self._sent_environment_info = False
        pass

    @staticmethod
    def receiver_singleton():
        """Access the singleton receiver"""

        if Receiver._instance:
            return Receiver._instance

        instance = None

        #with Receiver._instance_lock:
        if not Receiver._instance:
            _logger.debug('Creating Receiver in process pid= %d., thread id=%d', os.getpid(), get_ident())
            _logger.debug('Receiver was initialized from: %r',''.join(traceback.format_stack()[:-1]))

            instance = Receiver()

            Receiver._instance = instance
            Receiver._pid = os.getpid()
        if instance:
            _logger.debug('Begin bootstrap')
            instance.bootstrap()

        return Receiver._instance

    def bootstrap(self):
        """Now bootstrap the Receiver."""       
        self._instance_agent = threatstack.processor.processor_instance()
        _logger.debug('Starting Threatstack Receiver pid=%d, threading.id=%d', os.getpid(), get_ident())

    def _reset_receiver(self):
        """ Check if we need to reset the receiver if the pids dont match """       
        pid = os.getpid()
        if self._pid != pid:
            _logger.debug('Reset the processor too, pid= %d., thread id=%d', os.getpid(), get_ident())
            self._instance_agent.reset_processor()
            
            _logger.debug('Receiver bootstrap pid= %d., thread id=%d', os.getpid(), get_ident())
            Receiver._instance.bootstrap()

    def set_event(self, event):
        """logs the event to the eventbucket"""
        # get line number and file path       

        self._reset_receiver()

        cf = currentframe().f_back
        filename = getframeinfo(cf).filename
        event['file_path'] = filename
        event['line_num'] = cf.f_lineno

        self._bucket_event.append(Event(event))
        self._bucket_event_length+=1

    def set_event_attack(self, event, type, isBlocked, request):
        """logs the event to the eventbucket"""

        self._reset_receiver()

        cf = currentframe().f_back
        filename = getframeinfo(cf).filename
        event['file_path'] = filename
        event['line_num'] = cf.f_lineno

        _logger.debug("setting attack_event pre count=%d, pid=%d, thread id=%d", self._bucket_event_length, os.getpid(), get_ident())
        self._bucket_event.append(AttackEvent(event, type, isBlocked, request))
        self._bucket_event_length+=1
        _logger.debug("setting attack_event post count=%d, pid=%d, thread id=%d", self._bucket_event_length, os.getpid(), get_ident())


    def set_environment_middleware(self, middleware):
        """updates with middleware"""
        
        self._reset_receiver()
        
        if (middleware not in self._bucket_environment):
            _logger.debug("Adding middleware %s", middleware)           
            self._bucket_environment[middleware] = True

    def set_environment_info(self, env_info):
        """updates with environment settings"""
        
        self._reset_receiver()
        
        for key,val in env_info.items():
            if (key not in self._bucket_environment):
                self._bucket_environment[key] = val
                
        _logger.debug("environment %d %s", len(self._bucket_environment), self._bucket_environment)

    def set_dependencies(self, dep_info):
        """updates with dependencies"""
        
        self._reset_receiver()
        
        for key,val in dep_info.items():
            if (key not in self._bucket_dependency):
                _logger.debug("Adding dependency info %s, %s", key, val)           
                self._bucket_dependency[key] = val
                
        _logger.debug("environment %d %s", len(self._bucket_environment), self._bucket_environment)

    def clear_event_bucket(self):
        """clean out the event queue"""
        self._bucket_event = []
        self._bucket_event_length = 0

    def _sendEnvInfo(self):
        """send environment info """
        if self._sent_environment_info is False and len(self._bucket_environment) > 0:
            # serialize the environment info bucket
            payload_env = []
            e = EnvironmentInfoEvent(self._bucket_environment)
            payload_env.append(e.prepare_for_send())

            payload_env = json.dumps(payload_env)
            _logger.debug('appending EnvironmentInfoEvent %s', payload_env)            
            # submit 
            self.post_data(payload_env)
            self._sent_environment_info = True        
        
    def _sendDependencyInfo(self):
        """send dependencies info """
        if self._sent_dependency_info is False and len(self._bucket_dependency) > 0:
            # serialize the environment info bucket
            payload_dependency = []
            e = DependenciesEvent(self._bucket_dependency)
            payload_dependency.append(e.prepare_for_send())

            payload_dependency = json.dumps(payload_dependency)
            _logger.debug('appending DependenciesEvent %s', payload_dependency)            
            # submit 
            self.post_data(payload_dependency)
            self._sent_dependency_info = True        

    def send_metrics(self):
        """go through event_bucket and environment_info to send"""

        self._sendEnvInfo()
        self._sendDependencyInfo()

        _logger.debug('event count = %d, os.pid=%d, thread id=%d', self._bucket_event_length, os.getpid(), get_ident())
        
        # serialize the event_bucket
        if self._bucket_event_length > 0:
            _logger.debug('self._bucket_event_length %d', self._bucket_event_length)
            payload = json.dumps(self._bucket_event, cls=EventEncoder)
            # submit 
            self.post_data(payload)      
            self.clear_event_bucket()
        

    def get_headers(self):
        """send custom headers using agent information"""
        headers = {}
        if self._instance_agent is not None:
            agent_info = self._instance_agent.get_agent_info()
            for item in agent_info:
                strItem = item.replace('_','-')
                headers['bluefyre-' + strItem] = agent_info[item]
        return headers


    def post_data(self, payload):
        """initiates http post"""
        try:
            headers = self.get_headers()            
            url = CONF['API_COLLECTOR_URL']
            
            cert_chain=True
            if(CONF['ENV'] == 'dev'):
                cert_chain = os.path.join(os.path.dirname(__file__), CONF['CERT_CHAIN'])
                _logger.debug("cert_chain path %s", cert_chain)
            _logger.debug("Bluefyre Payload: %s", payload)

            # fire request
            r = self._http_session.post(url, data=payload, headers=headers, verify=cert_chain)

            # log the content
            status_code = r.status_code
            content = r.content
            _logger.debug("Bluefyre Response %d %s", status_code, content)

        except requests.RequestException:
            exc_type, message = sys.exc_info()[:2]
            _logger.warning("Bluefyre request failed %s, %s", exc_type, message)

        except Exception:
            _logger.exception("Bluefyre request exception")


def receiver_instance():
    """Get the singleton instance of the receiver"""
    _logger.debug("calling receiver_instance, os.pid=%d", os.getpid())
    return Receiver.receiver_singleton()        
