'''_5361.py

KlingelnbergCycloPalloidConicalGearSetGearWhineAnalysis
'''


from mastapy.system_model.part_model.gears import _2100, _2102, _2104
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.system_deflections import _2302, _2305, _2308
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5310
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'KlingelnbergCycloPalloidConicalGearSetGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidConicalGearSetGearWhineAnalysis',)


class KlingelnbergCycloPalloidConicalGearSetGearWhineAnalysis(_5310.ConicalGearSetGearWhineAnalysis):
    '''KlingelnbergCycloPalloidConicalGearSetGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_GEAR_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidConicalGearSetGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2100.KlingelnbergCycloPalloidConicalGearSet':
        '''KlingelnbergCycloPalloidConicalGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2100.KlingelnbergCycloPalloidConicalGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set(self) -> '_2102.KlingelnbergCycloPalloidHypoidGearSet':
        '''KlingelnbergCycloPalloidHypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2102.KlingelnbergCycloPalloidHypoidGearSet.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to KlingelnbergCycloPalloidHypoidGearSet. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new(_2102.KlingelnbergCycloPalloidHypoidGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self) -> '_2104.KlingelnbergCycloPalloidSpiralBevelGearSet':
        '''KlingelnbergCycloPalloidSpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2104.KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to KlingelnbergCycloPalloidSpiralBevelGearSet. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new(_2104.KlingelnbergCycloPalloidSpiralBevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def system_deflection_results(self) -> '_2302.KlingelnbergCycloPalloidConicalGearSetSystemDeflection':
        '''KlingelnbergCycloPalloidConicalGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2302.KlingelnbergCycloPalloidConicalGearSetSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None

    @property
    def system_deflection_results_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set_system_deflection(self) -> '_2305.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection':
        '''KlingelnbergCycloPalloidHypoidGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2305.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to KlingelnbergCycloPalloidHypoidGearSetSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new(_2305.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None

    @property
    def system_deflection_results_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_system_deflection(self) -> '_2308.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection':
        '''KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2308.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new(_2308.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
