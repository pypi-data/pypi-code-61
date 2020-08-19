'''_4100.py

SynchroniserModalAnalysesAtSpeeds
'''


from mastapy.system_model.part_model.couplings import _2159
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6221
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns import _4083
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_MODAL_ANALYSES_AT_SPEEDS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtSpeedsNS', 'SynchroniserModalAnalysesAtSpeeds')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserModalAnalysesAtSpeeds',)


class SynchroniserModalAnalysesAtSpeeds(_4083.SpecialisedAssemblyModalAnalysesAtSpeeds):
    '''SynchroniserModalAnalysesAtSpeeds

    This is a mastapy class.
    '''

    TYPE = _SYNCHRONISER_MODAL_ANALYSES_AT_SPEEDS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SynchroniserModalAnalysesAtSpeeds.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2159.Synchroniser':
        '''Synchroniser: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2159.Synchroniser)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6221.SynchroniserLoadCase':
        '''SynchroniserLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6221.SynchroniserLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None
