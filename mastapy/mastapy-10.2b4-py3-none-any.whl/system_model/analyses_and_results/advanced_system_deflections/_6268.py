'''_6268.py

BearingAdvancedSystemDeflection
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.bearings.bearing_results import _1584, _1592, _1595
from mastapy._internal.cast_exception import CastException
from mastapy.bearings.bearing_results.rolling import (
    _1621, _1628, _1636, _1652,
    _1676
)
from mastapy.system_model.part_model import _2007
from mastapy.system_model.analyses_and_results.static_loads import _6081
from mastapy.system_model.analyses_and_results.system_deflections import _2238
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _6296
from mastapy._internal.python_net import python_net_import

_BEARING_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'BearingAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingAdvancedSystemDeflection',)


class BearingAdvancedSystemDeflection(_6296.ConnectorAdvancedSystemDeflection):
    '''BearingAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _BEARING_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BearingAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def use_variable_stiffness(self) -> 'bool':
        '''bool: 'UseVariableStiffness' is the original name of this property.'''

        return self.wrapped.UseVariableStiffness

    @use_variable_stiffness.setter
    def use_variable_stiffness(self, value: 'bool'):
        self.wrapped.UseVariableStiffness = bool(value) if value else False

    @property
    def duty_cycle(self) -> '_1584.LoadedBearingDutyCycle':
        '''LoadedBearingDutyCycle: 'DutyCycle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1584.LoadedBearingDutyCycle.TYPE not in self.wrapped.DutyCycle.__class__.__mro__:
            raise CastException('Failed to cast duty_cycle to LoadedBearingDutyCycle. Expected: {}.'.format(self.wrapped.DutyCycle.__class__.__qualname__))

        return constructor.new_override(self.wrapped.DutyCycle.__class__)(self.wrapped.DutyCycle) if self.wrapped.DutyCycle else None

    @property
    def component_design(self) -> '_2007.Bearing':
        '''Bearing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2007.Bearing)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6081.BearingLoadCase':
        '''BearingLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6081.BearingLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def planetaries(self) -> 'List[BearingAdvancedSystemDeflection]':
        '''List[BearingAdvancedSystemDeflection]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(BearingAdvancedSystemDeflection))
        return value

    @property
    def component_system_deflection_results(self) -> 'List[_2238.BearingSystemDeflection]':
        '''List[BearingSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentSystemDeflectionResults, constructor.new(_2238.BearingSystemDeflection))
        return value
