'''_1972.py

ImportedFEWithSelectionComponents
'''


from typing import Callable, List

from mastapy._internal import constructor, conversion
from mastapy.math_utility import _1069
from mastapy._math.vector_3d import Vector3D
from mastapy.system_model.imported_fes import (
    _1961, _1949, _1979, _1941,
    _1940, _1971
)
from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import (
    _1489, _1491, _1490, _1486,
    _1492, _1488, _1487, _1485
)
from mastapy._internal.python_net import python_net_import

_IMPORTED_FE_WITH_SELECTION_COMPONENTS = python_net_import('SMT.MastaAPI.SystemModel.ImportedFEs', 'ImportedFEWithSelectionComponents')


__docformat__ = 'restructuredtext en'
__all__ = ('ImportedFEWithSelectionComponents',)


class ImportedFEWithSelectionComponents(_1971.ImportedFEWithSelection):
    '''ImportedFEWithSelectionComponents

    This is a mastapy class.
    '''

    TYPE = _IMPORTED_FE_WITH_SELECTION_COMPONENTS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ImportedFEWithSelectionComponents.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def replace_selected_shaft(self) -> 'Callable[..., None]':
        '''Callable[..., None]: 'ReplaceSelectedShaft' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ReplaceSelectedShaft

    @property
    def auto_select_node_ring(self) -> 'Callable[..., None]':
        '''Callable[..., None]: 'AutoSelectNodeRing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AutoSelectNodeRing

    @property
    def use_selected_component_for_alignment(self) -> 'Callable[..., None]':
        '''Callable[..., None]: 'UseSelectedComponentForAlignment' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.UseSelectedComponentForAlignment

    @property
    def radius_of_circle_through_selected_nodes(self) -> 'float':
        '''float: 'RadiusOfCircleThroughSelectedNodes' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.RadiusOfCircleThroughSelectedNodes

    @property
    def manual_alignment(self) -> '_1069.CoordinateSystemEditor':
        '''CoordinateSystemEditor: 'ManualAlignment' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1069.CoordinateSystemEditor)(self.wrapped.ManualAlignment) if self.wrapped.ManualAlignment else None

    @property
    def distance_between_selected_nodes(self) -> 'Vector3D':
        '''Vector3D: 'DistanceBetweenSelectedNodes' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_vector3d(self.wrapped.DistanceBetweenSelectedNodes)
        return value

    @property
    def midpoint_of_selected_nodes(self) -> 'Vector3D':
        '''Vector3D: 'MidpointOfSelectedNodes' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_vector3d(self.wrapped.MidpointOfSelectedNodes)
        return value

    @property
    def centre_of_circle_through_selected_nodes(self) -> 'Vector3D':
        '''Vector3D: 'CentreOfCircleThroughSelectedNodes' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_vector3d(self.wrapped.CentreOfCircleThroughSelectedNodes)
        return value

    @property
    def component_links(self) -> 'List[_1961.ImportedFeLinkWithSelection]':
        '''List[ImportedFeLinkWithSelection]: 'ComponentLinks' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentLinks, constructor.new(_1961.ImportedFeLinkWithSelection))
        return value

    @property
    def links_for_selected_component(self) -> 'List[_1961.ImportedFeLinkWithSelection]':
        '''List[ImportedFeLinkWithSelection]: 'LinksForSelectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LinksForSelectedComponent, constructor.new(_1961.ImportedFeLinkWithSelection))
        return value

    @property
    def links_for_electric_machine(self) -> 'List[_1961.ImportedFeLinkWithSelection]':
        '''List[ImportedFeLinkWithSelection]: 'LinksForElectricMachine' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LinksForElectricMachine, constructor.new(_1961.ImportedFeLinkWithSelection))
        return value

    @property
    def rigid_element_properties(self) -> 'List[_1949.ElementPropertiesWithSelection[_1489.ElementPropertiesRigid]]':
        '''List[ElementPropertiesWithSelection[ElementPropertiesRigid]]: 'RigidElementProperties' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RigidElementProperties, constructor.new(_1949.ElementPropertiesWithSelection)[_1489.ElementPropertiesRigid])
        return value

    @property
    def solid_element_properties(self) -> 'List[_1949.ElementPropertiesWithSelection[_1491.ElementPropertiesSolid]]':
        '''List[ElementPropertiesWithSelection[ElementPropertiesSolid]]: 'SolidElementProperties' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SolidElementProperties, constructor.new(_1949.ElementPropertiesWithSelection)[_1491.ElementPropertiesSolid])
        return value

    @property
    def shell_element_properties(self) -> 'List[_1949.ElementPropertiesWithSelection[_1490.ElementPropertiesShell]]':
        '''List[ElementPropertiesWithSelection[ElementPropertiesShell]]: 'ShellElementProperties' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShellElementProperties, constructor.new(_1949.ElementPropertiesWithSelection)[_1490.ElementPropertiesShell])
        return value

    @property
    def beam_element_properties(self) -> 'List[_1949.ElementPropertiesWithSelection[_1486.ElementPropertiesBeam]]':
        '''List[ElementPropertiesWithSelection[ElementPropertiesBeam]]: 'BeamElementProperties' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeamElementProperties, constructor.new(_1949.ElementPropertiesWithSelection)[_1486.ElementPropertiesBeam])
        return value

    @property
    def spring_dashpot_element_properties(self) -> 'List[_1949.ElementPropertiesWithSelection[_1492.ElementPropertiesSpringDashpot]]':
        '''List[ElementPropertiesWithSelection[ElementPropertiesSpringDashpot]]: 'SpringDashpotElementProperties' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDashpotElementProperties, constructor.new(_1949.ElementPropertiesWithSelection)[_1492.ElementPropertiesSpringDashpot])
        return value

    @property
    def mass_element_properties(self) -> 'List[_1949.ElementPropertiesWithSelection[_1488.ElementPropertiesMass]]':
        '''List[ElementPropertiesWithSelection[ElementPropertiesMass]]: 'MassElementProperties' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassElementProperties, constructor.new(_1949.ElementPropertiesWithSelection)[_1488.ElementPropertiesMass])
        return value

    @property
    def interface_element_properties(self) -> 'List[_1949.ElementPropertiesWithSelection[_1487.ElementPropertiesInterface]]':
        '''List[ElementPropertiesWithSelection[ElementPropertiesInterface]]: 'InterfaceElementProperties' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.InterfaceElementProperties, constructor.new(_1949.ElementPropertiesWithSelection)[_1487.ElementPropertiesInterface])
        return value

    @property
    def other_element_properties(self) -> 'List[_1949.ElementPropertiesWithSelection[_1485.ElementPropertiesBase]]':
        '''List[ElementPropertiesWithSelection[ElementPropertiesBase]]: 'OtherElementProperties' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OtherElementProperties, constructor.new(_1949.ElementPropertiesWithSelection)[_1485.ElementPropertiesBase])
        return value

    @property
    def materials(self) -> 'List[_1979.MaterialPropertiesWithSelection]':
        '''List[MaterialPropertiesWithSelection]: 'Materials' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Materials, constructor.new(_1979.MaterialPropertiesWithSelection))
        return value

    @property
    def coordinate_systems(self) -> 'List[_1941.CoordinateSystemWithSelection]':
        '''List[CoordinateSystemWithSelection]: 'CoordinateSystems' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CoordinateSystems, constructor.new(_1941.CoordinateSystemWithSelection))
        return value

    @property
    def contact_pairs(self) -> 'List[_1940.ContactPairWithSelection]':
        '''List[ContactPairWithSelection]: 'ContactPairs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ContactPairs, constructor.new(_1940.ContactPairWithSelection))
        return value
