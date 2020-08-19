'''_6078.py

AGMAGleasonConicalGearSetLoadCase
'''


from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import (
    _2077, _2079, _2083, _2098,
    _2107, _2109, _2111, _2117
)
from mastapy._internal.cast_exception import CastException
from mastapy.gears.manufacturing.bevel import _578, _576, _577
from mastapy.system_model.analyses_and_results.static_loads import _6109
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'AGMAGleasonConicalGearSetLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalGearSetLoadCase',)


class AGMAGleasonConicalGearSetLoadCase(_6109.ConicalGearSetLoadCase):
    '''AGMAGleasonConicalGearSetLoadCase

    This is a mastapy class.
    '''

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalGearSetLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def override_manufacturing_config_micro_geometry(self) -> 'bool':
        '''bool: 'OverrideManufacturingConfigMicroGeometry' is the original name of this property.'''

        return self.wrapped.OverrideManufacturingConfigMicroGeometry

    @override_manufacturing_config_micro_geometry.setter
    def override_manufacturing_config_micro_geometry(self, value: 'bool'):
        self.wrapped.OverrideManufacturingConfigMicroGeometry = bool(value) if value else False

    @property
    def assembly_design(self) -> '_2077.AGMAGleasonConicalGearSet':
        '''AGMAGleasonConicalGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2077.AGMAGleasonConicalGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_design_of_type_bevel_differential_gear_set(self) -> '_2079.BevelDifferentialGearSet':
        '''BevelDifferentialGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2079.BevelDifferentialGearSet.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to BevelDifferentialGearSet. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new(_2079.BevelDifferentialGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_design_of_type_bevel_gear_set(self) -> '_2083.BevelGearSet':
        '''BevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2083.BevelGearSet.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to BevelGearSet. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new(_2083.BevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_design_of_type_hypoid_gear_set(self) -> '_2098.HypoidGearSet':
        '''HypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2098.HypoidGearSet.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to HypoidGearSet. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new(_2098.HypoidGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_design_of_type_spiral_bevel_gear_set(self) -> '_2107.SpiralBevelGearSet':
        '''SpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2107.SpiralBevelGearSet.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to SpiralBevelGearSet. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new(_2107.SpiralBevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_design_of_type_straight_bevel_diff_gear_set(self) -> '_2109.StraightBevelDiffGearSet':
        '''StraightBevelDiffGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2109.StraightBevelDiffGearSet.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to StraightBevelDiffGearSet. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new(_2109.StraightBevelDiffGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_design_of_type_straight_bevel_gear_set(self) -> '_2111.StraightBevelGearSet':
        '''StraightBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2111.StraightBevelGearSet.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to StraightBevelGearSet. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new(_2111.StraightBevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_design_of_type_zerol_bevel_gear_set(self) -> '_2117.ZerolBevelGearSet':
        '''ZerolBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2117.ZerolBevelGearSet.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to ZerolBevelGearSet. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new(_2117.ZerolBevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def overridden_manufacturing_config_micro_geometry(self) -> '_578.ConicalSetMicroGeometryConfigBase':
        '''ConicalSetMicroGeometryConfigBase: 'OverriddenManufacturingConfigMicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_578.ConicalSetMicroGeometryConfigBase)(self.wrapped.OverriddenManufacturingConfigMicroGeometry) if self.wrapped.OverriddenManufacturingConfigMicroGeometry else None

    @property
    def overridden_manufacturing_config_micro_geometry_of_type_conical_set_manufacturing_config(self) -> '_576.ConicalSetManufacturingConfig':
        '''ConicalSetManufacturingConfig: 'OverriddenManufacturingConfigMicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _576.ConicalSetManufacturingConfig.TYPE not in self.wrapped.OverriddenManufacturingConfigMicroGeometry.__class__.__mro__:
            raise CastException('Failed to cast overridden_manufacturing_config_micro_geometry to ConicalSetManufacturingConfig. Expected: {}.'.format(self.wrapped.OverriddenManufacturingConfigMicroGeometry.__class__.__qualname__))

        return constructor.new(_576.ConicalSetManufacturingConfig)(self.wrapped.OverriddenManufacturingConfigMicroGeometry) if self.wrapped.OverriddenManufacturingConfigMicroGeometry else None

    @property
    def overridden_manufacturing_config_micro_geometry_of_type_conical_set_micro_geometry_config(self) -> '_577.ConicalSetMicroGeometryConfig':
        '''ConicalSetMicroGeometryConfig: 'OverriddenManufacturingConfigMicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _577.ConicalSetMicroGeometryConfig.TYPE not in self.wrapped.OverriddenManufacturingConfigMicroGeometry.__class__.__mro__:
            raise CastException('Failed to cast overridden_manufacturing_config_micro_geometry to ConicalSetMicroGeometryConfig. Expected: {}.'.format(self.wrapped.OverriddenManufacturingConfigMicroGeometry.__class__.__qualname__))

        return constructor.new(_577.ConicalSetMicroGeometryConfig)(self.wrapped.OverriddenManufacturingConfigMicroGeometry) if self.wrapped.OverriddenManufacturingConfigMicroGeometry else None
