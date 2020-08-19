'''_2334.py

ShaftToMountableComponentConnectionSystemDeflection
'''


from mastapy.system_model.connections_and_sockets import _1877, _1854, _1869
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.power_flows import _3333, _3263, _3319
from mastapy.system_model.analyses_and_results.system_deflections import _2267
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'ShaftToMountableComponentConnectionSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftToMountableComponentConnectionSystemDeflection',)


class ShaftToMountableComponentConnectionSystemDeflection(_2267.ConnectionSystemDeflection):
    '''ShaftToMountableComponentConnectionSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ShaftToMountableComponentConnectionSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_1877.ShaftToMountableComponentConnection':
        '''ShaftToMountableComponentConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1877.ShaftToMountableComponentConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_coaxial_connection(self) -> '_1854.CoaxialConnection':
        '''CoaxialConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1854.CoaxialConnection.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to CoaxialConnection. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1854.CoaxialConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_planetary_connection(self) -> '_1869.PlanetaryConnection':
        '''PlanetaryConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1869.PlanetaryConnection.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to PlanetaryConnection. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1869.PlanetaryConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def power_flow_results(self) -> '_3333.ShaftToMountableComponentConnectionPowerFlow':
        '''ShaftToMountableComponentConnectionPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3333.ShaftToMountableComponentConnectionPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults else None

    @property
    def power_flow_results_of_type_coaxial_connection_power_flow(self) -> '_3263.CoaxialConnectionPowerFlow':
        '''CoaxialConnectionPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _3263.CoaxialConnectionPowerFlow.TYPE not in self.wrapped.PowerFlowResults.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to CoaxialConnectionPowerFlow. Expected: {}.'.format(self.wrapped.PowerFlowResults.__class__.__qualname__))

        return constructor.new(_3263.CoaxialConnectionPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults else None

    @property
    def power_flow_results_of_type_planetary_connection_power_flow(self) -> '_3319.PlanetaryConnectionPowerFlow':
        '''PlanetaryConnectionPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _3319.PlanetaryConnectionPowerFlow.TYPE not in self.wrapped.PowerFlowResults.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to PlanetaryConnectionPowerFlow. Expected: {}.'.format(self.wrapped.PowerFlowResults.__class__.__qualname__))

        return constructor.new(_3319.PlanetaryConnectionPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults else None
