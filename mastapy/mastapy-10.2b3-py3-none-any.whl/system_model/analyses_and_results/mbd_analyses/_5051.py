'''_5051.py

HypoidGearSetMultiBodyDynamicsAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2098
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6162
from mastapy.system_model.analyses_and_results.mbd_analyses import _5050, _5049, _4994
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_MULTI_BODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'HypoidGearSetMultiBodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetMultiBodyDynamicsAnalysis',)


class HypoidGearSetMultiBodyDynamicsAnalysis(_4994.AGMAGleasonConicalGearSetMultiBodyDynamicsAnalysis):
    '''HypoidGearSetMultiBodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _HYPOID_GEAR_SET_MULTI_BODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearSetMultiBodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2098.HypoidGearSet':
        '''HypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2098.HypoidGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6162.HypoidGearSetLoadCase':
        '''HypoidGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6162.HypoidGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def gears(self) -> 'List[_5050.HypoidGearMultiBodyDynamicsAnalysis]':
        '''List[HypoidGearMultiBodyDynamicsAnalysis]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Gears, constructor.new(_5050.HypoidGearMultiBodyDynamicsAnalysis))
        return value

    @property
    def hypoid_gears_multi_body_dynamics_analysis(self) -> 'List[_5050.HypoidGearMultiBodyDynamicsAnalysis]':
        '''List[HypoidGearMultiBodyDynamicsAnalysis]: 'HypoidGearsMultiBodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearsMultiBodyDynamicsAnalysis, constructor.new(_5050.HypoidGearMultiBodyDynamicsAnalysis))
        return value

    @property
    def hypoid_meshes_multi_body_dynamics_analysis(self) -> 'List[_5049.HypoidGearMeshMultiBodyDynamicsAnalysis]':
        '''List[HypoidGearMeshMultiBodyDynamicsAnalysis]: 'HypoidMeshesMultiBodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidMeshesMultiBodyDynamicsAnalysis, constructor.new(_5049.HypoidGearMeshMultiBodyDynamicsAnalysis))
        return value
