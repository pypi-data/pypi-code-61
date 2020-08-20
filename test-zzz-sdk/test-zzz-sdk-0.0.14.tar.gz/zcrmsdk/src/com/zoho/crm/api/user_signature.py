try:
    import logging
    import re
    import traceback
    from zcrmsdk.src.com.zoho.api.exception.sdk_exception import SDKException
    from zcrmsdk.src.com.zoho.crm.api.util.constants import Constants

except Exception:
    import logging
    import re
    import traceback
    from ...api.exception.sdk_exception import SDKException
    from .util.constants import Constants


class UserSignature(object):

    """
    The class representing the CRM user email.
    """

    logger = logging.getLogger('SDKLogger')

    regex = Constants.EMAIL_REGEX

    def __init__(self, email):

        """
        Creates an UserSignature class instance with the specified user email.

        Parameters:
            email (str) : A string containing the CRM user email
        """

        error = {}

        if re.search(UserSignature.regex, email) is None:
            error[Constants.FIELD] = Constants.EMAIL
            error[Constants.EXPECTED_TYPE] = Constants.EMAIL

            raise SDKException(Constants.USER_ERROR, None, details=error, cause=traceback.format_stack(limit=6))

        self.email = email
