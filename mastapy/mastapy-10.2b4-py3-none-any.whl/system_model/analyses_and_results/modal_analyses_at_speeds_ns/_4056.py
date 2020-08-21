'''_4056.py

KlingelnbergCycloPalloidHypoidGearSetModalAnalysesAtSpeeds
'''


from typing import List

from mastapy.system_model.part_model.gears import _2102
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6171
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns import _4055, _4054, _4053
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_MODAL_ANALYSES_AT_SPEEDS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtSpeedsNS', 'KlingelnbergCycloPalloidHypoidGearSetModalAnalysesAtSpeeds')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearSetModalAnalysesAtSpeeds',)


class KlingelnbergCycloPalloidHypoidGearSetModalAnalysesAtSpeeds(_4053.KlingelnbergCycloPalloidConicalGearSetModalAnalysesAtSpeeds):
    '''KlingelnbergCycloPalloidHypoidGearSetModalAnalysesAtSpeeds

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_MODAL_ANALYSES_AT_SPEEDS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearSetModalAnalysesAtSpeeds.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2102.KlingelnbergCycloPalloidHypoidGearSet':
        '''KlingelnbergCycloPalloidHypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2102.KlingelnbergCycloPalloidHypoidGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6171.KlingelnbergCycloPalloidHypoidGearSetLoadCase':
        '''KlingelnbergCycloPalloidHypoidGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6171.KlingelnbergCycloPalloidHypoidGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_modal_analyses_at_speeds(self) -> 'List[_4055.KlingelnbergCycloPalloidHypoidGearModalAnalysesAtSpeeds]':
        '''List[KlingelnbergCycloPalloidHypoidGearModalAnalysesAtSpeeds]: 'KlingelnbergCycloPalloidHypoidGearsModalAnalysesAtSpeeds' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearsModalAnalysesAtSpeeds, constructor.new(_4055.KlingelnbergCycloPalloidHypoidGearModalAnalysesAtSpeeds))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_modal_analyses_at_speeds(self) -> 'List[_4054.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysesAtSpeeds]':
        '''List[KlingelnbergCycloPalloidHypoidGearMeshModalAnalysesAtSpeeds]: 'KlingelnbergCycloPalloidHypoidMeshesModalAnalysesAtSpeeds' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidMeshesModalAnalysesAtSpeeds, constructor.new(_4054.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysesAtSpeeds))
        return value
