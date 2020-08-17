from os import environ
from threatstack.config import CONF, Config

def test_default_config():
    assert CONF["AGENT_VERSION"] == "0.0.10"
    assert CONF["API_COLLECTOR_URL"] == "https://appsec-sensors.threatstack.com/api/events"
    assert CONF["COLLECTOR_INTERVAL"] == 10
    assert CONF["ENV"] == "production"
    assert not CONF["BLOCK_XSS"]
    assert not CONF["BLOCK_SQLI"]
    assert not CONF["BLOCK_NOSQLI"]

def test_specific_config():
    env = environ
    env['BLUEFYRE_API_COLLECTOR_URL'] = 'http://localhost:8888/events'
    env['BLUEFYRE_AGENT_ID'] = '1234'
    env['THREATSTACK_BLOCK_SQLI'] = 'yEs'
    env['THREATSTACK_BLOCK_XSS'] = 'TrUe'
    env['BLUEFYRE_BLOCK_NOSQLI'] = '1'
    env['BLUEFYRE_COLLECTOR_INTERVAL'] = '30'
    env['THREATSTACK_ENV'] = 'dev'
    env['BLUEFYRE_ENV'] = 'should not be used'
    conf = Config()
    assert conf["API_COLLECTOR_URL"] == env['BLUEFYRE_API_COLLECTOR_URL']
    assert conf["COLLECTOR_INTERVAL"] == int(env['BLUEFYRE_COLLECTOR_INTERVAL'])
    assert conf["ENV"] == env['THREATSTACK_ENV']
    assert conf["BLOCK_XSS"]
    assert conf["BLOCK_SQLI"]
    assert conf["BLOCK_NOSQLI"]
