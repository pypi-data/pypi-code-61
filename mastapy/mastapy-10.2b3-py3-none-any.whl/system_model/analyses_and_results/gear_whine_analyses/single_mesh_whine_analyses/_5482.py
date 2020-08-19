'''_5482.py

FaceGearMeshSingleMeshWhineAnalysis
'''


from mastapy.system_model.connections_and_sockets.gears import _1893
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6141
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses import _5486
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_SINGLE_MESH_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.SingleMeshWhineAnalyses', 'FaceGearMeshSingleMeshWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearMeshSingleMeshWhineAnalysis',)


class FaceGearMeshSingleMeshWhineAnalysis(_5486.GearMeshSingleMeshWhineAnalysis):
    '''FaceGearMeshSingleMeshWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _FACE_GEAR_MESH_SINGLE_MESH_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearMeshSingleMeshWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_1893.FaceGearMesh':
        '''FaceGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1893.FaceGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_load_case(self) -> '_6141.FaceGearMeshLoadCase':
        '''FaceGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6141.FaceGearMeshLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase else None
