# coding: utf-8

__all__ = ['DesktopSession']

from appdirs import *
import os
import logging
import platform
import socket
from requests_async import codes as requests_async_codes
from requests_async import ConnectTimeout

from refinitiv.dataplatform import __version__
from .session import Session

from refinitiv.dataplatform.delivery.stream.streaming_connection_config import StreamingConnectionConfiguration
from refinitiv.dataplatform.delivery.stream.omm_stream_connection import OMMStreamConnection


class DesktopSession(Session):
    class Params(Session.Params):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

    def __init__(self, app_key, on_state=None, on_event=None, env=None, **kwargs):
        super().__init__(app_key=app_key,
                         on_state=on_state,
                         on_event=on_event,
                         token=kwargs.get("token"),
                         deployed_platform_username=kwargs.get("deployed_platform_username"),
                         dacs_position=kwargs.get("dacs_position"),
                         dacs_application_id=kwargs.get("dacs_application_id"))
        self._http_session.trust_env = False
        self._port = None
        self._udf_url = None
        self._timeout = 30
        self._user = "root"
        self._check_port_result = False

    def _get_udf_url(self):
        """
        Returns the scripting proxy url.
        """
        return self._udf_url

    def _get_rdp_url_root(self):
        return f"http://localhost:{self._port}/api/rdp"

    def _get_http_session(self):
        """
        Returns the scripting proxy http session for requests.
        """
        return self._http_session

    def set_timeout(self, timeout):
        """
        Set the timeout for requests.
        """
        self._timeout = timeout

    def get_timeout(self):
        """
        Returns the timeout for requests.
        """
        return self._timeout

    def set_port_number(self, port_number, logger=None):
        """
        Set the port number to reach Desktop API proxy.
        """
        self._port = port_number
        if port_number:
            self._udf_url = f"http://localhost:{self._port}/api/v1/data"
            self._streaming_config.host = f"localhost:{self._port}/api/v1/data/streaming/pricing"

            self.close()
        else:
            self._udf_url = None

        if logger:
            logger.info(f"Set Proxy port number to {self._port}")

    def get_port_number(self):
        """
        Returns the port number
        """
        return self._port

    def is_session_logged(self, stream_connection_name:str=None):
        """ note that currently the desktop session support only 1 websocket connection """
        stream_connection_name = 'pricing' if stream_connection_name is None else stream_connection_name
        assert(stream_connection_name in self._stream_connection_name_to_stream_connection_dict)
        return True if self._stream_connection_name_to_stream_connection_dict[stream_connection_name].ready.done() else False

    def _init_streaming_config(self):
        self._streaming_config.application_id = self._dacs_params.dacs_application_id
        self._streaming_config.position = self._dacs_params.dacs_position

        self._streaming_config.login_message = {
            "ID": "",
            "Domain": "Login",
            "Key": {
                "Name": "john doe",
                "Elements": {
                    "AppKey": self.app_key,
                    "ApplicationId": self._dacs_params.dacs_application_id,
                    "Position": self._dacs_params.dacs_position
                }
            }
        }
        # provide app_key to Desktop API Proxy through x_tr_applicationid header when starting websocket
        self._streaming_config._header = [f"x-tr-applicationid: {self.app_key}"]

    ############################################################
    #   multi-websockets support

    def _get_stream_status(self, stream_connection_name:str):
        """ this method is designed for getting a status of given stream service.

    Parameters
    ----------
        a enum of stream service
    Returns
    -------
    enum
        status of stream service.
        """
        return self._status

    def _set_stream_status(self, streaming_connection:str, stream_status):
        """ set status of given stream service

    Parameters
    ----------
    enum
        a service enum of stream
    enum
        a status enum of stream
    Returns
    -------
        """
        self._status = stream_status

    async def _get_stream_connection_configuration(self, stream_connection_name:str):
        """ this method is designed to retrieve the stream connection configuration.
        in the platform session two possible configurations including RDP platform or deployed platform.

        Parameters
        ----------
        enum
            a service enum of stream
        Returns
        -------
        obj
            a stream connection configuration object
        """
        assert (stream_connection_name == 'pricing')

        #   construct the stream connection configuration
        stream_config = StreamingConnectionConfiguration()

        #   set the configuration
        #       url
        stream_config.websocket_endpoints = [f"localhost:{self._port}/api/v1/data/streaming/pricing", ]
        #       dacs position
        stream_config.position = self._dacs_params.dacs_position
        #       application id
        stream_config.application_id = self._dacs_params.dacs_application_id

        # provide app_key to Desktop API Proxy through x_tr_applicationid header when starting websocket
        stream_config._header = [f"x-tr-applicationid: {self.app_key}", ]

        #   done
        return stream_config

    #   session abstractmethod
    async def _create_and_start_stream_connection(self, stream_connection_name:str):
        """ this method is designed to construct the stream connection from given stream service
                and start the connection as a separated thread

        Parameters
        ----------
        enum
            a service enum of stream
        Returns
        -------
        obj
            a created stream connection object
        """

        #   get the stream config by given stream service
        stream_config = await self._get_stream_connection_configuration(stream_connection_name)

        #   set the stream connection class by type

        # warning :: DESKTOP SESSION SUPPORT ONLY PRICING
        assert stream_connection_name == 'pricing'
        websocket_thread_name = "WebSocket {}".format(self.session_id)

        stream_connection = OMMStreamConnection(websocket_thread_name, self,
                                                stream_connection_name, stream_config)

        #   store stream connection
        self._stream_connection_name_to_stream_connection_dict[stream_connection_name] = stream_connection

        #   done
        return stream_connection

    ##################################################
    #   OMM login message for each kind of session ie. desktop, platform or deployed platform

    def get_omm_login_message_key_data(self):
        """ return the login message for omm 'key'
        """
        return {"Name": "john doe",
                "Elements": {
                    "AppKey": self.app_key,
                    "ApplicationId": self._dacs_params.dacs_application_id,
                    "Position": self._dacs_params.dacs_position
                }
            }

    #######################################
    #  methods to open and close session  #
    #######################################
    def open(self):
        if self._state in [Session.State.Pending, Session.State.Open]:
            # session is already opened or is opening
            return self._state

        # call Session.open() based on open_async() => _init_streaming_config will be called later
        return super(DesktopSession, self).open()

    def close(self):
        return super(DesktopSession, self).close()

    ############################################
    #  methods to open asynchronously session  #
    ############################################
    async def open_async(self):
        if self._state in [Session.State.Pending, Session.State.Open]:
            # session is already opened or is opening
            return self._state

        port_number = await self.identify_scripting_proxy_port()
        if port_number:
            self.set_port_number(port_number)
            self.log(logging.INFO, f"Application ID: {self.app_key}")
            self._state = Session.State.Open
            self._on_state(Session.State.Open, "Session is opened.")
            self._init_streaming_config()
        else:
            # port number wasn't identified => do nothing ?
            self.log(logging.ERROR, "Port number was not identified, cannot send any request")

        await super(DesktopSession, self).open_async()

        return self._state

    @staticmethod
    def read_firstline_in_file(filename, logger=None):
        try:
            f = open(filename)
            first_line = f.readline()
            f.close()
            return first_line
        except IOError as e:
            if logger:
                logger.error(f"I/O error({e.errno}): {e.strerror}")
            return ""

    async def identify_scripting_proxy_port(self):
        """
        Returns the port used by the Scripting Proxy stored in a configuration file.
        """

        port = None
        path = []
        app_names = ["Data API Proxy", "Eikon API proxy", "Eikon Scripting Proxy"]
        for app_author in ["Refinitiv", "Thomson Reuters"]:
            if platform.system() == "Linux":
                path = path + [user_config_dir(app_name, app_author, roaming=True)
                               for app_name in app_names if os.path.isdir(user_config_dir(app_name, app_author, roaming=True))]
            else:
                path = path + [user_data_dir(app_name, app_author, roaming=True)
                               for app_name in app_names if os.path.isdir(user_data_dir(app_name, app_author, roaming=True))]

        if len(path):
            port_in_use_file = os.path.join(path[0], ".portInUse")

            # Test if ".portInUse" file exists
            if os.path.exists(port_in_use_file):
                # First test to read .portInUse file
                firstline = self.read_firstline_in_file(port_in_use_file)
                if firstline != "":
                    saved_port = firstline.strip()
                    await self.check_port(saved_port)
                    if self._check_port_result:
                        port = saved_port
                        self.log(logging.INFO, f"Port {port} was retrieved from .portInUse file")

        if port is None:
            self.log(logging.INFO, "Warning: file .portInUse was not found. Try to fallback to default port number.")
            port_list = ["9000", "36036"]
            for port_number in port_list:
                self.log(logging.INFO, f"Try defaulting to port {port_number}...")
                await self.check_port(port_number)
                if self._check_port_result:
                    return port_number

        if port is None:
            self.log(logging.ERROR,
                     "Error: no proxy address identified.\nCheck if Desktop is running.")
            return None

        await self.handshake(port)

        return port

    async def check_port(self, port, timeout=(10.0, 15.0)):
        url = f"http://localhost:{port}/api/v1/data"
        try:
            response = await self.http_request_async(url=url,
                                                     method="GET",
                                                     # headers=_headers,
                                                     # json=body,
                                                     timeout=timeout)

            # response = await self._http_session.get(url,
            #                        headers={"x-tr-applicationid": self.app_key},
            #                        timeout=timeout)

            self.log(logging.INFO, f"Checking port {port} response : {response.status_code} - {response.text}")
            self._check_port_result = True
            return
        except (socket.timeout, ConnectTimeout):
            self.log(logging.ERROR, f"Timeout on checking port {port}")
        except ConnectionError as e:
            self.log(logging.CRITICAL, f"Connexion Error on checking port {port} : {e!r}")
        except Exception as e:
            self.log(logging.DEBUG, f"Error on checking port {port} : {e!r}")
        self._check_port_result = False

    async def handshake(self, port, timeout=(5.0, 5.0)):
        url = f"http://localhost:{port}/api/handshake"
        self.log(logging.INFO, f"Try to handshake on url {url}...")
        try:
            # DAPI for E4 - API Proxy - Handshake
            _body = {
                "AppKey": self.app_key,
                "AppScope": "trapi",
                "ApiVersion": "1",
                "LibraryName": "RDP Python Library",
                "LibraryVersion": __version__
            }

            _headers = {"Content-Type": "application/json"}

            try:
                response = await self.http_request_async(url=url,
                                                         method="POST",
                                                         headers=_headers,
                                                         json=_body,
                                                         timeout=timeout)

                # response = await self._http_session.post(url,
                #                                          headers=_headers,
                #                                          json=_body,
                #                                          timeout=timeout)
                self.log(logging.INFO, f"Response : {response.status_code} - {response.text}")
            except Exception as e:
                self.log(1, f'HTTP request failed: {e!r}')
                response = requests.models.Response()
                response.url = url
                response.request = _prepared_request
                response.code = type(e).__name__
                if hasattr(e, "message"):
                    response._content = e.message
                    response.reason = e.message
                else:
                    response._content = str(e)
                    response.reason = str(e)
                response.status_code = -1
                return False

            if response.status_code is requests_async_codes.ok:
                result = response.json()
                self._access_token = result.get("access_token")
            else:
                self.log(logging.DEBUG, f"Response {response.status_code} on handshake port {port} : {response.text}")

            return True
        except (socket.timeout, ConnectTimeout):
            self.log(logging.ERROR, f"Timeout on handshake port {port}")
        except Exception as e:
            self.log(logging.ERROR, f"Error on handshake port {port} : {e!r}")
        return False
