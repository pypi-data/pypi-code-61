from fancy.eventbus import EventListener
from fancy.eventbus.executor import ExecutorBase


class MainExecutorBase(ExecutorBase):
    def execute(self, event_listener: EventListener) -> bool:
        return event_listener(event_listener.event)
