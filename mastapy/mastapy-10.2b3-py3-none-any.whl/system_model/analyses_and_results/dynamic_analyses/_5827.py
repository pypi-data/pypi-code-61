'''_5827.py

AssemblyDynamicAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _2002
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6080
from mastapy.system_model.analyses_and_results.dynamic_analyses import (
    _5828, _5830, _5833, _5839,
    _5840, _5842, _5847, _5851,
    _5861, _5865, _5873, _5874,
    _5881, _5882, _5889, _5892,
    _5893, _5894, _5896, _5899,
    _5903, _5904, _5905, _5912,
    _5907, _5911, _5917, _5919,
    _5923, _5926, _5929, _5934,
    _5937, _5941, _5944, _5822
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'AssemblyDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyDynamicAnalysis',)


class AssemblyDynamicAnalysis(_5822.AbstractAssemblyDynamicAnalysis):
    '''AssemblyDynamicAnalysis

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2002.Assembly':
        '''Assembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2002.Assembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6080.AssemblyLoadCase':
        '''AssemblyLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6080.AssemblyLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def bearings(self) -> 'List[_5828.BearingDynamicAnalysis]':
        '''List[BearingDynamicAnalysis]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_5828.BearingDynamicAnalysis))
        return value

    @property
    def belt_drives(self) -> 'List[_5830.BeltDriveDynamicAnalysis]':
        '''List[BeltDriveDynamicAnalysis]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_5830.BeltDriveDynamicAnalysis))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_5833.BevelDifferentialGearSetDynamicAnalysis]':
        '''List[BevelDifferentialGearSetDynamicAnalysis]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_5833.BevelDifferentialGearSetDynamicAnalysis))
        return value

    @property
    def bolts(self) -> 'List[_5839.BoltDynamicAnalysis]':
        '''List[BoltDynamicAnalysis]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_5839.BoltDynamicAnalysis))
        return value

    @property
    def bolted_joints(self) -> 'List[_5840.BoltedJointDynamicAnalysis]':
        '''List[BoltedJointDynamicAnalysis]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_5840.BoltedJointDynamicAnalysis))
        return value

    @property
    def clutches(self) -> 'List[_5842.ClutchDynamicAnalysis]':
        '''List[ClutchDynamicAnalysis]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_5842.ClutchDynamicAnalysis))
        return value

    @property
    def concept_couplings(self) -> 'List[_5847.ConceptCouplingDynamicAnalysis]':
        '''List[ConceptCouplingDynamicAnalysis]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_5847.ConceptCouplingDynamicAnalysis))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_5851.ConceptGearSetDynamicAnalysis]':
        '''List[ConceptGearSetDynamicAnalysis]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_5851.ConceptGearSetDynamicAnalysis))
        return value

    @property
    def cv_ts(self) -> 'List[_5861.CVTDynamicAnalysis]':
        '''List[CVTDynamicAnalysis]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_5861.CVTDynamicAnalysis))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_5865.CylindricalGearSetDynamicAnalysis]':
        '''List[CylindricalGearSetDynamicAnalysis]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_5865.CylindricalGearSetDynamicAnalysis))
        return value

    @property
    def face_gear_sets(self) -> 'List[_5873.FaceGearSetDynamicAnalysis]':
        '''List[FaceGearSetDynamicAnalysis]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_5873.FaceGearSetDynamicAnalysis))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_5874.FlexiblePinAssemblyDynamicAnalysis]':
        '''List[FlexiblePinAssemblyDynamicAnalysis]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_5874.FlexiblePinAssemblyDynamicAnalysis))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_5881.HypoidGearSetDynamicAnalysis]':
        '''List[HypoidGearSetDynamicAnalysis]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_5881.HypoidGearSetDynamicAnalysis))
        return value

    @property
    def imported_fe_components(self) -> 'List[_5882.ImportedFEComponentDynamicAnalysis]':
        '''List[ImportedFEComponentDynamicAnalysis]: 'ImportedFEComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ImportedFEComponents, constructor.new(_5882.ImportedFEComponentDynamicAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_5889.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_5889.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_5892.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_5892.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis))
        return value

    @property
    def mass_discs(self) -> 'List[_5893.MassDiscDynamicAnalysis]':
        '''List[MassDiscDynamicAnalysis]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_5893.MassDiscDynamicAnalysis))
        return value

    @property
    def measurement_components(self) -> 'List[_5894.MeasurementComponentDynamicAnalysis]':
        '''List[MeasurementComponentDynamicAnalysis]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_5894.MeasurementComponentDynamicAnalysis))
        return value

    @property
    def oil_seals(self) -> 'List[_5896.OilSealDynamicAnalysis]':
        '''List[OilSealDynamicAnalysis]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_5896.OilSealDynamicAnalysis))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_5899.PartToPartShearCouplingDynamicAnalysis]':
        '''List[PartToPartShearCouplingDynamicAnalysis]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_5899.PartToPartShearCouplingDynamicAnalysis))
        return value

    @property
    def planet_carriers(self) -> 'List[_5903.PlanetCarrierDynamicAnalysis]':
        '''List[PlanetCarrierDynamicAnalysis]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_5903.PlanetCarrierDynamicAnalysis))
        return value

    @property
    def point_loads(self) -> 'List[_5904.PointLoadDynamicAnalysis]':
        '''List[PointLoadDynamicAnalysis]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_5904.PointLoadDynamicAnalysis))
        return value

    @property
    def power_loads(self) -> 'List[_5905.PowerLoadDynamicAnalysis]':
        '''List[PowerLoadDynamicAnalysis]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_5905.PowerLoadDynamicAnalysis))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_5912.ShaftHubConnectionDynamicAnalysis]':
        '''List[ShaftHubConnectionDynamicAnalysis]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_5912.ShaftHubConnectionDynamicAnalysis))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_5907.RollingRingAssemblyDynamicAnalysis]':
        '''List[RollingRingAssemblyDynamicAnalysis]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_5907.RollingRingAssemblyDynamicAnalysis))
        return value

    @property
    def shafts(self) -> 'List[_5911.ShaftDynamicAnalysis]':
        '''List[ShaftDynamicAnalysis]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_5911.ShaftDynamicAnalysis))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_5917.SpiralBevelGearSetDynamicAnalysis]':
        '''List[SpiralBevelGearSetDynamicAnalysis]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_5917.SpiralBevelGearSetDynamicAnalysis))
        return value

    @property
    def spring_dampers(self) -> 'List[_5919.SpringDamperDynamicAnalysis]':
        '''List[SpringDamperDynamicAnalysis]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_5919.SpringDamperDynamicAnalysis))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_5923.StraightBevelDiffGearSetDynamicAnalysis]':
        '''List[StraightBevelDiffGearSetDynamicAnalysis]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_5923.StraightBevelDiffGearSetDynamicAnalysis))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_5926.StraightBevelGearSetDynamicAnalysis]':
        '''List[StraightBevelGearSetDynamicAnalysis]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_5926.StraightBevelGearSetDynamicAnalysis))
        return value

    @property
    def synchronisers(self) -> 'List[_5929.SynchroniserDynamicAnalysis]':
        '''List[SynchroniserDynamicAnalysis]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_5929.SynchroniserDynamicAnalysis))
        return value

    @property
    def torque_converters(self) -> 'List[_5934.TorqueConverterDynamicAnalysis]':
        '''List[TorqueConverterDynamicAnalysis]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_5934.TorqueConverterDynamicAnalysis))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_5937.UnbalancedMassDynamicAnalysis]':
        '''List[UnbalancedMassDynamicAnalysis]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_5937.UnbalancedMassDynamicAnalysis))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_5941.WormGearSetDynamicAnalysis]':
        '''List[WormGearSetDynamicAnalysis]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_5941.WormGearSetDynamicAnalysis))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_5944.ZerolBevelGearSetDynamicAnalysis]':
        '''List[ZerolBevelGearSetDynamicAnalysis]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_5944.ZerolBevelGearSetDynamicAnalysis))
        return value
