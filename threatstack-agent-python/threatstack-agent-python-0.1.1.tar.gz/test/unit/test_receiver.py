import pytest
from threatstack import receiver, processor, agent

def test_build_receiver():
    r = receiver.Receiver()
    assert type(r) == receiver.Receiver

def test_set_event():
    agent.initialize()
    r = agent.receiver_instance()
    r.set_event({})