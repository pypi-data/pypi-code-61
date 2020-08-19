'''_3995.py

AssemblyModalAnalysesAtSpeeds
'''


from typing import List

from mastapy.system_model.part_model import _2002
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6080
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns import (
    _3996, _3998, _4001, _4008,
    _4007, _4011, _4016, _4019,
    _4029, _4033, _4040, _4041,
    _4048, _4049, _4056, _4059,
    _4060, _4061, _4065, _4069,
    _4072, _4073, _4074, _4080,
    _4076, _4081, _4086, _4089,
    _4093, _4096, _4100, _4104,
    _4107, _4111, _4114, _3990
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_MODAL_ANALYSES_AT_SPEEDS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtSpeedsNS', 'AssemblyModalAnalysesAtSpeeds')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyModalAnalysesAtSpeeds',)


class AssemblyModalAnalysesAtSpeeds(_3990.AbstractAssemblyModalAnalysesAtSpeeds):
    '''AssemblyModalAnalysesAtSpeeds

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_MODAL_ANALYSES_AT_SPEEDS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyModalAnalysesAtSpeeds.TYPE'):
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
    def bearings(self) -> 'List[_3996.BearingModalAnalysesAtSpeeds]':
        '''List[BearingModalAnalysesAtSpeeds]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_3996.BearingModalAnalysesAtSpeeds))
        return value

    @property
    def belt_drives(self) -> 'List[_3998.BeltDriveModalAnalysesAtSpeeds]':
        '''List[BeltDriveModalAnalysesAtSpeeds]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_3998.BeltDriveModalAnalysesAtSpeeds))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_4001.BevelDifferentialGearSetModalAnalysesAtSpeeds]':
        '''List[BevelDifferentialGearSetModalAnalysesAtSpeeds]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_4001.BevelDifferentialGearSetModalAnalysesAtSpeeds))
        return value

    @property
    def bolts(self) -> 'List[_4008.BoltModalAnalysesAtSpeeds]':
        '''List[BoltModalAnalysesAtSpeeds]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_4008.BoltModalAnalysesAtSpeeds))
        return value

    @property
    def bolted_joints(self) -> 'List[_4007.BoltedJointModalAnalysesAtSpeeds]':
        '''List[BoltedJointModalAnalysesAtSpeeds]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_4007.BoltedJointModalAnalysesAtSpeeds))
        return value

    @property
    def clutches(self) -> 'List[_4011.ClutchModalAnalysesAtSpeeds]':
        '''List[ClutchModalAnalysesAtSpeeds]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_4011.ClutchModalAnalysesAtSpeeds))
        return value

    @property
    def concept_couplings(self) -> 'List[_4016.ConceptCouplingModalAnalysesAtSpeeds]':
        '''List[ConceptCouplingModalAnalysesAtSpeeds]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_4016.ConceptCouplingModalAnalysesAtSpeeds))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_4019.ConceptGearSetModalAnalysesAtSpeeds]':
        '''List[ConceptGearSetModalAnalysesAtSpeeds]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_4019.ConceptGearSetModalAnalysesAtSpeeds))
        return value

    @property
    def cv_ts(self) -> 'List[_4029.CVTModalAnalysesAtSpeeds]':
        '''List[CVTModalAnalysesAtSpeeds]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_4029.CVTModalAnalysesAtSpeeds))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_4033.CylindricalGearSetModalAnalysesAtSpeeds]':
        '''List[CylindricalGearSetModalAnalysesAtSpeeds]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_4033.CylindricalGearSetModalAnalysesAtSpeeds))
        return value

    @property
    def face_gear_sets(self) -> 'List[_4040.FaceGearSetModalAnalysesAtSpeeds]':
        '''List[FaceGearSetModalAnalysesAtSpeeds]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_4040.FaceGearSetModalAnalysesAtSpeeds))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_4041.FlexiblePinAssemblyModalAnalysesAtSpeeds]':
        '''List[FlexiblePinAssemblyModalAnalysesAtSpeeds]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_4041.FlexiblePinAssemblyModalAnalysesAtSpeeds))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_4048.HypoidGearSetModalAnalysesAtSpeeds]':
        '''List[HypoidGearSetModalAnalysesAtSpeeds]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_4048.HypoidGearSetModalAnalysesAtSpeeds))
        return value

    @property
    def imported_fe_components(self) -> 'List[_4049.ImportedFEComponentModalAnalysesAtSpeeds]':
        '''List[ImportedFEComponentModalAnalysesAtSpeeds]: 'ImportedFEComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ImportedFEComponents, constructor.new(_4049.ImportedFEComponentModalAnalysesAtSpeeds))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_4056.KlingelnbergCycloPalloidHypoidGearSetModalAnalysesAtSpeeds]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetModalAnalysesAtSpeeds]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_4056.KlingelnbergCycloPalloidHypoidGearSetModalAnalysesAtSpeeds))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_4059.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysesAtSpeeds]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysesAtSpeeds]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_4059.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysesAtSpeeds))
        return value

    @property
    def mass_discs(self) -> 'List[_4060.MassDiscModalAnalysesAtSpeeds]':
        '''List[MassDiscModalAnalysesAtSpeeds]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_4060.MassDiscModalAnalysesAtSpeeds))
        return value

    @property
    def measurement_components(self) -> 'List[_4061.MeasurementComponentModalAnalysesAtSpeeds]':
        '''List[MeasurementComponentModalAnalysesAtSpeeds]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_4061.MeasurementComponentModalAnalysesAtSpeeds))
        return value

    @property
    def oil_seals(self) -> 'List[_4065.OilSealModalAnalysesAtSpeeds]':
        '''List[OilSealModalAnalysesAtSpeeds]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_4065.OilSealModalAnalysesAtSpeeds))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_4069.PartToPartShearCouplingModalAnalysesAtSpeeds]':
        '''List[PartToPartShearCouplingModalAnalysesAtSpeeds]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_4069.PartToPartShearCouplingModalAnalysesAtSpeeds))
        return value

    @property
    def planet_carriers(self) -> 'List[_4072.PlanetCarrierModalAnalysesAtSpeeds]':
        '''List[PlanetCarrierModalAnalysesAtSpeeds]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_4072.PlanetCarrierModalAnalysesAtSpeeds))
        return value

    @property
    def point_loads(self) -> 'List[_4073.PointLoadModalAnalysesAtSpeeds]':
        '''List[PointLoadModalAnalysesAtSpeeds]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_4073.PointLoadModalAnalysesAtSpeeds))
        return value

    @property
    def power_loads(self) -> 'List[_4074.PowerLoadModalAnalysesAtSpeeds]':
        '''List[PowerLoadModalAnalysesAtSpeeds]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_4074.PowerLoadModalAnalysesAtSpeeds))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_4080.ShaftHubConnectionModalAnalysesAtSpeeds]':
        '''List[ShaftHubConnectionModalAnalysesAtSpeeds]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_4080.ShaftHubConnectionModalAnalysesAtSpeeds))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_4076.RollingRingAssemblyModalAnalysesAtSpeeds]':
        '''List[RollingRingAssemblyModalAnalysesAtSpeeds]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_4076.RollingRingAssemblyModalAnalysesAtSpeeds))
        return value

    @property
    def shafts(self) -> 'List[_4081.ShaftModalAnalysesAtSpeeds]':
        '''List[ShaftModalAnalysesAtSpeeds]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_4081.ShaftModalAnalysesAtSpeeds))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_4086.SpiralBevelGearSetModalAnalysesAtSpeeds]':
        '''List[SpiralBevelGearSetModalAnalysesAtSpeeds]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_4086.SpiralBevelGearSetModalAnalysesAtSpeeds))
        return value

    @property
    def spring_dampers(self) -> 'List[_4089.SpringDamperModalAnalysesAtSpeeds]':
        '''List[SpringDamperModalAnalysesAtSpeeds]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_4089.SpringDamperModalAnalysesAtSpeeds))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_4093.StraightBevelDiffGearSetModalAnalysesAtSpeeds]':
        '''List[StraightBevelDiffGearSetModalAnalysesAtSpeeds]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_4093.StraightBevelDiffGearSetModalAnalysesAtSpeeds))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_4096.StraightBevelGearSetModalAnalysesAtSpeeds]':
        '''List[StraightBevelGearSetModalAnalysesAtSpeeds]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_4096.StraightBevelGearSetModalAnalysesAtSpeeds))
        return value

    @property
    def synchronisers(self) -> 'List[_4100.SynchroniserModalAnalysesAtSpeeds]':
        '''List[SynchroniserModalAnalysesAtSpeeds]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_4100.SynchroniserModalAnalysesAtSpeeds))
        return value

    @property
    def torque_converters(self) -> 'List[_4104.TorqueConverterModalAnalysesAtSpeeds]':
        '''List[TorqueConverterModalAnalysesAtSpeeds]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_4104.TorqueConverterModalAnalysesAtSpeeds))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_4107.UnbalancedMassModalAnalysesAtSpeeds]':
        '''List[UnbalancedMassModalAnalysesAtSpeeds]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_4107.UnbalancedMassModalAnalysesAtSpeeds))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_4111.WormGearSetModalAnalysesAtSpeeds]':
        '''List[WormGearSetModalAnalysesAtSpeeds]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_4111.WormGearSetModalAnalysesAtSpeeds))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_4114.ZerolBevelGearSetModalAnalysesAtSpeeds]':
        '''List[ZerolBevelGearSetModalAnalysesAtSpeeds]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_4114.ZerolBevelGearSetModalAnalysesAtSpeeds))
        return value
