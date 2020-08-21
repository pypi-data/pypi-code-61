'''_4001.py

BevelDifferentialGearSetModalAnalysesAtSpeeds
'''


from typing import List

from mastapy.system_model.part_model.gears import _2079
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6086
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns import _4000, _3999, _4006
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_MODAL_ANALYSES_AT_SPEEDS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtSpeedsNS', 'BevelDifferentialGearSetModalAnalysesAtSpeeds')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearSetModalAnalysesAtSpeeds',)


class BevelDifferentialGearSetModalAnalysesAtSpeeds(_4006.BevelGearSetModalAnalysesAtSpeeds):
    '''BevelDifferentialGearSetModalAnalysesAtSpeeds

    This is a mastapy class.
    '''

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_MODAL_ANALYSES_AT_SPEEDS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearSetModalAnalysesAtSpeeds.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2079.BevelDifferentialGearSet':
        '''BevelDifferentialGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2079.BevelDifferentialGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6086.BevelDifferentialGearSetLoadCase':
        '''BevelDifferentialGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6086.BevelDifferentialGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def bevel_differential_gears_modal_analyses_at_speeds(self) -> 'List[_4000.BevelDifferentialGearModalAnalysesAtSpeeds]':
        '''List[BevelDifferentialGearModalAnalysesAtSpeeds]: 'BevelDifferentialGearsModalAnalysesAtSpeeds' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearsModalAnalysesAtSpeeds, constructor.new(_4000.BevelDifferentialGearModalAnalysesAtSpeeds))
        return value

    @property
    def bevel_differential_meshes_modal_analyses_at_speeds(self) -> 'List[_3999.BevelDifferentialGearMeshModalAnalysesAtSpeeds]':
        '''List[BevelDifferentialGearMeshModalAnalysesAtSpeeds]: 'BevelDifferentialMeshesModalAnalysesAtSpeeds' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialMeshesModalAnalysesAtSpeeds, constructor.new(_3999.BevelDifferentialGearMeshModalAnalysesAtSpeeds))
        return value
