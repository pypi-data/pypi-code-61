'''_3951.py

PulleyCompoundModalAnalysesAtStiffnesses
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2148
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_stiffnesses_ns import _3830
from mastapy.system_model.analyses_and_results.modal_analyses_at_stiffnesses_ns.compound import _3906
from mastapy._internal.python_net import python_net_import

_PULLEY_COMPOUND_MODAL_ANALYSES_AT_STIFFNESSES = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtStiffnessesNS.Compound', 'PulleyCompoundModalAnalysesAtStiffnesses')


__docformat__ = 'restructuredtext en'
__all__ = ('PulleyCompoundModalAnalysesAtStiffnesses',)


class PulleyCompoundModalAnalysesAtStiffnesses(_3906.CouplingHalfCompoundModalAnalysesAtStiffnesses):
    '''PulleyCompoundModalAnalysesAtStiffnesses

    This is a mastapy class.
    '''

    TYPE = _PULLEY_COMPOUND_MODAL_ANALYSES_AT_STIFFNESSES

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PulleyCompoundModalAnalysesAtStiffnesses.TYPE'):
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
    def load_case_analyses_ready(self) -> 'List[_3830.PulleyModalAnalysesAtStiffnesses]':
        '''List[PulleyModalAnalysesAtStiffnesses]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_3830.PulleyModalAnalysesAtStiffnesses))
        return value

    @property
    def component_modal_analyses_at_stiffnesses_load_cases(self) -> 'List[_3830.PulleyModalAnalysesAtStiffnesses]':
        '''List[PulleyModalAnalysesAtStiffnesses]: 'ComponentModalAnalysesAtStiffnessesLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentModalAnalysesAtStiffnessesLoadCases, constructor.new(_3830.PulleyModalAnalysesAtStiffnesses))
        return value
