'''_4120.py

AssemblyCompoundModalAnalysesAtSpeeds
'''


from typing import List

from mastapy.system_model.part_model import _2002
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns import _3995
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns.compound import (
    _4121, _4123, _4126, _4132,
    _4133, _4134, _4139, _4144,
    _4154, _4158, _4164, _4165,
    _4172, _4173, _4180, _4183,
    _4184, _4185, _4187, _4189,
    _4194, _4195, _4196, _4203,
    _4198, _4202, _4208, _4209,
    _4214, _4217, _4220, _4224,
    _4228, _4232, _4235, _4115
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_COMPOUND_MODAL_ANALYSES_AT_SPEEDS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtSpeedsNS.Compound', 'AssemblyCompoundModalAnalysesAtSpeeds')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyCompoundModalAnalysesAtSpeeds',)


class AssemblyCompoundModalAnalysesAtSpeeds(_4115.AbstractAssemblyCompoundModalAnalysesAtSpeeds):
    '''AssemblyCompoundModalAnalysesAtSpeeds

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_COMPOUND_MODAL_ANALYSES_AT_SPEEDS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyCompoundModalAnalysesAtSpeeds.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2002.Assembly':
        '''Assembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2002.Assembly)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def assembly_design(self) -> '_2002.Assembly':
        '''Assembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2002.Assembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def load_case_analyses_ready(self) -> 'List[_3995.AssemblyModalAnalysesAtSpeeds]':
        '''List[AssemblyModalAnalysesAtSpeeds]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_3995.AssemblyModalAnalysesAtSpeeds))
        return value

    @property
    def assembly_modal_analyses_at_speeds_load_cases(self) -> 'List[_3995.AssemblyModalAnalysesAtSpeeds]':
        '''List[AssemblyModalAnalysesAtSpeeds]: 'AssemblyModalAnalysesAtSpeedsLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyModalAnalysesAtSpeedsLoadCases, constructor.new(_3995.AssemblyModalAnalysesAtSpeeds))
        return value

    @property
    def bearings(self) -> 'List[_4121.BearingCompoundModalAnalysesAtSpeeds]':
        '''List[BearingCompoundModalAnalysesAtSpeeds]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_4121.BearingCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def belt_drives(self) -> 'List[_4123.BeltDriveCompoundModalAnalysesAtSpeeds]':
        '''List[BeltDriveCompoundModalAnalysesAtSpeeds]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_4123.BeltDriveCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_4126.BevelDifferentialGearSetCompoundModalAnalysesAtSpeeds]':
        '''List[BevelDifferentialGearSetCompoundModalAnalysesAtSpeeds]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_4126.BevelDifferentialGearSetCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def bolts(self) -> 'List[_4132.BoltCompoundModalAnalysesAtSpeeds]':
        '''List[BoltCompoundModalAnalysesAtSpeeds]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_4132.BoltCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def bolted_joints(self) -> 'List[_4133.BoltedJointCompoundModalAnalysesAtSpeeds]':
        '''List[BoltedJointCompoundModalAnalysesAtSpeeds]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_4133.BoltedJointCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def clutches(self) -> 'List[_4134.ClutchCompoundModalAnalysesAtSpeeds]':
        '''List[ClutchCompoundModalAnalysesAtSpeeds]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_4134.ClutchCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def concept_couplings(self) -> 'List[_4139.ConceptCouplingCompoundModalAnalysesAtSpeeds]':
        '''List[ConceptCouplingCompoundModalAnalysesAtSpeeds]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_4139.ConceptCouplingCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_4144.ConceptGearSetCompoundModalAnalysesAtSpeeds]':
        '''List[ConceptGearSetCompoundModalAnalysesAtSpeeds]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_4144.ConceptGearSetCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def cv_ts(self) -> 'List[_4154.CVTCompoundModalAnalysesAtSpeeds]':
        '''List[CVTCompoundModalAnalysesAtSpeeds]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_4154.CVTCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_4158.CylindricalGearSetCompoundModalAnalysesAtSpeeds]':
        '''List[CylindricalGearSetCompoundModalAnalysesAtSpeeds]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_4158.CylindricalGearSetCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def face_gear_sets(self) -> 'List[_4164.FaceGearSetCompoundModalAnalysesAtSpeeds]':
        '''List[FaceGearSetCompoundModalAnalysesAtSpeeds]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_4164.FaceGearSetCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_4165.FlexiblePinAssemblyCompoundModalAnalysesAtSpeeds]':
        '''List[FlexiblePinAssemblyCompoundModalAnalysesAtSpeeds]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_4165.FlexiblePinAssemblyCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_4172.HypoidGearSetCompoundModalAnalysesAtSpeeds]':
        '''List[HypoidGearSetCompoundModalAnalysesAtSpeeds]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_4172.HypoidGearSetCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def imported_fe_components(self) -> 'List[_4173.ImportedFEComponentCompoundModalAnalysesAtSpeeds]':
        '''List[ImportedFEComponentCompoundModalAnalysesAtSpeeds]: 'ImportedFEComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ImportedFEComponents, constructor.new(_4173.ImportedFEComponentCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_4180.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysesAtSpeeds]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysesAtSpeeds]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_4180.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_4183.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysesAtSpeeds]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysesAtSpeeds]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_4183.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def mass_discs(self) -> 'List[_4184.MassDiscCompoundModalAnalysesAtSpeeds]':
        '''List[MassDiscCompoundModalAnalysesAtSpeeds]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_4184.MassDiscCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def measurement_components(self) -> 'List[_4185.MeasurementComponentCompoundModalAnalysesAtSpeeds]':
        '''List[MeasurementComponentCompoundModalAnalysesAtSpeeds]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_4185.MeasurementComponentCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def oil_seals(self) -> 'List[_4187.OilSealCompoundModalAnalysesAtSpeeds]':
        '''List[OilSealCompoundModalAnalysesAtSpeeds]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_4187.OilSealCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_4189.PartToPartShearCouplingCompoundModalAnalysesAtSpeeds]':
        '''List[PartToPartShearCouplingCompoundModalAnalysesAtSpeeds]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_4189.PartToPartShearCouplingCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def planet_carriers(self) -> 'List[_4194.PlanetCarrierCompoundModalAnalysesAtSpeeds]':
        '''List[PlanetCarrierCompoundModalAnalysesAtSpeeds]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_4194.PlanetCarrierCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def point_loads(self) -> 'List[_4195.PointLoadCompoundModalAnalysesAtSpeeds]':
        '''List[PointLoadCompoundModalAnalysesAtSpeeds]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_4195.PointLoadCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def power_loads(self) -> 'List[_4196.PowerLoadCompoundModalAnalysesAtSpeeds]':
        '''List[PowerLoadCompoundModalAnalysesAtSpeeds]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_4196.PowerLoadCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_4203.ShaftHubConnectionCompoundModalAnalysesAtSpeeds]':
        '''List[ShaftHubConnectionCompoundModalAnalysesAtSpeeds]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_4203.ShaftHubConnectionCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_4198.RollingRingAssemblyCompoundModalAnalysesAtSpeeds]':
        '''List[RollingRingAssemblyCompoundModalAnalysesAtSpeeds]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_4198.RollingRingAssemblyCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def shafts(self) -> 'List[_4202.ShaftCompoundModalAnalysesAtSpeeds]':
        '''List[ShaftCompoundModalAnalysesAtSpeeds]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_4202.ShaftCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_4208.SpiralBevelGearSetCompoundModalAnalysesAtSpeeds]':
        '''List[SpiralBevelGearSetCompoundModalAnalysesAtSpeeds]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_4208.SpiralBevelGearSetCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def spring_dampers(self) -> 'List[_4209.SpringDamperCompoundModalAnalysesAtSpeeds]':
        '''List[SpringDamperCompoundModalAnalysesAtSpeeds]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_4209.SpringDamperCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_4214.StraightBevelDiffGearSetCompoundModalAnalysesAtSpeeds]':
        '''List[StraightBevelDiffGearSetCompoundModalAnalysesAtSpeeds]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_4214.StraightBevelDiffGearSetCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_4217.StraightBevelGearSetCompoundModalAnalysesAtSpeeds]':
        '''List[StraightBevelGearSetCompoundModalAnalysesAtSpeeds]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_4217.StraightBevelGearSetCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def synchronisers(self) -> 'List[_4220.SynchroniserCompoundModalAnalysesAtSpeeds]':
        '''List[SynchroniserCompoundModalAnalysesAtSpeeds]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_4220.SynchroniserCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def torque_converters(self) -> 'List[_4224.TorqueConverterCompoundModalAnalysesAtSpeeds]':
        '''List[TorqueConverterCompoundModalAnalysesAtSpeeds]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_4224.TorqueConverterCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_4228.UnbalancedMassCompoundModalAnalysesAtSpeeds]':
        '''List[UnbalancedMassCompoundModalAnalysesAtSpeeds]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_4228.UnbalancedMassCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_4232.WormGearSetCompoundModalAnalysesAtSpeeds]':
        '''List[WormGearSetCompoundModalAnalysesAtSpeeds]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_4232.WormGearSetCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_4235.ZerolBevelGearSetCompoundModalAnalysesAtSpeeds]':
        '''List[ZerolBevelGearSetCompoundModalAnalysesAtSpeeds]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_4235.ZerolBevelGearSetCompoundModalAnalysesAtSpeeds))
        return value
