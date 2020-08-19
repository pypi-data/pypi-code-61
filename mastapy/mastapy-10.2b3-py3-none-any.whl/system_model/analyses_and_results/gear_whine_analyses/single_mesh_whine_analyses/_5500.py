'''_5500.py

KlingelnbergCycloPalloidHypoidGearSingleMeshWhineAnalysis
'''


from mastapy.system_model.part_model.gears import _2101
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6169
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses import _5497
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SINGLE_MESH_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.SingleMeshWhineAnalyses', 'KlingelnbergCycloPalloidHypoidGearSingleMeshWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearSingleMeshWhineAnalysis',)


class KlingelnbergCycloPalloidHypoidGearSingleMeshWhineAnalysis(_5497.KlingelnbergCycloPalloidConicalGearSingleMeshWhineAnalysis):
    '''KlingelnbergCycloPalloidHypoidGearSingleMeshWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SINGLE_MESH_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearSingleMeshWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2101.KlingelnbergCycloPalloidHypoidGear':
        '''KlingelnbergCycloPalloidHypoidGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2101.KlingelnbergCycloPalloidHypoidGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6169.KlingelnbergCycloPalloidHypoidGearLoadCase':
        '''KlingelnbergCycloPalloidHypoidGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6169.KlingelnbergCycloPalloidHypoidGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
