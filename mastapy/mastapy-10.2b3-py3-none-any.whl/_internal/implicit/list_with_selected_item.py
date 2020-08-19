'''list_with_selected_item.py

Implementations of 'ListWithSelectedItem' in Python.
As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
'''


from typing import List, Generic, TypeVar

from mastapy._internal import mixins, constructor, conversion
from mastapy._internal.python_net import python_net_import
from mastapy.gears.ltca.cylindrical import _631, _630
from mastapy.gears.manufacturing.cylindrical import _410
from mastapy.gears.manufacturing.bevel import _576
from mastapy.utility import _1151
from mastapy.utility.units_and_measurements import _1161, _1156
from mastapy.utility.units_and_measurements.measurements import (
    _1163, _1164, _1165, _1166,
    _1167, _1168, _1169, _1170,
    _1171, _1172, _1173, _1174,
    _1175, _1176, _1177, _1178,
    _1179, _1180, _1181, _1182,
    _1183, _1184, _1185, _1186,
    _1187, _1188, _1189, _1190,
    _1191, _1192, _1193, _1194,
    _1195, _1196, _1197, _1198,
    _1199, _1200, _1201, _1202,
    _1203, _1204, _1205, _1206,
    _1207, _1208, _1209, _1210,
    _1211, _1212, _1213, _1214,
    _1215, _1216, _1217, _1218,
    _1219, _1220, _1221, _1222,
    _1223, _1224, _1225, _1226,
    _1227, _1228, _1229, _1230,
    _1231, _1232, _1233, _1234,
    _1235, _1236, _1237, _1238,
    _1239, _1240, _1241, _1242,
    _1243, _1244, _1245, _1246,
    _1247, _1248, _1249, _1250,
    _1251, _1252, _1253, _1254,
    _1255, _1256, _1257, _1258,
    _1259, _1260, _1261, _1262,
    _1263, _1264, _1265, _1266,
    _1267, _1268, _1269
)
from mastapy._internal.cast_exception import CastException
from mastapy.utility.file_access_helpers import _1340
from mastapy.system_model.part_model import (
    _2037, _2015, _2011, _2004,
    _2007, _2009, _2014, _2018,
    _2020, _2023, _2027, _2028,
    _2029, _2031, _2034, _2036,
    _2042, _2043
)
from mastapy.system_model.imported_fes import (
    _1928, _1958, _1959, _1960,
    _1962, _1963, _1964, _1965,
    _1966, _1967, _1968, _1980,
    _1991, _1992, _1969, _1957,
    _1946
)
from mastapy.system_model.part_model.shaft_model import _2046
from mastapy.system_model.part_model.gears import (
    _2076, _2078, _2080, _2081,
    _2082, _2084, _2086, _2088,
    _2090, _2091, _2093, _2097,
    _2099, _2101, _2103, _2106,
    _2108, _2110, _2112, _2113,
    _2114, _2116, _2089, _2095,
    _2077, _2079, _2083, _2085,
    _2087, _2092, _2098, _2100,
    _2102, _2104, _2105, _2107,
    _2109, _2111, _2115, _2117
)
from mastapy.system_model.part_model.couplings import (
    _2138, _2141, _2143, _2145,
    _2147, _2148, _2154, _2156,
    _2158, _2161, _2162, _2163,
    _2165, _2167
)
from mastapy.system_model.part_model.part_groups import _2051
from mastapy.gears.gear_designs import _716
from mastapy.gears.gear_designs.zerol_bevel import _720
from mastapy.gears.gear_designs.worm import _725
from mastapy.gears.gear_designs.straight_bevel_diff import _729
from mastapy.gears.gear_designs.straight_bevel import _733
from mastapy.gears.gear_designs.spiral_bevel import _737
from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _741
from mastapy.gears.gear_designs.klingelnberg_hypoid import _745
from mastapy.gears.gear_designs.klingelnberg_conical import _749
from mastapy.gears.gear_designs.hypoid import _753
from mastapy.gears.gear_designs.face import _761
from mastapy.gears.gear_designs.cylindrical import _787, _796
from mastapy.gears.gear_designs.conical import _893
from mastapy.gears.gear_designs.concept import _915
from mastapy.gears.gear_designs.bevel import _919
from mastapy.gears.gear_designs.agma_gleason_conical import _932
from mastapy.system_model.analyses_and_results.system_deflections import (
    _2281, _2282, _2283, _2284
)
from mastapy.system_model.analyses_and_results.load_case_groups import _5261, _5262
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5357
from mastapy.system_model.analyses_and_results.gear_whine_analyses.whine_analyses_results import _5432
from mastapy.system_model.analyses_and_results.static_loads import _6211

_LIST_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.Utility.Property', 'ListWithSelectedItem')


__docformat__ = 'restructuredtext en'
__all__ = (
    'ListWithSelectedItem_str', 'ListWithSelectedItem_T',
    'ListWithSelectedItem_CylindricalGearMeshLoadDistributionAnalysis', 'ListWithSelectedItem_CylindricalGearLoadDistributionAnalysis',
    'ListWithSelectedItem_CylindricalSetManufacturingConfig', 'ListWithSelectedItem_ConicalSetManufacturingConfig',
    'ListWithSelectedItem_SystemDirectory', 'ListWithSelectedItem_Unit',
    'ListWithSelectedItem_MeasurementBase', 'ListWithSelectedItem_int',
    'ListWithSelectedItem_ColumnTitle', 'ListWithSelectedItem_PowerLoad',
    'ListWithSelectedItem_ImportedFELink', 'ListWithSelectedItem_ImportedFEStiffnessNode',
    'ListWithSelectedItem_Datum', 'ListWithSelectedItem_Component',
    'ListWithSelectedItem_ImportedFE', 'ListWithSelectedItem_CylindricalGear',
    'ListWithSelectedItem_GuideDxfModel', 'ListWithSelectedItem_ConcentricPartGroup',
    'ListWithSelectedItem_GearSetDesign', 'ListWithSelectedItem_ShaftHubConnection',
    'ListWithSelectedItem_TSelectableItem', 'ListWithSelectedItem_CylindricalGearSystemDeflection',
    'ListWithSelectedItem_DesignState', 'ListWithSelectedItem_ImportedFEComponent',
    'ListWithSelectedItem_ImportedFEComponentGearWhineAnalysis', 'ListWithSelectedItem_ResultLocationSelectionGroup',
    'ListWithSelectedItem_StaticLoadCase', 'ListWithSelectedItem_DutyCycle',
    'ListWithSelectedItem_float', 'ListWithSelectedItem_ElectricMachineDataSet',
    'ListWithSelectedItem_CylindricalGearSet', 'ListWithSelectedItem_PointLoad',
    'ListWithSelectedItem_GearSet'
)


T = TypeVar('T')
TSelectableItem = TypeVar('TSelectableItem')


class ListWithSelectedItem_str(str, mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_str

    A specific implementation of 'ListWithSelectedItem' for 'str' types.
    '''

    __hash__ = None
    __qualname__ = 'str'

    def __new__(cls, instance_to_wrap: 'ListWithSelectedItem_str.TYPE'):
        return str.__new__(cls, instance_to_wrap.SelectedValue) if instance_to_wrap.SelectedValue else None

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_str.TYPE'):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.SelectedValue
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> 'str':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return str

    @property
    def selected_value(self) -> 'str':
        '''str: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.enclosing.SelectedValue

    @property
    def available_values(self) -> 'List[str]':
        '''List[str]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, str)
        return value


class ListWithSelectedItem_T(Generic[T], mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_T

    A specific implementation of 'ListWithSelectedItem' for 'T' types.
    '''

    __hash__ = None
    __qualname__ = 'T'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_T.TYPE'):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.SelectedValue
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> 'T':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return T

    @property
    def selected_value(self) -> 'T':
        '''T: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(T)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def available_values(self) -> 'List[T]':
        '''List[T]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, constructor.new(T))
        return value


class ListWithSelectedItem_CylindricalGearMeshLoadDistributionAnalysis(_631.CylindricalGearMeshLoadDistributionAnalysis, mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_CylindricalGearMeshLoadDistributionAnalysis

    A specific implementation of 'ListWithSelectedItem' for 'CylindricalGearMeshLoadDistributionAnalysis' types.
    '''

    __hash__ = None
    __qualname__ = 'CylindricalGearMeshLoadDistributionAnalysis'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CylindricalGearMeshLoadDistributionAnalysis.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_631.CylindricalGearMeshLoadDistributionAnalysis.TYPE':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _631.CylindricalGearMeshLoadDistributionAnalysis.TYPE

    @property
    def selected_value(self) -> '_631.CylindricalGearMeshLoadDistributionAnalysis':
        '''CylindricalGearMeshLoadDistributionAnalysis: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_631.CylindricalGearMeshLoadDistributionAnalysis)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def available_values(self) -> 'List[_631.CylindricalGearMeshLoadDistributionAnalysis]':
        '''List[CylindricalGearMeshLoadDistributionAnalysis]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, constructor.new(_631.CylindricalGearMeshLoadDistributionAnalysis))
        return value


class ListWithSelectedItem_CylindricalGearLoadDistributionAnalysis(_630.CylindricalGearLoadDistributionAnalysis, mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_CylindricalGearLoadDistributionAnalysis

    A specific implementation of 'ListWithSelectedItem' for 'CylindricalGearLoadDistributionAnalysis' types.
    '''

    __hash__ = None
    __qualname__ = 'CylindricalGearLoadDistributionAnalysis'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CylindricalGearLoadDistributionAnalysis.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_630.CylindricalGearLoadDistributionAnalysis.TYPE':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _630.CylindricalGearLoadDistributionAnalysis.TYPE

    @property
    def selected_value(self) -> '_630.CylindricalGearLoadDistributionAnalysis':
        '''CylindricalGearLoadDistributionAnalysis: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_630.CylindricalGearLoadDistributionAnalysis)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def available_values(self) -> 'List[_630.CylindricalGearLoadDistributionAnalysis]':
        '''List[CylindricalGearLoadDistributionAnalysis]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, constructor.new(_630.CylindricalGearLoadDistributionAnalysis))
        return value


class ListWithSelectedItem_CylindricalSetManufacturingConfig(_410.CylindricalSetManufacturingConfig, mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_CylindricalSetManufacturingConfig

    A specific implementation of 'ListWithSelectedItem' for 'CylindricalSetManufacturingConfig' types.
    '''

    __hash__ = None
    __qualname__ = 'CylindricalSetManufacturingConfig'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CylindricalSetManufacturingConfig.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_410.CylindricalSetManufacturingConfig.TYPE':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _410.CylindricalSetManufacturingConfig.TYPE

    @property
    def selected_value(self) -> '_410.CylindricalSetManufacturingConfig':
        '''CylindricalSetManufacturingConfig: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_410.CylindricalSetManufacturingConfig)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def available_values(self) -> 'List[_410.CylindricalSetManufacturingConfig]':
        '''List[CylindricalSetManufacturingConfig]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, constructor.new(_410.CylindricalSetManufacturingConfig))
        return value


class ListWithSelectedItem_ConicalSetManufacturingConfig(_576.ConicalSetManufacturingConfig, mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_ConicalSetManufacturingConfig

    A specific implementation of 'ListWithSelectedItem' for 'ConicalSetManufacturingConfig' types.
    '''

    __hash__ = None
    __qualname__ = 'ConicalSetManufacturingConfig'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ConicalSetManufacturingConfig.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_576.ConicalSetManufacturingConfig.TYPE':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _576.ConicalSetManufacturingConfig.TYPE

    @property
    def selected_value(self) -> '_576.ConicalSetManufacturingConfig':
        '''ConicalSetManufacturingConfig: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_576.ConicalSetManufacturingConfig)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def available_values(self) -> 'List[_576.ConicalSetManufacturingConfig]':
        '''List[ConicalSetManufacturingConfig]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, constructor.new(_576.ConicalSetManufacturingConfig))
        return value


class ListWithSelectedItem_SystemDirectory(_1151.SystemDirectory, mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_SystemDirectory

    A specific implementation of 'ListWithSelectedItem' for 'SystemDirectory' types.
    '''

    __hash__ = None
    __qualname__ = 'SystemDirectory'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_SystemDirectory.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1151.SystemDirectory.TYPE':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1151.SystemDirectory.TYPE

    @property
    def selected_value(self) -> '_1151.SystemDirectory':
        '''SystemDirectory: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1151.SystemDirectory)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def available_values(self) -> 'List[_1151.SystemDirectory]':
        '''List[SystemDirectory]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, constructor.new(_1151.SystemDirectory))
        return value


class ListWithSelectedItem_Unit(_1161.Unit, mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_Unit

    A specific implementation of 'ListWithSelectedItem' for 'Unit' types.
    '''

    __hash__ = None
    __qualname__ = 'Unit'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_Unit.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1161.Unit.TYPE':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1161.Unit.TYPE

    @property
    def selected_value(self) -> '_1161.Unit':
        '''Unit: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1161.Unit)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def available_values(self) -> 'List[_1161.Unit]':
        '''List[Unit]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, constructor.new(_1161.Unit))
        return value


class ListWithSelectedItem_MeasurementBase(_1156.MeasurementBase, mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_MeasurementBase

    A specific implementation of 'ListWithSelectedItem' for 'MeasurementBase' types.
    '''

    __hash__ = None
    __qualname__ = 'MeasurementBase'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_MeasurementBase.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1156.MeasurementBase.TYPE':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1156.MeasurementBase.TYPE

    @property
    def selected_value(self) -> '_1156.MeasurementBase':
        '''MeasurementBase: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1156.MeasurementBase)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_acceleration(self) -> '_1163.Acceleration':
        '''Acceleration: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1163.Acceleration.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Acceleration. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1163.Acceleration)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_angle(self) -> '_1164.Angle':
        '''Angle: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1164.Angle.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Angle. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1164.Angle)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_angle_per_unit_temperature(self) -> '_1165.AnglePerUnitTemperature':
        '''AnglePerUnitTemperature: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1165.AnglePerUnitTemperature.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AnglePerUnitTemperature. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1165.AnglePerUnitTemperature)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_angle_small(self) -> '_1166.AngleSmall':
        '''AngleSmall: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1166.AngleSmall.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AngleSmall. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1166.AngleSmall)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_angle_very_small(self) -> '_1167.AngleVerySmall':
        '''AngleVerySmall: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1167.AngleVerySmall.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AngleVerySmall. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1167.AngleVerySmall)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_angular_acceleration(self) -> '_1168.AngularAcceleration':
        '''AngularAcceleration: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1168.AngularAcceleration.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AngularAcceleration. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1168.AngularAcceleration)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_angular_compliance(self) -> '_1169.AngularCompliance':
        '''AngularCompliance: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1169.AngularCompliance.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AngularCompliance. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1169.AngularCompliance)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_angular_jerk(self) -> '_1170.AngularJerk':
        '''AngularJerk: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1170.AngularJerk.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AngularJerk. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1170.AngularJerk)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_angular_stiffness(self) -> '_1171.AngularStiffness':
        '''AngularStiffness: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1171.AngularStiffness.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AngularStiffness. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1171.AngularStiffness)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_angular_velocity(self) -> '_1172.AngularVelocity':
        '''AngularVelocity: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1172.AngularVelocity.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AngularVelocity. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1172.AngularVelocity)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_area(self) -> '_1173.Area':
        '''Area: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1173.Area.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Area. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1173.Area)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_area_small(self) -> '_1174.AreaSmall':
        '''AreaSmall: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1174.AreaSmall.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AreaSmall. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1174.AreaSmall)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_cycles(self) -> '_1175.Cycles':
        '''Cycles: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1175.Cycles.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Cycles. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1175.Cycles)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_damage(self) -> '_1176.Damage':
        '''Damage: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1176.Damage.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Damage. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1176.Damage)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_damage_rate(self) -> '_1177.DamageRate':
        '''DamageRate: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1177.DamageRate.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to DamageRate. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1177.DamageRate)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_decibel(self) -> '_1178.Decibel':
        '''Decibel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1178.Decibel.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Decibel. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1178.Decibel)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_density(self) -> '_1179.Density':
        '''Density: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1179.Density.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Density. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1179.Density)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_energy(self) -> '_1180.Energy':
        '''Energy: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1180.Energy.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Energy. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1180.Energy)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_energy_per_unit_area(self) -> '_1181.EnergyPerUnitArea':
        '''EnergyPerUnitArea: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1181.EnergyPerUnitArea.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to EnergyPerUnitArea. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1181.EnergyPerUnitArea)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_energy_per_unit_area_small(self) -> '_1182.EnergyPerUnitAreaSmall':
        '''EnergyPerUnitAreaSmall: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1182.EnergyPerUnitAreaSmall.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to EnergyPerUnitAreaSmall. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1182.EnergyPerUnitAreaSmall)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_energy_small(self) -> '_1183.EnergySmall':
        '''EnergySmall: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1183.EnergySmall.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to EnergySmall. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1183.EnergySmall)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_enum(self) -> '_1184.Enum':
        '''Enum: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1184.Enum.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Enum. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1184.Enum)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_flow_rate(self) -> '_1185.FlowRate':
        '''FlowRate: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1185.FlowRate.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to FlowRate. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1185.FlowRate)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_force(self) -> '_1186.Force':
        '''Force: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1186.Force.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Force. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1186.Force)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_force_per_unit_length(self) -> '_1187.ForcePerUnitLength':
        '''ForcePerUnitLength: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1187.ForcePerUnitLength.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ForcePerUnitLength. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1187.ForcePerUnitLength)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_force_per_unit_pressure(self) -> '_1188.ForcePerUnitPressure':
        '''ForcePerUnitPressure: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1188.ForcePerUnitPressure.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ForcePerUnitPressure. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1188.ForcePerUnitPressure)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_force_per_unit_temperature(self) -> '_1189.ForcePerUnitTemperature':
        '''ForcePerUnitTemperature: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1189.ForcePerUnitTemperature.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ForcePerUnitTemperature. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1189.ForcePerUnitTemperature)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_fraction_measurement_base(self) -> '_1190.FractionMeasurementBase':
        '''FractionMeasurementBase: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1190.FractionMeasurementBase.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to FractionMeasurementBase. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1190.FractionMeasurementBase)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_frequency(self) -> '_1191.Frequency':
        '''Frequency: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1191.Frequency.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Frequency. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1191.Frequency)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_fuel_consumption_engine(self) -> '_1192.FuelConsumptionEngine':
        '''FuelConsumptionEngine: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1192.FuelConsumptionEngine.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to FuelConsumptionEngine. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1192.FuelConsumptionEngine)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_fuel_efficiency_vehicle(self) -> '_1193.FuelEfficiencyVehicle':
        '''FuelEfficiencyVehicle: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1193.FuelEfficiencyVehicle.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to FuelEfficiencyVehicle. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1193.FuelEfficiencyVehicle)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_gradient(self) -> '_1194.Gradient':
        '''Gradient: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1194.Gradient.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Gradient. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1194.Gradient)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_heat_conductivity(self) -> '_1195.HeatConductivity':
        '''HeatConductivity: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1195.HeatConductivity.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to HeatConductivity. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1195.HeatConductivity)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_heat_transfer(self) -> '_1196.HeatTransfer':
        '''HeatTransfer: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1196.HeatTransfer.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to HeatTransfer. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1196.HeatTransfer)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_heat_transfer_coefficient_for_plastic_gear_tooth(self) -> '_1197.HeatTransferCoefficientForPlasticGearTooth':
        '''HeatTransferCoefficientForPlasticGearTooth: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1197.HeatTransferCoefficientForPlasticGearTooth.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to HeatTransferCoefficientForPlasticGearTooth. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1197.HeatTransferCoefficientForPlasticGearTooth)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_heat_transfer_resistance(self) -> '_1198.HeatTransferResistance':
        '''HeatTransferResistance: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1198.HeatTransferResistance.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to HeatTransferResistance. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1198.HeatTransferResistance)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_impulse(self) -> '_1199.Impulse':
        '''Impulse: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1199.Impulse.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Impulse. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1199.Impulse)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_index(self) -> '_1200.Index':
        '''Index: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1200.Index.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Index. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1200.Index)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_integer(self) -> '_1201.Integer':
        '''Integer: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1201.Integer.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Integer. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1201.Integer)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_inverse_short_length(self) -> '_1202.InverseShortLength':
        '''InverseShortLength: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1202.InverseShortLength.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to InverseShortLength. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1202.InverseShortLength)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_inverse_short_time(self) -> '_1203.InverseShortTime':
        '''InverseShortTime: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1203.InverseShortTime.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to InverseShortTime. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1203.InverseShortTime)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_jerk(self) -> '_1204.Jerk':
        '''Jerk: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1204.Jerk.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Jerk. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1204.Jerk)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_kinematic_viscosity(self) -> '_1205.KinematicViscosity':
        '''KinematicViscosity: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1205.KinematicViscosity.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KinematicViscosity. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1205.KinematicViscosity)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_length_long(self) -> '_1206.LengthLong':
        '''LengthLong: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1206.LengthLong.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LengthLong. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1206.LengthLong)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_length_medium(self) -> '_1207.LengthMedium':
        '''LengthMedium: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1207.LengthMedium.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LengthMedium. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1207.LengthMedium)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_length_per_unit_temperature(self) -> '_1208.LengthPerUnitTemperature':
        '''LengthPerUnitTemperature: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1208.LengthPerUnitTemperature.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LengthPerUnitTemperature. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1208.LengthPerUnitTemperature)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_length_short(self) -> '_1209.LengthShort':
        '''LengthShort: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1209.LengthShort.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LengthShort. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1209.LengthShort)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_length_to_the_fourth(self) -> '_1210.LengthToTheFourth':
        '''LengthToTheFourth: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1210.LengthToTheFourth.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LengthToTheFourth. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1210.LengthToTheFourth)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_length_very_long(self) -> '_1211.LengthVeryLong':
        '''LengthVeryLong: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1211.LengthVeryLong.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LengthVeryLong. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1211.LengthVeryLong)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_length_very_short(self) -> '_1212.LengthVeryShort':
        '''LengthVeryShort: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1212.LengthVeryShort.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LengthVeryShort. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1212.LengthVeryShort)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_length_very_short_per_length_short(self) -> '_1213.LengthVeryShortPerLengthShort':
        '''LengthVeryShortPerLengthShort: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1213.LengthVeryShortPerLengthShort.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LengthVeryShortPerLengthShort. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1213.LengthVeryShortPerLengthShort)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_linear_angular_damping(self) -> '_1214.LinearAngularDamping':
        '''LinearAngularDamping: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1214.LinearAngularDamping.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LinearAngularDamping. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1214.LinearAngularDamping)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_linear_angular_stiffness_cross_term(self) -> '_1215.LinearAngularStiffnessCrossTerm':
        '''LinearAngularStiffnessCrossTerm: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1215.LinearAngularStiffnessCrossTerm.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LinearAngularStiffnessCrossTerm. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1215.LinearAngularStiffnessCrossTerm)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_linear_damping(self) -> '_1216.LinearDamping':
        '''LinearDamping: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1216.LinearDamping.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LinearDamping. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1216.LinearDamping)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_linear_flexibility(self) -> '_1217.LinearFlexibility':
        '''LinearFlexibility: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1217.LinearFlexibility.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LinearFlexibility. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1217.LinearFlexibility)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_linear_stiffness(self) -> '_1218.LinearStiffness':
        '''LinearStiffness: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1218.LinearStiffness.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LinearStiffness. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1218.LinearStiffness)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_mass(self) -> '_1219.Mass':
        '''Mass: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1219.Mass.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Mass. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1219.Mass)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_mass_per_unit_length(self) -> '_1220.MassPerUnitLength':
        '''MassPerUnitLength: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1220.MassPerUnitLength.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MassPerUnitLength. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1220.MassPerUnitLength)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_mass_per_unit_time(self) -> '_1221.MassPerUnitTime':
        '''MassPerUnitTime: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1221.MassPerUnitTime.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MassPerUnitTime. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1221.MassPerUnitTime)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_moment_of_inertia(self) -> '_1222.MomentOfInertia':
        '''MomentOfInertia: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1222.MomentOfInertia.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MomentOfInertia. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1222.MomentOfInertia)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_moment_of_inertia_per_unit_length(self) -> '_1223.MomentOfInertiaPerUnitLength':
        '''MomentOfInertiaPerUnitLength: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1223.MomentOfInertiaPerUnitLength.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MomentOfInertiaPerUnitLength. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1223.MomentOfInertiaPerUnitLength)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_moment_per_unit_pressure(self) -> '_1224.MomentPerUnitPressure':
        '''MomentPerUnitPressure: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1224.MomentPerUnitPressure.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MomentPerUnitPressure. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1224.MomentPerUnitPressure)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_number(self) -> '_1225.Number':
        '''Number: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1225.Number.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Number. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1225.Number)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_percentage(self) -> '_1226.Percentage':
        '''Percentage: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1226.Percentage.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Percentage. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1226.Percentage)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_power(self) -> '_1227.Power':
        '''Power: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1227.Power.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Power. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1227.Power)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_power_per_small_area(self) -> '_1228.PowerPerSmallArea':
        '''PowerPerSmallArea: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1228.PowerPerSmallArea.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PowerPerSmallArea. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1228.PowerPerSmallArea)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_power_per_unit_time(self) -> '_1229.PowerPerUnitTime':
        '''PowerPerUnitTime: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1229.PowerPerUnitTime.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PowerPerUnitTime. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1229.PowerPerUnitTime)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_power_small(self) -> '_1230.PowerSmall':
        '''PowerSmall: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1230.PowerSmall.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PowerSmall. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1230.PowerSmall)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_power_small_per_area(self) -> '_1231.PowerSmallPerArea':
        '''PowerSmallPerArea: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1231.PowerSmallPerArea.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PowerSmallPerArea. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1231.PowerSmallPerArea)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_power_small_per_unit_area_per_unit_time(self) -> '_1232.PowerSmallPerUnitAreaPerUnitTime':
        '''PowerSmallPerUnitAreaPerUnitTime: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1232.PowerSmallPerUnitAreaPerUnitTime.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PowerSmallPerUnitAreaPerUnitTime. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1232.PowerSmallPerUnitAreaPerUnitTime)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_power_small_per_unit_time(self) -> '_1233.PowerSmallPerUnitTime':
        '''PowerSmallPerUnitTime: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1233.PowerSmallPerUnitTime.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PowerSmallPerUnitTime. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1233.PowerSmallPerUnitTime)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_pressure(self) -> '_1234.Pressure':
        '''Pressure: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1234.Pressure.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Pressure. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1234.Pressure)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_pressure_per_unit_time(self) -> '_1235.PressurePerUnitTime':
        '''PressurePerUnitTime: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1235.PressurePerUnitTime.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PressurePerUnitTime. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1235.PressurePerUnitTime)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_pressure_velocity_product(self) -> '_1236.PressureVelocityProduct':
        '''PressureVelocityProduct: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1236.PressureVelocityProduct.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PressureVelocityProduct. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1236.PressureVelocityProduct)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_pressure_viscosity_coefficient(self) -> '_1237.PressureViscosityCoefficient':
        '''PressureViscosityCoefficient: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1237.PressureViscosityCoefficient.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PressureViscosityCoefficient. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1237.PressureViscosityCoefficient)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_price(self) -> '_1238.Price':
        '''Price: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1238.Price.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Price. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1238.Price)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_quadratic_angular_damping(self) -> '_1239.QuadraticAngularDamping':
        '''QuadraticAngularDamping: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1239.QuadraticAngularDamping.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to QuadraticAngularDamping. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1239.QuadraticAngularDamping)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_quadratic_drag(self) -> '_1240.QuadraticDrag':
        '''QuadraticDrag: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1240.QuadraticDrag.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to QuadraticDrag. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1240.QuadraticDrag)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_rescaled_measurement(self) -> '_1241.RescaledMeasurement':
        '''RescaledMeasurement: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1241.RescaledMeasurement.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to RescaledMeasurement. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1241.RescaledMeasurement)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_rotatum(self) -> '_1242.Rotatum':
        '''Rotatum: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1242.Rotatum.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Rotatum. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1242.Rotatum)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_safety_factor(self) -> '_1243.SafetyFactor':
        '''SafetyFactor: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1243.SafetyFactor.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SafetyFactor. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1243.SafetyFactor)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_specific_acoustic_impedance(self) -> '_1244.SpecificAcousticImpedance':
        '''SpecificAcousticImpedance: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1244.SpecificAcousticImpedance.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SpecificAcousticImpedance. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1244.SpecificAcousticImpedance)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_specific_heat(self) -> '_1245.SpecificHeat':
        '''SpecificHeat: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1245.SpecificHeat.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SpecificHeat. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1245.SpecificHeat)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_square_root_of_unit_force_per_unit_area(self) -> '_1246.SquareRootOfUnitForcePerUnitArea':
        '''SquareRootOfUnitForcePerUnitArea: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1246.SquareRootOfUnitForcePerUnitArea.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SquareRootOfUnitForcePerUnitArea. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1246.SquareRootOfUnitForcePerUnitArea)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_stiffness_per_unit_face_width(self) -> '_1247.StiffnessPerUnitFaceWidth':
        '''StiffnessPerUnitFaceWidth: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1247.StiffnessPerUnitFaceWidth.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to StiffnessPerUnitFaceWidth. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1247.StiffnessPerUnitFaceWidth)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_stress(self) -> '_1248.Stress':
        '''Stress: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1248.Stress.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Stress. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1248.Stress)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_temperature(self) -> '_1249.Temperature':
        '''Temperature: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1249.Temperature.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Temperature. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1249.Temperature)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_temperature_difference(self) -> '_1250.TemperatureDifference':
        '''TemperatureDifference: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1250.TemperatureDifference.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to TemperatureDifference. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1250.TemperatureDifference)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_temperature_per_unit_time(self) -> '_1251.TemperaturePerUnitTime':
        '''TemperaturePerUnitTime: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1251.TemperaturePerUnitTime.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to TemperaturePerUnitTime. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1251.TemperaturePerUnitTime)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_text(self) -> '_1252.Text':
        '''Text: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1252.Text.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Text. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1252.Text)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_thermal_contact_coefficient(self) -> '_1253.ThermalContactCoefficient':
        '''ThermalContactCoefficient: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1253.ThermalContactCoefficient.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ThermalContactCoefficient. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1253.ThermalContactCoefficient)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_thermal_expansion_coefficient(self) -> '_1254.ThermalExpansionCoefficient':
        '''ThermalExpansionCoefficient: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1254.ThermalExpansionCoefficient.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ThermalExpansionCoefficient. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1254.ThermalExpansionCoefficient)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_thermo_elastic_factor(self) -> '_1255.ThermoElasticFactor':
        '''ThermoElasticFactor: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1255.ThermoElasticFactor.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ThermoElasticFactor. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1255.ThermoElasticFactor)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_time(self) -> '_1256.Time':
        '''Time: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1256.Time.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Time. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1256.Time)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_time_short(self) -> '_1257.TimeShort':
        '''TimeShort: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1257.TimeShort.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to TimeShort. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1257.TimeShort)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_time_very_short(self) -> '_1258.TimeVeryShort':
        '''TimeVeryShort: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1258.TimeVeryShort.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to TimeVeryShort. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1258.TimeVeryShort)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_torque(self) -> '_1259.Torque':
        '''Torque: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1259.Torque.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Torque. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1259.Torque)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_torque_converter_inverse_k(self) -> '_1260.TorqueConverterInverseK':
        '''TorqueConverterInverseK: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1260.TorqueConverterInverseK.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to TorqueConverterInverseK. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1260.TorqueConverterInverseK)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_torque_converter_k(self) -> '_1261.TorqueConverterK':
        '''TorqueConverterK: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1261.TorqueConverterK.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to TorqueConverterK. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1261.TorqueConverterK)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_torque_per_unit_temperature(self) -> '_1262.TorquePerUnitTemperature':
        '''TorquePerUnitTemperature: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1262.TorquePerUnitTemperature.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to TorquePerUnitTemperature. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1262.TorquePerUnitTemperature)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_velocity(self) -> '_1263.Velocity':
        '''Velocity: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1263.Velocity.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Velocity. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1263.Velocity)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_velocity_small(self) -> '_1264.VelocitySmall':
        '''VelocitySmall: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1264.VelocitySmall.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to VelocitySmall. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1264.VelocitySmall)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_viscosity(self) -> '_1265.Viscosity':
        '''Viscosity: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1265.Viscosity.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Viscosity. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1265.Viscosity)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_voltage(self) -> '_1266.Voltage':
        '''Voltage: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1266.Voltage.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Voltage. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1266.Voltage)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_volume(self) -> '_1267.Volume':
        '''Volume: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1267.Volume.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Volume. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1267.Volume)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_wear_coefficient(self) -> '_1268.WearCoefficient':
        '''WearCoefficient: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1268.WearCoefficient.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to WearCoefficient. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1268.WearCoefficient)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_yank(self) -> '_1269.Yank':
        '''Yank: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1269.Yank.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Yank. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1269.Yank)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def available_values(self) -> 'List[_1156.MeasurementBase]':
        '''List[MeasurementBase]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, constructor.new(_1156.MeasurementBase))
        return value


class ListWithSelectedItem_int(int, mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_int

    A specific implementation of 'ListWithSelectedItem' for 'int' types.
    '''

    __hash__ = None
    __qualname__ = 'int'

    def __new__(cls, instance_to_wrap: 'ListWithSelectedItem_int.TYPE'):
        return int.__new__(cls, instance_to_wrap.SelectedValue) if instance_to_wrap.SelectedValue else 0

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_int.TYPE'):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.SelectedValue
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> 'int':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return int

    @property
    def selected_value(self) -> 'int':
        '''int: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.enclosing.SelectedValue

    @property
    def available_values(self) -> 'List[int]':
        '''List[int]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, int)
        return value


class ListWithSelectedItem_ColumnTitle(_1340.ColumnTitle, mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_ColumnTitle

    A specific implementation of 'ListWithSelectedItem' for 'ColumnTitle' types.
    '''

    __hash__ = None
    __qualname__ = 'ColumnTitle'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ColumnTitle.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1340.ColumnTitle.TYPE':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1340.ColumnTitle.TYPE

    @property
    def selected_value(self) -> '_1340.ColumnTitle':
        '''ColumnTitle: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1340.ColumnTitle)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def available_values(self) -> 'List[_1340.ColumnTitle]':
        '''List[ColumnTitle]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, constructor.new(_1340.ColumnTitle))
        return value


class ListWithSelectedItem_PowerLoad(_2037.PowerLoad, mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_PowerLoad

    A specific implementation of 'ListWithSelectedItem' for 'PowerLoad' types.
    '''

    __hash__ = None
    __qualname__ = 'PowerLoad'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_PowerLoad.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2037.PowerLoad.TYPE':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _2037.PowerLoad.TYPE

    @property
    def selected_value(self) -> '_2037.PowerLoad':
        '''PowerLoad: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2037.PowerLoad)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def available_values(self) -> 'List[_2037.PowerLoad]':
        '''List[PowerLoad]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, constructor.new(_2037.PowerLoad))
        return value


class ListWithSelectedItem_ImportedFELink(_1928.ImportedFELink, mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_ImportedFELink

    A specific implementation of 'ListWithSelectedItem' for 'ImportedFELink' types.
    '''

    __hash__ = None
    __qualname__ = 'ImportedFELink'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ImportedFELink.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1928.ImportedFELink.TYPE':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1928.ImportedFELink.TYPE

    @property
    def selected_value(self) -> '_1928.ImportedFELink':
        '''ImportedFELink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1928.ImportedFELink)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_imported_fe_electric_machine_stator_link(self) -> '_1958.ImportedFEElectricMachineStatorLink':
        '''ImportedFEElectricMachineStatorLink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1958.ImportedFEElectricMachineStatorLink.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ImportedFEElectricMachineStatorLink. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1958.ImportedFEElectricMachineStatorLink)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_imported_fe_gear_mesh_link(self) -> '_1959.ImportedFEGearMeshLink':
        '''ImportedFEGearMeshLink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1959.ImportedFEGearMeshLink.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ImportedFEGearMeshLink. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1959.ImportedFEGearMeshLink)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_imported_fe_gear_with_duplicated_meshes_link(self) -> '_1960.ImportedFEGearWithDuplicatedMeshesLink':
        '''ImportedFEGearWithDuplicatedMeshesLink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1960.ImportedFEGearWithDuplicatedMeshesLink.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ImportedFEGearWithDuplicatedMeshesLink. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1960.ImportedFEGearWithDuplicatedMeshesLink)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_imported_fe_multi_node_connector_link(self) -> '_1962.ImportedFEMultiNodeConnectorLink':
        '''ImportedFEMultiNodeConnectorLink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1962.ImportedFEMultiNodeConnectorLink.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ImportedFEMultiNodeConnectorLink. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1962.ImportedFEMultiNodeConnectorLink)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_imported_fe_multi_node_link(self) -> '_1963.ImportedFEMultiNodeLink':
        '''ImportedFEMultiNodeLink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1963.ImportedFEMultiNodeLink.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ImportedFEMultiNodeLink. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1963.ImportedFEMultiNodeLink)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_imported_fe_node_link(self) -> '_1964.ImportedFENodeLink':
        '''ImportedFENodeLink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1964.ImportedFENodeLink.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ImportedFENodeLink. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1964.ImportedFENodeLink)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_imported_fe_planetary_connector_multi_node_link(self) -> '_1965.ImportedFEPlanetaryConnectorMultiNodeLink':
        '''ImportedFEPlanetaryConnectorMultiNodeLink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1965.ImportedFEPlanetaryConnectorMultiNodeLink.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ImportedFEPlanetaryConnectorMultiNodeLink. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1965.ImportedFEPlanetaryConnectorMultiNodeLink)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_imported_fe_planet_based_link(self) -> '_1966.ImportedFEPlanetBasedLink':
        '''ImportedFEPlanetBasedLink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1966.ImportedFEPlanetBasedLink.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ImportedFEPlanetBasedLink. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1966.ImportedFEPlanetBasedLink)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_imported_fe_planet_carrier_link(self) -> '_1967.ImportedFEPlanetCarrierLink':
        '''ImportedFEPlanetCarrierLink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1967.ImportedFEPlanetCarrierLink.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ImportedFEPlanetCarrierLink. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1967.ImportedFEPlanetCarrierLink)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_imported_fe_point_load_link(self) -> '_1968.ImportedFEPointLoadLink':
        '''ImportedFEPointLoadLink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1968.ImportedFEPointLoadLink.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ImportedFEPointLoadLink. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1968.ImportedFEPointLoadLink)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_multi_angle_connection_link(self) -> '_1980.MultiAngleConnectionLink':
        '''MultiAngleConnectionLink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1980.MultiAngleConnectionLink.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MultiAngleConnectionLink. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1980.MultiAngleConnectionLink)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_rolling_ring_connection_link(self) -> '_1991.RollingRingConnectionLink':
        '''RollingRingConnectionLink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1991.RollingRingConnectionLink.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to RollingRingConnectionLink. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1991.RollingRingConnectionLink)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_shaft_hub_connection_fe_link(self) -> '_1992.ShaftHubConnectionFELink':
        '''ShaftHubConnectionFELink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1992.ShaftHubConnectionFELink.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ShaftHubConnectionFELink. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_1992.ShaftHubConnectionFELink)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def available_values(self) -> 'List[_1928.ImportedFELink]':
        '''List[ImportedFELink]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, constructor.new(_1928.ImportedFELink))
        return value


class ListWithSelectedItem_ImportedFEStiffnessNode(_1969.ImportedFEStiffnessNode, mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_ImportedFEStiffnessNode

    A specific implementation of 'ListWithSelectedItem' for 'ImportedFEStiffnessNode' types.
    '''

    __hash__ = None
    __qualname__ = 'ImportedFEStiffnessNode'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ImportedFEStiffnessNode.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1969.ImportedFEStiffnessNode.TYPE':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1969.ImportedFEStiffnessNode.TYPE

    @property
    def selected_value(self) -> '_1969.ImportedFEStiffnessNode':
        '''ImportedFEStiffnessNode: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1969.ImportedFEStiffnessNode)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def available_values(self) -> 'List[_1969.ImportedFEStiffnessNode]':
        '''List[ImportedFEStiffnessNode]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, constructor.new(_1969.ImportedFEStiffnessNode))
        return value


class ListWithSelectedItem_Datum(_2015.Datum, mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_Datum

    A specific implementation of 'ListWithSelectedItem' for 'Datum' types.
    '''

    __hash__ = None
    __qualname__ = 'Datum'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_Datum.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2015.Datum.TYPE':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _2015.Datum.TYPE

    @property
    def selected_value(self) -> '_2015.Datum':
        '''Datum: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2015.Datum)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def available_values(self) -> 'List[_2015.Datum]':
        '''List[Datum]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, constructor.new(_2015.Datum))
        return value


class ListWithSelectedItem_Component(_2011.Component, mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_Component

    A specific implementation of 'ListWithSelectedItem' for 'Component' types.
    '''

    __hash__ = None
    __qualname__ = 'Component'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_Component.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2011.Component.TYPE':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _2011.Component.TYPE

    @property
    def selected_value(self) -> '_2011.Component':
        '''Component: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2011.Component)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_abstract_shaft_or_housing(self) -> '_2004.AbstractShaftOrHousing':
        '''AbstractShaftOrHousing: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2004.AbstractShaftOrHousing.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AbstractShaftOrHousing. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2004.AbstractShaftOrHousing)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_bearing(self) -> '_2007.Bearing':
        '''Bearing: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2007.Bearing.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Bearing. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2007.Bearing)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_bolt(self) -> '_2009.Bolt':
        '''Bolt: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2009.Bolt.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Bolt. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2009.Bolt)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_connector(self) -> '_2014.Connector':
        '''Connector: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2014.Connector.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Connector. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2014.Connector)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_datum(self) -> '_2015.Datum':
        '''Datum: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2015.Datum.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Datum. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2015.Datum)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_external_cad_model(self) -> '_2018.ExternalCADModel':
        '''ExternalCADModel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2018.ExternalCADModel.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ExternalCADModel. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2018.ExternalCADModel)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_guide_dxf_model(self) -> '_2020.GuideDxfModel':
        '''GuideDxfModel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2020.GuideDxfModel.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to GuideDxfModel. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2020.GuideDxfModel)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_imported_fe_component(self) -> '_2023.ImportedFEComponent':
        '''ImportedFEComponent: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2023.ImportedFEComponent.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ImportedFEComponent. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2023.ImportedFEComponent)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_mass_disc(self) -> '_2027.MassDisc':
        '''MassDisc: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2027.MassDisc.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MassDisc. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2027.MassDisc)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_measurement_component(self) -> '_2028.MeasurementComponent':
        '''MeasurementComponent: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2028.MeasurementComponent.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MeasurementComponent. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2028.MeasurementComponent)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_mountable_component(self) -> '_2029.MountableComponent':
        '''MountableComponent: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2029.MountableComponent.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MountableComponent. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2029.MountableComponent)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_oil_seal(self) -> '_2031.OilSeal':
        '''OilSeal: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2031.OilSeal.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to OilSeal. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2031.OilSeal)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_planet_carrier(self) -> '_2034.PlanetCarrier':
        '''PlanetCarrier: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2034.PlanetCarrier.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PlanetCarrier. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2034.PlanetCarrier)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_point_load(self) -> '_2036.PointLoad':
        '''PointLoad: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2036.PointLoad.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PointLoad. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2036.PointLoad)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_power_load(self) -> '_2037.PowerLoad':
        '''PowerLoad: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2037.PowerLoad.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PowerLoad. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2037.PowerLoad)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_unbalanced_mass(self) -> '_2042.UnbalancedMass':
        '''UnbalancedMass: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2042.UnbalancedMass.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to UnbalancedMass. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2042.UnbalancedMass)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_virtual_component(self) -> '_2043.VirtualComponent':
        '''VirtualComponent: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2043.VirtualComponent.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to VirtualComponent. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2043.VirtualComponent)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_shaft(self) -> '_2046.Shaft':
        '''Shaft: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2046.Shaft.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Shaft. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2046.Shaft)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_agma_gleason_conical_gear(self) -> '_2076.AGMAGleasonConicalGear':
        '''AGMAGleasonConicalGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2076.AGMAGleasonConicalGear.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AGMAGleasonConicalGear. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2076.AGMAGleasonConicalGear)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_bevel_differential_gear(self) -> '_2078.BevelDifferentialGear':
        '''BevelDifferentialGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2078.BevelDifferentialGear.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to BevelDifferentialGear. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2078.BevelDifferentialGear)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_bevel_differential_planet_gear(self) -> '_2080.BevelDifferentialPlanetGear':
        '''BevelDifferentialPlanetGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2080.BevelDifferentialPlanetGear.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to BevelDifferentialPlanetGear. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2080.BevelDifferentialPlanetGear)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_bevel_differential_sun_gear(self) -> '_2081.BevelDifferentialSunGear':
        '''BevelDifferentialSunGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2081.BevelDifferentialSunGear.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to BevelDifferentialSunGear. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2081.BevelDifferentialSunGear)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_bevel_gear(self) -> '_2082.BevelGear':
        '''BevelGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2082.BevelGear.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to BevelGear. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2082.BevelGear)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_concept_gear(self) -> '_2084.ConceptGear':
        '''ConceptGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2084.ConceptGear.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ConceptGear. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2084.ConceptGear)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_conical_gear(self) -> '_2086.ConicalGear':
        '''ConicalGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2086.ConicalGear.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ConicalGear. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2086.ConicalGear)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_cylindrical_gear(self) -> '_2088.CylindricalGear':
        '''CylindricalGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2088.CylindricalGear.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalGear. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2088.CylindricalGear)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_cylindrical_planet_gear(self) -> '_2090.CylindricalPlanetGear':
        '''CylindricalPlanetGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2090.CylindricalPlanetGear.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalPlanetGear. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2090.CylindricalPlanetGear)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_face_gear(self) -> '_2091.FaceGear':
        '''FaceGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2091.FaceGear.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to FaceGear. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2091.FaceGear)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_gear(self) -> '_2093.Gear':
        '''Gear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2093.Gear.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Gear. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2093.Gear)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_hypoid_gear(self) -> '_2097.HypoidGear':
        '''HypoidGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2097.HypoidGear.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to HypoidGear. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2097.HypoidGear)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_klingelnberg_cyclo_palloid_conical_gear(self) -> '_2099.KlingelnbergCycloPalloidConicalGear':
        '''KlingelnbergCycloPalloidConicalGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2099.KlingelnbergCycloPalloidConicalGear.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KlingelnbergCycloPalloidConicalGear. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2099.KlingelnbergCycloPalloidConicalGear)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_klingelnberg_cyclo_palloid_hypoid_gear(self) -> '_2101.KlingelnbergCycloPalloidHypoidGear':
        '''KlingelnbergCycloPalloidHypoidGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2101.KlingelnbergCycloPalloidHypoidGear.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KlingelnbergCycloPalloidHypoidGear. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2101.KlingelnbergCycloPalloidHypoidGear)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear(self) -> '_2103.KlingelnbergCycloPalloidSpiralBevelGear':
        '''KlingelnbergCycloPalloidSpiralBevelGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2103.KlingelnbergCycloPalloidSpiralBevelGear.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KlingelnbergCycloPalloidSpiralBevelGear. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2103.KlingelnbergCycloPalloidSpiralBevelGear)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_spiral_bevel_gear(self) -> '_2106.SpiralBevelGear':
        '''SpiralBevelGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2106.SpiralBevelGear.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SpiralBevelGear. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2106.SpiralBevelGear)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_straight_bevel_diff_gear(self) -> '_2108.StraightBevelDiffGear':
        '''StraightBevelDiffGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2108.StraightBevelDiffGear.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to StraightBevelDiffGear. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2108.StraightBevelDiffGear)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_straight_bevel_gear(self) -> '_2110.StraightBevelGear':
        '''StraightBevelGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2110.StraightBevelGear.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to StraightBevelGear. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2110.StraightBevelGear)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_straight_bevel_planet_gear(self) -> '_2112.StraightBevelPlanetGear':
        '''StraightBevelPlanetGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2112.StraightBevelPlanetGear.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to StraightBevelPlanetGear. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2112.StraightBevelPlanetGear)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_straight_bevel_sun_gear(self) -> '_2113.StraightBevelSunGear':
        '''StraightBevelSunGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2113.StraightBevelSunGear.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to StraightBevelSunGear. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2113.StraightBevelSunGear)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_worm_gear(self) -> '_2114.WormGear':
        '''WormGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2114.WormGear.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to WormGear. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2114.WormGear)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_zerol_bevel_gear(self) -> '_2116.ZerolBevelGear':
        '''ZerolBevelGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2116.ZerolBevelGear.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ZerolBevelGear. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2116.ZerolBevelGear)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_clutch_half(self) -> '_2138.ClutchHalf':
        '''ClutchHalf: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2138.ClutchHalf.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ClutchHalf. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2138.ClutchHalf)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_concept_coupling_half(self) -> '_2141.ConceptCouplingHalf':
        '''ConceptCouplingHalf: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2141.ConceptCouplingHalf.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ConceptCouplingHalf. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2141.ConceptCouplingHalf)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_coupling_half(self) -> '_2143.CouplingHalf':
        '''CouplingHalf: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2143.CouplingHalf.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CouplingHalf. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2143.CouplingHalf)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_cvt_pulley(self) -> '_2145.CVTPulley':
        '''CVTPulley: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2145.CVTPulley.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CVTPulley. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2145.CVTPulley)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_part_to_part_shear_coupling_half(self) -> '_2147.PartToPartShearCouplingHalf':
        '''PartToPartShearCouplingHalf: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2147.PartToPartShearCouplingHalf.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PartToPartShearCouplingHalf. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2147.PartToPartShearCouplingHalf)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_pulley(self) -> '_2148.Pulley':
        '''Pulley: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2148.Pulley.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Pulley. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2148.Pulley)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_rolling_ring(self) -> '_2154.RollingRing':
        '''RollingRing: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2154.RollingRing.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to RollingRing. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2154.RollingRing)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_shaft_hub_connection(self) -> '_2156.ShaftHubConnection':
        '''ShaftHubConnection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2156.ShaftHubConnection.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ShaftHubConnection. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2156.ShaftHubConnection)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_spring_damper_half(self) -> '_2158.SpringDamperHalf':
        '''SpringDamperHalf: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2158.SpringDamperHalf.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SpringDamperHalf. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2158.SpringDamperHalf)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_synchroniser_half(self) -> '_2161.SynchroniserHalf':
        '''SynchroniserHalf: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2161.SynchroniserHalf.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SynchroniserHalf. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2161.SynchroniserHalf)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_synchroniser_part(self) -> '_2162.SynchroniserPart':
        '''SynchroniserPart: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2162.SynchroniserPart.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SynchroniserPart. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2162.SynchroniserPart)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_synchroniser_sleeve(self) -> '_2163.SynchroniserSleeve':
        '''SynchroniserSleeve: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2163.SynchroniserSleeve.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SynchroniserSleeve. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2163.SynchroniserSleeve)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_torque_converter_pump(self) -> '_2165.TorqueConverterPump':
        '''TorqueConverterPump: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2165.TorqueConverterPump.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to TorqueConverterPump. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2165.TorqueConverterPump)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_torque_converter_turbine(self) -> '_2167.TorqueConverterTurbine':
        '''TorqueConverterTurbine: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2167.TorqueConverterTurbine.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to TorqueConverterTurbine. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2167.TorqueConverterTurbine)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def available_values(self) -> 'List[_2011.Component]':
        '''List[Component]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, constructor.new(_2011.Component))
        return value


class ListWithSelectedItem_ImportedFE(_1957.ImportedFE, mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_ImportedFE

    A specific implementation of 'ListWithSelectedItem' for 'ImportedFE' types.
    '''

    __hash__ = None
    __qualname__ = 'ImportedFE'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ImportedFE.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1957.ImportedFE.TYPE':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1957.ImportedFE.TYPE

    @property
    def selected_value(self) -> '_1957.ImportedFE':
        '''ImportedFE: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1957.ImportedFE)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def available_values(self) -> 'List[_1957.ImportedFE]':
        '''List[ImportedFE]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, constructor.new(_1957.ImportedFE))
        return value


class ListWithSelectedItem_CylindricalGear(_2088.CylindricalGear, mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_CylindricalGear

    A specific implementation of 'ListWithSelectedItem' for 'CylindricalGear' types.
    '''

    __hash__ = None
    __qualname__ = 'CylindricalGear'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CylindricalGear.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2088.CylindricalGear.TYPE':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _2088.CylindricalGear.TYPE

    @property
    def selected_value(self) -> '_2088.CylindricalGear':
        '''CylindricalGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2088.CylindricalGear)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def available_values(self) -> 'List[_2088.CylindricalGear]':
        '''List[CylindricalGear]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, constructor.new(_2088.CylindricalGear))
        return value


class ListWithSelectedItem_GuideDxfModel(_2020.GuideDxfModel, mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_GuideDxfModel

    A specific implementation of 'ListWithSelectedItem' for 'GuideDxfModel' types.
    '''

    __hash__ = None
    __qualname__ = 'GuideDxfModel'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_GuideDxfModel.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2020.GuideDxfModel.TYPE':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _2020.GuideDxfModel.TYPE

    @property
    def selected_value(self) -> '_2020.GuideDxfModel':
        '''GuideDxfModel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2020.GuideDxfModel)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def available_values(self) -> 'List[_2020.GuideDxfModel]':
        '''List[GuideDxfModel]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, constructor.new(_2020.GuideDxfModel))
        return value


class ListWithSelectedItem_ConcentricPartGroup(_2051.ConcentricPartGroup, mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_ConcentricPartGroup

    A specific implementation of 'ListWithSelectedItem' for 'ConcentricPartGroup' types.
    '''

    __hash__ = None
    __qualname__ = 'ConcentricPartGroup'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ConcentricPartGroup.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2051.ConcentricPartGroup.TYPE':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _2051.ConcentricPartGroup.TYPE

    @property
    def selected_value(self) -> '_2051.ConcentricPartGroup':
        '''ConcentricPartGroup: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2051.ConcentricPartGroup)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def available_values(self) -> 'List[_2051.ConcentricPartGroup]':
        '''List[ConcentricPartGroup]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, constructor.new(_2051.ConcentricPartGroup))
        return value


class ListWithSelectedItem_GearSetDesign(_716.GearSetDesign, mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_GearSetDesign

    A specific implementation of 'ListWithSelectedItem' for 'GearSetDesign' types.
    '''

    __hash__ = None
    __qualname__ = 'GearSetDesign'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_GearSetDesign.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_716.GearSetDesign.TYPE':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _716.GearSetDesign.TYPE

    @property
    def selected_value(self) -> '_716.GearSetDesign':
        '''GearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_716.GearSetDesign)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_zerol_bevel_gear_set_design(self) -> '_720.ZerolBevelGearSetDesign':
        '''ZerolBevelGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _720.ZerolBevelGearSetDesign.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ZerolBevelGearSetDesign. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_720.ZerolBevelGearSetDesign)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_worm_gear_set_design(self) -> '_725.WormGearSetDesign':
        '''WormGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _725.WormGearSetDesign.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to WormGearSetDesign. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_725.WormGearSetDesign)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_straight_bevel_diff_gear_set_design(self) -> '_729.StraightBevelDiffGearSetDesign':
        '''StraightBevelDiffGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _729.StraightBevelDiffGearSetDesign.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to StraightBevelDiffGearSetDesign. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_729.StraightBevelDiffGearSetDesign)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_straight_bevel_gear_set_design(self) -> '_733.StraightBevelGearSetDesign':
        '''StraightBevelGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _733.StraightBevelGearSetDesign.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to StraightBevelGearSetDesign. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_733.StraightBevelGearSetDesign)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_spiral_bevel_gear_set_design(self) -> '_737.SpiralBevelGearSetDesign':
        '''SpiralBevelGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _737.SpiralBevelGearSetDesign.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SpiralBevelGearSetDesign. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_737.SpiralBevelGearSetDesign)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_design(self) -> '_741.KlingelnbergCycloPalloidSpiralBevelGearSetDesign':
        '''KlingelnbergCycloPalloidSpiralBevelGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _741.KlingelnbergCycloPalloidSpiralBevelGearSetDesign.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KlingelnbergCycloPalloidSpiralBevelGearSetDesign. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_741.KlingelnbergCycloPalloidSpiralBevelGearSetDesign)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set_design(self) -> '_745.KlingelnbergCycloPalloidHypoidGearSetDesign':
        '''KlingelnbergCycloPalloidHypoidGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _745.KlingelnbergCycloPalloidHypoidGearSetDesign.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KlingelnbergCycloPalloidHypoidGearSetDesign. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_745.KlingelnbergCycloPalloidHypoidGearSetDesign)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_klingelnberg_conical_gear_set_design(self) -> '_749.KlingelnbergConicalGearSetDesign':
        '''KlingelnbergConicalGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _749.KlingelnbergConicalGearSetDesign.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KlingelnbergConicalGearSetDesign. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_749.KlingelnbergConicalGearSetDesign)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_hypoid_gear_set_design(self) -> '_753.HypoidGearSetDesign':
        '''HypoidGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _753.HypoidGearSetDesign.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to HypoidGearSetDesign. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_753.HypoidGearSetDesign)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_face_gear_set_design(self) -> '_761.FaceGearSetDesign':
        '''FaceGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _761.FaceGearSetDesign.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to FaceGearSetDesign. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_761.FaceGearSetDesign)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_cylindrical_gear_set_design(self) -> '_787.CylindricalGearSetDesign':
        '''CylindricalGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _787.CylindricalGearSetDesign.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalGearSetDesign. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_787.CylindricalGearSetDesign)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_cylindrical_planetary_gear_set_design(self) -> '_796.CylindricalPlanetaryGearSetDesign':
        '''CylindricalPlanetaryGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _796.CylindricalPlanetaryGearSetDesign.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalPlanetaryGearSetDesign. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_796.CylindricalPlanetaryGearSetDesign)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_conical_gear_set_design(self) -> '_893.ConicalGearSetDesign':
        '''ConicalGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _893.ConicalGearSetDesign.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ConicalGearSetDesign. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_893.ConicalGearSetDesign)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_concept_gear_set_design(self) -> '_915.ConceptGearSetDesign':
        '''ConceptGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _915.ConceptGearSetDesign.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ConceptGearSetDesign. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_915.ConceptGearSetDesign)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_bevel_gear_set_design(self) -> '_919.BevelGearSetDesign':
        '''BevelGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _919.BevelGearSetDesign.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to BevelGearSetDesign. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_919.BevelGearSetDesign)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_agma_gleason_conical_gear_set_design(self) -> '_932.AGMAGleasonConicalGearSetDesign':
        '''AGMAGleasonConicalGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _932.AGMAGleasonConicalGearSetDesign.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AGMAGleasonConicalGearSetDesign. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_932.AGMAGleasonConicalGearSetDesign)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def available_values(self) -> 'List[_716.GearSetDesign]':
        '''List[GearSetDesign]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, constructor.new(_716.GearSetDesign))
        return value


class ListWithSelectedItem_ShaftHubConnection(_2156.ShaftHubConnection, mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_ShaftHubConnection

    A specific implementation of 'ListWithSelectedItem' for 'ShaftHubConnection' types.
    '''

    __hash__ = None
    __qualname__ = 'ShaftHubConnection'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ShaftHubConnection.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2156.ShaftHubConnection.TYPE':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _2156.ShaftHubConnection.TYPE

    @property
    def selected_value(self) -> '_2156.ShaftHubConnection':
        '''ShaftHubConnection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2156.ShaftHubConnection)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def available_values(self) -> 'List[_2156.ShaftHubConnection]':
        '''List[ShaftHubConnection]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, constructor.new(_2156.ShaftHubConnection))
        return value


class ListWithSelectedItem_TSelectableItem(Generic[TSelectableItem], mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_TSelectableItem

    A specific implementation of 'ListWithSelectedItem' for 'TSelectableItem' types.
    '''

    __hash__ = None
    __qualname__ = 'TSelectableItem'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_TSelectableItem.TYPE'):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.SelectedValue
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> 'TSelectableItem':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return TSelectableItem

    @property
    def selected_value(self) -> 'TSelectableItem':
        '''TSelectableItem: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(TSelectableItem)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def available_values(self) -> 'List[TSelectableItem]':
        '''List[TSelectableItem]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, constructor.new(TSelectableItem))
        return value


class ListWithSelectedItem_CylindricalGearSystemDeflection(_2281.CylindricalGearSystemDeflection, mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_CylindricalGearSystemDeflection

    A specific implementation of 'ListWithSelectedItem' for 'CylindricalGearSystemDeflection' types.
    '''

    __hash__ = None
    __qualname__ = 'CylindricalGearSystemDeflection'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CylindricalGearSystemDeflection.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2281.CylindricalGearSystemDeflection.TYPE':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _2281.CylindricalGearSystemDeflection.TYPE

    @property
    def selected_value(self) -> '_2281.CylindricalGearSystemDeflection':
        '''CylindricalGearSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2281.CylindricalGearSystemDeflection)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_cylindrical_gear_system_deflection_timestep(self) -> '_2282.CylindricalGearSystemDeflectionTimestep':
        '''CylindricalGearSystemDeflectionTimestep: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2282.CylindricalGearSystemDeflectionTimestep.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalGearSystemDeflectionTimestep. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2282.CylindricalGearSystemDeflectionTimestep)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_cylindrical_gear_system_deflection_with_ltca_results(self) -> '_2283.CylindricalGearSystemDeflectionWithLTCAResults':
        '''CylindricalGearSystemDeflectionWithLTCAResults: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2283.CylindricalGearSystemDeflectionWithLTCAResults.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalGearSystemDeflectionWithLTCAResults. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2283.CylindricalGearSystemDeflectionWithLTCAResults)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_cylindrical_planet_gear_system_deflection(self) -> '_2284.CylindricalPlanetGearSystemDeflection':
        '''CylindricalPlanetGearSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2284.CylindricalPlanetGearSystemDeflection.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalPlanetGearSystemDeflection. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2284.CylindricalPlanetGearSystemDeflection)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def available_values(self) -> 'List[_2281.CylindricalGearSystemDeflection]':
        '''List[CylindricalGearSystemDeflection]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, constructor.new(_2281.CylindricalGearSystemDeflection))
        return value


class ListWithSelectedItem_DesignState(_5261.DesignState, mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_DesignState

    A specific implementation of 'ListWithSelectedItem' for 'DesignState' types.
    '''

    __hash__ = None
    __qualname__ = 'DesignState'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_DesignState.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_5261.DesignState.TYPE':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _5261.DesignState.TYPE

    @property
    def selected_value(self) -> '_5261.DesignState':
        '''DesignState: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5261.DesignState)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def available_values(self) -> 'List[_5261.DesignState]':
        '''List[DesignState]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, constructor.new(_5261.DesignState))
        return value


class ListWithSelectedItem_ImportedFEComponent(_2023.ImportedFEComponent, mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_ImportedFEComponent

    A specific implementation of 'ListWithSelectedItem' for 'ImportedFEComponent' types.
    '''

    __hash__ = None
    __qualname__ = 'ImportedFEComponent'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ImportedFEComponent.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2023.ImportedFEComponent.TYPE':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _2023.ImportedFEComponent.TYPE

    @property
    def selected_value(self) -> '_2023.ImportedFEComponent':
        '''ImportedFEComponent: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2023.ImportedFEComponent)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def available_values(self) -> 'List[_2023.ImportedFEComponent]':
        '''List[ImportedFEComponent]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, constructor.new(_2023.ImportedFEComponent))
        return value


class ListWithSelectedItem_ImportedFEComponentGearWhineAnalysis(_5357.ImportedFEComponentGearWhineAnalysis, mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_ImportedFEComponentGearWhineAnalysis

    A specific implementation of 'ListWithSelectedItem' for 'ImportedFEComponentGearWhineAnalysis' types.
    '''

    __hash__ = None
    __qualname__ = 'ImportedFEComponentGearWhineAnalysis'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ImportedFEComponentGearWhineAnalysis.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_5357.ImportedFEComponentGearWhineAnalysis.TYPE':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _5357.ImportedFEComponentGearWhineAnalysis.TYPE

    @property
    def selected_value(self) -> '_5357.ImportedFEComponentGearWhineAnalysis':
        '''ImportedFEComponentGearWhineAnalysis: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5357.ImportedFEComponentGearWhineAnalysis)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def available_values(self) -> 'List[_5357.ImportedFEComponentGearWhineAnalysis]':
        '''List[ImportedFEComponentGearWhineAnalysis]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, constructor.new(_5357.ImportedFEComponentGearWhineAnalysis))
        return value


class ListWithSelectedItem_ResultLocationSelectionGroup(_5432.ResultLocationSelectionGroup, mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_ResultLocationSelectionGroup

    A specific implementation of 'ListWithSelectedItem' for 'ResultLocationSelectionGroup' types.
    '''

    __hash__ = None
    __qualname__ = 'ResultLocationSelectionGroup'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ResultLocationSelectionGroup.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_5432.ResultLocationSelectionGroup.TYPE':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _5432.ResultLocationSelectionGroup.TYPE

    @property
    def selected_value(self) -> '_5432.ResultLocationSelectionGroup':
        '''ResultLocationSelectionGroup: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5432.ResultLocationSelectionGroup)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def available_values(self) -> 'List[_5432.ResultLocationSelectionGroup]':
        '''List[ResultLocationSelectionGroup]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, constructor.new(_5432.ResultLocationSelectionGroup))
        return value


class ListWithSelectedItem_StaticLoadCase(_6211.StaticLoadCase, mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_StaticLoadCase

    A specific implementation of 'ListWithSelectedItem' for 'StaticLoadCase' types.
    '''

    __hash__ = None
    __qualname__ = 'StaticLoadCase'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_StaticLoadCase.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_6211.StaticLoadCase.TYPE':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _6211.StaticLoadCase.TYPE

    @property
    def selected_value(self) -> '_6211.StaticLoadCase':
        '''StaticLoadCase: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6211.StaticLoadCase)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def available_values(self) -> 'List[_6211.StaticLoadCase]':
        '''List[StaticLoadCase]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, constructor.new(_6211.StaticLoadCase))
        return value


class ListWithSelectedItem_DutyCycle(_5262.DutyCycle, mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_DutyCycle

    A specific implementation of 'ListWithSelectedItem' for 'DutyCycle' types.
    '''

    __hash__ = None
    __qualname__ = 'DutyCycle'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_DutyCycle.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_5262.DutyCycle.TYPE':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _5262.DutyCycle.TYPE

    @property
    def selected_value(self) -> '_5262.DutyCycle':
        '''DutyCycle: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5262.DutyCycle)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def available_values(self) -> 'List[_5262.DutyCycle]':
        '''List[DutyCycle]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, constructor.new(_5262.DutyCycle))
        return value


class ListWithSelectedItem_float(float, mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_float

    A specific implementation of 'ListWithSelectedItem' for 'float' types.
    '''

    __hash__ = None
    __qualname__ = 'float'

    def __new__(cls, instance_to_wrap: 'ListWithSelectedItem_float.TYPE'):
        return float.__new__(cls, instance_to_wrap.SelectedValue) if instance_to_wrap.SelectedValue else 0.0

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_float.TYPE'):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.SelectedValue
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> 'float':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return float

    @property
    def selected_value(self) -> 'float':
        '''float: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.enclosing.SelectedValue

    @property
    def available_values(self) -> 'List[float]':
        '''List[float]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_list_float(self.enclosing.AvailableValues)
        return value


class ListWithSelectedItem_ElectricMachineDataSet(_1946.ElectricMachineDataSet, mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_ElectricMachineDataSet

    A specific implementation of 'ListWithSelectedItem' for 'ElectricMachineDataSet' types.
    '''

    __hash__ = None
    __qualname__ = 'ElectricMachineDataSet'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ElectricMachineDataSet.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1946.ElectricMachineDataSet.TYPE':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1946.ElectricMachineDataSet.TYPE

    @property
    def selected_value(self) -> '_1946.ElectricMachineDataSet':
        '''ElectricMachineDataSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1946.ElectricMachineDataSet)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def available_values(self) -> 'List[_1946.ElectricMachineDataSet]':
        '''List[ElectricMachineDataSet]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, constructor.new(_1946.ElectricMachineDataSet))
        return value


class ListWithSelectedItem_CylindricalGearSet(_2089.CylindricalGearSet, mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_CylindricalGearSet

    A specific implementation of 'ListWithSelectedItem' for 'CylindricalGearSet' types.
    '''

    __hash__ = None
    __qualname__ = 'CylindricalGearSet'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CylindricalGearSet.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2089.CylindricalGearSet.TYPE':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _2089.CylindricalGearSet.TYPE

    @property
    def selected_value(self) -> '_2089.CylindricalGearSet':
        '''CylindricalGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2089.CylindricalGearSet)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def available_values(self) -> 'List[_2089.CylindricalGearSet]':
        '''List[CylindricalGearSet]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, constructor.new(_2089.CylindricalGearSet))
        return value


class ListWithSelectedItem_PointLoad(_2036.PointLoad, mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_PointLoad

    A specific implementation of 'ListWithSelectedItem' for 'PointLoad' types.
    '''

    __hash__ = None
    __qualname__ = 'PointLoad'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_PointLoad.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2036.PointLoad.TYPE':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _2036.PointLoad.TYPE

    @property
    def selected_value(self) -> '_2036.PointLoad':
        '''PointLoad: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2036.PointLoad)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def available_values(self) -> 'List[_2036.PointLoad]':
        '''List[PointLoad]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, constructor.new(_2036.PointLoad))
        return value


class ListWithSelectedItem_GearSet(_2095.GearSet, mixins.ListWithSelectedItemMixin):
    '''ListWithSelectedItem_GearSet

    A specific implementation of 'ListWithSelectedItem' for 'GearSet' types.
    '''

    __hash__ = None
    __qualname__ = 'GearSet'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_GearSet.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2095.GearSet.TYPE':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _2095.GearSet.TYPE

    @property
    def selected_value(self) -> '_2095.GearSet':
        '''GearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2095.GearSet)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_agma_gleason_conical_gear_set(self) -> '_2077.AGMAGleasonConicalGearSet':
        '''AGMAGleasonConicalGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2077.AGMAGleasonConicalGearSet.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AGMAGleasonConicalGearSet. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2077.AGMAGleasonConicalGearSet)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_bevel_differential_gear_set(self) -> '_2079.BevelDifferentialGearSet':
        '''BevelDifferentialGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2079.BevelDifferentialGearSet.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to BevelDifferentialGearSet. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2079.BevelDifferentialGearSet)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_bevel_gear_set(self) -> '_2083.BevelGearSet':
        '''BevelGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2083.BevelGearSet.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to BevelGearSet. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2083.BevelGearSet)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_concept_gear_set(self) -> '_2085.ConceptGearSet':
        '''ConceptGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2085.ConceptGearSet.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ConceptGearSet. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2085.ConceptGearSet)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_conical_gear_set(self) -> '_2087.ConicalGearSet':
        '''ConicalGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2087.ConicalGearSet.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ConicalGearSet. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2087.ConicalGearSet)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_cylindrical_gear_set(self) -> '_2089.CylindricalGearSet':
        '''CylindricalGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2089.CylindricalGearSet.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalGearSet. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2089.CylindricalGearSet)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_face_gear_set(self) -> '_2092.FaceGearSet':
        '''FaceGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2092.FaceGearSet.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to FaceGearSet. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2092.FaceGearSet)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_hypoid_gear_set(self) -> '_2098.HypoidGearSet':
        '''HypoidGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2098.HypoidGearSet.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to HypoidGearSet. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2098.HypoidGearSet)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_klingelnberg_cyclo_palloid_conical_gear_set(self) -> '_2100.KlingelnbergCycloPalloidConicalGearSet':
        '''KlingelnbergCycloPalloidConicalGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2100.KlingelnbergCycloPalloidConicalGearSet.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KlingelnbergCycloPalloidConicalGearSet. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2100.KlingelnbergCycloPalloidConicalGearSet)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set(self) -> '_2102.KlingelnbergCycloPalloidHypoidGearSet':
        '''KlingelnbergCycloPalloidHypoidGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2102.KlingelnbergCycloPalloidHypoidGearSet.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KlingelnbergCycloPalloidHypoidGearSet. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2102.KlingelnbergCycloPalloidHypoidGearSet)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self) -> '_2104.KlingelnbergCycloPalloidSpiralBevelGearSet':
        '''KlingelnbergCycloPalloidSpiralBevelGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2104.KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KlingelnbergCycloPalloidSpiralBevelGearSet. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2104.KlingelnbergCycloPalloidSpiralBevelGearSet)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_planetary_gear_set(self) -> '_2105.PlanetaryGearSet':
        '''PlanetaryGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2105.PlanetaryGearSet.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PlanetaryGearSet. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2105.PlanetaryGearSet)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_spiral_bevel_gear_set(self) -> '_2107.SpiralBevelGearSet':
        '''SpiralBevelGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2107.SpiralBevelGearSet.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SpiralBevelGearSet. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2107.SpiralBevelGearSet)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_straight_bevel_diff_gear_set(self) -> '_2109.StraightBevelDiffGearSet':
        '''StraightBevelDiffGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2109.StraightBevelDiffGearSet.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to StraightBevelDiffGearSet. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2109.StraightBevelDiffGearSet)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_straight_bevel_gear_set(self) -> '_2111.StraightBevelGearSet':
        '''StraightBevelGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2111.StraightBevelGearSet.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to StraightBevelGearSet. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2111.StraightBevelGearSet)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_worm_gear_set(self) -> '_2115.WormGearSet':
        '''WormGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2115.WormGearSet.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to WormGearSet. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2115.WormGearSet)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def selected_value_of_type_zerol_bevel_gear_set(self) -> '_2117.ZerolBevelGearSet':
        '''ZerolBevelGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2117.ZerolBevelGearSet.TYPE not in self.enclosing.SelectedValue.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ZerolBevelGearSet. Expected: {}.'.format(self.enclosing.SelectedValue.__class__.__qualname__))

        return constructor.new(_2117.ZerolBevelGearSet)(self.enclosing.SelectedValue) if self.enclosing.SelectedValue else None

    @property
    def available_values(self) -> 'List[_2095.GearSet]':
        '''List[GearSet]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.enclosing.AvailableValues, constructor.new(_2095.GearSet))
        return value
