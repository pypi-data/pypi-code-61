'''_3687.py

KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool
'''


from typing import List

from mastapy.system_model.part_model.gears import _2101
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _3557
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _3684
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool',)


class KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool(_3684.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool):
    '''KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2101.KlingelnbergCycloPalloidHypoidGear':
        '''KlingelnbergCycloPalloidHypoidGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2101.KlingelnbergCycloPalloidHypoidGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def load_case_analyses_ready(self) -> 'List[_3557.KlingelnbergCycloPalloidHypoidGearParametricStudyTool]':
        '''List[KlingelnbergCycloPalloidHypoidGearParametricStudyTool]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_3557.KlingelnbergCycloPalloidHypoidGearParametricStudyTool))
        return value

    @property
    def component_parametric_study_tool_load_cases(self) -> 'List[_3557.KlingelnbergCycloPalloidHypoidGearParametricStudyTool]':
        '''List[KlingelnbergCycloPalloidHypoidGearParametricStudyTool]: 'ComponentParametricStudyToolLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentParametricStudyToolLoadCases, constructor.new(_3557.KlingelnbergCycloPalloidHypoidGearParametricStudyTool))
        return value
