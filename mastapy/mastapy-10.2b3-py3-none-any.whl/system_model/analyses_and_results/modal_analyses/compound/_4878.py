'''_4878.py

BevelDifferentialGearCompoundModalAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2078
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4733
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4883
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'BevelDifferentialGearCompoundModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearCompoundModalAnalysis',)


class BevelDifferentialGearCompoundModalAnalysis(_4883.BevelGearCompoundModalAnalysis):
    '''BevelDifferentialGearCompoundModalAnalysis

    This is a mastapy class.
    '''

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_COMPOUND_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2078.BevelDifferentialGear':
        '''BevelDifferentialGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2078.BevelDifferentialGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def load_case_analyses_ready(self) -> 'List[_4733.BevelDifferentialGearModalAnalysis]':
        '''List[BevelDifferentialGearModalAnalysis]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_4733.BevelDifferentialGearModalAnalysis))
        return value

    @property
    def component_modal_analysis_load_cases(self) -> 'List[_4733.BevelDifferentialGearModalAnalysis]':
        '''List[BevelDifferentialGearModalAnalysis]: 'ComponentModalAnalysisLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentModalAnalysisLoadCases, constructor.new(_4733.BevelDifferentialGearModalAnalysis))
        return value
