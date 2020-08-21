'''_5841.py

ClutchConnectionDynamicAnalysis
'''


from mastapy.system_model.connections_and_sockets.couplings import _1915
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6094
from mastapy.system_model.analyses_and_results.dynamic_analyses import _5857
from mastapy._internal.python_net import python_net_import

_CLUTCH_CONNECTION_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'ClutchConnectionDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchConnectionDynamicAnalysis',)


class ClutchConnectionDynamicAnalysis(_5857.CouplingConnectionDynamicAnalysis):
    '''ClutchConnectionDynamicAnalysis

    This is a mastapy class.
    '''

    TYPE = _CLUTCH_CONNECTION_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchConnectionDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_1915.ClutchConnection':
        '''ClutchConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1915.ClutchConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_load_case(self) -> '_6094.ClutchConnectionLoadCase':
        '''ClutchConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6094.ClutchConnectionLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase else None
