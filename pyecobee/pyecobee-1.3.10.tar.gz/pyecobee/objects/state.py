"""
This module is home to the State class
"""
from pyecobee.ecobee_object import EcobeeObject


class State(EcobeeObject):
    """
    This class has been auto generated by scraping
    https://www.ecobee.com/home/developer/api/documentation/v1/objects/State.shtml

    Attribute names have been generated by converting ecobee property
    names from camelCase to snake_case.

    A getter property has been generated for each attribute.
    A setter property has been generated for each attribute whose value
    of READONLY is "no".

    An __init__ argument without a default value has been generated if
    the value of REQUIRED is "yes".
    An __init__ argument with a default value of None has been generated
    if the value of REQUIRED is "no".
    """

    __slots__ = ['_max_value', '_min_value', '_type', '_actions']

    attribute_name_map = {
        'max_value': 'maxValue',
        'maxValue': 'max_value',
        'min_value': 'minValue',
        'minValue': 'min_value',
        'type': 'type',
        'actions': 'actions',
    }

    attribute_type_map = {
        'max_value': 'int',
        'min_value': 'int',
        'type': 'six.text_type',
        'actions': 'List[Action]',
    }

    def __init__(self, max_value=None, min_value=None, type_=None, actions=None):
        """
        Construct a State instance
        """
        self._max_value = max_value
        self._min_value = min_value
        self._type = type_
        self._actions = actions

    @property
    def max_value(self):
        """
        Gets the max_value attribute of this State instance.

        :return: The value of the max_value attribute of this State
        instance.
        :rtype: int
        """

        return self._max_value

    @property
    def min_value(self):
        """
        Gets the min_value attribute of this State instance.

        :return: The value of the min_value attribute of this State
        instance.
        :rtype: int
        """

        return self._min_value

    @property
    def type(self):
        """
        Gets the type attribute of this State instance.

        :return: The value of the type attribute of this State instance.
        :rtype: six.text_type
        """

        return self._type

    @property
    def actions(self):
        """
        Gets the actions attribute of this State instance.

        :return: The value of the actions attribute of this State
        instance.
        :rtype: List[Action]
        """

        return self._actions
