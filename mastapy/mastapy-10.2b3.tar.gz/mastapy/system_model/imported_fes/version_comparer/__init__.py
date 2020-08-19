'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._1996 import DesignResults
    from ._1997 import ImportedFEResults
    from ._1998 import ImportedFEVersionComparer
    from ._1999 import LoadCaseResults
    from ._2000 import LoadCasesToRun
    from ._2001 import NodeComparisonResult
