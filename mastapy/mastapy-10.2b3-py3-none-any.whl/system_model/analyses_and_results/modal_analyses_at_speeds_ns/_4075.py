'''_4075.py

PulleyModalAnalysesAtSpeeds
'''


from mastapy.system_model.part_model.couplings import _2148
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6194
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns import _4026
from mastapy._internal.python_net import python_net_import

_PULLEY_MODAL_ANALYSES_AT_SPEEDS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtSpeedsNS', 'PulleyModalAnalysesAtSpeeds')


__docformat__ = 'restructuredtext en'
__all__ = ('PulleyModalAnalysesAtSpeeds',)


class PulleyModalAnalysesAtSpeeds(_4026.CouplingHalfModalAnalysesAtSpeeds):
    '''PulleyModalAnalysesAtSpeeds

    This is a mastapy class.
    '''

    TYPE = _PULLEY_MODAL_ANALYSES_AT_SPEEDS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PulleyModalAnalysesAtSpeeds.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2148.Pulley':
        '''Pulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2148.Pulley)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6194.PulleyLoadCase':
        '''PulleyLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6194.PulleyLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
