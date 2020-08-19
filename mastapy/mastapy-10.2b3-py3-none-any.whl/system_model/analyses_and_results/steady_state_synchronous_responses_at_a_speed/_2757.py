'''_2757.py

BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed
'''


from mastapy.system_model.part_model.gears import _2078
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6084
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _2762
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed', 'BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed',)


class BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed(_2762.BevelGearSteadyStateSynchronousResponseAtASpeed):
    '''BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    '''

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2078.BevelDifferentialGear':
        '''BevelDifferentialGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2078.BevelDifferentialGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6084.BevelDifferentialGearLoadCase':
        '''BevelDifferentialGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6084.BevelDifferentialGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
