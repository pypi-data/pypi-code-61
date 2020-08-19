'''_5284.py

BeltConnectionGearWhineAnalysis
'''


from mastapy.system_model.connections_and_sockets import _1853
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6082
from mastapy.system_model.analyses_and_results.system_deflections import _2239
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5358
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'BeltConnectionGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BeltConnectionGearWhineAnalysis',)


class BeltConnectionGearWhineAnalysis(_5358.InterMountableComponentConnectionGearWhineAnalysis):
    '''BeltConnectionGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _BELT_CONNECTION_GEAR_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BeltConnectionGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_1853.BeltConnection':
        '''BeltConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1853.BeltConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_load_case(self) -> '_6082.BeltConnectionLoadCase':
        '''BeltConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6082.BeltConnectionLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase else None

    @property
    def system_deflection_results(self) -> '_2239.BeltConnectionSystemDeflection':
        '''BeltConnectionSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2239.BeltConnectionSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
