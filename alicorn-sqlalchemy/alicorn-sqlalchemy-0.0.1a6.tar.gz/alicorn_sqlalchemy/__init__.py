#  Copyright (c) 2020 Chris Stranex
#  See LICENSE for licencing information.
#
#  There is NO WARRANTY, to the extent permitted by law.
#
from threading import Lock

from alicorn.extension import Extension
from alicorn._core import local
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, Session


class AlicornSqlAlchemy(Extension):
    """An SQLAlchemy extension for alicorn"""

    _app = None
    _engine_lock = Lock()
    session: Session = None

    Base = declarative_base()
    Session = Session

    def register(self, app):
        app.register_signal_handler('alicorn.server_before_start', self._configure_session)
        self._app = app

    def _configure_session(self):
        """Creates a session to be used for any requests"""
        print(self._app.config.get('sqlalchemy.uri', 'sqlite://'))
        self.engine = sqlalchemy.create_engine(
            self._app.config.get('sqlalchemy.uri', 'sqlite://'),
            **self._app.config.get('sqlalchemy.engine_options', {})
        )
        self.session = scoped_session(sessionmaker(bind=self.engine), scopefunc=self._current_request)

    def _current_request(self):
        return local.context

    def get_session(self, *args, **kwargs):
        return self.session
