
class Header(object):

    """
    This class represents the HTTP header name and class name.
    """

    def __init__(self, name, class_name=None):

        """
        Creates an Header class instance with the following parameters

        Parameters:
            name (str) : A string containing the header name.
            class_name (str) : A string containing the header class name.
        """

        self.name = name
        self.class_name = class_name
