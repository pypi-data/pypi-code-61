from ..util import logger
import uuid
import datetime
import json
import six

from threatstack.config import CONF

_logger = logger.getLogger(__name__)

class Event(object):
    """
    Base event data sent to back end
    """
    def __init__(self, payload, request=None):
        self._data = {}

        # parse out the request
        req = {}
        if request is not None:

            # Django request
            if hasattr(request, 'META'):
                req["url"] = request.META.get('PATH_INFO','')
                req["ip_address"] = request.META.get('REMOTE_ADDR','')
                req["method"] = request.META.get('REQUEST_METHOD','')
                self._data["event_sourceip"] = request.META.get('REMOTE_ADDR','')
            elif hasattr(request,'headers') and hasattr(request.headers, 'environ'):
                req["url"] = request.headers.environ['PATH_INFO']
                req["ip_address"] = request.headers.environ['REMOTE_ADDR']
                req["method"] = request.headers.environ['REQUEST_METHOD']
                self._data["event_sourceip"] = request.headers.environ['REMOTE_ADDR']

            requestHeaders = {}
            if hasattr(request,'headers'):
                for k, v in six.iteritems(request.headers):
                    requestHeaders[k] = v
                req["headers"] = requestHeaders
            elif hasattr(request,'META'):                
                for k, v in six.iteritems(request.META):
                    requestHeaders[k] = v
                req["headers"] = requestHeaders
        
        for key, values in six.iteritems(payload):
            if key == "payload":
                values['req'] = req
            self._data[key] = values
            
        self._data['event_type'] = 'instrumentation'
        self._data['timestamp'] = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%SZ')
        if 'module_name' not in self._data:
            self._data['module_name'] = 'threatstack-agent-python'
        self._data['event_id'] = str(uuid.uuid4())
        self._data['agent_type'] = 'python'         

        _logger.debug("self._data = %s", self._data)

        # TODO: get license key from config file
        #self._data['license_key'] = 'LICENSE_KEY_NOT_SET'
        # TODO: fix this
        #self._data['agent_version'] = 'AGENT_VERSION_NOT_SET'


    def capture_metadata(self):
        """
        Get metadata information
        """
        self._data.timestamp = datetime.datetime.now()
        self._data.event_id = uuid.uuid4()
        #self._data.request_id = 
        

class EventEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Event):
            return o._data
        if isinstance(o, datetime.datetime):
            return o.__str__()        
        if isinstance(o, datetime.timedelta):
            return ""
        if isinstance(o, set):
            _logger.debug("setting %s to empty string", o)
            return ""

        try:
            returnObj = json.JSONEncoder.default(self, o)
        except (ValueError, TypeError):  # includes simplejson.decoder.JSONEncodeError
            _logger.debug("json encoding failed for %s", o)
            returnObj = ""

        return returnObj

