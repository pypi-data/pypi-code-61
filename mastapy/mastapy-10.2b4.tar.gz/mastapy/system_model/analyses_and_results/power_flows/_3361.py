'''_3361.py

WormGearPowerFlow
'''


from mastapy.system_model.part_model.gears import _2114
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6236
from mastapy.gears.rating.worm import _176
from mastapy.system_model.analyses_and_results.power_flows import _3294
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'WormGearPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearPowerFlow',)


class WormGearPowerFlow(_3294.GearPowerFlow):
    '''WormGearPowerFlow

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2114.WormGear':
        '''WormGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2114.WormGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6236.WormGearLoadCase':
        '''WormGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6236.WormGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def component_detailed_analysis(self) -> '_176.WormGearRating':
        '''WormGearRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_176.WormGearRating)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None
