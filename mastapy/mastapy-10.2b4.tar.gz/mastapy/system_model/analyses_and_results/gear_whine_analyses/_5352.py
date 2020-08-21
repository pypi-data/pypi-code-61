'''_5352.py

GuideDxfModelGearWhineAnalysis
'''


from mastapy.system_model.part_model import _2020
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6151
from mastapy.system_model.analyses_and_results.system_deflections import _2295
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5301
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'GuideDxfModelGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GuideDxfModelGearWhineAnalysis',)


class GuideDxfModelGearWhineAnalysis(_5301.ComponentGearWhineAnalysis):
    '''GuideDxfModelGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _GUIDE_DXF_MODEL_GEAR_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GuideDxfModelGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2020.GuideDxfModel':
        '''GuideDxfModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2020.GuideDxfModel)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6151.GuideDxfModelLoadCase':
        '''GuideDxfModelLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6151.GuideDxfModelLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def system_deflection_results(self) -> '_2295.GuideDxfModelSystemDeflection':
        '''GuideDxfModelSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2295.GuideDxfModelSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
