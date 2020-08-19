'''_5936.py

TorqueConverterTurbineDynamicAnalysis
'''


from mastapy.system_model.part_model.couplings import _2167
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6229
from mastapy.system_model.analyses_and_results.dynamic_analyses import _5859
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'TorqueConverterTurbineDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterTurbineDynamicAnalysis',)


class TorqueConverterTurbineDynamicAnalysis(_5859.CouplingHalfDynamicAnalysis):
    '''TorqueConverterTurbineDynamicAnalysis

    This is a mastapy class.
    '''

    TYPE = _TORQUE_CONVERTER_TURBINE_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterTurbineDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2167.TorqueConverterTurbine':
        '''TorqueConverterTurbine: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2167.TorqueConverterTurbine)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6229.TorqueConverterTurbineLoadCase':
        '''TorqueConverterTurbineLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6229.TorqueConverterTurbineLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
