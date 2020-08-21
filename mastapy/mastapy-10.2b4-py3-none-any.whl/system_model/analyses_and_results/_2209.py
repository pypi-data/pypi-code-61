'''_2209.py

CompoundAdvancedSystemDeflectionAnalysis
'''


from typing import Iterable

from mastapy.system_model.part_model import (
    _2003, _2004, _2007, _2009,
    _2010, _2011, _2014, _2015,
    _2018, _2019, _2002, _2020,
    _2023, _2027, _2028, _2029,
    _2031, _2033, _2034, _2036,
    _2037, _2039, _2041, _2042,
    _2043
)
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _6388, _6389, _6394, _6405,
    _6406, _6411, _6422, _6433,
    _6434, _6438, _6393, _6442,
    _6446, _6457, _6458, _6459,
    _6460, _6461, _6467, _6468,
    _6469, _6474, _6478, _6501,
    _6502, _6475, _6415, _6417,
    _6435, _6437, _6390, _6392,
    _6397, _6399, _6400, _6401,
    _6402, _6404, _6418, _6420,
    _6429, _6431, _6432, _6439,
    _6441, _6443, _6445, _6448,
    _6450, _6451, _6453, _6454,
    _6456, _6466, _6479, _6481,
    _6485, _6487, _6488, _6490,
    _6491, _6492, _6503, _6505,
    _6506, _6508, _6462, _6464,
    _6396, _6407, _6409, _6412,
    _6414, _6423, _6425, _6427,
    _6428, _6470, _6476, _6472,
    _6471, _6482, _6484, _6493,
    _6494, _6495, _6496, _6497,
    _6499, _6500, _6426, _6395,
    _6410, _6421, _6447, _6465,
    _6473, _6477, _6398, _6416,
    _6436, _6486, _6403, _6419,
    _6391, _6430, _6444, _6449,
    _6452, _6455, _6480, _6489,
    _6504, _6507, _6440, _6463,
    _6408, _6413, _6424, _6483,
    _6498
)
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.shaft_model import _2046
from mastapy.system_model.part_model.gears import (
    _2084, _2085, _2091, _2092,
    _2076, _2077, _2078, _2079,
    _2080, _2081, _2082, _2083,
    _2086, _2087, _2088, _2089,
    _2090, _2093, _2095, _2097,
    _2098, _2099, _2100, _2101,
    _2102, _2103, _2104, _2105,
    _2106, _2107, _2108, _2109,
    _2110, _2111, _2112, _2113,
    _2114, _2115, _2116, _2117
)
from mastapy.system_model.part_model.couplings import (
    _2146, _2147, _2135, _2137,
    _2138, _2140, _2141, _2142,
    _2143, _2144, _2145, _2148,
    _2156, _2154, _2155, _2157,
    _2158, _2159, _2161, _2162,
    _2163, _2164, _2165, _2167
)
from mastapy.system_model.connections_and_sockets import (
    _1858, _1853, _1854, _1857,
    _1866, _1869, _1873, _1877
)
from mastapy.system_model.connections_and_sockets.gears import (
    _1883, _1887, _1893, _1907,
    _1885, _1889, _1881, _1891,
    _1897, _1900, _1901, _1902,
    _1905, _1909, _1911, _1913,
    _1895
)
from mastapy.system_model.connections_and_sockets.couplings import (
    _1921, _1915, _1917, _1919,
    _1923, _1925
)
from mastapy.system_model.analyses_and_results import _2176
from mastapy._internal.python_net import python_net_import

_COMPOUND_ADVANCED_SYSTEM_DEFLECTION_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'CompoundAdvancedSystemDeflectionAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CompoundAdvancedSystemDeflectionAnalysis',)


class CompoundAdvancedSystemDeflectionAnalysis(_2176.CompoundAnalysis):
    '''CompoundAdvancedSystemDeflectionAnalysis

    This is a mastapy class.
    '''

    TYPE = _COMPOUND_ADVANCED_SYSTEM_DEFLECTION_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CompoundAdvancedSystemDeflectionAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def results_for_abstract_assembly(self, design_entity: '_2003.AbstractAssembly') -> 'Iterable[_6388.AbstractAssemblyCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.AbstractAssemblyCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2003.AbstractAssembly.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6388.AbstractAssemblyCompoundAdvancedSystemDeflection))

    def results_for_abstract_shaft_or_housing(self, design_entity: '_2004.AbstractShaftOrHousing') -> 'Iterable[_6389.AbstractShaftOrHousingCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.AbstractShaftOrHousingCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2004.AbstractShaftOrHousing.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6389.AbstractShaftOrHousingCompoundAdvancedSystemDeflection))

    def results_for_bearing(self, design_entity: '_2007.Bearing') -> 'Iterable[_6394.BearingCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.BearingCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2007.Bearing.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6394.BearingCompoundAdvancedSystemDeflection))

    def results_for_bolt(self, design_entity: '_2009.Bolt') -> 'Iterable[_6405.BoltCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.BoltCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2009.Bolt.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6405.BoltCompoundAdvancedSystemDeflection))

    def results_for_bolted_joint(self, design_entity: '_2010.BoltedJoint') -> 'Iterable[_6406.BoltedJointCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.BoltedJointCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2010.BoltedJoint.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6406.BoltedJointCompoundAdvancedSystemDeflection))

    def results_for_component(self, design_entity: '_2011.Component') -> 'Iterable[_6411.ComponentCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Component)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ComponentCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2011.Component.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6411.ComponentCompoundAdvancedSystemDeflection))

    def results_for_connector(self, design_entity: '_2014.Connector') -> 'Iterable[_6422.ConnectorCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Connector)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ConnectorCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2014.Connector.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6422.ConnectorCompoundAdvancedSystemDeflection))

    def results_for_datum(self, design_entity: '_2015.Datum') -> 'Iterable[_6433.DatumCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Datum)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.DatumCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2015.Datum.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6433.DatumCompoundAdvancedSystemDeflection))

    def results_for_external_cad_model(self, design_entity: '_2018.ExternalCADModel') -> 'Iterable[_6434.ExternalCADModelCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ExternalCADModelCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2018.ExternalCADModel.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6434.ExternalCADModelCompoundAdvancedSystemDeflection))

    def results_for_flexible_pin_assembly(self, design_entity: '_2019.FlexiblePinAssembly') -> 'Iterable[_6438.FlexiblePinAssemblyCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.FlexiblePinAssemblyCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2019.FlexiblePinAssembly.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6438.FlexiblePinAssemblyCompoundAdvancedSystemDeflection))

    def results_for_assembly(self, design_entity: '_2002.Assembly') -> 'Iterable[_6393.AssemblyCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.AssemblyCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2002.Assembly.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6393.AssemblyCompoundAdvancedSystemDeflection))

    def results_for_guide_dxf_model(self, design_entity: '_2020.GuideDxfModel') -> 'Iterable[_6442.GuideDxfModelCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.GuideDxfModelCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2020.GuideDxfModel.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6442.GuideDxfModelCompoundAdvancedSystemDeflection))

    def results_for_imported_fe_component(self, design_entity: '_2023.ImportedFEComponent') -> 'Iterable[_6446.ImportedFEComponentCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ImportedFEComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ImportedFEComponentCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2023.ImportedFEComponent.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6446.ImportedFEComponentCompoundAdvancedSystemDeflection))

    def results_for_mass_disc(self, design_entity: '_2027.MassDisc') -> 'Iterable[_6457.MassDiscCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.MassDiscCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2027.MassDisc.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6457.MassDiscCompoundAdvancedSystemDeflection))

    def results_for_measurement_component(self, design_entity: '_2028.MeasurementComponent') -> 'Iterable[_6458.MeasurementComponentCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.MeasurementComponentCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2028.MeasurementComponent.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6458.MeasurementComponentCompoundAdvancedSystemDeflection))

    def results_for_mountable_component(self, design_entity: '_2029.MountableComponent') -> 'Iterable[_6459.MountableComponentCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.MountableComponentCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2029.MountableComponent.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6459.MountableComponentCompoundAdvancedSystemDeflection))

    def results_for_oil_seal(self, design_entity: '_2031.OilSeal') -> 'Iterable[_6460.OilSealCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.OilSealCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2031.OilSeal.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6460.OilSealCompoundAdvancedSystemDeflection))

    def results_for_part(self, design_entity: '_2033.Part') -> 'Iterable[_6461.PartCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Part)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.PartCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2033.Part.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6461.PartCompoundAdvancedSystemDeflection))

    def results_for_planet_carrier(self, design_entity: '_2034.PlanetCarrier') -> 'Iterable[_6467.PlanetCarrierCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.PlanetCarrierCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2034.PlanetCarrier.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6467.PlanetCarrierCompoundAdvancedSystemDeflection))

    def results_for_point_load(self, design_entity: '_2036.PointLoad') -> 'Iterable[_6468.PointLoadCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.PointLoadCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2036.PointLoad.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6468.PointLoadCompoundAdvancedSystemDeflection))

    def results_for_power_load(self, design_entity: '_2037.PowerLoad') -> 'Iterable[_6469.PowerLoadCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.PowerLoadCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2037.PowerLoad.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6469.PowerLoadCompoundAdvancedSystemDeflection))

    def results_for_root_assembly(self, design_entity: '_2039.RootAssembly') -> 'Iterable[_6474.RootAssemblyCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.RootAssemblyCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2039.RootAssembly.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6474.RootAssemblyCompoundAdvancedSystemDeflection))

    def results_for_specialised_assembly(self, design_entity: '_2041.SpecialisedAssembly') -> 'Iterable[_6478.SpecialisedAssemblyCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.SpecialisedAssemblyCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2041.SpecialisedAssembly.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6478.SpecialisedAssemblyCompoundAdvancedSystemDeflection))

    def results_for_unbalanced_mass(self, design_entity: '_2042.UnbalancedMass') -> 'Iterable[_6501.UnbalancedMassCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.UnbalancedMassCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2042.UnbalancedMass.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6501.UnbalancedMassCompoundAdvancedSystemDeflection))

    def results_for_virtual_component(self, design_entity: '_2043.VirtualComponent') -> 'Iterable[_6502.VirtualComponentCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.VirtualComponentCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2043.VirtualComponent.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6502.VirtualComponentCompoundAdvancedSystemDeflection))

    def results_for_shaft(self, design_entity: '_2046.Shaft') -> 'Iterable[_6475.ShaftCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ShaftCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2046.Shaft.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6475.ShaftCompoundAdvancedSystemDeflection))

    def results_for_concept_gear(self, design_entity: '_2084.ConceptGear') -> 'Iterable[_6415.ConceptGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ConceptGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2084.ConceptGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6415.ConceptGearCompoundAdvancedSystemDeflection))

    def results_for_concept_gear_set(self, design_entity: '_2085.ConceptGearSet') -> 'Iterable[_6417.ConceptGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ConceptGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2085.ConceptGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6417.ConceptGearSetCompoundAdvancedSystemDeflection))

    def results_for_face_gear(self, design_entity: '_2091.FaceGear') -> 'Iterable[_6435.FaceGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.FaceGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2091.FaceGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6435.FaceGearCompoundAdvancedSystemDeflection))

    def results_for_face_gear_set(self, design_entity: '_2092.FaceGearSet') -> 'Iterable[_6437.FaceGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.FaceGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2092.FaceGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6437.FaceGearSetCompoundAdvancedSystemDeflection))

    def results_for_agma_gleason_conical_gear(self, design_entity: '_2076.AGMAGleasonConicalGear') -> 'Iterable[_6390.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2076.AGMAGleasonConicalGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6390.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection))

    def results_for_agma_gleason_conical_gear_set(self, design_entity: '_2077.AGMAGleasonConicalGearSet') -> 'Iterable[_6392.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2077.AGMAGleasonConicalGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6392.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection))

    def results_for_bevel_differential_gear(self, design_entity: '_2078.BevelDifferentialGear') -> 'Iterable[_6397.BevelDifferentialGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.BevelDifferentialGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2078.BevelDifferentialGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6397.BevelDifferentialGearCompoundAdvancedSystemDeflection))

    def results_for_bevel_differential_gear_set(self, design_entity: '_2079.BevelDifferentialGearSet') -> 'Iterable[_6399.BevelDifferentialGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.BevelDifferentialGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2079.BevelDifferentialGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6399.BevelDifferentialGearSetCompoundAdvancedSystemDeflection))

    def results_for_bevel_differential_planet_gear(self, design_entity: '_2080.BevelDifferentialPlanetGear') -> 'Iterable[_6400.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2080.BevelDifferentialPlanetGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6400.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection))

    def results_for_bevel_differential_sun_gear(self, design_entity: '_2081.BevelDifferentialSunGear') -> 'Iterable[_6401.BevelDifferentialSunGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.BevelDifferentialSunGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2081.BevelDifferentialSunGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6401.BevelDifferentialSunGearCompoundAdvancedSystemDeflection))

    def results_for_bevel_gear(self, design_entity: '_2082.BevelGear') -> 'Iterable[_6402.BevelGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.BevelGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2082.BevelGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6402.BevelGearCompoundAdvancedSystemDeflection))

    def results_for_bevel_gear_set(self, design_entity: '_2083.BevelGearSet') -> 'Iterable[_6404.BevelGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.BevelGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2083.BevelGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6404.BevelGearSetCompoundAdvancedSystemDeflection))

    def results_for_conical_gear(self, design_entity: '_2086.ConicalGear') -> 'Iterable[_6418.ConicalGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ConicalGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2086.ConicalGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6418.ConicalGearCompoundAdvancedSystemDeflection))

    def results_for_conical_gear_set(self, design_entity: '_2087.ConicalGearSet') -> 'Iterable[_6420.ConicalGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ConicalGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2087.ConicalGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6420.ConicalGearSetCompoundAdvancedSystemDeflection))

    def results_for_cylindrical_gear(self, design_entity: '_2088.CylindricalGear') -> 'Iterable[_6429.CylindricalGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.CylindricalGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2088.CylindricalGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6429.CylindricalGearCompoundAdvancedSystemDeflection))

    def results_for_cylindrical_gear_set(self, design_entity: '_2089.CylindricalGearSet') -> 'Iterable[_6431.CylindricalGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.CylindricalGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2089.CylindricalGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6431.CylindricalGearSetCompoundAdvancedSystemDeflection))

    def results_for_cylindrical_planet_gear(self, design_entity: '_2090.CylindricalPlanetGear') -> 'Iterable[_6432.CylindricalPlanetGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.CylindricalPlanetGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2090.CylindricalPlanetGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6432.CylindricalPlanetGearCompoundAdvancedSystemDeflection))

    def results_for_gear(self, design_entity: '_2093.Gear') -> 'Iterable[_6439.GearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.GearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2093.Gear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6439.GearCompoundAdvancedSystemDeflection))

    def results_for_gear_set(self, design_entity: '_2095.GearSet') -> 'Iterable[_6441.GearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.GearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2095.GearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6441.GearSetCompoundAdvancedSystemDeflection))

    def results_for_hypoid_gear(self, design_entity: '_2097.HypoidGear') -> 'Iterable[_6443.HypoidGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.HypoidGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2097.HypoidGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6443.HypoidGearCompoundAdvancedSystemDeflection))

    def results_for_hypoid_gear_set(self, design_entity: '_2098.HypoidGearSet') -> 'Iterable[_6445.HypoidGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.HypoidGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2098.HypoidGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6445.HypoidGearSetCompoundAdvancedSystemDeflection))

    def results_for_klingelnberg_cyclo_palloid_conical_gear(self, design_entity: '_2099.KlingelnbergCycloPalloidConicalGear') -> 'Iterable[_6448.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2099.KlingelnbergCycloPalloidConicalGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6448.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection))

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(self, design_entity: '_2100.KlingelnbergCycloPalloidConicalGearSet') -> 'Iterable[_6450.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2100.KlingelnbergCycloPalloidConicalGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6450.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(self, design_entity: '_2101.KlingelnbergCycloPalloidHypoidGear') -> 'Iterable[_6451.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2101.KlingelnbergCycloPalloidHypoidGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6451.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(self, design_entity: '_2102.KlingelnbergCycloPalloidHypoidGearSet') -> 'Iterable[_6453.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2102.KlingelnbergCycloPalloidHypoidGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6453.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(self, design_entity: '_2103.KlingelnbergCycloPalloidSpiralBevelGear') -> 'Iterable[_6454.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2103.KlingelnbergCycloPalloidSpiralBevelGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6454.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, design_entity: '_2104.KlingelnbergCycloPalloidSpiralBevelGearSet') -> 'Iterable[_6456.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2104.KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6456.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection))

    def results_for_planetary_gear_set(self, design_entity: '_2105.PlanetaryGearSet') -> 'Iterable[_6466.PlanetaryGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.PlanetaryGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2105.PlanetaryGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6466.PlanetaryGearSetCompoundAdvancedSystemDeflection))

    def results_for_spiral_bevel_gear(self, design_entity: '_2106.SpiralBevelGear') -> 'Iterable[_6479.SpiralBevelGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.SpiralBevelGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2106.SpiralBevelGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6479.SpiralBevelGearCompoundAdvancedSystemDeflection))

    def results_for_spiral_bevel_gear_set(self, design_entity: '_2107.SpiralBevelGearSet') -> 'Iterable[_6481.SpiralBevelGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.SpiralBevelGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2107.SpiralBevelGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6481.SpiralBevelGearSetCompoundAdvancedSystemDeflection))

    def results_for_straight_bevel_diff_gear(self, design_entity: '_2108.StraightBevelDiffGear') -> 'Iterable[_6485.StraightBevelDiffGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.StraightBevelDiffGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2108.StraightBevelDiffGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6485.StraightBevelDiffGearCompoundAdvancedSystemDeflection))

    def results_for_straight_bevel_diff_gear_set(self, design_entity: '_2109.StraightBevelDiffGearSet') -> 'Iterable[_6487.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2109.StraightBevelDiffGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6487.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection))

    def results_for_straight_bevel_gear(self, design_entity: '_2110.StraightBevelGear') -> 'Iterable[_6488.StraightBevelGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.StraightBevelGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2110.StraightBevelGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6488.StraightBevelGearCompoundAdvancedSystemDeflection))

    def results_for_straight_bevel_gear_set(self, design_entity: '_2111.StraightBevelGearSet') -> 'Iterable[_6490.StraightBevelGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.StraightBevelGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2111.StraightBevelGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6490.StraightBevelGearSetCompoundAdvancedSystemDeflection))

    def results_for_straight_bevel_planet_gear(self, design_entity: '_2112.StraightBevelPlanetGear') -> 'Iterable[_6491.StraightBevelPlanetGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.StraightBevelPlanetGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2112.StraightBevelPlanetGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6491.StraightBevelPlanetGearCompoundAdvancedSystemDeflection))

    def results_for_straight_bevel_sun_gear(self, design_entity: '_2113.StraightBevelSunGear') -> 'Iterable[_6492.StraightBevelSunGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.StraightBevelSunGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2113.StraightBevelSunGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6492.StraightBevelSunGearCompoundAdvancedSystemDeflection))

    def results_for_worm_gear(self, design_entity: '_2114.WormGear') -> 'Iterable[_6503.WormGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.WormGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2114.WormGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6503.WormGearCompoundAdvancedSystemDeflection))

    def results_for_worm_gear_set(self, design_entity: '_2115.WormGearSet') -> 'Iterable[_6505.WormGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.WormGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2115.WormGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6505.WormGearSetCompoundAdvancedSystemDeflection))

    def results_for_zerol_bevel_gear(self, design_entity: '_2116.ZerolBevelGear') -> 'Iterable[_6506.ZerolBevelGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ZerolBevelGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2116.ZerolBevelGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6506.ZerolBevelGearCompoundAdvancedSystemDeflection))

    def results_for_zerol_bevel_gear_set(self, design_entity: '_2117.ZerolBevelGearSet') -> 'Iterable[_6508.ZerolBevelGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ZerolBevelGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2117.ZerolBevelGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6508.ZerolBevelGearSetCompoundAdvancedSystemDeflection))

    def results_for_part_to_part_shear_coupling(self, design_entity: '_2146.PartToPartShearCoupling') -> 'Iterable[_6462.PartToPartShearCouplingCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCoupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.PartToPartShearCouplingCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2146.PartToPartShearCoupling.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6462.PartToPartShearCouplingCompoundAdvancedSystemDeflection))

    def results_for_part_to_part_shear_coupling_half(self, design_entity: '_2147.PartToPartShearCouplingHalf') -> 'Iterable[_6464.PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2147.PartToPartShearCouplingHalf.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6464.PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection))

    def results_for_belt_drive(self, design_entity: '_2135.BeltDrive') -> 'Iterable[_6396.BeltDriveCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.BeltDriveCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2135.BeltDrive.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6396.BeltDriveCompoundAdvancedSystemDeflection))

    def results_for_clutch(self, design_entity: '_2137.Clutch') -> 'Iterable[_6407.ClutchCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ClutchCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2137.Clutch.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6407.ClutchCompoundAdvancedSystemDeflection))

    def results_for_clutch_half(self, design_entity: '_2138.ClutchHalf') -> 'Iterable[_6409.ClutchHalfCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ClutchHalfCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2138.ClutchHalf.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6409.ClutchHalfCompoundAdvancedSystemDeflection))

    def results_for_concept_coupling(self, design_entity: '_2140.ConceptCoupling') -> 'Iterable[_6412.ConceptCouplingCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ConceptCouplingCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2140.ConceptCoupling.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6412.ConceptCouplingCompoundAdvancedSystemDeflection))

    def results_for_concept_coupling_half(self, design_entity: '_2141.ConceptCouplingHalf') -> 'Iterable[_6414.ConceptCouplingHalfCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ConceptCouplingHalfCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2141.ConceptCouplingHalf.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6414.ConceptCouplingHalfCompoundAdvancedSystemDeflection))

    def results_for_coupling(self, design_entity: '_2142.Coupling') -> 'Iterable[_6423.CouplingCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.CouplingCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2142.Coupling.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6423.CouplingCompoundAdvancedSystemDeflection))

    def results_for_coupling_half(self, design_entity: '_2143.CouplingHalf') -> 'Iterable[_6425.CouplingHalfCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.CouplingHalfCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2143.CouplingHalf.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6425.CouplingHalfCompoundAdvancedSystemDeflection))

    def results_for_cvt(self, design_entity: '_2144.CVT') -> 'Iterable[_6427.CVTCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.CVTCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2144.CVT.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6427.CVTCompoundAdvancedSystemDeflection))

    def results_for_cvt_pulley(self, design_entity: '_2145.CVTPulley') -> 'Iterable[_6428.CVTPulleyCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.CVTPulleyCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2145.CVTPulley.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6428.CVTPulleyCompoundAdvancedSystemDeflection))

    def results_for_pulley(self, design_entity: '_2148.Pulley') -> 'Iterable[_6470.PulleyCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.PulleyCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2148.Pulley.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6470.PulleyCompoundAdvancedSystemDeflection))

    def results_for_shaft_hub_connection(self, design_entity: '_2156.ShaftHubConnection') -> 'Iterable[_6476.ShaftHubConnectionCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ShaftHubConnectionCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2156.ShaftHubConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6476.ShaftHubConnectionCompoundAdvancedSystemDeflection))

    def results_for_rolling_ring(self, design_entity: '_2154.RollingRing') -> 'Iterable[_6472.RollingRingCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.RollingRingCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2154.RollingRing.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6472.RollingRingCompoundAdvancedSystemDeflection))

    def results_for_rolling_ring_assembly(self, design_entity: '_2155.RollingRingAssembly') -> 'Iterable[_6471.RollingRingAssemblyCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.RollingRingAssemblyCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2155.RollingRingAssembly.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6471.RollingRingAssemblyCompoundAdvancedSystemDeflection))

    def results_for_spring_damper(self, design_entity: '_2157.SpringDamper') -> 'Iterable[_6482.SpringDamperCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.SpringDamperCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2157.SpringDamper.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6482.SpringDamperCompoundAdvancedSystemDeflection))

    def results_for_spring_damper_half(self, design_entity: '_2158.SpringDamperHalf') -> 'Iterable[_6484.SpringDamperHalfCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.SpringDamperHalfCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2158.SpringDamperHalf.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6484.SpringDamperHalfCompoundAdvancedSystemDeflection))

    def results_for_synchroniser(self, design_entity: '_2159.Synchroniser') -> 'Iterable[_6493.SynchroniserCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.SynchroniserCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2159.Synchroniser.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6493.SynchroniserCompoundAdvancedSystemDeflection))

    def results_for_synchroniser_half(self, design_entity: '_2161.SynchroniserHalf') -> 'Iterable[_6494.SynchroniserHalfCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.SynchroniserHalfCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2161.SynchroniserHalf.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6494.SynchroniserHalfCompoundAdvancedSystemDeflection))

    def results_for_synchroniser_part(self, design_entity: '_2162.SynchroniserPart') -> 'Iterable[_6495.SynchroniserPartCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.SynchroniserPartCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2162.SynchroniserPart.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6495.SynchroniserPartCompoundAdvancedSystemDeflection))

    def results_for_synchroniser_sleeve(self, design_entity: '_2163.SynchroniserSleeve') -> 'Iterable[_6496.SynchroniserSleeveCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.SynchroniserSleeveCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2163.SynchroniserSleeve.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6496.SynchroniserSleeveCompoundAdvancedSystemDeflection))

    def results_for_torque_converter(self, design_entity: '_2164.TorqueConverter') -> 'Iterable[_6497.TorqueConverterCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.TorqueConverterCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2164.TorqueConverter.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6497.TorqueConverterCompoundAdvancedSystemDeflection))

    def results_for_torque_converter_pump(self, design_entity: '_2165.TorqueConverterPump') -> 'Iterable[_6499.TorqueConverterPumpCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.TorqueConverterPumpCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2165.TorqueConverterPump.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6499.TorqueConverterPumpCompoundAdvancedSystemDeflection))

    def results_for_torque_converter_turbine(self, design_entity: '_2167.TorqueConverterTurbine') -> 'Iterable[_6500.TorqueConverterTurbineCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.TorqueConverterTurbineCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2167.TorqueConverterTurbine.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6500.TorqueConverterTurbineCompoundAdvancedSystemDeflection))

    def results_for_cvt_belt_connection(self, design_entity: '_1858.CVTBeltConnection') -> 'Iterable[_6426.CVTBeltConnectionCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.CVTBeltConnectionCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1858.CVTBeltConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6426.CVTBeltConnectionCompoundAdvancedSystemDeflection))

    def results_for_belt_connection(self, design_entity: '_1853.BeltConnection') -> 'Iterable[_6395.BeltConnectionCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.BeltConnectionCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1853.BeltConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6395.BeltConnectionCompoundAdvancedSystemDeflection))

    def results_for_coaxial_connection(self, design_entity: '_1854.CoaxialConnection') -> 'Iterable[_6410.CoaxialConnectionCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.CoaxialConnectionCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1854.CoaxialConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6410.CoaxialConnectionCompoundAdvancedSystemDeflection))

    def results_for_connection(self, design_entity: '_1857.Connection') -> 'Iterable[_6421.ConnectionCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ConnectionCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1857.Connection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6421.ConnectionCompoundAdvancedSystemDeflection))

    def results_for_inter_mountable_component_connection(self, design_entity: '_1866.InterMountableComponentConnection') -> 'Iterable[_6447.InterMountableComponentConnectionCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.InterMountableComponentConnectionCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1866.InterMountableComponentConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6447.InterMountableComponentConnectionCompoundAdvancedSystemDeflection))

    def results_for_planetary_connection(self, design_entity: '_1869.PlanetaryConnection') -> 'Iterable[_6465.PlanetaryConnectionCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.PlanetaryConnectionCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1869.PlanetaryConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6465.PlanetaryConnectionCompoundAdvancedSystemDeflection))

    def results_for_rolling_ring_connection(self, design_entity: '_1873.RollingRingConnection') -> 'Iterable[_6473.RollingRingConnectionCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.RollingRingConnectionCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1873.RollingRingConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6473.RollingRingConnectionCompoundAdvancedSystemDeflection))

    def results_for_shaft_to_mountable_component_connection(self, design_entity: '_1877.ShaftToMountableComponentConnection') -> 'Iterable[_6477.ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1877.ShaftToMountableComponentConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6477.ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection))

    def results_for_bevel_differential_gear_mesh(self, design_entity: '_1883.BevelDifferentialGearMesh') -> 'Iterable[_6398.BevelDifferentialGearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.BevelDifferentialGearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1883.BevelDifferentialGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6398.BevelDifferentialGearMeshCompoundAdvancedSystemDeflection))

    def results_for_concept_gear_mesh(self, design_entity: '_1887.ConceptGearMesh') -> 'Iterable[_6416.ConceptGearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ConceptGearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1887.ConceptGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6416.ConceptGearMeshCompoundAdvancedSystemDeflection))

    def results_for_face_gear_mesh(self, design_entity: '_1893.FaceGearMesh') -> 'Iterable[_6436.FaceGearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.FaceGearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1893.FaceGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6436.FaceGearMeshCompoundAdvancedSystemDeflection))

    def results_for_straight_bevel_diff_gear_mesh(self, design_entity: '_1907.StraightBevelDiffGearMesh') -> 'Iterable[_6486.StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1907.StraightBevelDiffGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6486.StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection))

    def results_for_bevel_gear_mesh(self, design_entity: '_1885.BevelGearMesh') -> 'Iterable[_6403.BevelGearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.BevelGearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1885.BevelGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6403.BevelGearMeshCompoundAdvancedSystemDeflection))

    def results_for_conical_gear_mesh(self, design_entity: '_1889.ConicalGearMesh') -> 'Iterable[_6419.ConicalGearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ConicalGearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1889.ConicalGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6419.ConicalGearMeshCompoundAdvancedSystemDeflection))

    def results_for_agma_gleason_conical_gear_mesh(self, design_entity: '_1881.AGMAGleasonConicalGearMesh') -> 'Iterable[_6391.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1881.AGMAGleasonConicalGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6391.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection))

    def results_for_cylindrical_gear_mesh(self, design_entity: '_1891.CylindricalGearMesh') -> 'Iterable[_6430.CylindricalGearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.CylindricalGearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1891.CylindricalGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6430.CylindricalGearMeshCompoundAdvancedSystemDeflection))

    def results_for_hypoid_gear_mesh(self, design_entity: '_1897.HypoidGearMesh') -> 'Iterable[_6444.HypoidGearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.HypoidGearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1897.HypoidGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6444.HypoidGearMeshCompoundAdvancedSystemDeflection))

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(self, design_entity: '_1900.KlingelnbergCycloPalloidConicalGearMesh') -> 'Iterable[_6449.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1900.KlingelnbergCycloPalloidConicalGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6449.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self, design_entity: '_1901.KlingelnbergCycloPalloidHypoidGearMesh') -> 'Iterable[_6452.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1901.KlingelnbergCycloPalloidHypoidGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6452.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self, design_entity: '_1902.KlingelnbergCycloPalloidSpiralBevelGearMesh') -> 'Iterable[_6455.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1902.KlingelnbergCycloPalloidSpiralBevelGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6455.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection))

    def results_for_spiral_bevel_gear_mesh(self, design_entity: '_1905.SpiralBevelGearMesh') -> 'Iterable[_6480.SpiralBevelGearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.SpiralBevelGearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1905.SpiralBevelGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6480.SpiralBevelGearMeshCompoundAdvancedSystemDeflection))

    def results_for_straight_bevel_gear_mesh(self, design_entity: '_1909.StraightBevelGearMesh') -> 'Iterable[_6489.StraightBevelGearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.StraightBevelGearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1909.StraightBevelGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6489.StraightBevelGearMeshCompoundAdvancedSystemDeflection))

    def results_for_worm_gear_mesh(self, design_entity: '_1911.WormGearMesh') -> 'Iterable[_6504.WormGearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.WormGearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1911.WormGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6504.WormGearMeshCompoundAdvancedSystemDeflection))

    def results_for_zerol_bevel_gear_mesh(self, design_entity: '_1913.ZerolBevelGearMesh') -> 'Iterable[_6507.ZerolBevelGearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ZerolBevelGearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1913.ZerolBevelGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6507.ZerolBevelGearMeshCompoundAdvancedSystemDeflection))

    def results_for_gear_mesh(self, design_entity: '_1895.GearMesh') -> 'Iterable[_6440.GearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.GearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1895.GearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6440.GearMeshCompoundAdvancedSystemDeflection))

    def results_for_part_to_part_shear_coupling_connection(self, design_entity: '_1921.PartToPartShearCouplingConnection') -> 'Iterable[_6463.PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1921.PartToPartShearCouplingConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6463.PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection))

    def results_for_clutch_connection(self, design_entity: '_1915.ClutchConnection') -> 'Iterable[_6408.ClutchConnectionCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ClutchConnectionCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1915.ClutchConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6408.ClutchConnectionCompoundAdvancedSystemDeflection))

    def results_for_concept_coupling_connection(self, design_entity: '_1917.ConceptCouplingConnection') -> 'Iterable[_6413.ConceptCouplingConnectionCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ConceptCouplingConnectionCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1917.ConceptCouplingConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6413.ConceptCouplingConnectionCompoundAdvancedSystemDeflection))

    def results_for_coupling_connection(self, design_entity: '_1919.CouplingConnection') -> 'Iterable[_6424.CouplingConnectionCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.CouplingConnectionCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1919.CouplingConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6424.CouplingConnectionCompoundAdvancedSystemDeflection))

    def results_for_spring_damper_connection(self, design_entity: '_1923.SpringDamperConnection') -> 'Iterable[_6483.SpringDamperConnectionCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.SpringDamperConnectionCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1923.SpringDamperConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6483.SpringDamperConnectionCompoundAdvancedSystemDeflection))

    def results_for_torque_converter_connection(self, design_entity: '_1925.TorqueConverterConnection') -> 'Iterable[_6498.TorqueConverterConnectionCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.TorqueConverterConnectionCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1925.TorqueConverterConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6498.TorqueConverterConnectionCompoundAdvancedSystemDeflection))
