'''_5302.py

ConceptCouplingConnectionGearWhineAnalysis
'''


from mastapy.system_model.connections_and_sockets.couplings import _1917
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6099
from mastapy.system_model.analyses_and_results.system_deflections import _2257
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5313
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'ConceptCouplingConnectionGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingConnectionGearWhineAnalysis',)


class ConceptCouplingConnectionGearWhineAnalysis(_5313.CouplingConnectionGearWhineAnalysis):
    '''ConceptCouplingConnectionGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_COUPLING_CONNECTION_GEAR_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptCouplingConnectionGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_1917.ConceptCouplingConnection':
        '''ConceptCouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1917.ConceptCouplingConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_load_case(self) -> '_6099.ConceptCouplingConnectionLoadCase':
        '''ConceptCouplingConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6099.ConceptCouplingConnectionLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase else None

    @property
    def system_deflection_results(self) -> '_2257.ConceptCouplingConnectionSystemDeflection':
        '''ConceptCouplingConnectionSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2257.ConceptCouplingConnectionSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
