'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._2118 import BoostPressureInputOptions
    from ._2119 import InputPowerInputOptions
    from ._2120 import PressureRatioInputOptions
    from ._2121 import RotorSetDataInputFileOptions
    from ._2122 import RotorSetMeasuredPoint
    from ._2123 import RotorSpeedInputOptions
    from ._2124 import SuperchargerMap
    from ._2125 import SuperchargerMaps
    from ._2126 import SuperchargerRotorSet
    from ._2127 import SuperchargerRotorSetDatabase
    from ._2128 import YVariableForImportedData
