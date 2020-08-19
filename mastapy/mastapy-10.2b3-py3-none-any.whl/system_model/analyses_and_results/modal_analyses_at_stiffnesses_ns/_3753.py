'''_3753.py

BeltDriveModalAnalysesAtStiffnesses
'''


from mastapy.system_model.part_model.couplings import _2135
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6083
from mastapy.system_model.analyses_and_results.modal_analyses_at_stiffnesses_ns import _3838
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_MODAL_ANALYSES_AT_STIFFNESSES = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtStiffnessesNS', 'BeltDriveModalAnalysesAtStiffnesses')


__docformat__ = 'restructuredtext en'
__all__ = ('BeltDriveModalAnalysesAtStiffnesses',)


class BeltDriveModalAnalysesAtStiffnesses(_3838.SpecialisedAssemblyModalAnalysesAtStiffnesses):
    '''BeltDriveModalAnalysesAtStiffnesses

    This is a mastapy class.
    '''

    TYPE = _BELT_DRIVE_MODAL_ANALYSES_AT_STIFFNESSES

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BeltDriveModalAnalysesAtStiffnesses.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2135.BeltDrive':
        '''BeltDrive: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2135.BeltDrive)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6083.BeltDriveLoadCase':
        '''BeltDriveLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6083.BeltDriveLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None
