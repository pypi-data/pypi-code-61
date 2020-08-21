'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._1915 import ClutchConnection
    from ._1916 import ClutchSocket
    from ._1917 import ConceptCouplingConnection
    from ._1918 import ConceptCouplingSocket
    from ._1919 import CouplingConnection
    from ._1920 import CouplingSocket
    from ._1921 import PartToPartShearCouplingConnection
    from ._1922 import PartToPartShearCouplingSocket
    from ._1923 import SpringDamperConnection
    from ._1924 import SpringDamperSocket
    from ._1925 import TorqueConverterConnection
    from ._1926 import TorqueConverterPumpSocket
    from ._1927 import TorqueConverterTurbineSocket
