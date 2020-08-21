'''_4852.py

WormGearModalAnalysis
'''


from mastapy.system_model.part_model.gears import _2114
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6236
from mastapy.system_model.analyses_and_results.system_deflections import _2367
from mastapy.system_model.analyses_and_results.modal_analyses import _4777
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'WormGearModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearModalAnalysis',)


class WormGearModalAnalysis(_4777.GearModalAnalysis):
    '''WormGearModalAnalysis

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearModalAnalysis.TYPE'):
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
    def system_deflection_results(self) -> '_2367.WormGearSystemDeflection':
        '''WormGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2367.WormGearSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
