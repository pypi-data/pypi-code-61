'''_5515.py

PlanetCarrierSingleMeshWhineAnalysis
'''


from mastapy.system_model.part_model import _2034
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6189
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses import _5507
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_SINGLE_MESH_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.SingleMeshWhineAnalyses', 'PlanetCarrierSingleMeshWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetCarrierSingleMeshWhineAnalysis',)


class PlanetCarrierSingleMeshWhineAnalysis(_5507.MountableComponentSingleMeshWhineAnalysis):
    '''PlanetCarrierSingleMeshWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _PLANET_CARRIER_SINGLE_MESH_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PlanetCarrierSingleMeshWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2034.PlanetCarrier':
        '''PlanetCarrier: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2034.PlanetCarrier)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6189.PlanetCarrierLoadCase':
        '''PlanetCarrierLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6189.PlanetCarrierLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
