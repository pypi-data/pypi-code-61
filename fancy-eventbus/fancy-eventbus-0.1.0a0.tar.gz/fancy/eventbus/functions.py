from fancy.eventbus import EventBus

"""
Provide some convenient functions
"""

default_bus = EventBus.get_default()

__slot__ = [
    'post', 'cancel', 'register', 'unregister'
]


def post(event: object, bus: EventBus = default_bus):
    bus.post(event)


def cancel(event: object, bus: EventBus = default_bus):
    bus.cancel(event)


def register(event_listeners: object, bus: EventBus = default_bus):
    return bus.register(event_listeners)


def unregister(event_listeners: object, bus: EventBus = default_bus):
    return bus.unregister(event_listeners)
