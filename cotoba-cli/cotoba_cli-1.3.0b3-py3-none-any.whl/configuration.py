import toml
import os
from logging import config as logging_config

CONFIG_DIRECTORY_NAME = '.cotoba'
LOGFILE_NAME = 'cotoba-cli.log'


def config_directory():
    """
    returns config directry.
    if not directory exists, make directory.

    Returns
    -------
    directory: str
      config directory
    """
    home_directory = os.environ.get('COTOBA_HOME', os.path.expanduser('~'))
    directory = os.path.join(home_directory, CONFIG_DIRECTORY_NAME)
    if not os.path.exists(directory):
        os.mkdir(directory)
    return directory


class BaseConfiguration(object):
    """
    Singleton base class to handle configuration file.
    """

    def __new__(cls, *args, **kargs):
        if not hasattr(cls, '_instance'):
            instance = super(BaseConfiguration, cls).__new__(cls)
            home_dir = config_directory()
            cls._config_filepath = os.path.join(home_dir, instance.config_filename)
            if not os.path.exists(cls._config_filepath):
                with open(cls._config_filepath, 'w') as f:
                    toml.dump(instance.default_config, f)

            instance.load_config()
            cls._instance = instance

        return cls._instance

    @property
    def config(self):
        return self._config

    @property
    def config_filepath(self):
        return self._config_filepath

    @property
    def config_filename(self):
        raise NotImplementedError()

    @property
    def default_config(self):
        raise NotImplementedError()

    def load_config(self):
        with open(self._config_filepath, 'r') as f:
            self._config = toml.load(f)

    def save_config(self):
        with open(self._config_filepath, 'w') as f:
            toml.dump(self._config, f)


class Configuration(BaseConfiguration):
    DEFAULT_AUTH = 'YXAtbm9ydGhlYXN0LTFfNVMweWt0cFpxLDQ2aHB0MGhhcm5ha2N1YnN0czlzcTR1NXQz'

    @property
    def config_filename(self):
        return 'config.toml'

    @property
    def default_config(self):
        return {
            'default': {
                'endpoint-url': 'https://api.cotoba.net/',
                'locale': 'ja-JP'
            }
        }

    @property
    def endpoint_url(self):
        return self._config['default']['endpoint-url']

    @endpoint_url.setter
    def endpoint_url(self, v):
        self._config['default']['endpoint-url'] = v

    @property
    def locale(self):
        return self._config['default']['locale']

    @locale.setter
    def locale(self, v):
        self._config['default']['locale'] = v

    @property
    def authorization(self):
        # if authorization is not set, returns default auth value
        # this process hides default auth value from production users.
        return self._config['default'].get('authorization', self.DEFAULT_AUTH)

    @authorization.setter
    def authorization(self, v):
        self._config['default']['authorization'] = v


class Session(BaseConfiguration):
    @property
    def config_filename(self):
        return 'session.toml'

    @property
    def default_config(self):
        return {
            'default': {
                'id': '',
                'id_token': '',
                'access_token': '',
                'refresh_token': '',
            }
        }

    @property
    def id(self):
        return self._config['default']['id']

    @id.setter
    def id(self, v):
        self._config['default']['id'] = v

    @property
    def id_token(self):
        return self._config['default']['id_token']

    @id_token.setter
    def id_token(self, v):
        self._config['default']['id_token'] = v

    @property
    def access_token(self):
        return self._config['default']['access_token']

    @access_token.setter
    def access_token(self, v):
        self._config['default']['access_token'] = v

    @property
    def refresh_token(self):
        return self._config['default']['refresh_token']

    @refresh_token.setter
    def refresh_token(self, v):
        self._config['default']['refresh_token'] = v


def logfile_path():
    directory = config_directory()
    logfile_path = os.path.join(directory, LOGFILE_NAME)
    return logfile_path


def initialize_logger():
    logging_config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'formatter': {
                'format': '[%(levelname)s] %(asctime)s %(pathname)s(%(lineno)s): %(message)s'
            }
        },
        'handlers': {
            'file_handler': {
                'level': 'INFO',
                'formatter': 'formatter',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': logfile_path(),
                'maxBytes': 1000000,
                'backupCount': 3,
                'encoding': 'utf-8',
            },
            'console_handler': {
                'class': 'logging.StreamHandler',
                'formatter': 'formatter',
                'level': 'WARN',
            }
        },
        'root': {
            'handlers': ['file_handler', 'console_handler'],
        }
    })
