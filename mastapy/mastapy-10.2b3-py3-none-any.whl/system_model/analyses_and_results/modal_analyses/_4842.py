'''_4842.py

TorqueConverterPumpModalAnalysis
'''


from mastapy.system_model.part_model.couplings import _2165
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6228
from mastapy.system_model.analyses_and_results.system_deflections import _2358
from mastapy.system_model.analyses_and_results.modal_analyses import _4760
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'TorqueConverterPumpModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterPumpModalAnalysis',)


class TorqueConverterPumpModalAnalysis(_4760.CouplingHalfModalAnalysis):
    '''TorqueConverterPumpModalAnalysis

    This is a mastapy class.
    '''

    TYPE = _TORQUE_CONVERTER_PUMP_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterPumpModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2165.TorqueConverterPump':
        '''TorqueConverterPump: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2165.TorqueConverterPump)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6228.TorqueConverterPumpLoadCase':
        '''TorqueConverterPumpLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6228.TorqueConverterPumpLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def system_deflection_results(self) -> '_2358.TorqueConverterPumpSystemDeflection':
        '''TorqueConverterPumpSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2358.TorqueConverterPumpSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
