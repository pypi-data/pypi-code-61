'''_2364.py

VirtualComponentSystemDeflection
'''


from mastapy.system_model.part_model import (
    _2043, _2027, _2028, _2036,
    _2037, _2042
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.power_flows import (
    _3359, _3311, _3312, _3322,
    _3325, _3358
)
from mastapy.system_model.analyses_and_results.system_deflections import _2314
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'VirtualComponentSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('VirtualComponentSystemDeflection',)


class VirtualComponentSystemDeflection(_2314.MountableComponentSystemDeflection):
    '''VirtualComponentSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _VIRTUAL_COMPONENT_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'VirtualComponentSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2043.VirtualComponent':
        '''VirtualComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2043.VirtualComponent)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_mass_disc(self) -> '_2027.MassDisc':
        '''MassDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2027.MassDisc.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to MassDisc. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2027.MassDisc)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_measurement_component(self) -> '_2028.MeasurementComponent':
        '''MeasurementComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2028.MeasurementComponent.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to MeasurementComponent. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2028.MeasurementComponent)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_point_load(self) -> '_2036.PointLoad':
        '''PointLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2036.PointLoad.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to PointLoad. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2036.PointLoad)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_power_load(self) -> '_2037.PowerLoad':
        '''PowerLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2037.PowerLoad.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to PowerLoad. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2037.PowerLoad)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_unbalanced_mass(self) -> '_2042.UnbalancedMass':
        '''UnbalancedMass: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2042.UnbalancedMass.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to UnbalancedMass. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2042.UnbalancedMass)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def power_flow_results(self) -> '_3359.VirtualComponentPowerFlow':
        '''VirtualComponentPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3359.VirtualComponentPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults else None

    @property
    def power_flow_results_of_type_mass_disc_power_flow(self) -> '_3311.MassDiscPowerFlow':
        '''MassDiscPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _3311.MassDiscPowerFlow.TYPE not in self.wrapped.PowerFlowResults.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to MassDiscPowerFlow. Expected: {}.'.format(self.wrapped.PowerFlowResults.__class__.__qualname__))

        return constructor.new(_3311.MassDiscPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults else None

    @property
    def power_flow_results_of_type_measurement_component_power_flow(self) -> '_3312.MeasurementComponentPowerFlow':
        '''MeasurementComponentPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _3312.MeasurementComponentPowerFlow.TYPE not in self.wrapped.PowerFlowResults.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to MeasurementComponentPowerFlow. Expected: {}.'.format(self.wrapped.PowerFlowResults.__class__.__qualname__))

        return constructor.new(_3312.MeasurementComponentPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults else None

    @property
    def power_flow_results_of_type_point_load_power_flow(self) -> '_3322.PointLoadPowerFlow':
        '''PointLoadPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _3322.PointLoadPowerFlow.TYPE not in self.wrapped.PowerFlowResults.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to PointLoadPowerFlow. Expected: {}.'.format(self.wrapped.PowerFlowResults.__class__.__qualname__))

        return constructor.new(_3322.PointLoadPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults else None

    @property
    def power_flow_results_of_type_power_load_power_flow(self) -> '_3325.PowerLoadPowerFlow':
        '''PowerLoadPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _3325.PowerLoadPowerFlow.TYPE not in self.wrapped.PowerFlowResults.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to PowerLoadPowerFlow. Expected: {}.'.format(self.wrapped.PowerFlowResults.__class__.__qualname__))

        return constructor.new(_3325.PowerLoadPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults else None

    @property
    def power_flow_results_of_type_unbalanced_mass_power_flow(self) -> '_3358.UnbalancedMassPowerFlow':
        '''UnbalancedMassPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _3358.UnbalancedMassPowerFlow.TYPE not in self.wrapped.PowerFlowResults.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to UnbalancedMassPowerFlow. Expected: {}.'.format(self.wrapped.PowerFlowResults.__class__.__qualname__))

        return constructor.new(_3358.UnbalancedMassPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults else None
