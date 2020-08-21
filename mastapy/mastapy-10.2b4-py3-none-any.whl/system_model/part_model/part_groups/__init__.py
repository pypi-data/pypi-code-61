'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._2050 import ConcentricOrParallelPartGroup
    from ._2051 import ConcentricPartGroup
    from ._2052 import ConcentricPartGroupParallelToThis
    from ._2053 import DesignMeasurements
    from ._2054 import ParallelPartGroup
    from ._2055 import PartGroup
