import pytest
import datetime
from threatstack.models import event, attackevent, environmentinfoevent

# tests for event.py
def test_build_event():
    e = event.Event({})
    assert e._data['event_type'] == 'instrumentation'
    assert e._data['agent_type'] == 'python'
    assert e._data['module_name'] == 'threatstack-agent-python'
    assert type(e._data['timestamp']) is str
    assert type(e._data['event_id']) is str

def test_event_with_request():
    r = {'META':{'PATH_INFO':'/'}, 'headers': {}}
    e = event.Event({},r)
    assert type(e._data) is dict

def test_build_event_encoder():
    e = event.Event({})
    ee = event.EventEncoder()
    assert type(ee.default(e)) is dict

def test_event_encoder_date():
    ee = event.EventEncoder()
    d = datetime.datetime.now()
    assert type(ee.default(d)) is str

def test_event_encoder_timedelta():
    ee = event.EventEncoder()
    d = datetime.timedelta()
    assert type(ee.default(d)) is str

def test_event_encoder_set():
    ee = event.EventEncoder()
    s = set()
    assert type(ee.default(s)) is str

# tests for attackevent.py
def test_build_attack_event():
    e = attackevent.AttackEvent({'attack_details': 'test', 'params_in': None, 'path': None, 'method': None})
    assert e._data['event_type'] == 'attack'

def test_clone_attack_event():
    payload = {
        'attack_details': 'test',
        'params_in': None
    }
    ae = attackevent.AttackEvent(payload)
    assert type(ae._data['payload']) == dict

def test_prepare_for_send():
    e = attackevent.AttackEvent({'attack_details': 'test', 'params_in': None, 'path': None, 'method': None})
    d = e.prepare_for_send() 
    assert type(d) is dict

# tests for environmentinfoevent
def test_environment_info_event():
    e = environmentinfoevent.EnvironmentInfoEvent({})
    assert e._data['event_type'] == 'environment'
    assert e._data['agent_type'] == 'python'
    assert e._data['module_name'] == 'threatstack-agent-python'
    assert type(e._data['timestamp']) is str
    assert type(e._data['event_id']) is str

def test_prepare_for_send_environment_event():
    e = environmentinfoevent.EnvironmentInfoEvent({})
    d = e.prepare_for_send() 
    assert type(d) is dict