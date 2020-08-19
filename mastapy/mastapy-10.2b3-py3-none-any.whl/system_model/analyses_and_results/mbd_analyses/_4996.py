'''_4996.py

AssemblyMultiBodyDynamicsAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _2002
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6080
from mastapy.system_model.analyses_and_results.mbd_analyses import (
    _4997, _5000, _5003, _5010,
    _5009, _5013, _5019, _5022,
    _5032, _5036, _5042, _5043,
    _5051, _5052, _5063, _5066,
    _5067, _5071, _5074, _5078,
    _5081, _5082, _5083, _5091,
    _5085, _5092, _5098, _5101,
    _5104, _5107, _5111, _5116,
    _5120, _5125, _5128, _5057,
    _4991, _5047, _4990
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_MULTI_BODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'AssemblyMultiBodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyMultiBodyDynamicsAnalysis',)


class AssemblyMultiBodyDynamicsAnalysis(_4990.AbstractAssemblyMultiBodyDynamicsAnalysis):
    '''AssemblyMultiBodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_MULTI_BODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyMultiBodyDynamicsAnalysis.TYPE'):
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
    def bearings(self) -> 'List[_4997.BearingMultiBodyDynamicsAnalysis]':
        '''List[BearingMultiBodyDynamicsAnalysis]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_4997.BearingMultiBodyDynamicsAnalysis))
        return value

    @property
    def belt_drives(self) -> 'List[_5000.BeltDriveMultiBodyDynamicsAnalysis]':
        '''List[BeltDriveMultiBodyDynamicsAnalysis]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_5000.BeltDriveMultiBodyDynamicsAnalysis))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_5003.BevelDifferentialGearSetMultiBodyDynamicsAnalysis]':
        '''List[BevelDifferentialGearSetMultiBodyDynamicsAnalysis]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_5003.BevelDifferentialGearSetMultiBodyDynamicsAnalysis))
        return value

    @property
    def bolts(self) -> 'List[_5010.BoltMultiBodyDynamicsAnalysis]':
        '''List[BoltMultiBodyDynamicsAnalysis]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_5010.BoltMultiBodyDynamicsAnalysis))
        return value

    @property
    def bolted_joints(self) -> 'List[_5009.BoltedJointMultiBodyDynamicsAnalysis]':
        '''List[BoltedJointMultiBodyDynamicsAnalysis]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_5009.BoltedJointMultiBodyDynamicsAnalysis))
        return value

    @property
    def clutches(self) -> 'List[_5013.ClutchMultiBodyDynamicsAnalysis]':
        '''List[ClutchMultiBodyDynamicsAnalysis]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_5013.ClutchMultiBodyDynamicsAnalysis))
        return value

    @property
    def concept_couplings(self) -> 'List[_5019.ConceptCouplingMultiBodyDynamicsAnalysis]':
        '''List[ConceptCouplingMultiBodyDynamicsAnalysis]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_5019.ConceptCouplingMultiBodyDynamicsAnalysis))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_5022.ConceptGearSetMultiBodyDynamicsAnalysis]':
        '''List[ConceptGearSetMultiBodyDynamicsAnalysis]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_5022.ConceptGearSetMultiBodyDynamicsAnalysis))
        return value

    @property
    def cv_ts(self) -> 'List[_5032.CVTMultiBodyDynamicsAnalysis]':
        '''List[CVTMultiBodyDynamicsAnalysis]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_5032.CVTMultiBodyDynamicsAnalysis))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_5036.CylindricalGearSetMultiBodyDynamicsAnalysis]':
        '''List[CylindricalGearSetMultiBodyDynamicsAnalysis]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_5036.CylindricalGearSetMultiBodyDynamicsAnalysis))
        return value

    @property
    def face_gear_sets(self) -> 'List[_5042.FaceGearSetMultiBodyDynamicsAnalysis]':
        '''List[FaceGearSetMultiBodyDynamicsAnalysis]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_5042.FaceGearSetMultiBodyDynamicsAnalysis))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_5043.FlexiblePinAssemblyMultiBodyDynamicsAnalysis]':
        '''List[FlexiblePinAssemblyMultiBodyDynamicsAnalysis]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_5043.FlexiblePinAssemblyMultiBodyDynamicsAnalysis))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_5051.HypoidGearSetMultiBodyDynamicsAnalysis]':
        '''List[HypoidGearSetMultiBodyDynamicsAnalysis]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_5051.HypoidGearSetMultiBodyDynamicsAnalysis))
        return value

    @property
    def imported_fe_components(self) -> 'List[_5052.ImportedFEComponentMultiBodyDynamicsAnalysis]':
        '''List[ImportedFEComponentMultiBodyDynamicsAnalysis]: 'ImportedFEComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ImportedFEComponents, constructor.new(_5052.ImportedFEComponentMultiBodyDynamicsAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_5063.KlingelnbergCycloPalloidHypoidGearSetMultiBodyDynamicsAnalysis]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetMultiBodyDynamicsAnalysis]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_5063.KlingelnbergCycloPalloidHypoidGearSetMultiBodyDynamicsAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_5066.KlingelnbergCycloPalloidSpiralBevelGearSetMultiBodyDynamicsAnalysis]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetMultiBodyDynamicsAnalysis]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_5066.KlingelnbergCycloPalloidSpiralBevelGearSetMultiBodyDynamicsAnalysis))
        return value

    @property
    def mass_discs(self) -> 'List[_5067.MassDiscMultiBodyDynamicsAnalysis]':
        '''List[MassDiscMultiBodyDynamicsAnalysis]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_5067.MassDiscMultiBodyDynamicsAnalysis))
        return value

    @property
    def measurement_components(self) -> 'List[_5071.MeasurementComponentMultiBodyDynamicsAnalysis]':
        '''List[MeasurementComponentMultiBodyDynamicsAnalysis]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_5071.MeasurementComponentMultiBodyDynamicsAnalysis))
        return value

    @property
    def oil_seals(self) -> 'List[_5074.OilSealMultiBodyDynamicsAnalysis]':
        '''List[OilSealMultiBodyDynamicsAnalysis]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_5074.OilSealMultiBodyDynamicsAnalysis))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_5078.PartToPartShearCouplingMultiBodyDynamicsAnalysis]':
        '''List[PartToPartShearCouplingMultiBodyDynamicsAnalysis]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_5078.PartToPartShearCouplingMultiBodyDynamicsAnalysis))
        return value

    @property
    def planet_carriers(self) -> 'List[_5081.PlanetCarrierMultiBodyDynamicsAnalysis]':
        '''List[PlanetCarrierMultiBodyDynamicsAnalysis]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_5081.PlanetCarrierMultiBodyDynamicsAnalysis))
        return value

    @property
    def point_loads(self) -> 'List[_5082.PointLoadMultiBodyDynamicsAnalysis]':
        '''List[PointLoadMultiBodyDynamicsAnalysis]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_5082.PointLoadMultiBodyDynamicsAnalysis))
        return value

    @property
    def power_loads(self) -> 'List[_5083.PowerLoadMultiBodyDynamicsAnalysis]':
        '''List[PowerLoadMultiBodyDynamicsAnalysis]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_5083.PowerLoadMultiBodyDynamicsAnalysis))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_5091.ShaftHubConnectionMultiBodyDynamicsAnalysis]':
        '''List[ShaftHubConnectionMultiBodyDynamicsAnalysis]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_5091.ShaftHubConnectionMultiBodyDynamicsAnalysis))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_5085.RollingRingAssemblyMultiBodyDynamicsAnalysis]':
        '''List[RollingRingAssemblyMultiBodyDynamicsAnalysis]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_5085.RollingRingAssemblyMultiBodyDynamicsAnalysis))
        return value

    @property
    def shafts(self) -> 'List[_5092.ShaftMultiBodyDynamicsAnalysis]':
        '''List[ShaftMultiBodyDynamicsAnalysis]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_5092.ShaftMultiBodyDynamicsAnalysis))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_5098.SpiralBevelGearSetMultiBodyDynamicsAnalysis]':
        '''List[SpiralBevelGearSetMultiBodyDynamicsAnalysis]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_5098.SpiralBevelGearSetMultiBodyDynamicsAnalysis))
        return value

    @property
    def spring_dampers(self) -> 'List[_5101.SpringDamperMultiBodyDynamicsAnalysis]':
        '''List[SpringDamperMultiBodyDynamicsAnalysis]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_5101.SpringDamperMultiBodyDynamicsAnalysis))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_5104.StraightBevelDiffGearSetMultiBodyDynamicsAnalysis]':
        '''List[StraightBevelDiffGearSetMultiBodyDynamicsAnalysis]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_5104.StraightBevelDiffGearSetMultiBodyDynamicsAnalysis))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_5107.StraightBevelGearSetMultiBodyDynamicsAnalysis]':
        '''List[StraightBevelGearSetMultiBodyDynamicsAnalysis]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_5107.StraightBevelGearSetMultiBodyDynamicsAnalysis))
        return value

    @property
    def synchronisers(self) -> 'List[_5111.SynchroniserMultiBodyDynamicsAnalysis]':
        '''List[SynchroniserMultiBodyDynamicsAnalysis]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_5111.SynchroniserMultiBodyDynamicsAnalysis))
        return value

    @property
    def torque_converters(self) -> 'List[_5116.TorqueConverterMultiBodyDynamicsAnalysis]':
        '''List[TorqueConverterMultiBodyDynamicsAnalysis]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_5116.TorqueConverterMultiBodyDynamicsAnalysis))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_5120.UnbalancedMassMultiBodyDynamicsAnalysis]':
        '''List[UnbalancedMassMultiBodyDynamicsAnalysis]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_5120.UnbalancedMassMultiBodyDynamicsAnalysis))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_5125.WormGearSetMultiBodyDynamicsAnalysis]':
        '''List[WormGearSetMultiBodyDynamicsAnalysis]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_5125.WormGearSetMultiBodyDynamicsAnalysis))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_5128.ZerolBevelGearSetMultiBodyDynamicsAnalysis]':
        '''List[ZerolBevelGearSetMultiBodyDynamicsAnalysis]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_5128.ZerolBevelGearSetMultiBodyDynamicsAnalysis))
        return value

    @property
    def connections(self) -> 'List[_5057.InterMountableComponentConnectionMultiBodyDynamicsAnalysis]':
        '''List[InterMountableComponentConnectionMultiBodyDynamicsAnalysis]: 'Connections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Connections, constructor.new(_5057.InterMountableComponentConnectionMultiBodyDynamicsAnalysis))
        return value

    @property
    def shafts_and_housings(self) -> 'List[_4991.AbstractShaftOrHousingMultiBodyDynamicsAnalysis]':
        '''List[AbstractShaftOrHousingMultiBodyDynamicsAnalysis]: 'ShaftsAndHousings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftsAndHousings, constructor.new(_4991.AbstractShaftOrHousingMultiBodyDynamicsAnalysis))
        return value

    @property
    def gear_sets(self) -> 'List[_5047.GearSetMultiBodyDynamicsAnalysis]':
        '''List[GearSetMultiBodyDynamicsAnalysis]: 'GearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.GearSets, constructor.new(_5047.GearSetMultiBodyDynamicsAnalysis))
        return value
