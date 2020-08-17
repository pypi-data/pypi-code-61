"""Control switches."""

from datetime import timedelta

from ProgettiHWSW.ProgettiHWSWAPI import ProgettiHWSWAPI
from ProgettiHWSW.relay import Relay

from homeassistant.components.switch import PLATFORM_SCHEMA, SwitchEntity

from . import setup_switch
from .const import (
    CONFIG_HOST_ENTRY,
    CONFIG_SWITCH_OUTPUTS_ENTRY,
    DEFAULT_POLLING_INTERVAL_SEC,
    SWITCH_PLATFORM_SCHEMA,
)

SCAN_INTERVAL = timedelta(seconds=DEFAULT_POLLING_INTERVAL_SEC)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(SWITCH_PLATFORM_SCHEMA)


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set the switch platform up."""
    switches = []
    outputs = config[CONFIG_SWITCH_OUTPUTS_ENTRY]
    host = config[CONFIG_HOST_ENTRY]
    api_instance = ProgettiHWSWAPI(host)

    for switch_number, switch_details in outputs.items():
        switches.append(
            ProgettihwswSwitch(
                hass,
                switch_details["name"],
                setup_switch(api_instance, int(switch_number), switch_details["mode"]),
            )
        )
    add_entities(switches, True)


class ProgettihwswSwitch(SwitchEntity):
    """Represent a switch entity."""

    def __init__(self, hass, name, switch: Relay):
        """Initialize the values."""
        self._switch = switch
        self._name = name
        self._state = None

    def added_to_hass(self):
        """Run this function when entity is added to HASS."""

        def setup_entity():
            """Set switch entity up when HA starts."""
            self._switch.update()
            self._state = self._switch.is_on
            self.schedule_update_ha_state(True)

        self.hass.add_executor_job(setup_entity)

    def turn_on(self, **kwargs):
        """Turn the switch on."""
        return self._switch.control(True)

    def turn_off(self, **kwargs):
        """Turn the switch off."""
        return self._switch.control(False)

    def toggle(self, **kwargs):
        """Toggle the state of switch."""
        return self._switch.toggle()

    @property
    def name(self):
        """Return the switch name."""
        return self._name

    @property
    def is_on(self):
        """Get switch state."""
        return self._state

    @property
    def should_poll(self):
        """Poll for new switch state."""
        return True

    def update(self):
        """Update the state of switch."""
        self._switch.update()
        self._state = self._switch.is_on
        return True
