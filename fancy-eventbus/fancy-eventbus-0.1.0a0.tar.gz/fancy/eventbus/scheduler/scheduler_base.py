from abc import ABC, abstractmethod
from typing import TypeVar, Generic


T = TypeVar("T")


class SchedulerBase(ABC, Generic[T]):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> T:
        pass

    @abstractmethod
    def add(self, item: T) -> None:
        pass

    @abstractmethod
    def remove(self, item: T) -> None:
        pass
