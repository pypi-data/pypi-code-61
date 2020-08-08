"""
This module is home to the RuntimeReport class
"""
from pyecobee.ecobee_object import EcobeeObject


class RuntimeReport(EcobeeObject):
    """
    This class has been auto generated by scraping
    https://www.ecobee.com/home/developer/api/documentation/v1/objects/RuntimeReport.shtml

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

    __slots__ = ['_thermostat_identifier', '_row_count', '_row_list']

    attribute_name_map = {
        'thermostat_identifier': 'thermostatIdentifier',
        'thermostatIdentifier': 'thermostat_identifier',
        'row_count': 'rowCount',
        'rowCount': 'row_count',
        'row_list': 'rowList',
        'rowList': 'row_list',
    }

    attribute_type_map = {
        'thermostat_identifier': 'six.text_type',
        'row_count': 'int',
        'row_list': 'List[six.text_type]',
    }

    def __init__(self, thermostat_identifier=None, row_count=None, row_list=None):
        """
        Construct a RuntimeReport instance
        """
        self._thermostat_identifier = thermostat_identifier
        self._row_count = row_count
        self._row_list = row_list

    @property
    def thermostat_identifier(self):
        """
        Gets the thermostat_identifier attribute of this RuntimeReport
        instance.

        :return: The value of the thermostat_identifier attribute of
        this RuntimeReport instance.
        :rtype: six.text_type
        """

        return self._thermostat_identifier

    @property
    def row_count(self):
        """
        Gets the row_count attribute of this RuntimeReport instance.

        :return: The value of the row_count attribute of this
        RuntimeReport instance.
        :rtype: int
        """

        return self._row_count

    @property
    def row_list(self):
        """
        Gets the row_list attribute of this RuntimeReport instance.

        :return: The value of the row_list attribute of this
        RuntimeReport instance.
        :rtype: List[six.text_type]
        """

        return self._row_list
