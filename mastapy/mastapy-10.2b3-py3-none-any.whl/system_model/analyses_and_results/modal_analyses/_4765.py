'''_4765.py

CylindricalGearMeshModalAnalysis
'''


from typing import List

from mastapy.system_model.connections_and_sockets.gears import _1891
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6120
from mastapy.system_model.analyses_and_results.system_deflections import _2275, _2276, _2277
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.modal_analyses import _4776
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'CylindricalGearMeshModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMeshModalAnalysis',)


class CylindricalGearMeshModalAnalysis(_4776.GearMeshModalAnalysis):
    '''CylindricalGearMeshModalAnalysis

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_GEAR_MESH_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearMeshModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_1891.CylindricalGearMesh':
        '''CylindricalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1891.CylindricalGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_load_case(self) -> '_6120.CylindricalGearMeshLoadCase':
        '''CylindricalGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6120.CylindricalGearMeshLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase else None

    @property
    def system_deflection_results(self) -> '_2275.CylindricalGearMeshSystemDeflection':
        '''CylindricalGearMeshSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2275.CylindricalGearMeshSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None

    @property
    def system_deflection_results_of_type_cylindrical_gear_mesh_system_deflection_timestep(self) -> '_2276.CylindricalGearMeshSystemDeflectionTimestep':
        '''CylindricalGearMeshSystemDeflectionTimestep: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2276.CylindricalGearMeshSystemDeflectionTimestep.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to CylindricalGearMeshSystemDeflectionTimestep. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new(_2276.CylindricalGearMeshSystemDeflectionTimestep)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None

    @property
    def system_deflection_results_of_type_cylindrical_gear_mesh_system_deflection_with_ltca_results(self) -> '_2277.CylindricalGearMeshSystemDeflectionWithLTCAResults':
        '''CylindricalGearMeshSystemDeflectionWithLTCAResults: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2277.CylindricalGearMeshSystemDeflectionWithLTCAResults.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to CylindricalGearMeshSystemDeflectionWithLTCAResults. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new(_2277.CylindricalGearMeshSystemDeflectionWithLTCAResults)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None

    @property
    def planetaries(self) -> 'List[CylindricalGearMeshModalAnalysis]':
        '''List[CylindricalGearMeshModalAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(CylindricalGearMeshModalAnalysis))
        return value
