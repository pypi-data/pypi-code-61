import pytest
from threatstack import agent, receiver, processor

def test_initialize():
    agent.initialize()
    assert type(agent.receiver_instance()) is receiver.Receiver
    assert type(agent.processor_instance()) is processor.Processor

def test_get_agent_info():
    agent.initialize()
    p = agent.processor_instance()
    assert type(p.get_agent_info()) is dict

def test_reset_processor():
    agent.initialize()
    p = agent.processor_instance()
    p.reset_processor()
    assert type(p) is processor.Processor