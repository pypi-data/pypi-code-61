'''_4164.py

FaceGearSetCompoundModalAnalysesAtSpeeds
'''


from typing import List

from mastapy.system_model.part_model.gears import _2092
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns.compound import _4162, _4163, _4168
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns import _4040
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_COMPOUND_MODAL_ANALYSES_AT_SPEEDS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtSpeedsNS.Compound', 'FaceGearSetCompoundModalAnalysesAtSpeeds')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetCompoundModalAnalysesAtSpeeds',)


class FaceGearSetCompoundModalAnalysesAtSpeeds(_4168.GearSetCompoundModalAnalysesAtSpeeds):
    '''FaceGearSetCompoundModalAnalysesAtSpeeds

    This is a mastapy class.
    '''

    TYPE = _FACE_GEAR_SET_COMPOUND_MODAL_ANALYSES_AT_SPEEDS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearSetCompoundModalAnalysesAtSpeeds.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2092.FaceGearSet':
        '''FaceGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2092.FaceGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def assembly_design(self) -> '_2092.FaceGearSet':
        '''FaceGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2092.FaceGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def face_gears_compound_modal_analyses_at_speeds(self) -> 'List[_4162.FaceGearCompoundModalAnalysesAtSpeeds]':
        '''List[FaceGearCompoundModalAnalysesAtSpeeds]: 'FaceGearsCompoundModalAnalysesAtSpeeds' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearsCompoundModalAnalysesAtSpeeds, constructor.new(_4162.FaceGearCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def face_meshes_compound_modal_analyses_at_speeds(self) -> 'List[_4163.FaceGearMeshCompoundModalAnalysesAtSpeeds]':
        '''List[FaceGearMeshCompoundModalAnalysesAtSpeeds]: 'FaceMeshesCompoundModalAnalysesAtSpeeds' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceMeshesCompoundModalAnalysesAtSpeeds, constructor.new(_4163.FaceGearMeshCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def load_case_analyses_ready(self) -> 'List[_4040.FaceGearSetModalAnalysesAtSpeeds]':
        '''List[FaceGearSetModalAnalysesAtSpeeds]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_4040.FaceGearSetModalAnalysesAtSpeeds))
        return value

    @property
    def assembly_modal_analyses_at_speeds_load_cases(self) -> 'List[_4040.FaceGearSetModalAnalysesAtSpeeds]':
        '''List[FaceGearSetModalAnalysesAtSpeeds]: 'AssemblyModalAnalysesAtSpeedsLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyModalAnalysesAtSpeedsLoadCases, constructor.new(_4040.FaceGearSetModalAnalysesAtSpeeds))
        return value
