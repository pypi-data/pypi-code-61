'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._1024 import KeyedJointDesign
    from ._1025 import KeyTypes
    from ._1026 import KeywayJointHalfDesign
    from ._1027 import NumberOfKeys
