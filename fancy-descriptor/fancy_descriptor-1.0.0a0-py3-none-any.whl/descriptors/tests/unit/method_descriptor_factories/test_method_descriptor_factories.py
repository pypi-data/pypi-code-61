from fancy.descriptors.method_descriptor_base import SimpleMethodDescriptor
from fancy.descriptors.method_descriptor_factories import SimpleMethodDescriptorFactory


class TestMethodDescriptorFactories:

    def test_create(self):
        assert isinstance(SimpleMethodDescriptorFactory().create(lambda x: x), SimpleMethodDescriptor)
