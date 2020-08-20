from abc import ABC, abstractmethod
from typing import Callable

from fancy.descriptors.method_descriptor_base import MethodDescriptorBase
from fancy.descriptors.patterns import Singleton


class MethodDescriptorFactoryBase(ABC, Singleton):

    @abstractmethod
    def create(self, method: Callable) -> MethodDescriptorBase:
        pass
