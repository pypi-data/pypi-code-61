'''_2225.py

CompoundSingleMeshWhineAnalysisAnalysis
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
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound import (
    _5558, _5559, _5564, _5575,
    _5576, _5581, _5592, _5603,
    _5604, _5608, _5563, _5612,
    _5616, _5627, _5628, _5629,
    _5630, _5631, _5637, _5638,
    _5639, _5644, _5648, _5671,
    _5672, _5645, _5585, _5587,
    _5605, _5607, _5560, _5562,
    _5567, _5569, _5570, _5571,
    _5572, _5574, _5588, _5590,
    _5599, _5601, _5602, _5609,
    _5611, _5613, _5615, _5618,
    _5620, _5621, _5623, _5624,
    _5626, _5636, _5649, _5651,
    _5655, _5657, _5658, _5660,
    _5661, _5662, _5673, _5675,
    _5676, _5678, _5632, _5634,
    _5566, _5577, _5579, _5582,
    _5584, _5593, _5595, _5597,
    _5598, _5640, _5646, _5642,
    _5641, _5652, _5654, _5663,
    _5664, _5665, _5666, _5667,
    _5669, _5670, _5596, _5565,
    _5580, _5591, _5617, _5635,
    _5643, _5647, _5568, _5586,
    _5606, _5656, _5573, _5589,
    _5561, _5600, _5614, _5619,
    _5622, _5625, _5650, _5659,
    _5674, _5677, _5610, _5633,
    _5578, _5583, _5594, _5653,
    _5668
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

_COMPOUND_SINGLE_MESH_WHINE_ANALYSIS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'CompoundSingleMeshWhineAnalysisAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CompoundSingleMeshWhineAnalysisAnalysis',)


class CompoundSingleMeshWhineAnalysisAnalysis(_2176.CompoundAnalysis):
    '''CompoundSingleMeshWhineAnalysisAnalysis

    This is a mastapy class.
    '''

    TYPE = _COMPOUND_SINGLE_MESH_WHINE_ANALYSIS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CompoundSingleMeshWhineAnalysisAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def results_for_abstract_assembly(self, design_entity: '_2003.AbstractAssembly') -> 'Iterable[_5558.AbstractAssemblyCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.AbstractAssemblyCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2003.AbstractAssembly.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5558.AbstractAssemblyCompoundSingleMeshWhineAnalysis))

    def results_for_abstract_shaft_or_housing(self, design_entity: '_2004.AbstractShaftOrHousing') -> 'Iterable[_5559.AbstractShaftOrHousingCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.AbstractShaftOrHousingCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2004.AbstractShaftOrHousing.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5559.AbstractShaftOrHousingCompoundSingleMeshWhineAnalysis))

    def results_for_bearing(self, design_entity: '_2007.Bearing') -> 'Iterable[_5564.BearingCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.BearingCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2007.Bearing.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5564.BearingCompoundSingleMeshWhineAnalysis))

    def results_for_bolt(self, design_entity: '_2009.Bolt') -> 'Iterable[_5575.BoltCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.BoltCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2009.Bolt.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5575.BoltCompoundSingleMeshWhineAnalysis))

    def results_for_bolted_joint(self, design_entity: '_2010.BoltedJoint') -> 'Iterable[_5576.BoltedJointCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.BoltedJointCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2010.BoltedJoint.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5576.BoltedJointCompoundSingleMeshWhineAnalysis))

    def results_for_component(self, design_entity: '_2011.Component') -> 'Iterable[_5581.ComponentCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Component)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.ComponentCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2011.Component.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5581.ComponentCompoundSingleMeshWhineAnalysis))

    def results_for_connector(self, design_entity: '_2014.Connector') -> 'Iterable[_5592.ConnectorCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Connector)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.ConnectorCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2014.Connector.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5592.ConnectorCompoundSingleMeshWhineAnalysis))

    def results_for_datum(self, design_entity: '_2015.Datum') -> 'Iterable[_5603.DatumCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Datum)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.DatumCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2015.Datum.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5603.DatumCompoundSingleMeshWhineAnalysis))

    def results_for_external_cad_model(self, design_entity: '_2018.ExternalCADModel') -> 'Iterable[_5604.ExternalCADModelCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.ExternalCADModelCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2018.ExternalCADModel.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5604.ExternalCADModelCompoundSingleMeshWhineAnalysis))

    def results_for_flexible_pin_assembly(self, design_entity: '_2019.FlexiblePinAssembly') -> 'Iterable[_5608.FlexiblePinAssemblyCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.FlexiblePinAssemblyCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2019.FlexiblePinAssembly.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5608.FlexiblePinAssemblyCompoundSingleMeshWhineAnalysis))

    def results_for_assembly(self, design_entity: '_2002.Assembly') -> 'Iterable[_5563.AssemblyCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.AssemblyCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2002.Assembly.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5563.AssemblyCompoundSingleMeshWhineAnalysis))

    def results_for_guide_dxf_model(self, design_entity: '_2020.GuideDxfModel') -> 'Iterable[_5612.GuideDxfModelCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.GuideDxfModelCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2020.GuideDxfModel.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5612.GuideDxfModelCompoundSingleMeshWhineAnalysis))

    def results_for_imported_fe_component(self, design_entity: '_2023.ImportedFEComponent') -> 'Iterable[_5616.ImportedFEComponentCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ImportedFEComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.ImportedFEComponentCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2023.ImportedFEComponent.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5616.ImportedFEComponentCompoundSingleMeshWhineAnalysis))

    def results_for_mass_disc(self, design_entity: '_2027.MassDisc') -> 'Iterable[_5627.MassDiscCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.MassDiscCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2027.MassDisc.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5627.MassDiscCompoundSingleMeshWhineAnalysis))

    def results_for_measurement_component(self, design_entity: '_2028.MeasurementComponent') -> 'Iterable[_5628.MeasurementComponentCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.MeasurementComponentCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2028.MeasurementComponent.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5628.MeasurementComponentCompoundSingleMeshWhineAnalysis))

    def results_for_mountable_component(self, design_entity: '_2029.MountableComponent') -> 'Iterable[_5629.MountableComponentCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.MountableComponentCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2029.MountableComponent.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5629.MountableComponentCompoundSingleMeshWhineAnalysis))

    def results_for_oil_seal(self, design_entity: '_2031.OilSeal') -> 'Iterable[_5630.OilSealCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.OilSealCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2031.OilSeal.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5630.OilSealCompoundSingleMeshWhineAnalysis))

    def results_for_part(self, design_entity: '_2033.Part') -> 'Iterable[_5631.PartCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Part)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.PartCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2033.Part.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5631.PartCompoundSingleMeshWhineAnalysis))

    def results_for_planet_carrier(self, design_entity: '_2034.PlanetCarrier') -> 'Iterable[_5637.PlanetCarrierCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.PlanetCarrierCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2034.PlanetCarrier.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5637.PlanetCarrierCompoundSingleMeshWhineAnalysis))

    def results_for_point_load(self, design_entity: '_2036.PointLoad') -> 'Iterable[_5638.PointLoadCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.PointLoadCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2036.PointLoad.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5638.PointLoadCompoundSingleMeshWhineAnalysis))

    def results_for_power_load(self, design_entity: '_2037.PowerLoad') -> 'Iterable[_5639.PowerLoadCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.PowerLoadCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2037.PowerLoad.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5639.PowerLoadCompoundSingleMeshWhineAnalysis))

    def results_for_root_assembly(self, design_entity: '_2039.RootAssembly') -> 'Iterable[_5644.RootAssemblyCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.RootAssemblyCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2039.RootAssembly.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5644.RootAssemblyCompoundSingleMeshWhineAnalysis))

    def results_for_specialised_assembly(self, design_entity: '_2041.SpecialisedAssembly') -> 'Iterable[_5648.SpecialisedAssemblyCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.SpecialisedAssemblyCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2041.SpecialisedAssembly.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5648.SpecialisedAssemblyCompoundSingleMeshWhineAnalysis))

    def results_for_unbalanced_mass(self, design_entity: '_2042.UnbalancedMass') -> 'Iterable[_5671.UnbalancedMassCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.UnbalancedMassCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2042.UnbalancedMass.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5671.UnbalancedMassCompoundSingleMeshWhineAnalysis))

    def results_for_virtual_component(self, design_entity: '_2043.VirtualComponent') -> 'Iterable[_5672.VirtualComponentCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.VirtualComponentCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2043.VirtualComponent.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5672.VirtualComponentCompoundSingleMeshWhineAnalysis))

    def results_for_shaft(self, design_entity: '_2046.Shaft') -> 'Iterable[_5645.ShaftCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.ShaftCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2046.Shaft.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5645.ShaftCompoundSingleMeshWhineAnalysis))

    def results_for_concept_gear(self, design_entity: '_2084.ConceptGear') -> 'Iterable[_5585.ConceptGearCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.ConceptGearCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2084.ConceptGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5585.ConceptGearCompoundSingleMeshWhineAnalysis))

    def results_for_concept_gear_set(self, design_entity: '_2085.ConceptGearSet') -> 'Iterable[_5587.ConceptGearSetCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.ConceptGearSetCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2085.ConceptGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5587.ConceptGearSetCompoundSingleMeshWhineAnalysis))

    def results_for_face_gear(self, design_entity: '_2091.FaceGear') -> 'Iterable[_5605.FaceGearCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.FaceGearCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2091.FaceGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5605.FaceGearCompoundSingleMeshWhineAnalysis))

    def results_for_face_gear_set(self, design_entity: '_2092.FaceGearSet') -> 'Iterable[_5607.FaceGearSetCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.FaceGearSetCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2092.FaceGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5607.FaceGearSetCompoundSingleMeshWhineAnalysis))

    def results_for_agma_gleason_conical_gear(self, design_entity: '_2076.AGMAGleasonConicalGear') -> 'Iterable[_5560.AGMAGleasonConicalGearCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.AGMAGleasonConicalGearCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2076.AGMAGleasonConicalGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5560.AGMAGleasonConicalGearCompoundSingleMeshWhineAnalysis))

    def results_for_agma_gleason_conical_gear_set(self, design_entity: '_2077.AGMAGleasonConicalGearSet') -> 'Iterable[_5562.AGMAGleasonConicalGearSetCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.AGMAGleasonConicalGearSetCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2077.AGMAGleasonConicalGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5562.AGMAGleasonConicalGearSetCompoundSingleMeshWhineAnalysis))

    def results_for_bevel_differential_gear(self, design_entity: '_2078.BevelDifferentialGear') -> 'Iterable[_5567.BevelDifferentialGearCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.BevelDifferentialGearCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2078.BevelDifferentialGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5567.BevelDifferentialGearCompoundSingleMeshWhineAnalysis))

    def results_for_bevel_differential_gear_set(self, design_entity: '_2079.BevelDifferentialGearSet') -> 'Iterable[_5569.BevelDifferentialGearSetCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.BevelDifferentialGearSetCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2079.BevelDifferentialGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5569.BevelDifferentialGearSetCompoundSingleMeshWhineAnalysis))

    def results_for_bevel_differential_planet_gear(self, design_entity: '_2080.BevelDifferentialPlanetGear') -> 'Iterable[_5570.BevelDifferentialPlanetGearCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.BevelDifferentialPlanetGearCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2080.BevelDifferentialPlanetGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5570.BevelDifferentialPlanetGearCompoundSingleMeshWhineAnalysis))

    def results_for_bevel_differential_sun_gear(self, design_entity: '_2081.BevelDifferentialSunGear') -> 'Iterable[_5571.BevelDifferentialSunGearCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.BevelDifferentialSunGearCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2081.BevelDifferentialSunGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5571.BevelDifferentialSunGearCompoundSingleMeshWhineAnalysis))

    def results_for_bevel_gear(self, design_entity: '_2082.BevelGear') -> 'Iterable[_5572.BevelGearCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.BevelGearCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2082.BevelGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5572.BevelGearCompoundSingleMeshWhineAnalysis))

    def results_for_bevel_gear_set(self, design_entity: '_2083.BevelGearSet') -> 'Iterable[_5574.BevelGearSetCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.BevelGearSetCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2083.BevelGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5574.BevelGearSetCompoundSingleMeshWhineAnalysis))

    def results_for_conical_gear(self, design_entity: '_2086.ConicalGear') -> 'Iterable[_5588.ConicalGearCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.ConicalGearCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2086.ConicalGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5588.ConicalGearCompoundSingleMeshWhineAnalysis))

    def results_for_conical_gear_set(self, design_entity: '_2087.ConicalGearSet') -> 'Iterable[_5590.ConicalGearSetCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.ConicalGearSetCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2087.ConicalGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5590.ConicalGearSetCompoundSingleMeshWhineAnalysis))

    def results_for_cylindrical_gear(self, design_entity: '_2088.CylindricalGear') -> 'Iterable[_5599.CylindricalGearCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.CylindricalGearCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2088.CylindricalGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5599.CylindricalGearCompoundSingleMeshWhineAnalysis))

    def results_for_cylindrical_gear_set(self, design_entity: '_2089.CylindricalGearSet') -> 'Iterable[_5601.CylindricalGearSetCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.CylindricalGearSetCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2089.CylindricalGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5601.CylindricalGearSetCompoundSingleMeshWhineAnalysis))

    def results_for_cylindrical_planet_gear(self, design_entity: '_2090.CylindricalPlanetGear') -> 'Iterable[_5602.CylindricalPlanetGearCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.CylindricalPlanetGearCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2090.CylindricalPlanetGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5602.CylindricalPlanetGearCompoundSingleMeshWhineAnalysis))

    def results_for_gear(self, design_entity: '_2093.Gear') -> 'Iterable[_5609.GearCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.GearCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2093.Gear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5609.GearCompoundSingleMeshWhineAnalysis))

    def results_for_gear_set(self, design_entity: '_2095.GearSet') -> 'Iterable[_5611.GearSetCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.GearSetCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2095.GearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5611.GearSetCompoundSingleMeshWhineAnalysis))

    def results_for_hypoid_gear(self, design_entity: '_2097.HypoidGear') -> 'Iterable[_5613.HypoidGearCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.HypoidGearCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2097.HypoidGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5613.HypoidGearCompoundSingleMeshWhineAnalysis))

    def results_for_hypoid_gear_set(self, design_entity: '_2098.HypoidGearSet') -> 'Iterable[_5615.HypoidGearSetCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.HypoidGearSetCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2098.HypoidGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5615.HypoidGearSetCompoundSingleMeshWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_conical_gear(self, design_entity: '_2099.KlingelnbergCycloPalloidConicalGear') -> 'Iterable[_5618.KlingelnbergCycloPalloidConicalGearCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.KlingelnbergCycloPalloidConicalGearCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2099.KlingelnbergCycloPalloidConicalGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5618.KlingelnbergCycloPalloidConicalGearCompoundSingleMeshWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(self, design_entity: '_2100.KlingelnbergCycloPalloidConicalGearSet') -> 'Iterable[_5620.KlingelnbergCycloPalloidConicalGearSetCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.KlingelnbergCycloPalloidConicalGearSetCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2100.KlingelnbergCycloPalloidConicalGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5620.KlingelnbergCycloPalloidConicalGearSetCompoundSingleMeshWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(self, design_entity: '_2101.KlingelnbergCycloPalloidHypoidGear') -> 'Iterable[_5621.KlingelnbergCycloPalloidHypoidGearCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.KlingelnbergCycloPalloidHypoidGearCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2101.KlingelnbergCycloPalloidHypoidGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5621.KlingelnbergCycloPalloidHypoidGearCompoundSingleMeshWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(self, design_entity: '_2102.KlingelnbergCycloPalloidHypoidGearSet') -> 'Iterable[_5623.KlingelnbergCycloPalloidHypoidGearSetCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.KlingelnbergCycloPalloidHypoidGearSetCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2102.KlingelnbergCycloPalloidHypoidGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5623.KlingelnbergCycloPalloidHypoidGearSetCompoundSingleMeshWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(self, design_entity: '_2103.KlingelnbergCycloPalloidSpiralBevelGear') -> 'Iterable[_5624.KlingelnbergCycloPalloidSpiralBevelGearCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2103.KlingelnbergCycloPalloidSpiralBevelGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5624.KlingelnbergCycloPalloidSpiralBevelGearCompoundSingleMeshWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, design_entity: '_2104.KlingelnbergCycloPalloidSpiralBevelGearSet') -> 'Iterable[_5626.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2104.KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5626.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSingleMeshWhineAnalysis))

    def results_for_planetary_gear_set(self, design_entity: '_2105.PlanetaryGearSet') -> 'Iterable[_5636.PlanetaryGearSetCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.PlanetaryGearSetCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2105.PlanetaryGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5636.PlanetaryGearSetCompoundSingleMeshWhineAnalysis))

    def results_for_spiral_bevel_gear(self, design_entity: '_2106.SpiralBevelGear') -> 'Iterable[_5649.SpiralBevelGearCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.SpiralBevelGearCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2106.SpiralBevelGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5649.SpiralBevelGearCompoundSingleMeshWhineAnalysis))

    def results_for_spiral_bevel_gear_set(self, design_entity: '_2107.SpiralBevelGearSet') -> 'Iterable[_5651.SpiralBevelGearSetCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.SpiralBevelGearSetCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2107.SpiralBevelGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5651.SpiralBevelGearSetCompoundSingleMeshWhineAnalysis))

    def results_for_straight_bevel_diff_gear(self, design_entity: '_2108.StraightBevelDiffGear') -> 'Iterable[_5655.StraightBevelDiffGearCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.StraightBevelDiffGearCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2108.StraightBevelDiffGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5655.StraightBevelDiffGearCompoundSingleMeshWhineAnalysis))

    def results_for_straight_bevel_diff_gear_set(self, design_entity: '_2109.StraightBevelDiffGearSet') -> 'Iterable[_5657.StraightBevelDiffGearSetCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.StraightBevelDiffGearSetCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2109.StraightBevelDiffGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5657.StraightBevelDiffGearSetCompoundSingleMeshWhineAnalysis))

    def results_for_straight_bevel_gear(self, design_entity: '_2110.StraightBevelGear') -> 'Iterable[_5658.StraightBevelGearCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.StraightBevelGearCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2110.StraightBevelGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5658.StraightBevelGearCompoundSingleMeshWhineAnalysis))

    def results_for_straight_bevel_gear_set(self, design_entity: '_2111.StraightBevelGearSet') -> 'Iterable[_5660.StraightBevelGearSetCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.StraightBevelGearSetCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2111.StraightBevelGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5660.StraightBevelGearSetCompoundSingleMeshWhineAnalysis))

    def results_for_straight_bevel_planet_gear(self, design_entity: '_2112.StraightBevelPlanetGear') -> 'Iterable[_5661.StraightBevelPlanetGearCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.StraightBevelPlanetGearCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2112.StraightBevelPlanetGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5661.StraightBevelPlanetGearCompoundSingleMeshWhineAnalysis))

    def results_for_straight_bevel_sun_gear(self, design_entity: '_2113.StraightBevelSunGear') -> 'Iterable[_5662.StraightBevelSunGearCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.StraightBevelSunGearCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2113.StraightBevelSunGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5662.StraightBevelSunGearCompoundSingleMeshWhineAnalysis))

    def results_for_worm_gear(self, design_entity: '_2114.WormGear') -> 'Iterable[_5673.WormGearCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.WormGearCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2114.WormGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5673.WormGearCompoundSingleMeshWhineAnalysis))

    def results_for_worm_gear_set(self, design_entity: '_2115.WormGearSet') -> 'Iterable[_5675.WormGearSetCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.WormGearSetCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2115.WormGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5675.WormGearSetCompoundSingleMeshWhineAnalysis))

    def results_for_zerol_bevel_gear(self, design_entity: '_2116.ZerolBevelGear') -> 'Iterable[_5676.ZerolBevelGearCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.ZerolBevelGearCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2116.ZerolBevelGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5676.ZerolBevelGearCompoundSingleMeshWhineAnalysis))

    def results_for_zerol_bevel_gear_set(self, design_entity: '_2117.ZerolBevelGearSet') -> 'Iterable[_5678.ZerolBevelGearSetCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.ZerolBevelGearSetCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2117.ZerolBevelGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5678.ZerolBevelGearSetCompoundSingleMeshWhineAnalysis))

    def results_for_part_to_part_shear_coupling(self, design_entity: '_2146.PartToPartShearCoupling') -> 'Iterable[_5632.PartToPartShearCouplingCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCoupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.PartToPartShearCouplingCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2146.PartToPartShearCoupling.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5632.PartToPartShearCouplingCompoundSingleMeshWhineAnalysis))

    def results_for_part_to_part_shear_coupling_half(self, design_entity: '_2147.PartToPartShearCouplingHalf') -> 'Iterable[_5634.PartToPartShearCouplingHalfCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.PartToPartShearCouplingHalfCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2147.PartToPartShearCouplingHalf.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5634.PartToPartShearCouplingHalfCompoundSingleMeshWhineAnalysis))

    def results_for_belt_drive(self, design_entity: '_2135.BeltDrive') -> 'Iterable[_5566.BeltDriveCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.BeltDriveCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2135.BeltDrive.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5566.BeltDriveCompoundSingleMeshWhineAnalysis))

    def results_for_clutch(self, design_entity: '_2137.Clutch') -> 'Iterable[_5577.ClutchCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.ClutchCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2137.Clutch.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5577.ClutchCompoundSingleMeshWhineAnalysis))

    def results_for_clutch_half(self, design_entity: '_2138.ClutchHalf') -> 'Iterable[_5579.ClutchHalfCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.ClutchHalfCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2138.ClutchHalf.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5579.ClutchHalfCompoundSingleMeshWhineAnalysis))

    def results_for_concept_coupling(self, design_entity: '_2140.ConceptCoupling') -> 'Iterable[_5582.ConceptCouplingCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.ConceptCouplingCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2140.ConceptCoupling.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5582.ConceptCouplingCompoundSingleMeshWhineAnalysis))

    def results_for_concept_coupling_half(self, design_entity: '_2141.ConceptCouplingHalf') -> 'Iterable[_5584.ConceptCouplingHalfCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.ConceptCouplingHalfCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2141.ConceptCouplingHalf.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5584.ConceptCouplingHalfCompoundSingleMeshWhineAnalysis))

    def results_for_coupling(self, design_entity: '_2142.Coupling') -> 'Iterable[_5593.CouplingCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.CouplingCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2142.Coupling.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5593.CouplingCompoundSingleMeshWhineAnalysis))

    def results_for_coupling_half(self, design_entity: '_2143.CouplingHalf') -> 'Iterable[_5595.CouplingHalfCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.CouplingHalfCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2143.CouplingHalf.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5595.CouplingHalfCompoundSingleMeshWhineAnalysis))

    def results_for_cvt(self, design_entity: '_2144.CVT') -> 'Iterable[_5597.CVTCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.CVTCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2144.CVT.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5597.CVTCompoundSingleMeshWhineAnalysis))

    def results_for_cvt_pulley(self, design_entity: '_2145.CVTPulley') -> 'Iterable[_5598.CVTPulleyCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.CVTPulleyCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2145.CVTPulley.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5598.CVTPulleyCompoundSingleMeshWhineAnalysis))

    def results_for_pulley(self, design_entity: '_2148.Pulley') -> 'Iterable[_5640.PulleyCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.PulleyCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2148.Pulley.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5640.PulleyCompoundSingleMeshWhineAnalysis))

    def results_for_shaft_hub_connection(self, design_entity: '_2156.ShaftHubConnection') -> 'Iterable[_5646.ShaftHubConnectionCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.ShaftHubConnectionCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2156.ShaftHubConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5646.ShaftHubConnectionCompoundSingleMeshWhineAnalysis))

    def results_for_rolling_ring(self, design_entity: '_2154.RollingRing') -> 'Iterable[_5642.RollingRingCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.RollingRingCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2154.RollingRing.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5642.RollingRingCompoundSingleMeshWhineAnalysis))

    def results_for_rolling_ring_assembly(self, design_entity: '_2155.RollingRingAssembly') -> 'Iterable[_5641.RollingRingAssemblyCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.RollingRingAssemblyCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2155.RollingRingAssembly.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5641.RollingRingAssemblyCompoundSingleMeshWhineAnalysis))

    def results_for_spring_damper(self, design_entity: '_2157.SpringDamper') -> 'Iterable[_5652.SpringDamperCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.SpringDamperCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2157.SpringDamper.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5652.SpringDamperCompoundSingleMeshWhineAnalysis))

    def results_for_spring_damper_half(self, design_entity: '_2158.SpringDamperHalf') -> 'Iterable[_5654.SpringDamperHalfCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.SpringDamperHalfCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2158.SpringDamperHalf.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5654.SpringDamperHalfCompoundSingleMeshWhineAnalysis))

    def results_for_synchroniser(self, design_entity: '_2159.Synchroniser') -> 'Iterable[_5663.SynchroniserCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.SynchroniserCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2159.Synchroniser.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5663.SynchroniserCompoundSingleMeshWhineAnalysis))

    def results_for_synchroniser_half(self, design_entity: '_2161.SynchroniserHalf') -> 'Iterable[_5664.SynchroniserHalfCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.SynchroniserHalfCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2161.SynchroniserHalf.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5664.SynchroniserHalfCompoundSingleMeshWhineAnalysis))

    def results_for_synchroniser_part(self, design_entity: '_2162.SynchroniserPart') -> 'Iterable[_5665.SynchroniserPartCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.SynchroniserPartCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2162.SynchroniserPart.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5665.SynchroniserPartCompoundSingleMeshWhineAnalysis))

    def results_for_synchroniser_sleeve(self, design_entity: '_2163.SynchroniserSleeve') -> 'Iterable[_5666.SynchroniserSleeveCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.SynchroniserSleeveCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2163.SynchroniserSleeve.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5666.SynchroniserSleeveCompoundSingleMeshWhineAnalysis))

    def results_for_torque_converter(self, design_entity: '_2164.TorqueConverter') -> 'Iterable[_5667.TorqueConverterCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.TorqueConverterCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2164.TorqueConverter.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5667.TorqueConverterCompoundSingleMeshWhineAnalysis))

    def results_for_torque_converter_pump(self, design_entity: '_2165.TorqueConverterPump') -> 'Iterable[_5669.TorqueConverterPumpCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.TorqueConverterPumpCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2165.TorqueConverterPump.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5669.TorqueConverterPumpCompoundSingleMeshWhineAnalysis))

    def results_for_torque_converter_turbine(self, design_entity: '_2167.TorqueConverterTurbine') -> 'Iterable[_5670.TorqueConverterTurbineCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.TorqueConverterTurbineCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2167.TorqueConverterTurbine.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5670.TorqueConverterTurbineCompoundSingleMeshWhineAnalysis))

    def results_for_cvt_belt_connection(self, design_entity: '_1858.CVTBeltConnection') -> 'Iterable[_5596.CVTBeltConnectionCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.CVTBeltConnectionCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1858.CVTBeltConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5596.CVTBeltConnectionCompoundSingleMeshWhineAnalysis))

    def results_for_belt_connection(self, design_entity: '_1853.BeltConnection') -> 'Iterable[_5565.BeltConnectionCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.BeltConnectionCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1853.BeltConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5565.BeltConnectionCompoundSingleMeshWhineAnalysis))

    def results_for_coaxial_connection(self, design_entity: '_1854.CoaxialConnection') -> 'Iterable[_5580.CoaxialConnectionCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.CoaxialConnectionCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1854.CoaxialConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5580.CoaxialConnectionCompoundSingleMeshWhineAnalysis))

    def results_for_connection(self, design_entity: '_1857.Connection') -> 'Iterable[_5591.ConnectionCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.ConnectionCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1857.Connection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5591.ConnectionCompoundSingleMeshWhineAnalysis))

    def results_for_inter_mountable_component_connection(self, design_entity: '_1866.InterMountableComponentConnection') -> 'Iterable[_5617.InterMountableComponentConnectionCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.InterMountableComponentConnectionCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1866.InterMountableComponentConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5617.InterMountableComponentConnectionCompoundSingleMeshWhineAnalysis))

    def results_for_planetary_connection(self, design_entity: '_1869.PlanetaryConnection') -> 'Iterable[_5635.PlanetaryConnectionCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.PlanetaryConnectionCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1869.PlanetaryConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5635.PlanetaryConnectionCompoundSingleMeshWhineAnalysis))

    def results_for_rolling_ring_connection(self, design_entity: '_1873.RollingRingConnection') -> 'Iterable[_5643.RollingRingConnectionCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.RollingRingConnectionCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1873.RollingRingConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5643.RollingRingConnectionCompoundSingleMeshWhineAnalysis))

    def results_for_shaft_to_mountable_component_connection(self, design_entity: '_1877.ShaftToMountableComponentConnection') -> 'Iterable[_5647.ShaftToMountableComponentConnectionCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.ShaftToMountableComponentConnectionCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1877.ShaftToMountableComponentConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5647.ShaftToMountableComponentConnectionCompoundSingleMeshWhineAnalysis))

    def results_for_bevel_differential_gear_mesh(self, design_entity: '_1883.BevelDifferentialGearMesh') -> 'Iterable[_5568.BevelDifferentialGearMeshCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.BevelDifferentialGearMeshCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1883.BevelDifferentialGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5568.BevelDifferentialGearMeshCompoundSingleMeshWhineAnalysis))

    def results_for_concept_gear_mesh(self, design_entity: '_1887.ConceptGearMesh') -> 'Iterable[_5586.ConceptGearMeshCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.ConceptGearMeshCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1887.ConceptGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5586.ConceptGearMeshCompoundSingleMeshWhineAnalysis))

    def results_for_face_gear_mesh(self, design_entity: '_1893.FaceGearMesh') -> 'Iterable[_5606.FaceGearMeshCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.FaceGearMeshCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1893.FaceGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5606.FaceGearMeshCompoundSingleMeshWhineAnalysis))

    def results_for_straight_bevel_diff_gear_mesh(self, design_entity: '_1907.StraightBevelDiffGearMesh') -> 'Iterable[_5656.StraightBevelDiffGearMeshCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.StraightBevelDiffGearMeshCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1907.StraightBevelDiffGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5656.StraightBevelDiffGearMeshCompoundSingleMeshWhineAnalysis))

    def results_for_bevel_gear_mesh(self, design_entity: '_1885.BevelGearMesh') -> 'Iterable[_5573.BevelGearMeshCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.BevelGearMeshCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1885.BevelGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5573.BevelGearMeshCompoundSingleMeshWhineAnalysis))

    def results_for_conical_gear_mesh(self, design_entity: '_1889.ConicalGearMesh') -> 'Iterable[_5589.ConicalGearMeshCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.ConicalGearMeshCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1889.ConicalGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5589.ConicalGearMeshCompoundSingleMeshWhineAnalysis))

    def results_for_agma_gleason_conical_gear_mesh(self, design_entity: '_1881.AGMAGleasonConicalGearMesh') -> 'Iterable[_5561.AGMAGleasonConicalGearMeshCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.AGMAGleasonConicalGearMeshCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1881.AGMAGleasonConicalGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5561.AGMAGleasonConicalGearMeshCompoundSingleMeshWhineAnalysis))

    def results_for_cylindrical_gear_mesh(self, design_entity: '_1891.CylindricalGearMesh') -> 'Iterable[_5600.CylindricalGearMeshCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.CylindricalGearMeshCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1891.CylindricalGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5600.CylindricalGearMeshCompoundSingleMeshWhineAnalysis))

    def results_for_hypoid_gear_mesh(self, design_entity: '_1897.HypoidGearMesh') -> 'Iterable[_5614.HypoidGearMeshCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.HypoidGearMeshCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1897.HypoidGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5614.HypoidGearMeshCompoundSingleMeshWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(self, design_entity: '_1900.KlingelnbergCycloPalloidConicalGearMesh') -> 'Iterable[_5619.KlingelnbergCycloPalloidConicalGearMeshCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.KlingelnbergCycloPalloidConicalGearMeshCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1900.KlingelnbergCycloPalloidConicalGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5619.KlingelnbergCycloPalloidConicalGearMeshCompoundSingleMeshWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self, design_entity: '_1901.KlingelnbergCycloPalloidHypoidGearMesh') -> 'Iterable[_5622.KlingelnbergCycloPalloidHypoidGearMeshCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.KlingelnbergCycloPalloidHypoidGearMeshCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1901.KlingelnbergCycloPalloidHypoidGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5622.KlingelnbergCycloPalloidHypoidGearMeshCompoundSingleMeshWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self, design_entity: '_1902.KlingelnbergCycloPalloidSpiralBevelGearMesh') -> 'Iterable[_5625.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1902.KlingelnbergCycloPalloidSpiralBevelGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5625.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSingleMeshWhineAnalysis))

    def results_for_spiral_bevel_gear_mesh(self, design_entity: '_1905.SpiralBevelGearMesh') -> 'Iterable[_5650.SpiralBevelGearMeshCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.SpiralBevelGearMeshCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1905.SpiralBevelGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5650.SpiralBevelGearMeshCompoundSingleMeshWhineAnalysis))

    def results_for_straight_bevel_gear_mesh(self, design_entity: '_1909.StraightBevelGearMesh') -> 'Iterable[_5659.StraightBevelGearMeshCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.StraightBevelGearMeshCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1909.StraightBevelGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5659.StraightBevelGearMeshCompoundSingleMeshWhineAnalysis))

    def results_for_worm_gear_mesh(self, design_entity: '_1911.WormGearMesh') -> 'Iterable[_5674.WormGearMeshCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.WormGearMeshCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1911.WormGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5674.WormGearMeshCompoundSingleMeshWhineAnalysis))

    def results_for_zerol_bevel_gear_mesh(self, design_entity: '_1913.ZerolBevelGearMesh') -> 'Iterable[_5677.ZerolBevelGearMeshCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.ZerolBevelGearMeshCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1913.ZerolBevelGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5677.ZerolBevelGearMeshCompoundSingleMeshWhineAnalysis))

    def results_for_gear_mesh(self, design_entity: '_1895.GearMesh') -> 'Iterable[_5610.GearMeshCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.GearMeshCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1895.GearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5610.GearMeshCompoundSingleMeshWhineAnalysis))

    def results_for_part_to_part_shear_coupling_connection(self, design_entity: '_1921.PartToPartShearCouplingConnection') -> 'Iterable[_5633.PartToPartShearCouplingConnectionCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.PartToPartShearCouplingConnectionCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1921.PartToPartShearCouplingConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5633.PartToPartShearCouplingConnectionCompoundSingleMeshWhineAnalysis))

    def results_for_clutch_connection(self, design_entity: '_1915.ClutchConnection') -> 'Iterable[_5578.ClutchConnectionCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.ClutchConnectionCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1915.ClutchConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5578.ClutchConnectionCompoundSingleMeshWhineAnalysis))

    def results_for_concept_coupling_connection(self, design_entity: '_1917.ConceptCouplingConnection') -> 'Iterable[_5583.ConceptCouplingConnectionCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.ConceptCouplingConnectionCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1917.ConceptCouplingConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5583.ConceptCouplingConnectionCompoundSingleMeshWhineAnalysis))

    def results_for_coupling_connection(self, design_entity: '_1919.CouplingConnection') -> 'Iterable[_5594.CouplingConnectionCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.CouplingConnectionCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1919.CouplingConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5594.CouplingConnectionCompoundSingleMeshWhineAnalysis))

    def results_for_spring_damper_connection(self, design_entity: '_1923.SpringDamperConnection') -> 'Iterable[_5653.SpringDamperConnectionCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.SpringDamperConnectionCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1923.SpringDamperConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5653.SpringDamperConnectionCompoundSingleMeshWhineAnalysis))

    def results_for_torque_converter_connection(self, design_entity: '_1925.TorqueConverterConnection') -> 'Iterable[_5668.TorqueConverterConnectionCompoundSingleMeshWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound.TorqueConverterConnectionCompoundSingleMeshWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1925.TorqueConverterConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5668.TorqueConverterConnectionCompoundSingleMeshWhineAnalysis))
