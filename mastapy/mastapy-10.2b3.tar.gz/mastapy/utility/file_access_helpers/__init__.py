'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._1340 import ColumnTitle
    from ._1341 import TextFileDelimiterOptions
