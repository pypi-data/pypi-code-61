from typing import Dict, List

from fancy.eventbus import EventListener, EventScheduler
from fancy.eventbus.scheduler import SchedulerBase


class EventBus:
    _scheduler: SchedulerBase[EventListener]
    event_listener_map: Dict[type, List[EventListener]]

    default_bus: 'EventBus' = None

    @classmethod
    def get_default(cls) -> 'EventBus':
        if cls.default_bus is None:
            cls.default_bus = EventBus(EventScheduler.MULTILEVEL_FEEDBACK_QUEUE)
        return cls.default_bus

    def __init__(self, scheduler: SchedulerBase):
        self._scheduler = scheduler
        self.event_listener_map = {}

    def post(self, event: object) -> bool:
        """

        :param event:
        :return: Is the event has been handled by at least one listener
        """
        posted = False
        for event_type in self.event_listener_map.keys():
            if isinstance(event, event_type):
                posted = True
                self._post_listeners(event, self.event_listener_map[event_type])
        return posted

    def _post_listeners(self, event: object, listeners: List[EventListener]) -> None:
        for listener in listeners:
            listener = listener.clone()
            listener.event = event
            self._scheduler.add(listener)

    def cancel(self, event: object) -> bool:
        canceled = False
        for event_type in self.event_listener_map.keys():
            if isinstance(event, event_type):
                canceled = True
                self._cancel_listeners(event, self.event_listener_map[event_type])
        return canceled

    def _cancel_listeners(self, event: object, listeners: List[EventListener]):
        for listener in listeners:
            listener.event = event
            try:
                self._scheduler.remove(listener)
            except ValueError as _:
                pass

    def register(self, event_listeners: object) -> None:
        listeners: List[EventListener] = EventListener.get_marked_method(event_listeners).values()

        for listener in listeners:
            if listener.event_type not in self.event_listener_map:
                self.event_listener_map[listener.event_type] = [listener]
            else:
                self.event_listener_map[listener.event_type].append(listener)

    def unregister(self, event_listeners: object) -> None:
        listeners: List[EventListener] = EventListener.get_marked_method(event_listeners).values()

        for listener in listeners:
            if listener.event_type not in self.event_listener_map:
                raise ValueError(f"{EventBus.__name__}.unregister(item): item not in {EventBus.__name__}")
            self.event_listener_map[listener.event_type].remove(listener)

    def clear(self) -> None:
        self.event_listener_map = {}

    @property
    def scheduler(self) -> SchedulerBase[EventListener]:
        return self._scheduler
