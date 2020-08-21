

class Api(object):
    """TBD
    Args
    ----
    - address (str): The address of the traffic generator
    """
    def __init__(self, address):
        raise NotImplementedError

    def set_state(self, content):
        """TBD
        """
        raise NotImplementedError

    def get_state(self, content):
        """TBD
        """
        raise NotImplementedError
