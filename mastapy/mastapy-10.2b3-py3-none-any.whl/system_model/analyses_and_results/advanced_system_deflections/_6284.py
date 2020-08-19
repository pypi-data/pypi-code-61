'''_6284.py

CoaxialConnectionAdvancedSystemDeflection
'''


from typing import List

from mastapy.system_model.connections_and_sockets import _1854
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6097
from mastapy.system_model.analyses_and_results.system_deflections import _2254
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _6354
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'CoaxialConnectionAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('CoaxialConnectionAdvancedSystemDeflection',)


class CoaxialConnectionAdvancedSystemDeflection(_6354.ShaftToMountableComponentConnectionAdvancedSystemDeflection):
    '''CoaxialConnectionAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _COAXIAL_CONNECTION_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CoaxialConnectionAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_1854.CoaxialConnection':
        '''CoaxialConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1854.CoaxialConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_load_case(self) -> '_6097.CoaxialConnectionLoadCase':
        '''CoaxialConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6097.CoaxialConnectionLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase else None

    @property
    def connection_system_deflection_results(self) -> 'List[_2254.CoaxialConnectionSystemDeflection]':
        '''List[CoaxialConnectionSystemDeflection]: 'ConnectionSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionSystemDeflectionResults, constructor.new(_2254.CoaxialConnectionSystemDeflection))
        return value
