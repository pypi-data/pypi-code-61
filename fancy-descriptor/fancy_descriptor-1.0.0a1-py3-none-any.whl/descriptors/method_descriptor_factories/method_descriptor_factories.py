from typing import Callable

from fancy.descriptors.method_descriptor_factories import MethodDescriptorFactoryBase
from fancy.descriptors.method_descriptor_base import MethodDescriptorBase, SimpleMethodDescriptor


class SimpleMethodDescriptorFactory(MethodDescriptorFactoryBase):
    def create(self, method: Callable) -> MethodDescriptorBase:
        return SimpleMethodDescriptor(method)


class MethodDescriptorFactories:
    simple = SimpleMethodDescriptorFactory()
