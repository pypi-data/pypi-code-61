'''_4045.py

GuideDxfModelModalAnalysesAtSpeeds
'''


from mastapy.system_model.part_model import _2020
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6151
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns import _4013
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_MODAL_ANALYSES_AT_SPEEDS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtSpeedsNS', 'GuideDxfModelModalAnalysesAtSpeeds')


__docformat__ = 'restructuredtext en'
__all__ = ('GuideDxfModelModalAnalysesAtSpeeds',)


class GuideDxfModelModalAnalysesAtSpeeds(_4013.ComponentModalAnalysesAtSpeeds):
    '''GuideDxfModelModalAnalysesAtSpeeds

    This is a mastapy class.
    '''

    TYPE = _GUIDE_DXF_MODEL_MODAL_ANALYSES_AT_SPEEDS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GuideDxfModelModalAnalysesAtSpeeds.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2020.GuideDxfModel':
        '''GuideDxfModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2020.GuideDxfModel)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6151.GuideDxfModelLoadCase':
        '''GuideDxfModelLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6151.GuideDxfModelLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
