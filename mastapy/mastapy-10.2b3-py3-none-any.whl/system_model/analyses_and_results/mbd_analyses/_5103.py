'''_5103.py

StraightBevelDiffGearMultiBodyDynamicsAnalysis
'''


from mastapy.system_model.part_model.gears import _2108
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6212
from mastapy.system_model.analyses_and_results.mbd_analyses import _5007
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MULTI_BODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'StraightBevelDiffGearMultiBodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearMultiBodyDynamicsAnalysis',)


class StraightBevelDiffGearMultiBodyDynamicsAnalysis(_5007.BevelGearMultiBodyDynamicsAnalysis):
    '''StraightBevelDiffGearMultiBodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MULTI_BODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearMultiBodyDynamicsAnalysis.TYPE'):
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
