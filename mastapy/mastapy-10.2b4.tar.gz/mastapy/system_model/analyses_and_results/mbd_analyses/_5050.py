'''_5050.py

HypoidGearMultiBodyDynamicsAnalysis
'''


from mastapy.system_model.part_model.gears import _2097
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6160
from mastapy.system_model.analyses_and_results.mbd_analyses import _4993
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MULTI_BODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'HypoidGearMultiBodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearMultiBodyDynamicsAnalysis',)


class HypoidGearMultiBodyDynamicsAnalysis(_4993.AGMAGleasonConicalGearMultiBodyDynamicsAnalysis):
    '''HypoidGearMultiBodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _HYPOID_GEAR_MULTI_BODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearMultiBodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2097.HypoidGear':
        '''HypoidGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2097.HypoidGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6160.HypoidGearLoadCase':
        '''HypoidGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6160.HypoidGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
