'''_4792.py

KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis
'''


from mastapy.system_model.part_model.gears import _2103
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6172
from mastapy.system_model.analyses_and_results.system_deflections import _2309
from mastapy.system_model.analyses_and_results.modal_analyses import _4786
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis',)


class KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis(_4786.KlingelnbergCycloPalloidConicalGearModalAnalysis):
    '''KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2103.KlingelnbergCycloPalloidSpiralBevelGear':
        '''KlingelnbergCycloPalloidSpiralBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2103.KlingelnbergCycloPalloidSpiralBevelGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6172.KlingelnbergCycloPalloidSpiralBevelGearLoadCase':
        '''KlingelnbergCycloPalloidSpiralBevelGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6172.KlingelnbergCycloPalloidSpiralBevelGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def system_deflection_results(self) -> '_2309.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection':
        '''KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2309.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
