'''_2211.py

CompoundDynamicAnalysisAnalysis
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
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
    _5945, _5946, _5951, _5962,
    _5963, _5968, _5979, _5990,
    _5991, _5995, _5950, _5999,
    _6003, _6014, _6015, _6016,
    _6017, _6018, _6024, _6025,
    _6026, _6031, _6035, _6058,
    _6059, _6032, _5972, _5974,
    _5992, _5994, _5947, _5949,
    _5954, _5956, _5957, _5958,
    _5959, _5961, _5975, _5977,
    _5986, _5988, _5989, _5996,
    _5998, _6000, _6002, _6005,
    _6007, _6008, _6010, _6011,
    _6013, _6023, _6036, _6038,
    _6042, _6044, _6045, _6047,
    _6048, _6049, _6060, _6062,
    _6063, _6065, _6019, _6021,
    _5953, _5964, _5966, _5969,
    _5971, _5980, _5982, _5984,
    _5985, _6027, _6033, _6029,
    _6028, _6039, _6041, _6050,
    _6051, _6052, _6053, _6054,
    _6056, _6057, _5983, _5952,
    _5967, _5978, _6004, _6022,
    _6030, _6034, _5955, _5973,
    _5993, _6043, _5960, _5976,
    _5948, _5987, _6001, _6006,
    _6009, _6012, _6037, _6046,
    _6061, _6064, _5997, _6020,
    _5965, _5970, _5981, _6040,
    _6055
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

_COMPOUND_DYNAMIC_ANALYSIS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'CompoundDynamicAnalysisAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CompoundDynamicAnalysisAnalysis',)


class CompoundDynamicAnalysisAnalysis(_2176.CompoundAnalysis):
    '''CompoundDynamicAnalysisAnalysis

    This is a mastapy class.
    '''

    TYPE = _COMPOUND_DYNAMIC_ANALYSIS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CompoundDynamicAnalysisAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def results_for_abstract_assembly(self, design_entity: '_2003.AbstractAssembly') -> 'Iterable[_5945.AbstractAssemblyCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.AbstractAssemblyCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2003.AbstractAssembly.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5945.AbstractAssemblyCompoundDynamicAnalysis))

    def results_for_abstract_shaft_or_housing(self, design_entity: '_2004.AbstractShaftOrHousing') -> 'Iterable[_5946.AbstractShaftOrHousingCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.AbstractShaftOrHousingCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2004.AbstractShaftOrHousing.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5946.AbstractShaftOrHousingCompoundDynamicAnalysis))

    def results_for_bearing(self, design_entity: '_2007.Bearing') -> 'Iterable[_5951.BearingCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.BearingCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2007.Bearing.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5951.BearingCompoundDynamicAnalysis))

    def results_for_bolt(self, design_entity: '_2009.Bolt') -> 'Iterable[_5962.BoltCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.BoltCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2009.Bolt.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5962.BoltCompoundDynamicAnalysis))

    def results_for_bolted_joint(self, design_entity: '_2010.BoltedJoint') -> 'Iterable[_5963.BoltedJointCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.BoltedJointCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2010.BoltedJoint.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5963.BoltedJointCompoundDynamicAnalysis))

    def results_for_component(self, design_entity: '_2011.Component') -> 'Iterable[_5968.ComponentCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Component)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ComponentCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2011.Component.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5968.ComponentCompoundDynamicAnalysis))

    def results_for_connector(self, design_entity: '_2014.Connector') -> 'Iterable[_5979.ConnectorCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Connector)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ConnectorCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2014.Connector.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5979.ConnectorCompoundDynamicAnalysis))

    def results_for_datum(self, design_entity: '_2015.Datum') -> 'Iterable[_5990.DatumCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Datum)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.DatumCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2015.Datum.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5990.DatumCompoundDynamicAnalysis))

    def results_for_external_cad_model(self, design_entity: '_2018.ExternalCADModel') -> 'Iterable[_5991.ExternalCADModelCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ExternalCADModelCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2018.ExternalCADModel.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5991.ExternalCADModelCompoundDynamicAnalysis))

    def results_for_flexible_pin_assembly(self, design_entity: '_2019.FlexiblePinAssembly') -> 'Iterable[_5995.FlexiblePinAssemblyCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.FlexiblePinAssemblyCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2019.FlexiblePinAssembly.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5995.FlexiblePinAssemblyCompoundDynamicAnalysis))

    def results_for_assembly(self, design_entity: '_2002.Assembly') -> 'Iterable[_5950.AssemblyCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.AssemblyCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2002.Assembly.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5950.AssemblyCompoundDynamicAnalysis))

    def results_for_guide_dxf_model(self, design_entity: '_2020.GuideDxfModel') -> 'Iterable[_5999.GuideDxfModelCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.GuideDxfModelCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2020.GuideDxfModel.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5999.GuideDxfModelCompoundDynamicAnalysis))

    def results_for_imported_fe_component(self, design_entity: '_2023.ImportedFEComponent') -> 'Iterable[_6003.ImportedFEComponentCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ImportedFEComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ImportedFEComponentCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2023.ImportedFEComponent.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6003.ImportedFEComponentCompoundDynamicAnalysis))

    def results_for_mass_disc(self, design_entity: '_2027.MassDisc') -> 'Iterable[_6014.MassDiscCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.MassDiscCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2027.MassDisc.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6014.MassDiscCompoundDynamicAnalysis))

    def results_for_measurement_component(self, design_entity: '_2028.MeasurementComponent') -> 'Iterable[_6015.MeasurementComponentCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.MeasurementComponentCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2028.MeasurementComponent.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6015.MeasurementComponentCompoundDynamicAnalysis))

    def results_for_mountable_component(self, design_entity: '_2029.MountableComponent') -> 'Iterable[_6016.MountableComponentCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.MountableComponentCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2029.MountableComponent.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6016.MountableComponentCompoundDynamicAnalysis))

    def results_for_oil_seal(self, design_entity: '_2031.OilSeal') -> 'Iterable[_6017.OilSealCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.OilSealCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2031.OilSeal.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6017.OilSealCompoundDynamicAnalysis))

    def results_for_part(self, design_entity: '_2033.Part') -> 'Iterable[_6018.PartCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Part)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.PartCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2033.Part.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6018.PartCompoundDynamicAnalysis))

    def results_for_planet_carrier(self, design_entity: '_2034.PlanetCarrier') -> 'Iterable[_6024.PlanetCarrierCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.PlanetCarrierCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2034.PlanetCarrier.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6024.PlanetCarrierCompoundDynamicAnalysis))

    def results_for_point_load(self, design_entity: '_2036.PointLoad') -> 'Iterable[_6025.PointLoadCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.PointLoadCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2036.PointLoad.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6025.PointLoadCompoundDynamicAnalysis))

    def results_for_power_load(self, design_entity: '_2037.PowerLoad') -> 'Iterable[_6026.PowerLoadCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.PowerLoadCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2037.PowerLoad.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6026.PowerLoadCompoundDynamicAnalysis))

    def results_for_root_assembly(self, design_entity: '_2039.RootAssembly') -> 'Iterable[_6031.RootAssemblyCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.RootAssemblyCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2039.RootAssembly.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6031.RootAssemblyCompoundDynamicAnalysis))

    def results_for_specialised_assembly(self, design_entity: '_2041.SpecialisedAssembly') -> 'Iterable[_6035.SpecialisedAssemblyCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.SpecialisedAssemblyCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2041.SpecialisedAssembly.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6035.SpecialisedAssemblyCompoundDynamicAnalysis))

    def results_for_unbalanced_mass(self, design_entity: '_2042.UnbalancedMass') -> 'Iterable[_6058.UnbalancedMassCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.UnbalancedMassCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2042.UnbalancedMass.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6058.UnbalancedMassCompoundDynamicAnalysis))

    def results_for_virtual_component(self, design_entity: '_2043.VirtualComponent') -> 'Iterable[_6059.VirtualComponentCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.VirtualComponentCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2043.VirtualComponent.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6059.VirtualComponentCompoundDynamicAnalysis))

    def results_for_shaft(self, design_entity: '_2046.Shaft') -> 'Iterable[_6032.ShaftCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ShaftCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2046.Shaft.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6032.ShaftCompoundDynamicAnalysis))

    def results_for_concept_gear(self, design_entity: '_2084.ConceptGear') -> 'Iterable[_5972.ConceptGearCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ConceptGearCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2084.ConceptGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5972.ConceptGearCompoundDynamicAnalysis))

    def results_for_concept_gear_set(self, design_entity: '_2085.ConceptGearSet') -> 'Iterable[_5974.ConceptGearSetCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ConceptGearSetCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2085.ConceptGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5974.ConceptGearSetCompoundDynamicAnalysis))

    def results_for_face_gear(self, design_entity: '_2091.FaceGear') -> 'Iterable[_5992.FaceGearCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.FaceGearCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2091.FaceGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5992.FaceGearCompoundDynamicAnalysis))

    def results_for_face_gear_set(self, design_entity: '_2092.FaceGearSet') -> 'Iterable[_5994.FaceGearSetCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.FaceGearSetCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2092.FaceGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5994.FaceGearSetCompoundDynamicAnalysis))

    def results_for_agma_gleason_conical_gear(self, design_entity: '_2076.AGMAGleasonConicalGear') -> 'Iterable[_5947.AGMAGleasonConicalGearCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.AGMAGleasonConicalGearCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2076.AGMAGleasonConicalGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5947.AGMAGleasonConicalGearCompoundDynamicAnalysis))

    def results_for_agma_gleason_conical_gear_set(self, design_entity: '_2077.AGMAGleasonConicalGearSet') -> 'Iterable[_5949.AGMAGleasonConicalGearSetCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.AGMAGleasonConicalGearSetCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2077.AGMAGleasonConicalGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5949.AGMAGleasonConicalGearSetCompoundDynamicAnalysis))

    def results_for_bevel_differential_gear(self, design_entity: '_2078.BevelDifferentialGear') -> 'Iterable[_5954.BevelDifferentialGearCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.BevelDifferentialGearCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2078.BevelDifferentialGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5954.BevelDifferentialGearCompoundDynamicAnalysis))

    def results_for_bevel_differential_gear_set(self, design_entity: '_2079.BevelDifferentialGearSet') -> 'Iterable[_5956.BevelDifferentialGearSetCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.BevelDifferentialGearSetCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2079.BevelDifferentialGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5956.BevelDifferentialGearSetCompoundDynamicAnalysis))

    def results_for_bevel_differential_planet_gear(self, design_entity: '_2080.BevelDifferentialPlanetGear') -> 'Iterable[_5957.BevelDifferentialPlanetGearCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.BevelDifferentialPlanetGearCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2080.BevelDifferentialPlanetGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5957.BevelDifferentialPlanetGearCompoundDynamicAnalysis))

    def results_for_bevel_differential_sun_gear(self, design_entity: '_2081.BevelDifferentialSunGear') -> 'Iterable[_5958.BevelDifferentialSunGearCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.BevelDifferentialSunGearCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2081.BevelDifferentialSunGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5958.BevelDifferentialSunGearCompoundDynamicAnalysis))

    def results_for_bevel_gear(self, design_entity: '_2082.BevelGear') -> 'Iterable[_5959.BevelGearCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.BevelGearCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2082.BevelGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5959.BevelGearCompoundDynamicAnalysis))

    def results_for_bevel_gear_set(self, design_entity: '_2083.BevelGearSet') -> 'Iterable[_5961.BevelGearSetCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.BevelGearSetCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2083.BevelGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5961.BevelGearSetCompoundDynamicAnalysis))

    def results_for_conical_gear(self, design_entity: '_2086.ConicalGear') -> 'Iterable[_5975.ConicalGearCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ConicalGearCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2086.ConicalGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5975.ConicalGearCompoundDynamicAnalysis))

    def results_for_conical_gear_set(self, design_entity: '_2087.ConicalGearSet') -> 'Iterable[_5977.ConicalGearSetCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ConicalGearSetCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2087.ConicalGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5977.ConicalGearSetCompoundDynamicAnalysis))

    def results_for_cylindrical_gear(self, design_entity: '_2088.CylindricalGear') -> 'Iterable[_5986.CylindricalGearCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.CylindricalGearCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2088.CylindricalGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5986.CylindricalGearCompoundDynamicAnalysis))

    def results_for_cylindrical_gear_set(self, design_entity: '_2089.CylindricalGearSet') -> 'Iterable[_5988.CylindricalGearSetCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.CylindricalGearSetCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2089.CylindricalGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5988.CylindricalGearSetCompoundDynamicAnalysis))

    def results_for_cylindrical_planet_gear(self, design_entity: '_2090.CylindricalPlanetGear') -> 'Iterable[_5989.CylindricalPlanetGearCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.CylindricalPlanetGearCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2090.CylindricalPlanetGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5989.CylindricalPlanetGearCompoundDynamicAnalysis))

    def results_for_gear(self, design_entity: '_2093.Gear') -> 'Iterable[_5996.GearCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.GearCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2093.Gear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5996.GearCompoundDynamicAnalysis))

    def results_for_gear_set(self, design_entity: '_2095.GearSet') -> 'Iterable[_5998.GearSetCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.GearSetCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2095.GearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5998.GearSetCompoundDynamicAnalysis))

    def results_for_hypoid_gear(self, design_entity: '_2097.HypoidGear') -> 'Iterable[_6000.HypoidGearCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.HypoidGearCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2097.HypoidGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6000.HypoidGearCompoundDynamicAnalysis))

    def results_for_hypoid_gear_set(self, design_entity: '_2098.HypoidGearSet') -> 'Iterable[_6002.HypoidGearSetCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.HypoidGearSetCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2098.HypoidGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6002.HypoidGearSetCompoundDynamicAnalysis))

    def results_for_klingelnberg_cyclo_palloid_conical_gear(self, design_entity: '_2099.KlingelnbergCycloPalloidConicalGear') -> 'Iterable[_6005.KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2099.KlingelnbergCycloPalloidConicalGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6005.KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis))

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(self, design_entity: '_2100.KlingelnbergCycloPalloidConicalGearSet') -> 'Iterable[_6007.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2100.KlingelnbergCycloPalloidConicalGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6007.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(self, design_entity: '_2101.KlingelnbergCycloPalloidHypoidGear') -> 'Iterable[_6008.KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2101.KlingelnbergCycloPalloidHypoidGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6008.KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(self, design_entity: '_2102.KlingelnbergCycloPalloidHypoidGearSet') -> 'Iterable[_6010.KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2102.KlingelnbergCycloPalloidHypoidGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6010.KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(self, design_entity: '_2103.KlingelnbergCycloPalloidSpiralBevelGear') -> 'Iterable[_6011.KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2103.KlingelnbergCycloPalloidSpiralBevelGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6011.KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, design_entity: '_2104.KlingelnbergCycloPalloidSpiralBevelGearSet') -> 'Iterable[_6013.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2104.KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6013.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis))

    def results_for_planetary_gear_set(self, design_entity: '_2105.PlanetaryGearSet') -> 'Iterable[_6023.PlanetaryGearSetCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.PlanetaryGearSetCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2105.PlanetaryGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6023.PlanetaryGearSetCompoundDynamicAnalysis))

    def results_for_spiral_bevel_gear(self, design_entity: '_2106.SpiralBevelGear') -> 'Iterable[_6036.SpiralBevelGearCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.SpiralBevelGearCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2106.SpiralBevelGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6036.SpiralBevelGearCompoundDynamicAnalysis))

    def results_for_spiral_bevel_gear_set(self, design_entity: '_2107.SpiralBevelGearSet') -> 'Iterable[_6038.SpiralBevelGearSetCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.SpiralBevelGearSetCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2107.SpiralBevelGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6038.SpiralBevelGearSetCompoundDynamicAnalysis))

    def results_for_straight_bevel_diff_gear(self, design_entity: '_2108.StraightBevelDiffGear') -> 'Iterable[_6042.StraightBevelDiffGearCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.StraightBevelDiffGearCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2108.StraightBevelDiffGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6042.StraightBevelDiffGearCompoundDynamicAnalysis))

    def results_for_straight_bevel_diff_gear_set(self, design_entity: '_2109.StraightBevelDiffGearSet') -> 'Iterable[_6044.StraightBevelDiffGearSetCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.StraightBevelDiffGearSetCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2109.StraightBevelDiffGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6044.StraightBevelDiffGearSetCompoundDynamicAnalysis))

    def results_for_straight_bevel_gear(self, design_entity: '_2110.StraightBevelGear') -> 'Iterable[_6045.StraightBevelGearCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.StraightBevelGearCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2110.StraightBevelGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6045.StraightBevelGearCompoundDynamicAnalysis))

    def results_for_straight_bevel_gear_set(self, design_entity: '_2111.StraightBevelGearSet') -> 'Iterable[_6047.StraightBevelGearSetCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.StraightBevelGearSetCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2111.StraightBevelGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6047.StraightBevelGearSetCompoundDynamicAnalysis))

    def results_for_straight_bevel_planet_gear(self, design_entity: '_2112.StraightBevelPlanetGear') -> 'Iterable[_6048.StraightBevelPlanetGearCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.StraightBevelPlanetGearCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2112.StraightBevelPlanetGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6048.StraightBevelPlanetGearCompoundDynamicAnalysis))

    def results_for_straight_bevel_sun_gear(self, design_entity: '_2113.StraightBevelSunGear') -> 'Iterable[_6049.StraightBevelSunGearCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.StraightBevelSunGearCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2113.StraightBevelSunGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6049.StraightBevelSunGearCompoundDynamicAnalysis))

    def results_for_worm_gear(self, design_entity: '_2114.WormGear') -> 'Iterable[_6060.WormGearCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.WormGearCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2114.WormGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6060.WormGearCompoundDynamicAnalysis))

    def results_for_worm_gear_set(self, design_entity: '_2115.WormGearSet') -> 'Iterable[_6062.WormGearSetCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.WormGearSetCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2115.WormGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6062.WormGearSetCompoundDynamicAnalysis))

    def results_for_zerol_bevel_gear(self, design_entity: '_2116.ZerolBevelGear') -> 'Iterable[_6063.ZerolBevelGearCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ZerolBevelGearCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2116.ZerolBevelGear.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6063.ZerolBevelGearCompoundDynamicAnalysis))

    def results_for_zerol_bevel_gear_set(self, design_entity: '_2117.ZerolBevelGearSet') -> 'Iterable[_6065.ZerolBevelGearSetCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ZerolBevelGearSetCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2117.ZerolBevelGearSet.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6065.ZerolBevelGearSetCompoundDynamicAnalysis))

    def results_for_part_to_part_shear_coupling(self, design_entity: '_2146.PartToPartShearCoupling') -> 'Iterable[_6019.PartToPartShearCouplingCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCoupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.PartToPartShearCouplingCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2146.PartToPartShearCoupling.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6019.PartToPartShearCouplingCompoundDynamicAnalysis))

    def results_for_part_to_part_shear_coupling_half(self, design_entity: '_2147.PartToPartShearCouplingHalf') -> 'Iterable[_6021.PartToPartShearCouplingHalfCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.PartToPartShearCouplingHalfCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2147.PartToPartShearCouplingHalf.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6021.PartToPartShearCouplingHalfCompoundDynamicAnalysis))

    def results_for_belt_drive(self, design_entity: '_2135.BeltDrive') -> 'Iterable[_5953.BeltDriveCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.BeltDriveCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2135.BeltDrive.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5953.BeltDriveCompoundDynamicAnalysis))

    def results_for_clutch(self, design_entity: '_2137.Clutch') -> 'Iterable[_5964.ClutchCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ClutchCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2137.Clutch.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5964.ClutchCompoundDynamicAnalysis))

    def results_for_clutch_half(self, design_entity: '_2138.ClutchHalf') -> 'Iterable[_5966.ClutchHalfCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ClutchHalfCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2138.ClutchHalf.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5966.ClutchHalfCompoundDynamicAnalysis))

    def results_for_concept_coupling(self, design_entity: '_2140.ConceptCoupling') -> 'Iterable[_5969.ConceptCouplingCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ConceptCouplingCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2140.ConceptCoupling.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5969.ConceptCouplingCompoundDynamicAnalysis))

    def results_for_concept_coupling_half(self, design_entity: '_2141.ConceptCouplingHalf') -> 'Iterable[_5971.ConceptCouplingHalfCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ConceptCouplingHalfCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2141.ConceptCouplingHalf.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5971.ConceptCouplingHalfCompoundDynamicAnalysis))

    def results_for_coupling(self, design_entity: '_2142.Coupling') -> 'Iterable[_5980.CouplingCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.CouplingCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2142.Coupling.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5980.CouplingCompoundDynamicAnalysis))

    def results_for_coupling_half(self, design_entity: '_2143.CouplingHalf') -> 'Iterable[_5982.CouplingHalfCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.CouplingHalfCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2143.CouplingHalf.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5982.CouplingHalfCompoundDynamicAnalysis))

    def results_for_cvt(self, design_entity: '_2144.CVT') -> 'Iterable[_5984.CVTCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.CVTCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2144.CVT.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5984.CVTCompoundDynamicAnalysis))

    def results_for_cvt_pulley(self, design_entity: '_2145.CVTPulley') -> 'Iterable[_5985.CVTPulleyCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.CVTPulleyCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2145.CVTPulley.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5985.CVTPulleyCompoundDynamicAnalysis))

    def results_for_pulley(self, design_entity: '_2148.Pulley') -> 'Iterable[_6027.PulleyCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.PulleyCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2148.Pulley.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6027.PulleyCompoundDynamicAnalysis))

    def results_for_shaft_hub_connection(self, design_entity: '_2156.ShaftHubConnection') -> 'Iterable[_6033.ShaftHubConnectionCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ShaftHubConnectionCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2156.ShaftHubConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6033.ShaftHubConnectionCompoundDynamicAnalysis))

    def results_for_rolling_ring(self, design_entity: '_2154.RollingRing') -> 'Iterable[_6029.RollingRingCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.RollingRingCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2154.RollingRing.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6029.RollingRingCompoundDynamicAnalysis))

    def results_for_rolling_ring_assembly(self, design_entity: '_2155.RollingRingAssembly') -> 'Iterable[_6028.RollingRingAssemblyCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.RollingRingAssemblyCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2155.RollingRingAssembly.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6028.RollingRingAssemblyCompoundDynamicAnalysis))

    def results_for_spring_damper(self, design_entity: '_2157.SpringDamper') -> 'Iterable[_6039.SpringDamperCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.SpringDamperCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2157.SpringDamper.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6039.SpringDamperCompoundDynamicAnalysis))

    def results_for_spring_damper_half(self, design_entity: '_2158.SpringDamperHalf') -> 'Iterable[_6041.SpringDamperHalfCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.SpringDamperHalfCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2158.SpringDamperHalf.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6041.SpringDamperHalfCompoundDynamicAnalysis))

    def results_for_synchroniser(self, design_entity: '_2159.Synchroniser') -> 'Iterable[_6050.SynchroniserCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.SynchroniserCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2159.Synchroniser.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6050.SynchroniserCompoundDynamicAnalysis))

    def results_for_synchroniser_half(self, design_entity: '_2161.SynchroniserHalf') -> 'Iterable[_6051.SynchroniserHalfCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.SynchroniserHalfCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2161.SynchroniserHalf.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6051.SynchroniserHalfCompoundDynamicAnalysis))

    def results_for_synchroniser_part(self, design_entity: '_2162.SynchroniserPart') -> 'Iterable[_6052.SynchroniserPartCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.SynchroniserPartCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2162.SynchroniserPart.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6052.SynchroniserPartCompoundDynamicAnalysis))

    def results_for_synchroniser_sleeve(self, design_entity: '_2163.SynchroniserSleeve') -> 'Iterable[_6053.SynchroniserSleeveCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.SynchroniserSleeveCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2163.SynchroniserSleeve.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6053.SynchroniserSleeveCompoundDynamicAnalysis))

    def results_for_torque_converter(self, design_entity: '_2164.TorqueConverter') -> 'Iterable[_6054.TorqueConverterCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.TorqueConverterCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2164.TorqueConverter.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6054.TorqueConverterCompoundDynamicAnalysis))

    def results_for_torque_converter_pump(self, design_entity: '_2165.TorqueConverterPump') -> 'Iterable[_6056.TorqueConverterPumpCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.TorqueConverterPumpCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2165.TorqueConverterPump.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6056.TorqueConverterPumpCompoundDynamicAnalysis))

    def results_for_torque_converter_turbine(self, design_entity: '_2167.TorqueConverterTurbine') -> 'Iterable[_6057.TorqueConverterTurbineCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.TorqueConverterTurbineCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_2167.TorqueConverterTurbine.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6057.TorqueConverterTurbineCompoundDynamicAnalysis))

    def results_for_cvt_belt_connection(self, design_entity: '_1858.CVTBeltConnection') -> 'Iterable[_5983.CVTBeltConnectionCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.CVTBeltConnectionCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1858.CVTBeltConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5983.CVTBeltConnectionCompoundDynamicAnalysis))

    def results_for_belt_connection(self, design_entity: '_1853.BeltConnection') -> 'Iterable[_5952.BeltConnectionCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.BeltConnectionCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1853.BeltConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5952.BeltConnectionCompoundDynamicAnalysis))

    def results_for_coaxial_connection(self, design_entity: '_1854.CoaxialConnection') -> 'Iterable[_5967.CoaxialConnectionCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.CoaxialConnectionCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1854.CoaxialConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5967.CoaxialConnectionCompoundDynamicAnalysis))

    def results_for_connection(self, design_entity: '_1857.Connection') -> 'Iterable[_5978.ConnectionCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ConnectionCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1857.Connection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5978.ConnectionCompoundDynamicAnalysis))

    def results_for_inter_mountable_component_connection(self, design_entity: '_1866.InterMountableComponentConnection') -> 'Iterable[_6004.InterMountableComponentConnectionCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.InterMountableComponentConnectionCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1866.InterMountableComponentConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6004.InterMountableComponentConnectionCompoundDynamicAnalysis))

    def results_for_planetary_connection(self, design_entity: '_1869.PlanetaryConnection') -> 'Iterable[_6022.PlanetaryConnectionCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.PlanetaryConnectionCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1869.PlanetaryConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6022.PlanetaryConnectionCompoundDynamicAnalysis))

    def results_for_rolling_ring_connection(self, design_entity: '_1873.RollingRingConnection') -> 'Iterable[_6030.RollingRingConnectionCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.RollingRingConnectionCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1873.RollingRingConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6030.RollingRingConnectionCompoundDynamicAnalysis))

    def results_for_shaft_to_mountable_component_connection(self, design_entity: '_1877.ShaftToMountableComponentConnection') -> 'Iterable[_6034.ShaftToMountableComponentConnectionCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ShaftToMountableComponentConnectionCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1877.ShaftToMountableComponentConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6034.ShaftToMountableComponentConnectionCompoundDynamicAnalysis))

    def results_for_bevel_differential_gear_mesh(self, design_entity: '_1883.BevelDifferentialGearMesh') -> 'Iterable[_5955.BevelDifferentialGearMeshCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.BevelDifferentialGearMeshCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1883.BevelDifferentialGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5955.BevelDifferentialGearMeshCompoundDynamicAnalysis))

    def results_for_concept_gear_mesh(self, design_entity: '_1887.ConceptGearMesh') -> 'Iterable[_5973.ConceptGearMeshCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ConceptGearMeshCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1887.ConceptGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5973.ConceptGearMeshCompoundDynamicAnalysis))

    def results_for_face_gear_mesh(self, design_entity: '_1893.FaceGearMesh') -> 'Iterable[_5993.FaceGearMeshCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.FaceGearMeshCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1893.FaceGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5993.FaceGearMeshCompoundDynamicAnalysis))

    def results_for_straight_bevel_diff_gear_mesh(self, design_entity: '_1907.StraightBevelDiffGearMesh') -> 'Iterable[_6043.StraightBevelDiffGearMeshCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.StraightBevelDiffGearMeshCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1907.StraightBevelDiffGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6043.StraightBevelDiffGearMeshCompoundDynamicAnalysis))

    def results_for_bevel_gear_mesh(self, design_entity: '_1885.BevelGearMesh') -> 'Iterable[_5960.BevelGearMeshCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.BevelGearMeshCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1885.BevelGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5960.BevelGearMeshCompoundDynamicAnalysis))

    def results_for_conical_gear_mesh(self, design_entity: '_1889.ConicalGearMesh') -> 'Iterable[_5976.ConicalGearMeshCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ConicalGearMeshCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1889.ConicalGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5976.ConicalGearMeshCompoundDynamicAnalysis))

    def results_for_agma_gleason_conical_gear_mesh(self, design_entity: '_1881.AGMAGleasonConicalGearMesh') -> 'Iterable[_5948.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1881.AGMAGleasonConicalGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5948.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis))

    def results_for_cylindrical_gear_mesh(self, design_entity: '_1891.CylindricalGearMesh') -> 'Iterable[_5987.CylindricalGearMeshCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.CylindricalGearMeshCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1891.CylindricalGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5987.CylindricalGearMeshCompoundDynamicAnalysis))

    def results_for_hypoid_gear_mesh(self, design_entity: '_1897.HypoidGearMesh') -> 'Iterable[_6001.HypoidGearMeshCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.HypoidGearMeshCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1897.HypoidGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6001.HypoidGearMeshCompoundDynamicAnalysis))

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(self, design_entity: '_1900.KlingelnbergCycloPalloidConicalGearMesh') -> 'Iterable[_6006.KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1900.KlingelnbergCycloPalloidConicalGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6006.KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self, design_entity: '_1901.KlingelnbergCycloPalloidHypoidGearMesh') -> 'Iterable[_6009.KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1901.KlingelnbergCycloPalloidHypoidGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6009.KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self, design_entity: '_1902.KlingelnbergCycloPalloidSpiralBevelGearMesh') -> 'Iterable[_6012.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1902.KlingelnbergCycloPalloidSpiralBevelGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6012.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis))

    def results_for_spiral_bevel_gear_mesh(self, design_entity: '_1905.SpiralBevelGearMesh') -> 'Iterable[_6037.SpiralBevelGearMeshCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.SpiralBevelGearMeshCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1905.SpiralBevelGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6037.SpiralBevelGearMeshCompoundDynamicAnalysis))

    def results_for_straight_bevel_gear_mesh(self, design_entity: '_1909.StraightBevelGearMesh') -> 'Iterable[_6046.StraightBevelGearMeshCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.StraightBevelGearMeshCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1909.StraightBevelGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6046.StraightBevelGearMeshCompoundDynamicAnalysis))

    def results_for_worm_gear_mesh(self, design_entity: '_1911.WormGearMesh') -> 'Iterable[_6061.WormGearMeshCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.WormGearMeshCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1911.WormGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6061.WormGearMeshCompoundDynamicAnalysis))

    def results_for_zerol_bevel_gear_mesh(self, design_entity: '_1913.ZerolBevelGearMesh') -> 'Iterable[_6064.ZerolBevelGearMeshCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ZerolBevelGearMeshCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1913.ZerolBevelGearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6064.ZerolBevelGearMeshCompoundDynamicAnalysis))

    def results_for_gear_mesh(self, design_entity: '_1895.GearMesh') -> 'Iterable[_5997.GearMeshCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.GearMeshCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1895.GearMesh.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5997.GearMeshCompoundDynamicAnalysis))

    def results_for_part_to_part_shear_coupling_connection(self, design_entity: '_1921.PartToPartShearCouplingConnection') -> 'Iterable[_6020.PartToPartShearCouplingConnectionCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.PartToPartShearCouplingConnectionCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1921.PartToPartShearCouplingConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6020.PartToPartShearCouplingConnectionCompoundDynamicAnalysis))

    def results_for_clutch_connection(self, design_entity: '_1915.ClutchConnection') -> 'Iterable[_5965.ClutchConnectionCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ClutchConnectionCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1915.ClutchConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5965.ClutchConnectionCompoundDynamicAnalysis))

    def results_for_concept_coupling_connection(self, design_entity: '_1917.ConceptCouplingConnection') -> 'Iterable[_5970.ConceptCouplingConnectionCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ConceptCouplingConnectionCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1917.ConceptCouplingConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5970.ConceptCouplingConnectionCompoundDynamicAnalysis))

    def results_for_coupling_connection(self, design_entity: '_1919.CouplingConnection') -> 'Iterable[_5981.CouplingConnectionCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.CouplingConnectionCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1919.CouplingConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_5981.CouplingConnectionCompoundDynamicAnalysis))

    def results_for_spring_damper_connection(self, design_entity: '_1923.SpringDamperConnection') -> 'Iterable[_6040.SpringDamperConnectionCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.SpringDamperConnectionCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1923.SpringDamperConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6040.SpringDamperConnectionCompoundDynamicAnalysis))

    def results_for_torque_converter_connection(self, design_entity: '_1925.TorqueConverterConnection') -> 'Iterable[_6055.TorqueConverterConnectionCompoundDynamicAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.TorqueConverterConnectionCompoundDynamicAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor.Overloads[_1925.TorqueConverterConnection.TYPE](design_entity.wrapped if design_entity else None), constructor.new(_6055.TorqueConverterConnectionCompoundDynamicAnalysis))
