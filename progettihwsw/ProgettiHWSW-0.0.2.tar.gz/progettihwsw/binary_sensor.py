"""Control binary sensor instances."""

from ProgettiHWSW.ProgettiHWSWAPI import ProgettiHWSWAPI
from ProgettiHWSW.input import Input

from homeassistant.components.binary_sensor import PLATFORM_SCHEMA, BinarySensorEntity

from . import setup_input
from .const import CONFIG_HOST_ENTRY, CONFIG_INPUTS_ENTRY, SENSOR_PLATFORM_SCHEMA

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(SENSOR_PLATFORM_SCHEMA)


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set the progettihwsw platform up and create sensor instances."""
    binary_sensors = []
    inputs = config[CONFIG_INPUTS_ENTRY]
    host = config[CONFIG_HOST_ENTRY]
    api_instance = ProgettiHWSWAPI(host)

    for input_number, input_name in inputs.items():
        binary_sensors.append(
            ProgettihwswBinarySensor(
                hass, input_name, setup_input(api_instance, int(input_number))
            )
        )
    add_entities(binary_sensors, True)


class ProgettihwswBinarySensor(BinarySensorEntity):
    """Represent a binary sensor."""

    def __init__(self, hass, name, sensor: Input):
        """Set initializing values."""
        self._name = name
        self._sensor = sensor
        self._state = None

    def added_to_hass(self):
        """Run this function when entity is added to HASS."""

        def setup_entity():
            """Set up sensor entity when HA starts up."""
            self._sensor.update()
            self._state = self._sensor.is_on
            self.schedule_update_ha_state(True)

        self.hass.add_executor_job(setup_entity)

    @property
    def should_poll(self):
        """Poll for new switch state."""
        return True

    @property
    def name(self):
        """Return the sensor name."""
        return self._name

    @property
    def is_on(self):
        """Get sensor state."""
        return self._state

    def update(self):
        """Update the state of binary sensor."""
        self._sensor.update()
        self._state = self._sensor.is_on
        return True
