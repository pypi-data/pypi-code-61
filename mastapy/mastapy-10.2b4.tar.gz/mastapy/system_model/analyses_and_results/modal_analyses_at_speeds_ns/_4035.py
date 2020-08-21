'''_4035.py

DatumModalAnalysesAtSpeeds
'''


from mastapy.system_model.part_model import _2015
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6126
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns import _4013
from mastapy._internal.python_net import python_net_import

_DATUM_MODAL_ANALYSES_AT_SPEEDS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtSpeedsNS', 'DatumModalAnalysesAtSpeeds')


__docformat__ = 'restructuredtext en'
__all__ = ('DatumModalAnalysesAtSpeeds',)


class DatumModalAnalysesAtSpeeds(_4013.ComponentModalAnalysesAtSpeeds):
    '''DatumModalAnalysesAtSpeeds

    This is a mastapy class.
    '''

    TYPE = _DATUM_MODAL_ANALYSES_AT_SPEEDS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DatumModalAnalysesAtSpeeds.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2015.Datum':
        '''Datum: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2015.Datum)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6126.DatumLoadCase':
        '''DatumLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6126.DatumLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
