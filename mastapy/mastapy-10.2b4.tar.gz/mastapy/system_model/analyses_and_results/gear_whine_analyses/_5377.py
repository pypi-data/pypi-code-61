'''_5377.py

PlanetaryConnectionGearWhineAnalysis
'''


from mastapy.system_model.connections_and_sockets import _1869
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6186
from mastapy.system_model.analyses_and_results.system_deflections import _2321
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5389
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'PlanetaryConnectionGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetaryConnectionGearWhineAnalysis',)


class PlanetaryConnectionGearWhineAnalysis(_5389.ShaftToMountableComponentConnectionGearWhineAnalysis):
    '''PlanetaryConnectionGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _PLANETARY_CONNECTION_GEAR_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PlanetaryConnectionGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_1869.PlanetaryConnection':
        '''PlanetaryConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1869.PlanetaryConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_load_case(self) -> '_6186.PlanetaryConnectionLoadCase':
        '''PlanetaryConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6186.PlanetaryConnectionLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase else None

    @property
    def system_deflection_results(self) -> '_2321.PlanetaryConnectionSystemDeflection':
        '''PlanetaryConnectionSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2321.PlanetaryConnectionSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
