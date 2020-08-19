'''_3800.py

GuideDxfModelModalAnalysesAtStiffnesses
'''


from mastapy.system_model.part_model import _2020
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6151
from mastapy.system_model.analyses_and_results.modal_analyses_at_stiffnesses_ns import _3768
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_MODAL_ANALYSES_AT_STIFFNESSES = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtStiffnessesNS', 'GuideDxfModelModalAnalysesAtStiffnesses')


__docformat__ = 'restructuredtext en'
__all__ = ('GuideDxfModelModalAnalysesAtStiffnesses',)


class GuideDxfModelModalAnalysesAtStiffnesses(_3768.ComponentModalAnalysesAtStiffnesses):
    '''GuideDxfModelModalAnalysesAtStiffnesses

    This is a mastapy class.
    '''

    TYPE = _GUIDE_DXF_MODEL_MODAL_ANALYSES_AT_STIFFNESSES

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GuideDxfModelModalAnalysesAtStiffnesses.TYPE'):
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
