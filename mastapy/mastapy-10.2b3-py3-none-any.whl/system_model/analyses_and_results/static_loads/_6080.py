'''_6080.py

AssemblyLoadCase
'''


from typing import List

from mastapy.system_model.part_model import _2002
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import (
    _6081, _6083, _6086, _6093,
    _6092, _6096, _6101, _6104,
    _6116, _6122, _6142, _6143,
    _6162, _6163, _6171, _6174,
    _6175, _6176, _6180, _6185,
    _6189, _6192, _6193, _6200,
    _6196, _6201, _6207, _6210,
    _6214, _6217, _6221, _6227,
    _6234, _6238, _6241, _6074,
    _6094, _6147, _6073
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'AssemblyLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyLoadCase',)


class AssemblyLoadCase(_6073.AbstractAssemblyLoadCase):
    '''AssemblyLoadCase

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyLoadCase.TYPE'):
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
    def bearings(self) -> 'List[_6081.BearingLoadCase]':
        '''List[BearingLoadCase]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_6081.BearingLoadCase))
        return value

    @property
    def belt_drives(self) -> 'List[_6083.BeltDriveLoadCase]':
        '''List[BeltDriveLoadCase]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_6083.BeltDriveLoadCase))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_6086.BevelDifferentialGearSetLoadCase]':
        '''List[BevelDifferentialGearSetLoadCase]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_6086.BevelDifferentialGearSetLoadCase))
        return value

    @property
    def bolts(self) -> 'List[_6093.BoltLoadCase]':
        '''List[BoltLoadCase]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_6093.BoltLoadCase))
        return value

    @property
    def bolted_joints(self) -> 'List[_6092.BoltedJointLoadCase]':
        '''List[BoltedJointLoadCase]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_6092.BoltedJointLoadCase))
        return value

    @property
    def clutches(self) -> 'List[_6096.ClutchLoadCase]':
        '''List[ClutchLoadCase]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_6096.ClutchLoadCase))
        return value

    @property
    def concept_couplings(self) -> 'List[_6101.ConceptCouplingLoadCase]':
        '''List[ConceptCouplingLoadCase]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_6101.ConceptCouplingLoadCase))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_6104.ConceptGearSetLoadCase]':
        '''List[ConceptGearSetLoadCase]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_6104.ConceptGearSetLoadCase))
        return value

    @property
    def cv_ts(self) -> 'List[_6116.CVTLoadCase]':
        '''List[CVTLoadCase]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_6116.CVTLoadCase))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_6122.CylindricalGearSetLoadCase]':
        '''List[CylindricalGearSetLoadCase]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_6122.CylindricalGearSetLoadCase))
        return value

    @property
    def face_gear_sets(self) -> 'List[_6142.FaceGearSetLoadCase]':
        '''List[FaceGearSetLoadCase]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_6142.FaceGearSetLoadCase))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_6143.FlexiblePinAssemblyLoadCase]':
        '''List[FlexiblePinAssemblyLoadCase]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_6143.FlexiblePinAssemblyLoadCase))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_6162.HypoidGearSetLoadCase]':
        '''List[HypoidGearSetLoadCase]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_6162.HypoidGearSetLoadCase))
        return value

    @property
    def imported_fe_components(self) -> 'List[_6163.ImportedFEComponentLoadCase]':
        '''List[ImportedFEComponentLoadCase]: 'ImportedFEComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ImportedFEComponents, constructor.new(_6163.ImportedFEComponentLoadCase))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_6171.KlingelnbergCycloPalloidHypoidGearSetLoadCase]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetLoadCase]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_6171.KlingelnbergCycloPalloidHypoidGearSetLoadCase))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_6174.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_6174.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase))
        return value

    @property
    def mass_discs(self) -> 'List[_6175.MassDiscLoadCase]':
        '''List[MassDiscLoadCase]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_6175.MassDiscLoadCase))
        return value

    @property
    def measurement_components(self) -> 'List[_6176.MeasurementComponentLoadCase]':
        '''List[MeasurementComponentLoadCase]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_6176.MeasurementComponentLoadCase))
        return value

    @property
    def oil_seals(self) -> 'List[_6180.OilSealLoadCase]':
        '''List[OilSealLoadCase]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_6180.OilSealLoadCase))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_6185.PartToPartShearCouplingLoadCase]':
        '''List[PartToPartShearCouplingLoadCase]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_6185.PartToPartShearCouplingLoadCase))
        return value

    @property
    def planet_carriers(self) -> 'List[_6189.PlanetCarrierLoadCase]':
        '''List[PlanetCarrierLoadCase]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_6189.PlanetCarrierLoadCase))
        return value

    @property
    def point_loads(self) -> 'List[_6192.PointLoadLoadCase]':
        '''List[PointLoadLoadCase]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_6192.PointLoadLoadCase))
        return value

    @property
    def power_loads(self) -> 'List[_6193.PowerLoadLoadCase]':
        '''List[PowerLoadLoadCase]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_6193.PowerLoadLoadCase))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_6200.ShaftHubConnectionLoadCase]':
        '''List[ShaftHubConnectionLoadCase]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_6200.ShaftHubConnectionLoadCase))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_6196.RollingRingAssemblyLoadCase]':
        '''List[RollingRingAssemblyLoadCase]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_6196.RollingRingAssemblyLoadCase))
        return value

    @property
    def shafts(self) -> 'List[_6201.ShaftLoadCase]':
        '''List[ShaftLoadCase]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_6201.ShaftLoadCase))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_6207.SpiralBevelGearSetLoadCase]':
        '''List[SpiralBevelGearSetLoadCase]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_6207.SpiralBevelGearSetLoadCase))
        return value

    @property
    def spring_dampers(self) -> 'List[_6210.SpringDamperLoadCase]':
        '''List[SpringDamperLoadCase]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_6210.SpringDamperLoadCase))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_6214.StraightBevelDiffGearSetLoadCase]':
        '''List[StraightBevelDiffGearSetLoadCase]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_6214.StraightBevelDiffGearSetLoadCase))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_6217.StraightBevelGearSetLoadCase]':
        '''List[StraightBevelGearSetLoadCase]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_6217.StraightBevelGearSetLoadCase))
        return value

    @property
    def synchronisers(self) -> 'List[_6221.SynchroniserLoadCase]':
        '''List[SynchroniserLoadCase]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_6221.SynchroniserLoadCase))
        return value

    @property
    def torque_converters(self) -> 'List[_6227.TorqueConverterLoadCase]':
        '''List[TorqueConverterLoadCase]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_6227.TorqueConverterLoadCase))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_6234.UnbalancedMassLoadCase]':
        '''List[UnbalancedMassLoadCase]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_6234.UnbalancedMassLoadCase))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_6238.WormGearSetLoadCase]':
        '''List[WormGearSetLoadCase]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_6238.WormGearSetLoadCase))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_6241.ZerolBevelGearSetLoadCase]':
        '''List[ZerolBevelGearSetLoadCase]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_6241.ZerolBevelGearSetLoadCase))
        return value

    @property
    def shafts_and_housings(self) -> 'List[_6074.AbstractShaftOrHousingLoadCase]':
        '''List[AbstractShaftOrHousingLoadCase]: 'ShaftsAndHousings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftsAndHousings, constructor.new(_6074.AbstractShaftOrHousingLoadCase))
        return value

    @property
    def clutch_connections(self) -> 'List[_6094.ClutchConnectionLoadCase]':
        '''List[ClutchConnectionLoadCase]: 'ClutchConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ClutchConnections, constructor.new(_6094.ClutchConnectionLoadCase))
        return value

    @property
    def gear_meshes(self) -> 'List[_6147.GearMeshLoadCase]':
        '''List[GearMeshLoadCase]: 'GearMeshes' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.GearMeshes, constructor.new(_6147.GearMeshLoadCase))
        return value
