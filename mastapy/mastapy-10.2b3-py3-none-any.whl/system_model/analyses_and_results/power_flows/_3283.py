'''_3283.py

CylindricalGearMeshPowerFlow
'''


from mastapy.system_model.connections_and_sockets.gears import _1891
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6120
from mastapy.gears.rating.cylindrical import _257
from mastapy.system_model.analyses_and_results.power_flows import _3293
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'CylindricalGearMeshPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMeshPowerFlow',)


class CylindricalGearMeshPowerFlow(_3293.GearMeshPowerFlow):
    '''CylindricalGearMeshPowerFlow

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_GEAR_MESH_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearMeshPowerFlow.TYPE'):
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
    def rating(self) -> '_257.CylindricalGearMeshRating':
        '''CylindricalGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_257.CylindricalGearMeshRating)(self.wrapped.Rating) if self.wrapped.Rating else None

    @property
    def component_detailed_analysis(self) -> '_257.CylindricalGearMeshRating':
        '''CylindricalGearMeshRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_257.CylindricalGearMeshRating)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None
