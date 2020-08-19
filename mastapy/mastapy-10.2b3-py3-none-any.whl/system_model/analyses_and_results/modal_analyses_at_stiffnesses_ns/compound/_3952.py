'''_3952.py

RollingRingAssemblyCompoundModalAnalysesAtStiffnesses
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2155
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_stiffnesses_ns import _3831
from mastapy.system_model.analyses_and_results.modal_analyses_at_stiffnesses_ns.compound import _3959
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_COMPOUND_MODAL_ANALYSES_AT_STIFFNESSES = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtStiffnessesNS.Compound', 'RollingRingAssemblyCompoundModalAnalysesAtStiffnesses')


__docformat__ = 'restructuredtext en'
__all__ = ('RollingRingAssemblyCompoundModalAnalysesAtStiffnesses',)


class RollingRingAssemblyCompoundModalAnalysesAtStiffnesses(_3959.SpecialisedAssemblyCompoundModalAnalysesAtStiffnesses):
    '''RollingRingAssemblyCompoundModalAnalysesAtStiffnesses

    This is a mastapy class.
    '''

    TYPE = _ROLLING_RING_ASSEMBLY_COMPOUND_MODAL_ANALYSES_AT_STIFFNESSES

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RollingRingAssemblyCompoundModalAnalysesAtStiffnesses.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2155.RollingRingAssembly':
        '''RollingRingAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2155.RollingRingAssembly)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def assembly_design(self) -> '_2155.RollingRingAssembly':
        '''RollingRingAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2155.RollingRingAssembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def load_case_analyses_ready(self) -> 'List[_3831.RollingRingAssemblyModalAnalysesAtStiffnesses]':
        '''List[RollingRingAssemblyModalAnalysesAtStiffnesses]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_3831.RollingRingAssemblyModalAnalysesAtStiffnesses))
        return value

    @property
    def assembly_modal_analyses_at_stiffnesses_load_cases(self) -> 'List[_3831.RollingRingAssemblyModalAnalysesAtStiffnesses]':
        '''List[RollingRingAssemblyModalAnalysesAtStiffnesses]: 'AssemblyModalAnalysesAtStiffnessesLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyModalAnalysesAtStiffnessesLoadCases, constructor.new(_3831.RollingRingAssemblyModalAnalysesAtStiffnesses))
        return value
