'''_5529.py

SpiralBevelGearSetSingleMeshWhineAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2107
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6207
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses import _5530, _5528, _5450
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_SINGLE_MESH_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.SingleMeshWhineAnalyses', 'SpiralBevelGearSetSingleMeshWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearSetSingleMeshWhineAnalysis',)


class SpiralBevelGearSetSingleMeshWhineAnalysis(_5450.BevelGearSetSingleMeshWhineAnalysis):
    '''SpiralBevelGearSetSingleMeshWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _SPIRAL_BEVEL_GEAR_SET_SINGLE_MESH_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearSetSingleMeshWhineAnalysis.TYPE'):
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
    def spiral_bevel_gears_single_mesh_whine_analysis(self) -> 'List[_5530.SpiralBevelGearSingleMeshWhineAnalysis]':
        '''List[SpiralBevelGearSingleMeshWhineAnalysis]: 'SpiralBevelGearsSingleMeshWhineAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearsSingleMeshWhineAnalysis, constructor.new(_5530.SpiralBevelGearSingleMeshWhineAnalysis))
        return value

    @property
    def spiral_bevel_meshes_single_mesh_whine_analysis(self) -> 'List[_5528.SpiralBevelGearMeshSingleMeshWhineAnalysis]':
        '''List[SpiralBevelGearMeshSingleMeshWhineAnalysis]: 'SpiralBevelMeshesSingleMeshWhineAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelMeshesSingleMeshWhineAnalysis, constructor.new(_5528.SpiralBevelGearMeshSingleMeshWhineAnalysis))
        return value
