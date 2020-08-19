
try:
    from abc import abstractmethod, ABC
    import sys

except Exception as e:
    from abc import ABCMeta, abstractmethod
    import sys

if sys.version_info[0] < 3:

    class Token:

        """
        The class to verify and set token to the APIHTTPConnector instance, to authenticate requests.
        """

        __metaclass__ = ABCMeta


        @abstractmethod
        def authenticate(self, url_connection):

            try:
                from zcrmsdk.src.com.zoho.crm.api.util import APIHTTPConnector
            except Exception:
                from ...crm.api.util import APIHTTPConnector

            """
            This method to set token to APIHTTPConnector instance

            Parameters:
                url_connection (APIHTTPConnector) : A APIHTTPConnector class instance.
            """

            pass

else:

    class Token(ABC):

        """
        The class to verify and set token to the APIHTTPConnector instance, to authenticate requests.
        """

        @abstractmethod
        def authenticate(self, url_connection):

            try:
                from zcrmsdk.src.com.zoho.crm.api.util import APIHTTPConnector
            except Exception:
                from ...crm.api.util import APIHTTPConnector

            """
            This method to set token to APIHTTPConnector instance

            Parameters:
                url_connection (APIHTTPConnector) : A APIHTTPConnector class instance.
            """

            pass
