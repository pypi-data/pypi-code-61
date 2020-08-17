from ..util import logger
import uuid
import datetime
from threatstack.models.event import Event

_logger = logger.getLogger(__name__)

class EnvironmentInfoEvent(Event):
    """
    Environment event info
    """
    def __init__(self, payload):
        self._data = {}

        self._data['payload'] = payload
        self._data['timestamp'] = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%SZ')
        self._data['module_name'] = 'threatstack-agent-python'
        self._data['event_id'] = str(uuid.uuid4())
        self._data['agent_type'] = 'python'       

        self._data['event_type'] = 'environment'

    def prepare_for_send(self):
        """prepare into formattable dict for requests library"""
        dict_to_send = self._data

        return dict_to_send


