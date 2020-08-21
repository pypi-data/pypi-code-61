'''_2216.py

CompoundGearWhineAnalysisAnalysis
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
from mastapy.system_model.analyses_and_results.gear_whine_analyses.compound import (
    _5692, _5693, _5698, _5709,
    _5710, _5715, _5726, _5737,
    _5738, _5742, _5697, _5746,
    _5750, _5761, _5762, _5763,
    _5764, _5765, _5771, _5772,
    _5773, _5778, _5782, _5805,
    _5806, _5779, _5719, _5721,
    _5739, _5741, _5694, _5696,
    _5701, _5703, _5704, _5705,
    _5706, _5708, _5722, _5724,
    _5733, _5735, _5736, _5743,
    _5745, _5747, _5749, _5752,
    _5754, _5755, _5757, _5758,
    _5760, _5770, _5783, _5785,
    _5789, _5791, _5792, _5794,
    _5795, _5796, _5807, _5809,
    _5810, _5812, _5766, _5768,
    _5700, _5711, _5713, _5716,
    _5718, _5727, _5729, _5731,
    _5732, _5774, _5780, _5776,
    _5775, _5786, _5788, _5797,
    _5798, _5799, _5800, _5801,
    _5803, _5804, _5730, _5699,
    _5714, _5725, _5751, _5769,
    _5777, _5781, _5702, _5720,
    _5740, _5790, _5707, _5723,
    _5695, _5734, _5748, _5753,
    _5756, _5759, _5784, _5793,
    _5808, _5811, _5744, _5767,
    _5712, _5717, _5728, _5787,
    _5802
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

_COMPOUND_GEAR_WHINE_ANALYSIS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'CompoundGearWhineAnalysisAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CompoundGearWhineAnalysisAnalysis',)


class CompoundGearWhineAnalysisAnalysis(_2176.CompoundAnalysis):
    '''CompoundGearWhineAnalysisAnalysis

    This is a mastapy class.
    '''

    TYPE = _COMPOUND_GEAR_WHINE_ANALYSIS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CompoundGearWhineAnalysisAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def results_for_abstract_assembly(self, design_entity: '_2003.AbstractAssembly') -> 'Iterable[_5692.AbstractAssemblyCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.AbstractAssemblyCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2003.AbstractAssembly.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5692.AbstractAssemblyCompoundGearWhineAnalysis))

    def results_for_abstract_shaft_or_housing(self, design_entity: '_2004.AbstractShaftOrHousing') -> 'Iterable[_5693.AbstractShaftOrHousingCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.AbstractShaftOrHousingCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2004.AbstractShaftOrHousing.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5693.AbstractShaftOrHousingCompoundGearWhineAnalysis))

    def results_for_bearing(self, design_entity: '_2007.Bearing') -> 'Iterable[_5698.BearingCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BearingCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2007.Bearing.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5698.BearingCompoundGearWhineAnalysis))

    def results_for_bolt(self, design_entity: '_2009.Bolt') -> 'Iterable[_5709.BoltCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BoltCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2009.Bolt.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5709.BoltCompoundGearWhineAnalysis))

    def results_for_bolted_joint(self, design_entity: '_2010.BoltedJoint') -> 'Iterable[_5710.BoltedJointCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BoltedJointCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2010.BoltedJoint.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5710.BoltedJointCompoundGearWhineAnalysis))

    def results_for_component(self, design_entity: '_2011.Component') -> 'Iterable[_5715.ComponentCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Component)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ComponentCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2011.Component.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5715.ComponentCompoundGearWhineAnalysis))

    def results_for_connector(self, design_entity: '_2014.Connector') -> 'Iterable[_5726.ConnectorCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Connector)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ConnectorCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2014.Connector.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5726.ConnectorCompoundGearWhineAnalysis))

    def results_for_datum(self, design_entity: '_2015.Datum') -> 'Iterable[_5737.DatumCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Datum)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.DatumCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2015.Datum.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5737.DatumCompoundGearWhineAnalysis))

    def results_for_external_cad_model(self, design_entity: '_2018.ExternalCADModel') -> 'Iterable[_5738.ExternalCADModelCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ExternalCADModelCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2018.ExternalCADModel.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5738.ExternalCADModelCompoundGearWhineAnalysis))

    def results_for_flexible_pin_assembly(self, design_entity: '_2019.FlexiblePinAssembly') -> 'Iterable[_5742.FlexiblePinAssemblyCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.FlexiblePinAssemblyCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2019.FlexiblePinAssembly.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5742.FlexiblePinAssemblyCompoundGearWhineAnalysis))

    def results_for_assembly(self, design_entity: '_2002.Assembly') -> 'Iterable[_5697.AssemblyCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.AssemblyCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2002.Assembly.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5697.AssemblyCompoundGearWhineAnalysis))

    def results_for_guide_dxf_model(self, design_entity: '_2020.GuideDxfModel') -> 'Iterable[_5746.GuideDxfModelCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.GuideDxfModelCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2020.GuideDxfModel.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5746.GuideDxfModelCompoundGearWhineAnalysis))

    def results_for_imported_fe_component(self, design_entity: '_2023.ImportedFEComponent') -> 'Iterable[_5750.ImportedFEComponentCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ImportedFEComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ImportedFEComponentCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2023.ImportedFEComponent.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5750.ImportedFEComponentCompoundGearWhineAnalysis))

    def results_for_mass_disc(self, design_entity: '_2027.MassDisc') -> 'Iterable[_5761.MassDiscCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.MassDiscCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2027.MassDisc.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5761.MassDiscCompoundGearWhineAnalysis))

    def results_for_measurement_component(self, design_entity: '_2028.MeasurementComponent') -> 'Iterable[_5762.MeasurementComponentCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.MeasurementComponentCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2028.MeasurementComponent.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5762.MeasurementComponentCompoundGearWhineAnalysis))

    def results_for_mountable_component(self, design_entity: '_2029.MountableComponent') -> 'Iterable[_5763.MountableComponentCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.MountableComponentCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2029.MountableComponent.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5763.MountableComponentCompoundGearWhineAnalysis))

    def results_for_oil_seal(self, design_entity: '_2031.OilSeal') -> 'Iterable[_5764.OilSealCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.OilSealCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2031.OilSeal.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5764.OilSealCompoundGearWhineAnalysis))

    def results_for_part(self, design_entity: '_2033.Part') -> 'Iterable[_5765.PartCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Part)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.PartCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2033.Part.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5765.PartCompoundGearWhineAnalysis))

    def results_for_planet_carrier(self, design_entity: '_2034.PlanetCarrier') -> 'Iterable[_5771.PlanetCarrierCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.PlanetCarrierCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2034.PlanetCarrier.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5771.PlanetCarrierCompoundGearWhineAnalysis))

    def results_for_point_load(self, design_entity: '_2036.PointLoad') -> 'Iterable[_5772.PointLoadCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.PointLoadCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2036.PointLoad.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5772.PointLoadCompoundGearWhineAnalysis))

    def results_for_power_load(self, design_entity: '_2037.PowerLoad') -> 'Iterable[_5773.PowerLoadCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.PowerLoadCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2037.PowerLoad.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5773.PowerLoadCompoundGearWhineAnalysis))

    def results_for_root_assembly(self, design_entity: '_2039.RootAssembly') -> 'Iterable[_5778.RootAssemblyCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.RootAssemblyCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2039.RootAssembly.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5778.RootAssemblyCompoundGearWhineAnalysis))

    def results_for_specialised_assembly(self, design_entity: '_2041.SpecialisedAssembly') -> 'Iterable[_5782.SpecialisedAssemblyCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.SpecialisedAssemblyCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2041.SpecialisedAssembly.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5782.SpecialisedAssemblyCompoundGearWhineAnalysis))

    def results_for_unbalanced_mass(self, design_entity: '_2042.UnbalancedMass') -> 'Iterable[_5805.UnbalancedMassCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.UnbalancedMassCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2042.UnbalancedMass.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5805.UnbalancedMassCompoundGearWhineAnalysis))

    def results_for_virtual_component(self, design_entity: '_2043.VirtualComponent') -> 'Iterable[_5806.VirtualComponentCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.VirtualComponentCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2043.VirtualComponent.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5806.VirtualComponentCompoundGearWhineAnalysis))

    def results_for_shaft(self, design_entity: '_2046.Shaft') -> 'Iterable[_5779.ShaftCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ShaftCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2046.Shaft.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5779.ShaftCompoundGearWhineAnalysis))

    def results_for_concept_gear(self, design_entity: '_2084.ConceptGear') -> 'Iterable[_5719.ConceptGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ConceptGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2084.ConceptGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5719.ConceptGearCompoundGearWhineAnalysis))

    def results_for_concept_gear_set(self, design_entity: '_2085.ConceptGearSet') -> 'Iterable[_5721.ConceptGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ConceptGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2085.ConceptGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5721.ConceptGearSetCompoundGearWhineAnalysis))

    def results_for_face_gear(self, design_entity: '_2091.FaceGear') -> 'Iterable[_5739.FaceGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.FaceGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2091.FaceGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5739.FaceGearCompoundGearWhineAnalysis))

    def results_for_face_gear_set(self, design_entity: '_2092.FaceGearSet') -> 'Iterable[_5741.FaceGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.FaceGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2092.FaceGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5741.FaceGearSetCompoundGearWhineAnalysis))

    def results_for_agma_gleason_conical_gear(self, design_entity: '_2076.AGMAGleasonConicalGear') -> 'Iterable[_5694.AGMAGleasonConicalGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.AGMAGleasonConicalGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2076.AGMAGleasonConicalGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5694.AGMAGleasonConicalGearCompoundGearWhineAnalysis))

    def results_for_agma_gleason_conical_gear_set(self, design_entity: '_2077.AGMAGleasonConicalGearSet') -> 'Iterable[_5696.AGMAGleasonConicalGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.AGMAGleasonConicalGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2077.AGMAGleasonConicalGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5696.AGMAGleasonConicalGearSetCompoundGearWhineAnalysis))

    def results_for_bevel_differential_gear(self, design_entity: '_2078.BevelDifferentialGear') -> 'Iterable[_5701.BevelDifferentialGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BevelDifferentialGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2078.BevelDifferentialGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5701.BevelDifferentialGearCompoundGearWhineAnalysis))

    def results_for_bevel_differential_gear_set(self, design_entity: '_2079.BevelDifferentialGearSet') -> 'Iterable[_5703.BevelDifferentialGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BevelDifferentialGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2079.BevelDifferentialGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5703.BevelDifferentialGearSetCompoundGearWhineAnalysis))

    def results_for_bevel_differential_planet_gear(self, design_entity: '_2080.BevelDifferentialPlanetGear') -> 'Iterable[_5704.BevelDifferentialPlanetGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BevelDifferentialPlanetGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2080.BevelDifferentialPlanetGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5704.BevelDifferentialPlanetGearCompoundGearWhineAnalysis))

    def results_for_bevel_differential_sun_gear(self, design_entity: '_2081.BevelDifferentialSunGear') -> 'Iterable[_5705.BevelDifferentialSunGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BevelDifferentialSunGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2081.BevelDifferentialSunGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5705.BevelDifferentialSunGearCompoundGearWhineAnalysis))

    def results_for_bevel_gear(self, design_entity: '_2082.BevelGear') -> 'Iterable[_5706.BevelGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BevelGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2082.BevelGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5706.BevelGearCompoundGearWhineAnalysis))

    def results_for_bevel_gear_set(self, design_entity: '_2083.BevelGearSet') -> 'Iterable[_5708.BevelGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BevelGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2083.BevelGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5708.BevelGearSetCompoundGearWhineAnalysis))

    def results_for_conical_gear(self, design_entity: '_2086.ConicalGear') -> 'Iterable[_5722.ConicalGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ConicalGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2086.ConicalGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5722.ConicalGearCompoundGearWhineAnalysis))

    def results_for_conical_gear_set(self, design_entity: '_2087.ConicalGearSet') -> 'Iterable[_5724.ConicalGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ConicalGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2087.ConicalGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5724.ConicalGearSetCompoundGearWhineAnalysis))

    def results_for_cylindrical_gear(self, design_entity: '_2088.CylindricalGear') -> 'Iterable[_5733.CylindricalGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.CylindricalGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2088.CylindricalGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5733.CylindricalGearCompoundGearWhineAnalysis))

    def results_for_cylindrical_gear_set(self, design_entity: '_2089.CylindricalGearSet') -> 'Iterable[_5735.CylindricalGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.CylindricalGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2089.CylindricalGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5735.CylindricalGearSetCompoundGearWhineAnalysis))

    def results_for_cylindrical_planet_gear(self, design_entity: '_2090.CylindricalPlanetGear') -> 'Iterable[_5736.CylindricalPlanetGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.CylindricalPlanetGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2090.CylindricalPlanetGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5736.CylindricalPlanetGearCompoundGearWhineAnalysis))

    def results_for_gear(self, design_entity: '_2093.Gear') -> 'Iterable[_5743.GearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.GearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2093.Gear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5743.GearCompoundGearWhineAnalysis))

    def results_for_gear_set(self, design_entity: '_2095.GearSet') -> 'Iterable[_5745.GearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.GearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2095.GearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5745.GearSetCompoundGearWhineAnalysis))

    def results_for_hypoid_gear(self, design_entity: '_2097.HypoidGear') -> 'Iterable[_5747.HypoidGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.HypoidGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2097.HypoidGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5747.HypoidGearCompoundGearWhineAnalysis))

    def results_for_hypoid_gear_set(self, design_entity: '_2098.HypoidGearSet') -> 'Iterable[_5749.HypoidGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.HypoidGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2098.HypoidGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5749.HypoidGearSetCompoundGearWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_conical_gear(self, design_entity: '_2099.KlingelnbergCycloPalloidConicalGear') -> 'Iterable[_5752.KlingelnbergCycloPalloidConicalGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.KlingelnbergCycloPalloidConicalGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2099.KlingelnbergCycloPalloidConicalGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5752.KlingelnbergCycloPalloidConicalGearCompoundGearWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(self, design_entity: '_2100.KlingelnbergCycloPalloidConicalGearSet') -> 'Iterable[_5754.KlingelnbergCycloPalloidConicalGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.KlingelnbergCycloPalloidConicalGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2100.KlingelnbergCycloPalloidConicalGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5754.KlingelnbergCycloPalloidConicalGearSetCompoundGearWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(self, design_entity: '_2101.KlingelnbergCycloPalloidHypoidGear') -> 'Iterable[_5755.KlingelnbergCycloPalloidHypoidGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.KlingelnbergCycloPalloidHypoidGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2101.KlingelnbergCycloPalloidHypoidGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5755.KlingelnbergCycloPalloidHypoidGearCompoundGearWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(self, design_entity: '_2102.KlingelnbergCycloPalloidHypoidGearSet') -> 'Iterable[_5757.KlingelnbergCycloPalloidHypoidGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.KlingelnbergCycloPalloidHypoidGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2102.KlingelnbergCycloPalloidHypoidGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5757.KlingelnbergCycloPalloidHypoidGearSetCompoundGearWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(self, design_entity: '_2103.KlingelnbergCycloPalloidSpiralBevelGear') -> 'Iterable[_5758.KlingelnbergCycloPalloidSpiralBevelGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2103.KlingelnbergCycloPalloidSpiralBevelGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5758.KlingelnbergCycloPalloidSpiralBevelGearCompoundGearWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, design_entity: '_2104.KlingelnbergCycloPalloidSpiralBevelGearSet') -> 'Iterable[_5760.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2104.KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5760.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundGearWhineAnalysis))

    def results_for_planetary_gear_set(self, design_entity: '_2105.PlanetaryGearSet') -> 'Iterable[_5770.PlanetaryGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.PlanetaryGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2105.PlanetaryGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5770.PlanetaryGearSetCompoundGearWhineAnalysis))

    def results_for_spiral_bevel_gear(self, design_entity: '_2106.SpiralBevelGear') -> 'Iterable[_5783.SpiralBevelGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.SpiralBevelGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2106.SpiralBevelGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5783.SpiralBevelGearCompoundGearWhineAnalysis))

    def results_for_spiral_bevel_gear_set(self, design_entity: '_2107.SpiralBevelGearSet') -> 'Iterable[_5785.SpiralBevelGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.SpiralBevelGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2107.SpiralBevelGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5785.SpiralBevelGearSetCompoundGearWhineAnalysis))

    def results_for_straight_bevel_diff_gear(self, design_entity: '_2108.StraightBevelDiffGear') -> 'Iterable[_5789.StraightBevelDiffGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.StraightBevelDiffGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2108.StraightBevelDiffGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5789.StraightBevelDiffGearCompoundGearWhineAnalysis))

    def results_for_straight_bevel_diff_gear_set(self, design_entity: '_2109.StraightBevelDiffGearSet') -> 'Iterable[_5791.StraightBevelDiffGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.StraightBevelDiffGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2109.StraightBevelDiffGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5791.StraightBevelDiffGearSetCompoundGearWhineAnalysis))

    def results_for_straight_bevel_gear(self, design_entity: '_2110.StraightBevelGear') -> 'Iterable[_5792.StraightBevelGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.StraightBevelGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2110.StraightBevelGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5792.StraightBevelGearCompoundGearWhineAnalysis))

    def results_for_straight_bevel_gear_set(self, design_entity: '_2111.StraightBevelGearSet') -> 'Iterable[_5794.StraightBevelGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.StraightBevelGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2111.StraightBevelGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5794.StraightBevelGearSetCompoundGearWhineAnalysis))

    def results_for_straight_bevel_planet_gear(self, design_entity: '_2112.StraightBevelPlanetGear') -> 'Iterable[_5795.StraightBevelPlanetGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.StraightBevelPlanetGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2112.StraightBevelPlanetGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5795.StraightBevelPlanetGearCompoundGearWhineAnalysis))

    def results_for_straight_bevel_sun_gear(self, design_entity: '_2113.StraightBevelSunGear') -> 'Iterable[_5796.StraightBevelSunGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.StraightBevelSunGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2113.StraightBevelSunGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5796.StraightBevelSunGearCompoundGearWhineAnalysis))

    def results_for_worm_gear(self, design_entity: '_2114.WormGear') -> 'Iterable[_5807.WormGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.WormGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2114.WormGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5807.WormGearCompoundGearWhineAnalysis))

    def results_for_worm_gear_set(self, design_entity: '_2115.WormGearSet') -> 'Iterable[_5809.WormGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.WormGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2115.WormGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5809.WormGearSetCompoundGearWhineAnalysis))

    def results_for_zerol_bevel_gear(self, design_entity: '_2116.ZerolBevelGear') -> 'Iterable[_5810.ZerolBevelGearCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ZerolBevelGearCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2116.ZerolBevelGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5810.ZerolBevelGearCompoundGearWhineAnalysis))

    def results_for_zerol_bevel_gear_set(self, design_entity: '_2117.ZerolBevelGearSet') -> 'Iterable[_5812.ZerolBevelGearSetCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ZerolBevelGearSetCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2117.ZerolBevelGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5812.ZerolBevelGearSetCompoundGearWhineAnalysis))

    def results_for_part_to_part_shear_coupling(self, design_entity: '_2146.PartToPartShearCoupling') -> 'Iterable[_5766.PartToPartShearCouplingCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCoupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.PartToPartShearCouplingCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2146.PartToPartShearCoupling.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5766.PartToPartShearCouplingCompoundGearWhineAnalysis))

    def results_for_part_to_part_shear_coupling_half(self, design_entity: '_2147.PartToPartShearCouplingHalf') -> 'Iterable[_5768.PartToPartShearCouplingHalfCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.PartToPartShearCouplingHalfCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2147.PartToPartShearCouplingHalf.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5768.PartToPartShearCouplingHalfCompoundGearWhineAnalysis))

    def results_for_belt_drive(self, design_entity: '_2135.BeltDrive') -> 'Iterable[_5700.BeltDriveCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BeltDriveCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2135.BeltDrive.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5700.BeltDriveCompoundGearWhineAnalysis))

    def results_for_clutch(self, design_entity: '_2137.Clutch') -> 'Iterable[_5711.ClutchCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ClutchCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2137.Clutch.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5711.ClutchCompoundGearWhineAnalysis))

    def results_for_clutch_half(self, design_entity: '_2138.ClutchHalf') -> 'Iterable[_5713.ClutchHalfCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ClutchHalfCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2138.ClutchHalf.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5713.ClutchHalfCompoundGearWhineAnalysis))

    def results_for_concept_coupling(self, design_entity: '_2140.ConceptCoupling') -> 'Iterable[_5716.ConceptCouplingCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ConceptCouplingCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2140.ConceptCoupling.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5716.ConceptCouplingCompoundGearWhineAnalysis))

    def results_for_concept_coupling_half(self, design_entity: '_2141.ConceptCouplingHalf') -> 'Iterable[_5718.ConceptCouplingHalfCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ConceptCouplingHalfCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2141.ConceptCouplingHalf.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5718.ConceptCouplingHalfCompoundGearWhineAnalysis))

    def results_for_coupling(self, design_entity: '_2142.Coupling') -> 'Iterable[_5727.CouplingCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.CouplingCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2142.Coupling.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5727.CouplingCompoundGearWhineAnalysis))

    def results_for_coupling_half(self, design_entity: '_2143.CouplingHalf') -> 'Iterable[_5729.CouplingHalfCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.CouplingHalfCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2143.CouplingHalf.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5729.CouplingHalfCompoundGearWhineAnalysis))

    def results_for_cvt(self, design_entity: '_2144.CVT') -> 'Iterable[_5731.CVTCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.CVTCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2144.CVT.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5731.CVTCompoundGearWhineAnalysis))

    def results_for_cvt_pulley(self, design_entity: '_2145.CVTPulley') -> 'Iterable[_5732.CVTPulleyCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.CVTPulleyCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2145.CVTPulley.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5732.CVTPulleyCompoundGearWhineAnalysis))

    def results_for_pulley(self, design_entity: '_2148.Pulley') -> 'Iterable[_5774.PulleyCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.PulleyCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2148.Pulley.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5774.PulleyCompoundGearWhineAnalysis))

    def results_for_shaft_hub_connection(self, design_entity: '_2156.ShaftHubConnection') -> 'Iterable[_5780.ShaftHubConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ShaftHubConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2156.ShaftHubConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5780.ShaftHubConnectionCompoundGearWhineAnalysis))

    def results_for_rolling_ring(self, design_entity: '_2154.RollingRing') -> 'Iterable[_5776.RollingRingCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.RollingRingCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2154.RollingRing.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5776.RollingRingCompoundGearWhineAnalysis))

    def results_for_rolling_ring_assembly(self, design_entity: '_2155.RollingRingAssembly') -> 'Iterable[_5775.RollingRingAssemblyCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.RollingRingAssemblyCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2155.RollingRingAssembly.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5775.RollingRingAssemblyCompoundGearWhineAnalysis))

    def results_for_spring_damper(self, design_entity: '_2157.SpringDamper') -> 'Iterable[_5786.SpringDamperCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.SpringDamperCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2157.SpringDamper.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5786.SpringDamperCompoundGearWhineAnalysis))

    def results_for_spring_damper_half(self, design_entity: '_2158.SpringDamperHalf') -> 'Iterable[_5788.SpringDamperHalfCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.SpringDamperHalfCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2158.SpringDamperHalf.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5788.SpringDamperHalfCompoundGearWhineAnalysis))

    def results_for_synchroniser(self, design_entity: '_2159.Synchroniser') -> 'Iterable[_5797.SynchroniserCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.SynchroniserCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2159.Synchroniser.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5797.SynchroniserCompoundGearWhineAnalysis))

    def results_for_synchroniser_half(self, design_entity: '_2161.SynchroniserHalf') -> 'Iterable[_5798.SynchroniserHalfCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.SynchroniserHalfCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2161.SynchroniserHalf.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5798.SynchroniserHalfCompoundGearWhineAnalysis))

    def results_for_synchroniser_part(self, design_entity: '_2162.SynchroniserPart') -> 'Iterable[_5799.SynchroniserPartCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.SynchroniserPartCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2162.SynchroniserPart.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5799.SynchroniserPartCompoundGearWhineAnalysis))

    def results_for_synchroniser_sleeve(self, design_entity: '_2163.SynchroniserSleeve') -> 'Iterable[_5800.SynchroniserSleeveCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.SynchroniserSleeveCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2163.SynchroniserSleeve.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5800.SynchroniserSleeveCompoundGearWhineAnalysis))

    def results_for_torque_converter(self, design_entity: '_2164.TorqueConverter') -> 'Iterable[_5801.TorqueConverterCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.TorqueConverterCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2164.TorqueConverter.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5801.TorqueConverterCompoundGearWhineAnalysis))

    def results_for_torque_converter_pump(self, design_entity: '_2165.TorqueConverterPump') -> 'Iterable[_5803.TorqueConverterPumpCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.TorqueConverterPumpCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2165.TorqueConverterPump.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5803.TorqueConverterPumpCompoundGearWhineAnalysis))

    def results_for_torque_converter_turbine(self, design_entity: '_2167.TorqueConverterTurbine') -> 'Iterable[_5804.TorqueConverterTurbineCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.TorqueConverterTurbineCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2167.TorqueConverterTurbine.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5804.TorqueConverterTurbineCompoundGearWhineAnalysis))

    def results_for_cvt_belt_connection(self, design_entity: '_1858.CVTBeltConnection') -> 'Iterable[_5730.CVTBeltConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.CVTBeltConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1858.CVTBeltConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5730.CVTBeltConnectionCompoundGearWhineAnalysis))

    def results_for_belt_connection(self, design_entity: '_1853.BeltConnection') -> 'Iterable[_5699.BeltConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BeltConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1853.BeltConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5699.BeltConnectionCompoundGearWhineAnalysis))

    def results_for_coaxial_connection(self, design_entity: '_1854.CoaxialConnection') -> 'Iterable[_5714.CoaxialConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.CoaxialConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1854.CoaxialConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5714.CoaxialConnectionCompoundGearWhineAnalysis))

    def results_for_connection(self, design_entity: '_1857.Connection') -> 'Iterable[_5725.ConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1857.Connection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5725.ConnectionCompoundGearWhineAnalysis))

    def results_for_inter_mountable_component_connection(self, design_entity: '_1866.InterMountableComponentConnection') -> 'Iterable[_5751.InterMountableComponentConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.InterMountableComponentConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1866.InterMountableComponentConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5751.InterMountableComponentConnectionCompoundGearWhineAnalysis))

    def results_for_planetary_connection(self, design_entity: '_1869.PlanetaryConnection') -> 'Iterable[_5769.PlanetaryConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.PlanetaryConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1869.PlanetaryConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5769.PlanetaryConnectionCompoundGearWhineAnalysis))

    def results_for_rolling_ring_connection(self, design_entity: '_1873.RollingRingConnection') -> 'Iterable[_5777.RollingRingConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.RollingRingConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1873.RollingRingConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5777.RollingRingConnectionCompoundGearWhineAnalysis))

    def results_for_shaft_to_mountable_component_connection(self, design_entity: '_1877.ShaftToMountableComponentConnection') -> 'Iterable[_5781.ShaftToMountableComponentConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ShaftToMountableComponentConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1877.ShaftToMountableComponentConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5781.ShaftToMountableComponentConnectionCompoundGearWhineAnalysis))

    def results_for_bevel_differential_gear_mesh(self, design_entity: '_1883.BevelDifferentialGearMesh') -> 'Iterable[_5702.BevelDifferentialGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BevelDifferentialGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1883.BevelDifferentialGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5702.BevelDifferentialGearMeshCompoundGearWhineAnalysis))

    def results_for_concept_gear_mesh(self, design_entity: '_1887.ConceptGearMesh') -> 'Iterable[_5720.ConceptGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ConceptGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1887.ConceptGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5720.ConceptGearMeshCompoundGearWhineAnalysis))

    def results_for_face_gear_mesh(self, design_entity: '_1893.FaceGearMesh') -> 'Iterable[_5740.FaceGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.FaceGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1893.FaceGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5740.FaceGearMeshCompoundGearWhineAnalysis))

    def results_for_straight_bevel_diff_gear_mesh(self, design_entity: '_1907.StraightBevelDiffGearMesh') -> 'Iterable[_5790.StraightBevelDiffGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.StraightBevelDiffGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1907.StraightBevelDiffGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5790.StraightBevelDiffGearMeshCompoundGearWhineAnalysis))

    def results_for_bevel_gear_mesh(self, design_entity: '_1885.BevelGearMesh') -> 'Iterable[_5707.BevelGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.BevelGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1885.BevelGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5707.BevelGearMeshCompoundGearWhineAnalysis))

    def results_for_conical_gear_mesh(self, design_entity: '_1889.ConicalGearMesh') -> 'Iterable[_5723.ConicalGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ConicalGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1889.ConicalGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5723.ConicalGearMeshCompoundGearWhineAnalysis))

    def results_for_agma_gleason_conical_gear_mesh(self, design_entity: '_1881.AGMAGleasonConicalGearMesh') -> 'Iterable[_5695.AGMAGleasonConicalGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.AGMAGleasonConicalGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1881.AGMAGleasonConicalGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5695.AGMAGleasonConicalGearMeshCompoundGearWhineAnalysis))

    def results_for_cylindrical_gear_mesh(self, design_entity: '_1891.CylindricalGearMesh') -> 'Iterable[_5734.CylindricalGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.CylindricalGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1891.CylindricalGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5734.CylindricalGearMeshCompoundGearWhineAnalysis))

    def results_for_hypoid_gear_mesh(self, design_entity: '_1897.HypoidGearMesh') -> 'Iterable[_5748.HypoidGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.HypoidGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1897.HypoidGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5748.HypoidGearMeshCompoundGearWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(self, design_entity: '_1900.KlingelnbergCycloPalloidConicalGearMesh') -> 'Iterable[_5753.KlingelnbergCycloPalloidConicalGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.KlingelnbergCycloPalloidConicalGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1900.KlingelnbergCycloPalloidConicalGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5753.KlingelnbergCycloPalloidConicalGearMeshCompoundGearWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self, design_entity: '_1901.KlingelnbergCycloPalloidHypoidGearMesh') -> 'Iterable[_5756.KlingelnbergCycloPalloidHypoidGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.KlingelnbergCycloPalloidHypoidGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1901.KlingelnbergCycloPalloidHypoidGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5756.KlingelnbergCycloPalloidHypoidGearMeshCompoundGearWhineAnalysis))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self, design_entity: '_1902.KlingelnbergCycloPalloidSpiralBevelGearMesh') -> 'Iterable[_5759.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1902.KlingelnbergCycloPalloidSpiralBevelGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5759.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundGearWhineAnalysis))

    def results_for_spiral_bevel_gear_mesh(self, design_entity: '_1905.SpiralBevelGearMesh') -> 'Iterable[_5784.SpiralBevelGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.SpiralBevelGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1905.SpiralBevelGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5784.SpiralBevelGearMeshCompoundGearWhineAnalysis))

    def results_for_straight_bevel_gear_mesh(self, design_entity: '_1909.StraightBevelGearMesh') -> 'Iterable[_5793.StraightBevelGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.StraightBevelGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1909.StraightBevelGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5793.StraightBevelGearMeshCompoundGearWhineAnalysis))

    def results_for_worm_gear_mesh(self, design_entity: '_1911.WormGearMesh') -> 'Iterable[_5808.WormGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.WormGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1911.WormGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5808.WormGearMeshCompoundGearWhineAnalysis))

    def results_for_zerol_bevel_gear_mesh(self, design_entity: '_1913.ZerolBevelGearMesh') -> 'Iterable[_5811.ZerolBevelGearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ZerolBevelGearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1913.ZerolBevelGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5811.ZerolBevelGearMeshCompoundGearWhineAnalysis))

    def results_for_gear_mesh(self, design_entity: '_1895.GearMesh') -> 'Iterable[_5744.GearMeshCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.GearMeshCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1895.GearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5744.GearMeshCompoundGearWhineAnalysis))

    def results_for_part_to_part_shear_coupling_connection(self, design_entity: '_1921.PartToPartShearCouplingConnection') -> 'Iterable[_5767.PartToPartShearCouplingConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.PartToPartShearCouplingConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1921.PartToPartShearCouplingConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5767.PartToPartShearCouplingConnectionCompoundGearWhineAnalysis))

    def results_for_clutch_connection(self, design_entity: '_1915.ClutchConnection') -> 'Iterable[_5712.ClutchConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ClutchConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1915.ClutchConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5712.ClutchConnectionCompoundGearWhineAnalysis))

    def results_for_concept_coupling_connection(self, design_entity: '_1917.ConceptCouplingConnection') -> 'Iterable[_5717.ConceptCouplingConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.ConceptCouplingConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1917.ConceptCouplingConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5717.ConceptCouplingConnectionCompoundGearWhineAnalysis))

    def results_for_coupling_connection(self, design_entity: '_1919.CouplingConnection') -> 'Iterable[_5728.CouplingConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.CouplingConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1919.CouplingConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5728.CouplingConnectionCompoundGearWhineAnalysis))

    def results_for_spring_damper_connection(self, design_entity: '_1923.SpringDamperConnection') -> 'Iterable[_5787.SpringDamperConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.SpringDamperConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1923.SpringDamperConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5787.SpringDamperConnectionCompoundGearWhineAnalysis))

    def results_for_torque_converter_connection(self, design_entity: '_1925.TorqueConverterConnection') -> 'Iterable[_5802.TorqueConverterConnectionCompoundGearWhineAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.gear_whine_analyses.compound.TorqueConverterConnectionCompoundGearWhineAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1925.TorqueConverterConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5802.TorqueConverterConnectionCompoundGearWhineAnalysis))
