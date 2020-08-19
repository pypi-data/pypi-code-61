'''_5526.py

SingleMeshWhineAnalysis
'''


from mastapy.system_model.analyses_and_results.gear_whine_analyses import (
    _5277, _5325, _5326, _5327,
    _5328, _5329, _5330, _5331,
    _5332, _5333, _5334, _5335,
    _5343, _5345, _5346, _5351,
    _5376, _5390, _5415
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.analysis_cases import _6524
from mastapy._internal.python_net import python_net_import

_SINGLE_MESH_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.SingleMeshWhineAnalyses', 'SingleMeshWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SingleMeshWhineAnalysis',)


class SingleMeshWhineAnalysis(_6524.StaticLoadAnalysisCase):
    '''SingleMeshWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _SINGLE_MESH_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SingleMeshWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def excitation_detail(self) -> '_5277.AbstractPeriodicExcitationDetail':
        '''AbstractPeriodicExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5277.AbstractPeriodicExcitationDetail)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail else None

    @property
    def excitation_detail_of_type_electric_machine_periodic_excitation_detail(self) -> '_5325.ElectricMachinePeriodicExcitationDetail':
        '''ElectricMachinePeriodicExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5325.ElectricMachinePeriodicExcitationDetail.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to ElectricMachinePeriodicExcitationDetail. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new(_5325.ElectricMachinePeriodicExcitationDetail)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail else None

    @property
    def excitation_detail_of_type_electric_machine_rotor_x_force_periodic_excitation_detail(self) -> '_5326.ElectricMachineRotorXForcePeriodicExcitationDetail':
        '''ElectricMachineRotorXForcePeriodicExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5326.ElectricMachineRotorXForcePeriodicExcitationDetail.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to ElectricMachineRotorXForcePeriodicExcitationDetail. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new(_5326.ElectricMachineRotorXForcePeriodicExcitationDetail)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail else None

    @property
    def excitation_detail_of_type_electric_machine_rotor_x_moment_periodic_excitation_detail(self) -> '_5327.ElectricMachineRotorXMomentPeriodicExcitationDetail':
        '''ElectricMachineRotorXMomentPeriodicExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5327.ElectricMachineRotorXMomentPeriodicExcitationDetail.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to ElectricMachineRotorXMomentPeriodicExcitationDetail. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new(_5327.ElectricMachineRotorXMomentPeriodicExcitationDetail)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail else None

    @property
    def excitation_detail_of_type_electric_machine_rotor_y_force_periodic_excitation_detail(self) -> '_5328.ElectricMachineRotorYForcePeriodicExcitationDetail':
        '''ElectricMachineRotorYForcePeriodicExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5328.ElectricMachineRotorYForcePeriodicExcitationDetail.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to ElectricMachineRotorYForcePeriodicExcitationDetail. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new(_5328.ElectricMachineRotorYForcePeriodicExcitationDetail)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail else None

    @property
    def excitation_detail_of_type_electric_machine_rotor_y_moment_periodic_excitation_detail(self) -> '_5329.ElectricMachineRotorYMomentPeriodicExcitationDetail':
        '''ElectricMachineRotorYMomentPeriodicExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5329.ElectricMachineRotorYMomentPeriodicExcitationDetail.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to ElectricMachineRotorYMomentPeriodicExcitationDetail. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new(_5329.ElectricMachineRotorYMomentPeriodicExcitationDetail)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail else None

    @property
    def excitation_detail_of_type_electric_machine_rotor_z_force_periodic_excitation_detail(self) -> '_5330.ElectricMachineRotorZForcePeriodicExcitationDetail':
        '''ElectricMachineRotorZForcePeriodicExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5330.ElectricMachineRotorZForcePeriodicExcitationDetail.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to ElectricMachineRotorZForcePeriodicExcitationDetail. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new(_5330.ElectricMachineRotorZForcePeriodicExcitationDetail)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail else None

    @property
    def excitation_detail_of_type_electric_machine_stator_tooth_axial_loads_excitation_detail(self) -> '_5331.ElectricMachineStatorToothAxialLoadsExcitationDetail':
        '''ElectricMachineStatorToothAxialLoadsExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5331.ElectricMachineStatorToothAxialLoadsExcitationDetail.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to ElectricMachineStatorToothAxialLoadsExcitationDetail. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new(_5331.ElectricMachineStatorToothAxialLoadsExcitationDetail)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail else None

    @property
    def excitation_detail_of_type_electric_machine_stator_tooth_loads_excitation_detail(self) -> '_5332.ElectricMachineStatorToothLoadsExcitationDetail':
        '''ElectricMachineStatorToothLoadsExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5332.ElectricMachineStatorToothLoadsExcitationDetail.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to ElectricMachineStatorToothLoadsExcitationDetail. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new(_5332.ElectricMachineStatorToothLoadsExcitationDetail)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail else None

    @property
    def excitation_detail_of_type_electric_machine_stator_tooth_radial_loads_excitation_detail(self) -> '_5333.ElectricMachineStatorToothRadialLoadsExcitationDetail':
        '''ElectricMachineStatorToothRadialLoadsExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5333.ElectricMachineStatorToothRadialLoadsExcitationDetail.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to ElectricMachineStatorToothRadialLoadsExcitationDetail. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new(_5333.ElectricMachineStatorToothRadialLoadsExcitationDetail)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail else None

    @property
    def excitation_detail_of_type_electric_machine_stator_tooth_tangential_loads_excitation_detail(self) -> '_5334.ElectricMachineStatorToothTangentialLoadsExcitationDetail':
        '''ElectricMachineStatorToothTangentialLoadsExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5334.ElectricMachineStatorToothTangentialLoadsExcitationDetail.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to ElectricMachineStatorToothTangentialLoadsExcitationDetail. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new(_5334.ElectricMachineStatorToothTangentialLoadsExcitationDetail)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail else None

    @property
    def excitation_detail_of_type_electric_machine_torque_ripple_periodic_excitation_detail(self) -> '_5335.ElectricMachineTorqueRipplePeriodicExcitationDetail':
        '''ElectricMachineTorqueRipplePeriodicExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5335.ElectricMachineTorqueRipplePeriodicExcitationDetail.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to ElectricMachineTorqueRipplePeriodicExcitationDetail. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new(_5335.ElectricMachineTorqueRipplePeriodicExcitationDetail)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail else None

    @property
    def excitation_detail_of_type_gear_mesh_excitation_detail(self) -> '_5343.GearMeshExcitationDetail':
        '''GearMeshExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5343.GearMeshExcitationDetail.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to GearMeshExcitationDetail. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new(_5343.GearMeshExcitationDetail)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail else None

    @property
    def excitation_detail_of_type_gear_mesh_misalignment_excitation_detail(self) -> '_5345.GearMeshMisalignmentExcitationDetail':
        '''GearMeshMisalignmentExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5345.GearMeshMisalignmentExcitationDetail.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to GearMeshMisalignmentExcitationDetail. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new(_5345.GearMeshMisalignmentExcitationDetail)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail else None

    @property
    def excitation_detail_of_type_gear_mesh_te_excitation_detail(self) -> '_5346.GearMeshTEExcitationDetail':
        '''GearMeshTEExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5346.GearMeshTEExcitationDetail.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to GearMeshTEExcitationDetail. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new(_5346.GearMeshTEExcitationDetail)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail else None

    @property
    def excitation_detail_of_type_general_periodic_excitation_detail(self) -> '_5351.GeneralPeriodicExcitationDetail':
        '''GeneralPeriodicExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5351.GeneralPeriodicExcitationDetail.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to GeneralPeriodicExcitationDetail. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new(_5351.GeneralPeriodicExcitationDetail)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail else None

    @property
    def excitation_detail_of_type_periodic_excitation_with_reference_shaft(self) -> '_5376.PeriodicExcitationWithReferenceShaft':
        '''PeriodicExcitationWithReferenceShaft: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5376.PeriodicExcitationWithReferenceShaft.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to PeriodicExcitationWithReferenceShaft. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new(_5376.PeriodicExcitationWithReferenceShaft)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail else None

    @property
    def excitation_detail_of_type_single_node_periodic_excitation_with_reference_shaft(self) -> '_5390.SingleNodePeriodicExcitationWithReferenceShaft':
        '''SingleNodePeriodicExcitationWithReferenceShaft: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5390.SingleNodePeriodicExcitationWithReferenceShaft.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to SingleNodePeriodicExcitationWithReferenceShaft. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new(_5390.SingleNodePeriodicExcitationWithReferenceShaft)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail else None

    @property
    def excitation_detail_of_type_unbalanced_mass_excitation_detail(self) -> '_5415.UnbalancedMassExcitationDetail':
        '''UnbalancedMassExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5415.UnbalancedMassExcitationDetail.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to UnbalancedMassExcitationDetail. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new(_5415.UnbalancedMassExcitationDetail)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail else None
