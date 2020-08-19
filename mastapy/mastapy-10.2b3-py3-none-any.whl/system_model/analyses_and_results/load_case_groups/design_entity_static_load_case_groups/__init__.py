'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._5270 import AbstractAssemblyStaticLoadCaseGroup
    from ._5271 import ComponentStaticLoadCaseGroup
    from ._5272 import ConnectionStaticLoadCaseGroup
    from ._5273 import DesignEntityStaticLoadCaseGroup
    from ._5274 import GearSetStaticLoadCaseGroup
    from ._5275 import PartStaticLoadCaseGroup
