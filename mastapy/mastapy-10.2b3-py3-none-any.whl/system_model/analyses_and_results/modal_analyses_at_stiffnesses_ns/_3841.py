'''_3841.py

SpiralBevelGearSetModalAnalysesAtStiffnesses
'''


from typing import List

from mastapy.system_model.part_model.gears import _2107
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6207
from mastapy.system_model.analyses_and_results.modal_analyses_at_stiffnesses_ns import _3840, _3839, _3761
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_MODAL_ANALYSES_AT_STIFFNESSES = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtStiffnessesNS', 'SpiralBevelGearSetModalAnalysesAtStiffnesses')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearSetModalAnalysesAtStiffnesses',)


class SpiralBevelGearSetModalAnalysesAtStiffnesses(_3761.BevelGearSetModalAnalysesAtStiffnesses):
    '''SpiralBevelGearSetModalAnalysesAtStiffnesses

    This is a mastapy class.
    '''

    TYPE = _SPIRAL_BEVEL_GEAR_SET_MODAL_ANALYSES_AT_STIFFNESSES

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearSetModalAnalysesAtStiffnesses.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2107.SpiralBevelGearSet':
        '''SpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2107.SpiralBevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6207.SpiralBevelGearSetLoadCase':
        '''SpiralBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6207.SpiralBevelGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def spiral_bevel_gears_modal_analyses_at_stiffnesses(self) -> 'List[_3840.SpiralBevelGearModalAnalysesAtStiffnesses]':
        '''List[SpiralBevelGearModalAnalysesAtStiffnesses]: 'SpiralBevelGearsModalAnalysesAtStiffnesses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearsModalAnalysesAtStiffnesses, constructor.new(_3840.SpiralBevelGearModalAnalysesAtStiffnesses))
        return value

    @property
    def spiral_bevel_meshes_modal_analyses_at_stiffnesses(self) -> 'List[_3839.SpiralBevelGearMeshModalAnalysesAtStiffnesses]':
        '''List[SpiralBevelGearMeshModalAnalysesAtStiffnesses]: 'SpiralBevelMeshesModalAnalysesAtStiffnesses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelMeshesModalAnalysesAtStiffnesses, constructor.new(_3839.SpiralBevelGearMeshModalAnalysesAtStiffnesses))
        return value
