
try:
    from abc import ABC, abstractmethod
    import sys
    from zcrmsdk.src.com.zoho.crm.api import UserSignature
    from zcrmsdk.src.com.zoho.api.authenticator import Token

except Exception as e:
    from abc import ABCMeta, abstractmethod
    import sys
    from ....crm.api.user_signature import UserSignature
    from ..token import Token

if sys.version > '3':

    class TokenStore(ABC):

        """
        This class is to store user token details.
        """

        @abstractmethod
        def get_token(self, user, token):

            """
            The method to get user token details.

            Parameters:
                user (UserSignature) : A UserSignature class instance.
                token (Token) : A Token class instance.

            Returns:
                Token : A Token class instance representing the user token details.
            """

            pass

        @abstractmethod
        def save_token(self, user, token):

            """
            The method to store user token details.

            Parameters:
                user (UserSignature) : A UserSignature class instance.
                token (Token) : A Token class instance.

            Returns:
                Token : A Token class instance representing the user token details.
            """

            pass

        @abstractmethod
        def delete_token(self, user, token):

            """
            The method to delete user token details.

            Parameters:
                user (UserSignature) : A UserSignature class instance.
                token (Token) : A Token class instance.

            Returns:
                Token : A Token class instance representing the user token details.
            """

            pass

else:

    class TokenStore:

        """
        This class is to store user token details.
        """

        __metaclass__ = ABCMeta

        @abstractmethod
        def get_token(self, user, token):

            """
            The method to get user token details.

            Parameters:
                user (UserSignature) : A UserSignature class instance.
                token (Token) : A Token class instance.

            Returns:
                Token : A Token class instance representing the user token details.
            """

            pass

        @abstractmethod
        def save_token(self, user, token):

            """
            The method to store user token details.

            Parameters:
                user (UserSignature) : A UserSignature class instance.
                token (Token) : A Token class instance.

            Returns:
                Token : A Token class instance representing the user token details.
            """

            pass

        @abstractmethod
        def delete_token(self, user, token):

            """
            The method to delete user token details.

            Parameters:
                user (UserSignature) : A UserSignature class instance.
                token (Token) : A Token class instance.

            Returns:
                Token : A Token class instance representing the user token details.
            """

            pass
