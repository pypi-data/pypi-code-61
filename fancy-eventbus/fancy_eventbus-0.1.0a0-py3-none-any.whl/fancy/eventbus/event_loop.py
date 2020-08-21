from fancy.eventbus import EventBus, EventListener
from fancy.eventbus.events import StartEvent
from fancy.eventbus.execeptions import FancyEventBusException
from fancy.eventbus.scheduler import SchedulerBase


class EventLoop:
    _bus: EventBus
    _scheduler: SchedulerBase[EventListener]

    def __init__(self, bus: EventBus = None):
        if bus is None:
            bus = EventBus.get_default()
        self._bus = bus
        self._scheduler = bus.scheduler

    @property
    def bus(self) -> EventBus:
        return self._bus

    @property
    def scheduler(self) -> SchedulerBase:
        return self._scheduler

    def start(self) -> None:
        self._bus.post(StartEvent(self))
        while self._scheduler.has_next():
            try:
                listener = self._scheduler.next()
                should_cancel = not listener.execute()
                if should_cancel:
                    self._bus.cancel(listener.event)
            except FancyEventBusException as e:
                if e.should_shutdown_immediately():
                    break
                self._bus.post(e)
            except Exception as e:
                if not self._bus.post(e):
                    raise e
