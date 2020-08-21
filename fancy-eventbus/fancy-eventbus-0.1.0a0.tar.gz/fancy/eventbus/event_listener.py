import inspect
from typing import Callable, Optional, TYPE_CHECKING, get_type_hints

import fancy.descriptor as fd

from fancy.eventbus.scheduler import Prioritiable

if TYPE_CHECKING:
    from fancy.eventbus.executor import ExecutorBase


class EventListener(fd.MethodDescriptor, Prioritiable):
    _priority: int
    _event: Optional[object]
    _executor: 'ExecutorBase'
    _event_type: type = None

    def __init__(
            self,
            method: Callable,
            priority: int,
            executor: 'ExecutorBase',
            factory=None
    ):
        super().__init__(method, factory)
        self._priority = priority
        self._executor = executor
        annotations = list(inspect.signature(method).parameters.values())
        if len(annotations) != 2:
            raise TypeError(f"method inside {self.__class__.__name__} needs exactly one argument.")

    def execute(self) -> bool:
        result = self._executor.execute(self)
        return result is None or result is True

    @property
    def event(self) -> Optional[object]:
        return self._event

    @event.setter
    def event(self, value: object) -> None:
        self._event = value

    @property
    def event_type(self) -> type:
        # delay because forward-references maybe not defined before classes loaded completely
        if self._event_type is None:
            self._event_type = list(get_type_hints(self.get_method()).values())[0]
        return self._event_type

    def get_priority(self) -> int:
        return self._priority

    def set_priority(self, value: int) -> None:
        self._priority = value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.get_priority() == other.get_priority() and \
            self.event is other.event and \
            self._executor is other._executor and \
            self.true_instance is self.true_instance
