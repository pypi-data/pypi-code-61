'''_3092.py

StraightBevelDiffGearSteadyStateSynchronousResponse
'''


from mastapy.system_model.part_model.gears import _2108
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6212
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3005
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'StraightBevelDiffGearSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearSteadyStateSynchronousResponse',)


class StraightBevelDiffGearSteadyStateSynchronousResponse(_3005.BevelGearSteadyStateSynchronousResponse):
    '''StraightBevelDiffGearSteadyStateSynchronousResponse

    This is a mastapy class.
    '''

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2108.StraightBevelDiffGear':
        '''StraightBevelDiffGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2108.StraightBevelDiffGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6212.StraightBevelDiffGearLoadCase':
        '''StraightBevelDiffGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6212.StraightBevelDiffGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
