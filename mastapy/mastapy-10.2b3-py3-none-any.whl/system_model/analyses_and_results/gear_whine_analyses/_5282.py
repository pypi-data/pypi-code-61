'''_5282.py

AssemblyGearWhineAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _2002
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6080
from mastapy.system_model.analyses_and_results.system_deflections import _2237
from mastapy.system_model.analyses_and_results.gear_whine_analyses import (
    _5347, _5283, _5285, _5288,
    _5295, _5294, _5297, _5303,
    _5307, _5317, _5321, _5339,
    _5340, _5356, _5357, _5364,
    _5367, _5368, _5369, _5371,
    _5374, _5379, _5380, _5381,
    _5388, _5383, _5387, _5395,
    _5397, _5401, _5404, _5407,
    _5412, _5416, _5420, _5423,
    _5276
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'AssemblyGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyGearWhineAnalysis',)


class AssemblyGearWhineAnalysis(_5276.AbstractAssemblyGearWhineAnalysis):
    '''AssemblyGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_GEAR_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyGearWhineAnalysis.TYPE'):
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
    def system_deflection_results(self) -> '_2237.AssemblySystemDeflection':
        '''AssemblySystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2237.AssemblySystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None

    @property
    def loaded_gear_sets(self) -> 'List[_5347.GearSetGearWhineAnalysis]':
        '''List[GearSetGearWhineAnalysis]: 'LoadedGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadedGearSets, constructor.new(_5347.GearSetGearWhineAnalysis))
        return value

    @property
    def bearings(self) -> 'List[_5283.BearingGearWhineAnalysis]':
        '''List[BearingGearWhineAnalysis]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_5283.BearingGearWhineAnalysis))
        return value

    @property
    def belt_drives(self) -> 'List[_5285.BeltDriveGearWhineAnalysis]':
        '''List[BeltDriveGearWhineAnalysis]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_5285.BeltDriveGearWhineAnalysis))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_5288.BevelDifferentialGearSetGearWhineAnalysis]':
        '''List[BevelDifferentialGearSetGearWhineAnalysis]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_5288.BevelDifferentialGearSetGearWhineAnalysis))
        return value

    @property
    def bolts(self) -> 'List[_5295.BoltGearWhineAnalysis]':
        '''List[BoltGearWhineAnalysis]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_5295.BoltGearWhineAnalysis))
        return value

    @property
    def bolted_joints(self) -> 'List[_5294.BoltedJointGearWhineAnalysis]':
        '''List[BoltedJointGearWhineAnalysis]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_5294.BoltedJointGearWhineAnalysis))
        return value

    @property
    def clutches(self) -> 'List[_5297.ClutchGearWhineAnalysis]':
        '''List[ClutchGearWhineAnalysis]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_5297.ClutchGearWhineAnalysis))
        return value

    @property
    def concept_couplings(self) -> 'List[_5303.ConceptCouplingGearWhineAnalysis]':
        '''List[ConceptCouplingGearWhineAnalysis]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_5303.ConceptCouplingGearWhineAnalysis))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_5307.ConceptGearSetGearWhineAnalysis]':
        '''List[ConceptGearSetGearWhineAnalysis]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_5307.ConceptGearSetGearWhineAnalysis))
        return value

    @property
    def cv_ts(self) -> 'List[_5317.CVTGearWhineAnalysis]':
        '''List[CVTGearWhineAnalysis]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_5317.CVTGearWhineAnalysis))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_5321.CylindricalGearSetGearWhineAnalysis]':
        '''List[CylindricalGearSetGearWhineAnalysis]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_5321.CylindricalGearSetGearWhineAnalysis))
        return value

    @property
    def face_gear_sets(self) -> 'List[_5339.FaceGearSetGearWhineAnalysis]':
        '''List[FaceGearSetGearWhineAnalysis]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_5339.FaceGearSetGearWhineAnalysis))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_5340.FlexiblePinAssemblyGearWhineAnalysis]':
        '''List[FlexiblePinAssemblyGearWhineAnalysis]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_5340.FlexiblePinAssemblyGearWhineAnalysis))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_5356.HypoidGearSetGearWhineAnalysis]':
        '''List[HypoidGearSetGearWhineAnalysis]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_5356.HypoidGearSetGearWhineAnalysis))
        return value

    @property
    def imported_fe_components(self) -> 'List[_5357.ImportedFEComponentGearWhineAnalysis]':
        '''List[ImportedFEComponentGearWhineAnalysis]: 'ImportedFEComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ImportedFEComponents, constructor.new(_5357.ImportedFEComponentGearWhineAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_5364.KlingelnbergCycloPalloidHypoidGearSetGearWhineAnalysis]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetGearWhineAnalysis]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_5364.KlingelnbergCycloPalloidHypoidGearSetGearWhineAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_5367.KlingelnbergCycloPalloidSpiralBevelGearSetGearWhineAnalysis]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetGearWhineAnalysis]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_5367.KlingelnbergCycloPalloidSpiralBevelGearSetGearWhineAnalysis))
        return value

    @property
    def mass_discs(self) -> 'List[_5368.MassDiscGearWhineAnalysis]':
        '''List[MassDiscGearWhineAnalysis]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_5368.MassDiscGearWhineAnalysis))
        return value

    @property
    def measurement_components(self) -> 'List[_5369.MeasurementComponentGearWhineAnalysis]':
        '''List[MeasurementComponentGearWhineAnalysis]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_5369.MeasurementComponentGearWhineAnalysis))
        return value

    @property
    def oil_seals(self) -> 'List[_5371.OilSealGearWhineAnalysis]':
        '''List[OilSealGearWhineAnalysis]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_5371.OilSealGearWhineAnalysis))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_5374.PartToPartShearCouplingGearWhineAnalysis]':
        '''List[PartToPartShearCouplingGearWhineAnalysis]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_5374.PartToPartShearCouplingGearWhineAnalysis))
        return value

    @property
    def planet_carriers(self) -> 'List[_5379.PlanetCarrierGearWhineAnalysis]':
        '''List[PlanetCarrierGearWhineAnalysis]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_5379.PlanetCarrierGearWhineAnalysis))
        return value

    @property
    def point_loads(self) -> 'List[_5380.PointLoadGearWhineAnalysis]':
        '''List[PointLoadGearWhineAnalysis]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_5380.PointLoadGearWhineAnalysis))
        return value

    @property
    def power_loads(self) -> 'List[_5381.PowerLoadGearWhineAnalysis]':
        '''List[PowerLoadGearWhineAnalysis]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_5381.PowerLoadGearWhineAnalysis))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_5388.ShaftHubConnectionGearWhineAnalysis]':
        '''List[ShaftHubConnectionGearWhineAnalysis]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_5388.ShaftHubConnectionGearWhineAnalysis))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_5383.RollingRingAssemblyGearWhineAnalysis]':
        '''List[RollingRingAssemblyGearWhineAnalysis]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_5383.RollingRingAssemblyGearWhineAnalysis))
        return value

    @property
    def shafts(self) -> 'List[_5387.ShaftGearWhineAnalysis]':
        '''List[ShaftGearWhineAnalysis]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_5387.ShaftGearWhineAnalysis))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_5395.SpiralBevelGearSetGearWhineAnalysis]':
        '''List[SpiralBevelGearSetGearWhineAnalysis]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_5395.SpiralBevelGearSetGearWhineAnalysis))
        return value

    @property
    def spring_dampers(self) -> 'List[_5397.SpringDamperGearWhineAnalysis]':
        '''List[SpringDamperGearWhineAnalysis]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_5397.SpringDamperGearWhineAnalysis))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_5401.StraightBevelDiffGearSetGearWhineAnalysis]':
        '''List[StraightBevelDiffGearSetGearWhineAnalysis]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_5401.StraightBevelDiffGearSetGearWhineAnalysis))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_5404.StraightBevelGearSetGearWhineAnalysis]':
        '''List[StraightBevelGearSetGearWhineAnalysis]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_5404.StraightBevelGearSetGearWhineAnalysis))
        return value

    @property
    def synchronisers(self) -> 'List[_5407.SynchroniserGearWhineAnalysis]':
        '''List[SynchroniserGearWhineAnalysis]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_5407.SynchroniserGearWhineAnalysis))
        return value

    @property
    def torque_converters(self) -> 'List[_5412.TorqueConverterGearWhineAnalysis]':
        '''List[TorqueConverterGearWhineAnalysis]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_5412.TorqueConverterGearWhineAnalysis))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_5416.UnbalancedMassGearWhineAnalysis]':
        '''List[UnbalancedMassGearWhineAnalysis]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_5416.UnbalancedMassGearWhineAnalysis))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_5420.WormGearSetGearWhineAnalysis]':
        '''List[WormGearSetGearWhineAnalysis]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_5420.WormGearSetGearWhineAnalysis))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_5423.ZerolBevelGearSetGearWhineAnalysis]':
        '''List[ZerolBevelGearSetGearWhineAnalysis]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_5423.ZerolBevelGearSetGearWhineAnalysis))
        return value
