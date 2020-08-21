'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._1481 import ContactPairReporting
    from ._1482 import CoordinateSystemReporting
    from ._1483 import DegreeOfFreedomType
    from ._1484 import ElasticModulusOrthotropicComponents
    from ._1485 import ElementPropertiesBase
    from ._1486 import ElementPropertiesBeam
    from ._1487 import ElementPropertiesInterface
    from ._1488 import ElementPropertiesMass
    from ._1489 import ElementPropertiesRigid
    from ._1490 import ElementPropertiesShell
    from ._1491 import ElementPropertiesSolid
    from ._1492 import ElementPropertiesSpringDashpot
    from ._1493 import ElementPropertiesWithMaterial
    from ._1494 import MaterialPropertiesReporting
    from ._1495 import PoissonRatioOrthotropicComponents
    from ._1496 import RigidElementNodeDegreesOfFreedom
    from ._1497 import ShearModulusOrthotropicComponents
    from ._1498 import ThermalExpansionOrthotropicComponents
