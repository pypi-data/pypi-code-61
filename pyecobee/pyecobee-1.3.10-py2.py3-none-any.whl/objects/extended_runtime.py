"""
This module is home to the ExtendedRuntime class
"""
from pyecobee.ecobee_object import EcobeeObject


class ExtendedRuntime(EcobeeObject):
    """
    This class has been auto generated by scraping
    https://www.ecobee.com/home/developer/api/documentation/v1/objects/ExtendedRuntime.shtml

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

    __slots__ = [
        '_last_reading_timestamp',
        '_runtime_date',
        '_runtime_interval',
        '_actual_temperature',
        '_actual_humidity',
        '_desired_heat',
        '_desired_cool',
        '_desired_humidity',
        '_desired_dehumidity',
        '_dm_offset',
        '_hvac_mode',
        '_heat_pump1',
        '_heat_pump2',
        '_aux_heat1',
        '_aux_heat2',
        '_aux_heat3',
        '_cool1',
        '_cool2',
        '_fan',
        '_humidifier',
        '_dehumidifier',
        '_economizer',
        '_ventilator',
        '_current_electricity_bill',
        '_projected_electricity_bill',
    ]

    attribute_name_map = {
        'last_reading_timestamp': 'lastReadingTimestamp',
        'lastReadingTimestamp': 'last_reading_timestamp',
        'runtime_date': 'runtimeDate',
        'runtimeDate': 'runtime_date',
        'runtime_interval': 'runtimeInterval',
        'runtimeInterval': 'runtime_interval',
        'actual_temperature': 'actualTemperature',
        'actualTemperature': 'actual_temperature',
        'actual_humidity': 'actualHumidity',
        'actualHumidity': 'actual_humidity',
        'desired_heat': 'desiredHeat',
        'desiredHeat': 'desired_heat',
        'desired_cool': 'desiredCool',
        'desiredCool': 'desired_cool',
        'desired_humidity': 'desiredHumidity',
        'desiredHumidity': 'desired_humidity',
        'desired_dehumidity': 'desiredDehumidity',
        'desiredDehumidity': 'desired_dehumidity',
        'dm_offset': 'dmOffset',
        'dmOffset': 'dm_offset',
        'hvac_mode': 'hvacMode',
        'hvacMode': 'hvac_mode',
        'heat_pump1': 'heatPump1',
        'heatPump1': 'heat_pump1',
        'heat_pump2': 'heatPump2',
        'heatPump2': 'heat_pump2',
        'aux_heat1': 'auxHeat1',
        'auxHeat1': 'aux_heat1',
        'aux_heat2': 'auxHeat2',
        'auxHeat2': 'aux_heat2',
        'aux_heat3': 'auxHeat3',
        'auxHeat3': 'aux_heat3',
        'cool1': 'cool1',
        'cool2': 'cool2',
        'fan': 'fan',
        'humidifier': 'humidifier',
        'dehumidifier': 'dehumidifier',
        'economizer': 'economizer',
        'ventilator': 'ventilator',
        'current_electricity_bill': 'currentElectricityBill',
        'currentElectricityBill': 'current_electricity_bill',
        'projected_electricity_bill': 'projectedElectricityBill',
        'projectedElectricityBill': 'projected_electricity_bill',
    }

    attribute_type_map = {
        'last_reading_timestamp': 'six.text_type',
        'runtime_date': 'six.text_type',
        'runtime_interval': 'int',
        'actual_temperature': 'List[int]',
        'actual_humidity': 'List[int]',
        'desired_heat': 'List[int]',
        'desired_cool': 'List[int]',
        'desired_humidity': 'List[int]',
        'desired_dehumidity': 'List[int]',
        'dm_offset': 'List[int]',
        'hvac_mode': 'List[six.text_type]',
        'heat_pump1': 'List[int]',
        'heat_pump2': 'List[int]',
        'aux_heat1': 'List[int]',
        'aux_heat2': 'List[int]',
        'aux_heat3': 'List[int]',
        'cool1': 'List[int]',
        'cool2': 'List[int]',
        'fan': 'List[int]',
        'humidifier': 'List[int]',
        'dehumidifier': 'List[int]',
        'economizer': 'List[int]',
        'ventilator': 'List[int]',
        'current_electricity_bill': 'int',
        'projected_electricity_bill': 'int',
    }

    def __init__(
        self,
        last_reading_timestamp=None,
        runtime_date=None,
        runtime_interval=None,
        actual_temperature=None,
        actual_humidity=None,
        desired_heat=None,
        desired_cool=None,
        desired_humidity=None,
        desired_dehumidity=None,
        dm_offset=None,
        hvac_mode=None,
        heat_pump1=None,
        heat_pump2=None,
        aux_heat1=None,
        aux_heat2=None,
        aux_heat3=None,
        cool1=None,
        cool2=None,
        fan=None,
        humidifier=None,
        dehumidifier=None,
        economizer=None,
        ventilator=None,
        current_electricity_bill=None,
        projected_electricity_bill=None,
    ):
        """
        Construct an ExtendedRuntime instance
        """
        self._last_reading_timestamp = last_reading_timestamp
        self._runtime_date = runtime_date
        self._runtime_interval = runtime_interval
        self._actual_temperature = actual_temperature
        self._actual_humidity = actual_humidity
        self._desired_heat = desired_heat
        self._desired_cool = desired_cool
        self._desired_humidity = desired_humidity
        self._desired_dehumidity = desired_dehumidity
        self._dm_offset = dm_offset
        self._hvac_mode = hvac_mode
        self._heat_pump1 = heat_pump1
        self._heat_pump2 = heat_pump2
        self._aux_heat1 = aux_heat1
        self._aux_heat2 = aux_heat2
        self._aux_heat3 = aux_heat3
        self._cool1 = cool1
        self._cool2 = cool2
        self._fan = fan
        self._humidifier = humidifier
        self._dehumidifier = dehumidifier
        self._economizer = economizer
        self._ventilator = ventilator
        self._current_electricity_bill = current_electricity_bill
        self._projected_electricity_bill = projected_electricity_bill

    @property
    def last_reading_timestamp(self):
        """
        Gets the last_reading_timestamp attribute of this
        ExtendedRuntime instance.

        :return: The value of the last_reading_timestamp attribute of
        this ExtendedRuntime instance.
        :rtype: six.text_type
        """

        return self._last_reading_timestamp

    @property
    def runtime_date(self):
        """
        Gets the runtime_date attribute of this ExtendedRuntime
        instance.

        :return: The value of the runtime_date attribute of this
        ExtendedRuntime instance.
        :rtype: six.text_type
        """

        return self._runtime_date

    @property
    def runtime_interval(self):
        """
        Gets the runtime_interval attribute of this ExtendedRuntime
        instance.

        :return: The value of the runtime_interval attribute of this
        ExtendedRuntime instance.
        :rtype: int
        """

        return self._runtime_interval

    @property
    def actual_temperature(self):
        """
        Gets the actual_temperature attribute of this ExtendedRuntime
        instance.

        :return: The value of the actual_temperature attribute of this
        ExtendedRuntime instance.
        :rtype: List[int]
        """

        return self._actual_temperature

    @property
    def actual_humidity(self):
        """
        Gets the actual_humidity attribute of this ExtendedRuntime
        instance.

        :return: The value of the actual_humidity attribute of this
        ExtendedRuntime instance.
        :rtype: List[int]
        """

        return self._actual_humidity

    @property
    def desired_heat(self):
        """
        Gets the desired_heat attribute of this ExtendedRuntime
        instance.

        :return: The value of the desired_heat attribute of this
        ExtendedRuntime instance.
        :rtype: List[int]
        """

        return self._desired_heat

    @property
    def desired_cool(self):
        """
        Gets the desired_cool attribute of this ExtendedRuntime
        instance.

        :return: The value of the desired_cool attribute of this
        ExtendedRuntime instance.
        :rtype: List[int]
        """

        return self._desired_cool

    @property
    def desired_humidity(self):
        """
        Gets the desired_humidity attribute of this ExtendedRuntime
        instance.

        :return: The value of the desired_humidity attribute of this
        ExtendedRuntime instance.
        :rtype: List[int]
        """

        return self._desired_humidity

    @property
    def desired_dehumidity(self):
        """
        Gets the desired_dehumidity attribute of this ExtendedRuntime
        instance.

        :return: The value of the desired_dehumidity attribute of this
        ExtendedRuntime instance.
        :rtype: List[int]
        """

        return self._desired_dehumidity

    @property
    def dm_offset(self):
        """
        Gets the dm_offset attribute of this ExtendedRuntime instance.

        :return: The value of the dm_offset attribute of this
        ExtendedRuntime instance.
        :rtype: List[int]
        """

        return self._dm_offset

    @property
    def hvac_mode(self):
        """
        Gets the hvac_mode attribute of this ExtendedRuntime instance.

        :return: The value of the hvac_mode attribute of this
        ExtendedRuntime instance.
        :rtype: List[six.text_type]
        """

        return self._hvac_mode

    @property
    def heat_pump1(self):
        """
        Gets the heat_pump1 attribute of this ExtendedRuntime instance.

        :return: The value of the heat_pump1 attribute of this
        ExtendedRuntime instance.
        :rtype: List[int]
        """

        return self._heat_pump1

    @property
    def heat_pump2(self):
        """
        Gets the heat_pump2 attribute of this ExtendedRuntime instance.

        :return: The value of the heat_pump2 attribute of this
        ExtendedRuntime instance.
        :rtype: List[int]
        """

        return self._heat_pump2

    @property
    def aux_heat1(self):
        """
        Gets the aux_heat1 attribute of this ExtendedRuntime instance.

        :return: The value of the aux_heat1 attribute of this
        ExtendedRuntime instance.
        :rtype: List[int]
        """

        return self._aux_heat1

    @property
    def aux_heat2(self):
        """
        Gets the aux_heat2 attribute of this ExtendedRuntime instance.

        :return: The value of the aux_heat2 attribute of this
        ExtendedRuntime instance.
        :rtype: List[int]
        """

        return self._aux_heat2

    @property
    def aux_heat3(self):
        """
        Gets the aux_heat3 attribute of this ExtendedRuntime instance.

        :return: The value of the aux_heat3 attribute of this
        ExtendedRuntime instance.
        :rtype: List[int]
        """

        return self._aux_heat3

    @property
    def cool1(self):
        """
        Gets the cool1 attribute of this ExtendedRuntime instance.

        :return: The value of the cool1 attribute of this
        ExtendedRuntime instance.
        :rtype: List[int]
        """

        return self._cool1

    @property
    def cool2(self):
        """
        Gets the cool2 attribute of this ExtendedRuntime instance.

        :return: The value of the cool2 attribute of this
        ExtendedRuntime instance.
        :rtype: List[int]
        """

        return self._cool2

    @property
    def fan(self):
        """
        Gets the fan attribute of this ExtendedRuntime instance.

        :return: The value of the fan attribute of this ExtendedRuntime
        instance.
        :rtype: List[int]
        """

        return self._fan

    @property
    def humidifier(self):
        """
        Gets the humidifier attribute of this ExtendedRuntime instance.

        :return: The value of the humidifier attribute of this
        ExtendedRuntime instance.
        :rtype: List[int]
        """

        return self._humidifier

    @property
    def dehumidifier(self):
        """
        Gets the dehumidifier attribute of this ExtendedRuntime
        instance.

        :return: The value of the dehumidifier attribute of this
        ExtendedRuntime instance.
        :rtype: List[int]
        """

        return self._dehumidifier

    @property
    def economizer(self):
        """
        Gets the economizer attribute of this ExtendedRuntime instance.

        :return: The value of the economizer attribute of this
        ExtendedRuntime instance.
        :rtype: List[int]
        """

        return self._economizer

    @property
    def ventilator(self):
        """
        Gets the ventilator attribute of this ExtendedRuntime instance.

        :return: The value of the ventilator attribute of this
        ExtendedRuntime instance.
        :rtype: List[int]
        """

        return self._ventilator

    @property
    def current_electricity_bill(self):
        """
        Gets the current_electricity_bill attribute of this
        ExtendedRuntime instance.

        :return: The value of the current_electricity_bill attribute of
        this ExtendedRuntime instance.
        :rtype: int
        """

        return self._current_electricity_bill

    @property
    def projected_electricity_bill(self):
        """
        Gets the projected_electricity_bill attribute of this
        ExtendedRuntime instance.

        :return: The value of the projected_electricity_bill attribute
        of this ExtendedRuntime instance.
        :rtype: int
        """

        return self._projected_electricity_bill
