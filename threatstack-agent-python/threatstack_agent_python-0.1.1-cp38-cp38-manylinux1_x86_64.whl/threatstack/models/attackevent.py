from ..util import logger
import uuid
import datetime
import traceback

from threatstack.models.event import Event

_logger = logger.getLogger(__name__)

class AttackEvent(Event):
    """
    Attack event info
    """
    def __init__(self, payload, type='sqli', isBlocked=False, request=None):
        # unset stuff, this is ugly, refactor for later
        payload_clone = payload.copy()
        payload_clone.pop('params_in', None)
        payload_clone.pop('path', None)
        payload_clone.pop('method', None)
        payload_clone.pop('params', None)
        payload_clone.pop('attack_details', None)

        payload_clone['details'] = {
            "details": [payload['attack_details']],
            "in" : payload['params_in'],
            "type" : type,
            "isBlocked" : isBlocked,
            "action" : "wrapper_wsgi"
        }
        payload_clone['stack'] = traceback.format_stack(None,4)

        payload_new = {}
        payload_new['payload'] = {
            'attack': payload_clone,
        }
        super(AttackEvent, self).__init__(payload_new, request)    
        self._data['event_type'] = 'attack'
        _logger.debug("self._data = %s", self._data)

    def prepare_for_send(self):
        """prepare into formattable dict for requests library"""
        dict_to_send = self._data

        return dict_to_send


