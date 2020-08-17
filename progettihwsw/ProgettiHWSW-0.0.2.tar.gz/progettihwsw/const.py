"""Define constant variables for general usage."""

import voluptuous as vol

from homeassistant.helpers import config_validation as cv

DEFAULT_SWITCH_NAME = "Unnamed Relay"
DEFAULT_SWITCH_MODE = "bistable"

DEFAULT_POLLING_INTERVAL_SEC = 5

CONFIG_HOST_ENTRY = "host"
CONFIG_INPUTS_ENTRY = "inputs"
CONFIG_SWITCH_OUTPUTS_ENTRY = "outputs"
CONFIG_SWITCH_NAME_ENTRY = "name"
CONFIG_SWITCH_MODE_ENTRY = "mode"

SWITCH_PORT_SCHEMA = vol.Schema(
    {
        vol.Optional(CONFIG_SWITCH_NAME_ENTRY, default=DEFAULT_SWITCH_NAME): cv.string,
        vol.Optional(CONFIG_SWITCH_MODE_ENTRY, default=DEFAULT_SWITCH_MODE): cv.string,
    }
)

SWITCHES_SCHEMA = vol.Schema({cv.positive_int: SWITCH_PORT_SCHEMA})

SWITCH_PLATFORM_SCHEMA = {
    vol.Required(CONFIG_HOST_ENTRY): cv.string,
    vol.Required(CONFIG_SWITCH_OUTPUTS_ENTRY): SWITCHES_SCHEMA,
}

SENSORS_SCHEMA = vol.Schema({cv.positive_int: cv.string})

SENSOR_PLATFORM_SCHEMA = {
    vol.Required(CONFIG_HOST_ENTRY): cv.string,
    vol.Required(CONFIG_INPUTS_ENTRY): SENSORS_SCHEMA,
}
