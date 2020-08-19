'''_4087.py

SpringDamperConnectionModalAnalysesAtSpeeds
'''


from mastapy.system_model.connections_and_sockets.couplings import _1923
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6208
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns import _4025
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_MODAL_ANALYSES_AT_SPEEDS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtSpeedsNS', 'SpringDamperConnectionModalAnalysesAtSpeeds')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperConnectionModalAnalysesAtSpeeds',)


class SpringDamperConnectionModalAnalysesAtSpeeds(_4025.CouplingConnectionModalAnalysesAtSpeeds):
    '''SpringDamperConnectionModalAnalysesAtSpeeds

    This is a mastapy class.
    '''

    TYPE = _SPRING_DAMPER_CONNECTION_MODAL_ANALYSES_AT_SPEEDS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpringDamperConnectionModalAnalysesAtSpeeds.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_1923.SpringDamperConnection':
        '''SpringDamperConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1923.SpringDamperConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_load_case(self) -> '_6208.SpringDamperConnectionLoadCase':
        '''SpringDamperConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6208.SpringDamperConnectionLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase else None
