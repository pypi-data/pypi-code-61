""" Threatstack config module
"""
import logging
import uuid
import os

_logger = logging.getLogger(__name__)

TS_PREFIX = "THREATSTACK_"
BF_PREFIX = "BLUEFYRE_"
TRUTHY = ["1", "true", "yes"]
LOG_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

class Config(object):
    """Config for Threatstack

    Reads in environment variable
    """

    def __init__(self):
        """Inits Config."""
        from threatstack import version
        self.config = {
            "AGENT_VERSION": version,
            # unique id per app startup
            "AGENT_INSTANCE_ID": str(uuid.uuid4())
        }
        self.env = os.environ
        self.load()

    def _truthy_parser(self, value, default=None):
        if value is None:
            return default
        val = value.lower()
        if val in TRUTHY:
            return True
        return False

    # try THREATSTACK_VAR first
    # if not found, try BLUEFYRE_VAR second, use default value if not available either
    def read_str(self, name, default=None):
        res = self.env.get(TS_PREFIX + name, None)
        if not res:
            res = self.env.get(BF_PREFIX + name, default)
        return res

    def read_int(self, name, default=None):
        res = default
        try:
            res = int(self.read_str(name, default))
        except ValueError:
            _logger.warning('Invalid integer value for ' + name + ' var, defaulting to ' + str(default))
        return res

    def read_truthy(self, name, default=None):
        res = default
        try:
            res = self._truthy_parser(self.read_str(name, None), default)
        except:
            _logger.warning('Invalid boolean value for ' + name + ' var, defaulting to ' + str(default))
        return res

    def read_enum(self, name, allowed, default=None):
        res = self.env.get(TS_PREFIX + name, None)
        if not res:
            res = self.env.get(BF_PREFIX + name, default)
        if res and res not in allowed:
            _logger.warning('Invalid value for ' + name + ' var, allowed values are ' + str(allowed) +
                            ', defaulting to ' + str(default))
            res = default
        return res

    def read_in_env(self):
        """Reads in environment variables"""
        # read, validate and return values
        return {
            # proxy url
            "API_COLLECTOR_URL": self.read_str("API_COLLECTOR_URL", "https://appsec-sensors.threatstack.com/api/events"),

            # Specific agent Id
            "AGENT_ID": self.read_str("AGENT_ID"),

            # cert chain path.. only when ENVIRONMENT=dev
            "CERT_CHAIN": self.read_str("CERT_CHAIN", "ssl/ca-chain.cert.pem"),

            # Possible values = dev, production
            "ENV": self.read_str("ENV", "production"),

            # Collector interval in seconds
            "COLLECTOR_INTERVAL": self.read_int("COLLECTOR_INTERVAL", 10),

            # sql injection blocking
            "BLOCK_SQLI": self.read_truthy("BLOCK_SQLI", False),

            # xss blocking
            "BLOCK_XSS": self.read_truthy("BLOCK_XSS", False),

            # no sql injection blocking
            "BLOCK_NOSQLI": self.read_truthy("BLOCK_NOSQLI", False),

            # disable agent
            "DISABLED": self.read_truthy("DISABLED", False),

            # logging level, one of: DEBUG, INFO, WARNING, ERROR, CRITICAL. Defaults to CRITICAL
            "LOG_LEVEL": self.read_enum("LOG_LEVEL", LOG_LEVELS, 'CRITICAL'),

            # colored logs
            "LOG_COLORS": self.read_truthy("LOG_COLORS", False)
        }

    def load(self):
        self.config.update(self.read_in_env())

    def __getitem__(self, name):
        return self.config[name]

CONF = Config()
