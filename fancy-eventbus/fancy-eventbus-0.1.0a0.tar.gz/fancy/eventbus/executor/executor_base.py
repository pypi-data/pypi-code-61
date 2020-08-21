from abc import ABC, abstractmethod

from fancy.eventbus import EventListener


class ExecutorBase(ABC):
    @abstractmethod
    def execute(self, event_listener: EventListener) -> bool:
        pass
