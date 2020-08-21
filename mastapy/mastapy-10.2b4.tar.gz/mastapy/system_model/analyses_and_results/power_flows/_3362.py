'''_3362.py

WormGearSetPowerFlow
'''


from typing import List

from mastapy.system_model.part_model.gears import _2115
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6238
from mastapy.gears.rating.worm import _178
from mastapy.system_model.analyses_and_results.power_flows import _3361, _3360, _3295
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'WormGearSetPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetPowerFlow',)


class WormGearSetPowerFlow(_3295.GearSetPowerFlow):
    '''WormGearSetPowerFlow

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR_SET_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearSetPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2115.WormGearSet':
        '''WormGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2115.WormGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6238.WormGearSetLoadCase':
        '''WormGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6238.WormGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def rating(self) -> '_178.WormGearSetRating':
        '''WormGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_178.WormGearSetRating)(self.wrapped.Rating) if self.wrapped.Rating else None

    @property
    def component_detailed_analysis(self) -> '_178.WormGearSetRating':
        '''WormGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_178.WormGearSetRating)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def gears_power_flow(self) -> 'List[_3361.WormGearPowerFlow]':
        '''List[WormGearPowerFlow]: 'GearsPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.GearsPowerFlow, constructor.new(_3361.WormGearPowerFlow))
        return value

    @property
    def worm_gears_power_flow(self) -> 'List[_3361.WormGearPowerFlow]':
        '''List[WormGearPowerFlow]: 'WormGearsPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearsPowerFlow, constructor.new(_3361.WormGearPowerFlow))
        return value

    @property
    def meshes_power_flow(self) -> 'List[_3360.WormGearMeshPowerFlow]':
        '''List[WormGearMeshPowerFlow]: 'MeshesPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeshesPowerFlow, constructor.new(_3360.WormGearMeshPowerFlow))
        return value

    @property
    def worm_meshes_power_flow(self) -> 'List[_3360.WormGearMeshPowerFlow]':
        '''List[WormGearMeshPowerFlow]: 'WormMeshesPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormMeshesPowerFlow, constructor.new(_3360.WormGearMeshPowerFlow))
        return value
