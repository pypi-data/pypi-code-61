'''_4040.py

FaceGearSetModalAnalysesAtSpeeds
'''


from typing import List

from mastapy.system_model.part_model.gears import _2092
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6142
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns import _4039, _4038, _4044
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_MODAL_ANALYSES_AT_SPEEDS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtSpeedsNS', 'FaceGearSetModalAnalysesAtSpeeds')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetModalAnalysesAtSpeeds',)


class FaceGearSetModalAnalysesAtSpeeds(_4044.GearSetModalAnalysesAtSpeeds):
    '''FaceGearSetModalAnalysesAtSpeeds

    This is a mastapy class.
    '''

    TYPE = _FACE_GEAR_SET_MODAL_ANALYSES_AT_SPEEDS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearSetModalAnalysesAtSpeeds.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2092.FaceGearSet':
        '''FaceGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2092.FaceGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6142.FaceGearSetLoadCase':
        '''FaceGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6142.FaceGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def face_gears_modal_analyses_at_speeds(self) -> 'List[_4039.FaceGearModalAnalysesAtSpeeds]':
        '''List[FaceGearModalAnalysesAtSpeeds]: 'FaceGearsModalAnalysesAtSpeeds' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearsModalAnalysesAtSpeeds, constructor.new(_4039.FaceGearModalAnalysesAtSpeeds))
        return value

    @property
    def face_meshes_modal_analyses_at_speeds(self) -> 'List[_4038.FaceGearMeshModalAnalysesAtSpeeds]':
        '''List[FaceGearMeshModalAnalysesAtSpeeds]: 'FaceMeshesModalAnalysesAtSpeeds' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceMeshesModalAnalysesAtSpeeds, constructor.new(_4038.FaceGearMeshModalAnalysesAtSpeeds))
        return value
