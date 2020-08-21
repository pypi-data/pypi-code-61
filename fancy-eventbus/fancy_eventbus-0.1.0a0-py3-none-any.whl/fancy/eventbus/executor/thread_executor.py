from threading import Thread

from fancy.eventbus import EventListener
from fancy.eventbus.executor import ExecutorBase


class ThreadExecutorBase(ExecutorBase):
    def execute(self, event_listener: EventListener) -> bool:
        Thread(target=event_listener, args=(event_listener.event,), daemon=True).start()
        return True
