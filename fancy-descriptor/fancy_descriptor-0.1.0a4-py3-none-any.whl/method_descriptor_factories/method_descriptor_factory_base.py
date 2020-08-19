from abc import ABC, abstractmethod
from typing import Callable

from fancy_descriptors.method_descriptor_base import MethodDescriptorBase
from fancy_descriptors.patterns import Singleton


class MethodDescriptorFactoryBase(ABC, Singleton):

    @abstractmethod
    def create(self, method: Callable) -> MethodDescriptorBase:
        pass
