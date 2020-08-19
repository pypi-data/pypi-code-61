'''_4073.py

PointLoadModalAnalysesAtSpeeds
'''


from mastapy.system_model.part_model import _2036
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6192
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns import _4108
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_MODAL_ANALYSES_AT_SPEEDS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtSpeedsNS', 'PointLoadModalAnalysesAtSpeeds')


__docformat__ = 'restructuredtext en'
__all__ = ('PointLoadModalAnalysesAtSpeeds',)


class PointLoadModalAnalysesAtSpeeds(_4108.VirtualComponentModalAnalysesAtSpeeds):
    '''PointLoadModalAnalysesAtSpeeds

    This is a mastapy class.
    '''

    TYPE = _POINT_LOAD_MODAL_ANALYSES_AT_SPEEDS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PointLoadModalAnalysesAtSpeeds.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2036.PointLoad':
        '''PointLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2036.PointLoad)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6192.PointLoadLoadCase':
        '''PointLoadLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6192.PointLoadLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
