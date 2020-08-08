"""
This module is home to the ElectricityDevice class
"""
from pyecobee.ecobee_object import EcobeeObject


class ElectricityDevice(EcobeeObject):
    """
    This class has been auto generated by scraping
    https://www.ecobee.com/home/developer/api/documentation/v1/objects/ElectricityDevice.shtml

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

    __slots__ = ['_name', '_tiers', '_last_update', '_cost', '_consumption']

    attribute_name_map = {
        'name': 'name',
        'tiers': 'tiers',
        'last_update': 'lastUpdate',
        'lastUpdate': 'last_update',
        'cost': 'cost',
        'consumption': 'consumption',
    }

    attribute_type_map = {
        'name': 'six.text_type',
        'tiers': 'List[ElectricityTier]',
        'last_update': 'six.text_type',
        'cost': 'List[six.text_type]',
        'consumption': 'List[six.text_type]',
    }

    def __init__(
        self, name=None, tiers=None, last_update=None, cost=None, consumption=None
    ):
        """
        Construct an ElectricityDevice instance
        """
        self._name = name
        self._tiers = tiers
        self._last_update = last_update
        self._cost = cost
        self._consumption = consumption

    @property
    def name(self):
        """
        Gets the name attribute of this ElectricityDevice instance.

        :return: The value of the name attribute of this
        ElectricityDevice instance.
        :rtype: six.text_type
        """

        return self._name

    @property
    def tiers(self):
        """
        Gets the tiers attribute of this ElectricityDevice instance.

        :return: The value of the tiers attribute of this
        ElectricityDevice instance.
        :rtype: List[ElectricityTier]
        """

        return self._tiers

    @property
    def last_update(self):
        """
        Gets the last_update attribute of this ElectricityDevice
        instance.

        :return: The value of the last_update attribute of this
        ElectricityDevice instance.
        :rtype: six.text_type
        """

        return self._last_update

    @property
    def cost(self):
        """
        Gets the cost attribute of this ElectricityDevice instance.

        :return: The value of the cost attribute of this
        ElectricityDevice instance.
        :rtype: List[six.text_type]
        """

        return self._cost

    @property
    def consumption(self):
        """
        Gets the consumption attribute of this ElectricityDevice
        instance.

        :return: The value of the consumption attribute of this
        ElectricityDevice instance.
        :rtype: List[six.text_type]
        """

        return self._consumption
