from abc import ABC, abstractmethod


class Prioritiable(ABC):
    """
    higher number is present higher priority
    """
    @abstractmethod
    def get_priority(self) -> int:
        pass

    @abstractmethod
    def set_priority(self, value: int):
        pass
