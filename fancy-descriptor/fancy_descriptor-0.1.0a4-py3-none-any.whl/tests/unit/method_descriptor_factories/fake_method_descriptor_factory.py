from typing import Callable
from unittest.mock import MagicMock

from fancy_descriptors.method_descriptor_base import MethodDescriptor
from fancy_descriptors.method_descriptor_factories import MethodDescriptorFactoryBase


class FakeMethodDescriptorFactory(MethodDescriptorFactoryBase, MagicMock):
    def create(self, method: Callable) -> MethodDescriptor:
        pass
