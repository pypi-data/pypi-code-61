'''_5509.py

PartSingleMeshWhineAnalysis
'''


from mastapy.system_model.part_model import (
    _2033, _2002, _2003, _2004,
    _2007, _2009, _2010, _2011,
    _2014, _2015, _2018, _2019,
    _2020, _2023, _2027, _2028,
    _2029, _2031, _2034, _2036,
    _2037, _2039, _2041, _2042,
    _2043
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.part_model.shaft_model import _2046
from mastapy.system_model.part_model.gears import (
    _2076, _2077, _2078, _2079,
    _2080, _2081, _2082, _2083,
    _2084, _2085, _2086, _2087,
    _2088, _2089, _2090, _2091,
    _2092, _2093, _2095, _2097,
    _2098, _2099, _2100, _2101,
    _2102, _2103, _2104, _2105,
    _2106, _2107, _2108, _2109,
    _2110, _2111, _2112, _2113,
    _2114, _2115, _2116, _2117
)
from mastapy.system_model.part_model.couplings import (
    _2135, _2137, _2138, _2140,
    _2141, _2142, _2143, _2144,
    _2145, _2146, _2147, _2148,
    _2154, _2155, _2156, _2157,
    _2158, _2159, _2161, _2162,
    _2163, _2164, _2165, _2167
)
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses import _5526
from mastapy.system_model.analyses_and_results.modal_analyses import (
    _4803, _4723, _4724, _4726,
    _4727, _4728, _4729, _4731,
    _4733, _4734, _4735, _4736,
    _4738, _4739, _4740, _4741,
    _4743, _4744, _4746, _4748,
    _4749, _4751, _4752, _4754,
    _4755, _4757, _4760, _4761,
    _4763, _4764, _4766, _4767,
    _4768, _4769, _4770, _4772,
    _4773, _4774, _4777, _4778,
    _4779, _4781, _4782, _4783,
    _4786, _4787, _4789, _4790,
    _4792, _4793, _4794, _4795,
    _4800, _4801, _4805, _4806,
    _4808, _4809, _4810, _4811,
    _4812, _4813, _4815, _4816,
    _4817, _4818, _4821, _4823,
    _4824, _4826, _4827, _4829,
    _4830, _4832, _4833, _4834,
    _4835, _4836, _4837, _4838,
    _4839, _4841, _4842, _4843,
    _4844, _4845, _4852, _4853,
    _4855, _4856
)
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5350
from mastapy.system_model.analyses_and_results.analysis_cases import _6522
from mastapy._internal.python_net import python_net_import

_PART_SINGLE_MESH_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.SingleMeshWhineAnalyses', 'PartSingleMeshWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PartSingleMeshWhineAnalysis',)


class PartSingleMeshWhineAnalysis(_6522.PartStaticLoadAnalysisCase):
    '''PartSingleMeshWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _PART_SINGLE_MESH_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PartSingleMeshWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2033.Part':
        '''Part: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2033.Part)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_assembly(self) -> '_2002.Assembly':
        '''Assembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2002.Assembly.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Assembly. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2002.Assembly)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_abstract_assembly(self) -> '_2003.AbstractAssembly':
        '''AbstractAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2003.AbstractAssembly.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to AbstractAssembly. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2003.AbstractAssembly)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_abstract_shaft_or_housing(self) -> '_2004.AbstractShaftOrHousing':
        '''AbstractShaftOrHousing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2004.AbstractShaftOrHousing.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to AbstractShaftOrHousing. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2004.AbstractShaftOrHousing)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_bearing(self) -> '_2007.Bearing':
        '''Bearing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2007.Bearing.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Bearing. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2007.Bearing)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_bolt(self) -> '_2009.Bolt':
        '''Bolt: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2009.Bolt.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Bolt. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2009.Bolt)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_bolted_joint(self) -> '_2010.BoltedJoint':
        '''BoltedJoint: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2010.BoltedJoint.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to BoltedJoint. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2010.BoltedJoint)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_component(self) -> '_2011.Component':
        '''Component: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2011.Component.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Component. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2011.Component)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_connector(self) -> '_2014.Connector':
        '''Connector: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2014.Connector.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Connector. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2014.Connector)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_datum(self) -> '_2015.Datum':
        '''Datum: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2015.Datum.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Datum. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2015.Datum)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_external_cad_model(self) -> '_2018.ExternalCADModel':
        '''ExternalCADModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2018.ExternalCADModel.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ExternalCADModel. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2018.ExternalCADModel)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_flexible_pin_assembly(self) -> '_2019.FlexiblePinAssembly':
        '''FlexiblePinAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2019.FlexiblePinAssembly.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to FlexiblePinAssembly. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2019.FlexiblePinAssembly)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_guide_dxf_model(self) -> '_2020.GuideDxfModel':
        '''GuideDxfModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2020.GuideDxfModel.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to GuideDxfModel. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2020.GuideDxfModel)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_imported_fe_component(self) -> '_2023.ImportedFEComponent':
        '''ImportedFEComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2023.ImportedFEComponent.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ImportedFEComponent. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2023.ImportedFEComponent)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_mass_disc(self) -> '_2027.MassDisc':
        '''MassDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2027.MassDisc.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to MassDisc. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2027.MassDisc)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_measurement_component(self) -> '_2028.MeasurementComponent':
        '''MeasurementComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2028.MeasurementComponent.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to MeasurementComponent. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2028.MeasurementComponent)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_mountable_component(self) -> '_2029.MountableComponent':
        '''MountableComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2029.MountableComponent.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to MountableComponent. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2029.MountableComponent)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_oil_seal(self) -> '_2031.OilSeal':
        '''OilSeal: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2031.OilSeal.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to OilSeal. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2031.OilSeal)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_planet_carrier(self) -> '_2034.PlanetCarrier':
        '''PlanetCarrier: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2034.PlanetCarrier.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to PlanetCarrier. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2034.PlanetCarrier)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_point_load(self) -> '_2036.PointLoad':
        '''PointLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2036.PointLoad.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to PointLoad. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2036.PointLoad)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_power_load(self) -> '_2037.PowerLoad':
        '''PowerLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2037.PowerLoad.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to PowerLoad. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2037.PowerLoad)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_root_assembly(self) -> '_2039.RootAssembly':
        '''RootAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2039.RootAssembly.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to RootAssembly. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2039.RootAssembly)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_specialised_assembly(self) -> '_2041.SpecialisedAssembly':
        '''SpecialisedAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2041.SpecialisedAssembly.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to SpecialisedAssembly. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2041.SpecialisedAssembly)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_unbalanced_mass(self) -> '_2042.UnbalancedMass':
        '''UnbalancedMass: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2042.UnbalancedMass.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to UnbalancedMass. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2042.UnbalancedMass)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_virtual_component(self) -> '_2043.VirtualComponent':
        '''VirtualComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2043.VirtualComponent.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to VirtualComponent. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2043.VirtualComponent)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_shaft(self) -> '_2046.Shaft':
        '''Shaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2046.Shaft.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Shaft. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2046.Shaft)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_agma_gleason_conical_gear(self) -> '_2076.AGMAGleasonConicalGear':
        '''AGMAGleasonConicalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2076.AGMAGleasonConicalGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to AGMAGleasonConicalGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2076.AGMAGleasonConicalGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_agma_gleason_conical_gear_set(self) -> '_2077.AGMAGleasonConicalGearSet':
        '''AGMAGleasonConicalGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2077.AGMAGleasonConicalGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to AGMAGleasonConicalGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2077.AGMAGleasonConicalGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_bevel_differential_gear(self) -> '_2078.BevelDifferentialGear':
        '''BevelDifferentialGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2078.BevelDifferentialGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelDifferentialGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2078.BevelDifferentialGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_bevel_differential_gear_set(self) -> '_2079.BevelDifferentialGearSet':
        '''BevelDifferentialGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2079.BevelDifferentialGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelDifferentialGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2079.BevelDifferentialGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_bevel_differential_planet_gear(self) -> '_2080.BevelDifferentialPlanetGear':
        '''BevelDifferentialPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2080.BevelDifferentialPlanetGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelDifferentialPlanetGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2080.BevelDifferentialPlanetGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_bevel_differential_sun_gear(self) -> '_2081.BevelDifferentialSunGear':
        '''BevelDifferentialSunGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2081.BevelDifferentialSunGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelDifferentialSunGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2081.BevelDifferentialSunGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_bevel_gear(self) -> '_2082.BevelGear':
        '''BevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2082.BevelGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2082.BevelGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_bevel_gear_set(self) -> '_2083.BevelGearSet':
        '''BevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2083.BevelGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2083.BevelGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_concept_gear(self) -> '_2084.ConceptGear':
        '''ConceptGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2084.ConceptGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ConceptGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2084.ConceptGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_concept_gear_set(self) -> '_2085.ConceptGearSet':
        '''ConceptGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2085.ConceptGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ConceptGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2085.ConceptGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_conical_gear(self) -> '_2086.ConicalGear':
        '''ConicalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2086.ConicalGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ConicalGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2086.ConicalGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_conical_gear_set(self) -> '_2087.ConicalGearSet':
        '''ConicalGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2087.ConicalGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ConicalGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2087.ConicalGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_cylindrical_gear(self) -> '_2088.CylindricalGear':
        '''CylindricalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2088.CylindricalGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to CylindricalGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2088.CylindricalGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_cylindrical_gear_set(self) -> '_2089.CylindricalGearSet':
        '''CylindricalGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2089.CylindricalGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to CylindricalGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2089.CylindricalGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_cylindrical_planet_gear(self) -> '_2090.CylindricalPlanetGear':
        '''CylindricalPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2090.CylindricalPlanetGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to CylindricalPlanetGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2090.CylindricalPlanetGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_face_gear(self) -> '_2091.FaceGear':
        '''FaceGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2091.FaceGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to FaceGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2091.FaceGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_face_gear_set(self) -> '_2092.FaceGearSet':
        '''FaceGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2092.FaceGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to FaceGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2092.FaceGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_gear(self) -> '_2093.Gear':
        '''Gear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2093.Gear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Gear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2093.Gear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_gear_set(self) -> '_2095.GearSet':
        '''GearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2095.GearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to GearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2095.GearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_hypoid_gear(self) -> '_2097.HypoidGear':
        '''HypoidGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2097.HypoidGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to HypoidGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2097.HypoidGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_hypoid_gear_set(self) -> '_2098.HypoidGearSet':
        '''HypoidGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2098.HypoidGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to HypoidGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2098.HypoidGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_klingelnberg_cyclo_palloid_conical_gear(self) -> '_2099.KlingelnbergCycloPalloidConicalGear':
        '''KlingelnbergCycloPalloidConicalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2099.KlingelnbergCycloPalloidConicalGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to KlingelnbergCycloPalloidConicalGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2099.KlingelnbergCycloPalloidConicalGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_klingelnberg_cyclo_palloid_conical_gear_set(self) -> '_2100.KlingelnbergCycloPalloidConicalGearSet':
        '''KlingelnbergCycloPalloidConicalGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2100.KlingelnbergCycloPalloidConicalGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to KlingelnbergCycloPalloidConicalGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2100.KlingelnbergCycloPalloidConicalGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear(self) -> '_2101.KlingelnbergCycloPalloidHypoidGear':
        '''KlingelnbergCycloPalloidHypoidGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2101.KlingelnbergCycloPalloidHypoidGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to KlingelnbergCycloPalloidHypoidGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2101.KlingelnbergCycloPalloidHypoidGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set(self) -> '_2102.KlingelnbergCycloPalloidHypoidGearSet':
        '''KlingelnbergCycloPalloidHypoidGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2102.KlingelnbergCycloPalloidHypoidGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to KlingelnbergCycloPalloidHypoidGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2102.KlingelnbergCycloPalloidHypoidGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear(self) -> '_2103.KlingelnbergCycloPalloidSpiralBevelGear':
        '''KlingelnbergCycloPalloidSpiralBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2103.KlingelnbergCycloPalloidSpiralBevelGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to KlingelnbergCycloPalloidSpiralBevelGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2103.KlingelnbergCycloPalloidSpiralBevelGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self) -> '_2104.KlingelnbergCycloPalloidSpiralBevelGearSet':
        '''KlingelnbergCycloPalloidSpiralBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2104.KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to KlingelnbergCycloPalloidSpiralBevelGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2104.KlingelnbergCycloPalloidSpiralBevelGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_planetary_gear_set(self) -> '_2105.PlanetaryGearSet':
        '''PlanetaryGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2105.PlanetaryGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to PlanetaryGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2105.PlanetaryGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_spiral_bevel_gear(self) -> '_2106.SpiralBevelGear':
        '''SpiralBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2106.SpiralBevelGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to SpiralBevelGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2106.SpiralBevelGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_spiral_bevel_gear_set(self) -> '_2107.SpiralBevelGearSet':
        '''SpiralBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2107.SpiralBevelGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to SpiralBevelGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2107.SpiralBevelGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_straight_bevel_diff_gear(self) -> '_2108.StraightBevelDiffGear':
        '''StraightBevelDiffGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2108.StraightBevelDiffGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to StraightBevelDiffGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2108.StraightBevelDiffGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_straight_bevel_diff_gear_set(self) -> '_2109.StraightBevelDiffGearSet':
        '''StraightBevelDiffGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2109.StraightBevelDiffGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to StraightBevelDiffGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2109.StraightBevelDiffGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_straight_bevel_gear(self) -> '_2110.StraightBevelGear':
        '''StraightBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2110.StraightBevelGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to StraightBevelGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2110.StraightBevelGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_straight_bevel_gear_set(self) -> '_2111.StraightBevelGearSet':
        '''StraightBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2111.StraightBevelGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to StraightBevelGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2111.StraightBevelGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_straight_bevel_planet_gear(self) -> '_2112.StraightBevelPlanetGear':
        '''StraightBevelPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2112.StraightBevelPlanetGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to StraightBevelPlanetGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2112.StraightBevelPlanetGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_straight_bevel_sun_gear(self) -> '_2113.StraightBevelSunGear':
        '''StraightBevelSunGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2113.StraightBevelSunGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to StraightBevelSunGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2113.StraightBevelSunGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_worm_gear(self) -> '_2114.WormGear':
        '''WormGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2114.WormGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to WormGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2114.WormGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_worm_gear_set(self) -> '_2115.WormGearSet':
        '''WormGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2115.WormGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to WormGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2115.WormGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_zerol_bevel_gear(self) -> '_2116.ZerolBevelGear':
        '''ZerolBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2116.ZerolBevelGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ZerolBevelGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2116.ZerolBevelGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_zerol_bevel_gear_set(self) -> '_2117.ZerolBevelGearSet':
        '''ZerolBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2117.ZerolBevelGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ZerolBevelGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2117.ZerolBevelGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_belt_drive(self) -> '_2135.BeltDrive':
        '''BeltDrive: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2135.BeltDrive.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to BeltDrive. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2135.BeltDrive)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_clutch(self) -> '_2137.Clutch':
        '''Clutch: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2137.Clutch.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Clutch. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2137.Clutch)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_clutch_half(self) -> '_2138.ClutchHalf':
        '''ClutchHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2138.ClutchHalf.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ClutchHalf. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2138.ClutchHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_concept_coupling(self) -> '_2140.ConceptCoupling':
        '''ConceptCoupling: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2140.ConceptCoupling.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ConceptCoupling. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2140.ConceptCoupling)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_concept_coupling_half(self) -> '_2141.ConceptCouplingHalf':
        '''ConceptCouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2141.ConceptCouplingHalf.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ConceptCouplingHalf. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2141.ConceptCouplingHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_coupling(self) -> '_2142.Coupling':
        '''Coupling: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2142.Coupling.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Coupling. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2142.Coupling)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_coupling_half(self) -> '_2143.CouplingHalf':
        '''CouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2143.CouplingHalf.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to CouplingHalf. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2143.CouplingHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_cvt(self) -> '_2144.CVT':
        '''CVT: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2144.CVT.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to CVT. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2144.CVT)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_cvt_pulley(self) -> '_2145.CVTPulley':
        '''CVTPulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2145.CVTPulley.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to CVTPulley. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2145.CVTPulley)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_part_to_part_shear_coupling(self) -> '_2146.PartToPartShearCoupling':
        '''PartToPartShearCoupling: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2146.PartToPartShearCoupling.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to PartToPartShearCoupling. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2146.PartToPartShearCoupling)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_part_to_part_shear_coupling_half(self) -> '_2147.PartToPartShearCouplingHalf':
        '''PartToPartShearCouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2147.PartToPartShearCouplingHalf.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to PartToPartShearCouplingHalf. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2147.PartToPartShearCouplingHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_pulley(self) -> '_2148.Pulley':
        '''Pulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2148.Pulley.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Pulley. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2148.Pulley)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_rolling_ring(self) -> '_2154.RollingRing':
        '''RollingRing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2154.RollingRing.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to RollingRing. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2154.RollingRing)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_rolling_ring_assembly(self) -> '_2155.RollingRingAssembly':
        '''RollingRingAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2155.RollingRingAssembly.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to RollingRingAssembly. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2155.RollingRingAssembly)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_shaft_hub_connection(self) -> '_2156.ShaftHubConnection':
        '''ShaftHubConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2156.ShaftHubConnection.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ShaftHubConnection. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2156.ShaftHubConnection)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_spring_damper(self) -> '_2157.SpringDamper':
        '''SpringDamper: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2157.SpringDamper.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to SpringDamper. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2157.SpringDamper)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_spring_damper_half(self) -> '_2158.SpringDamperHalf':
        '''SpringDamperHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2158.SpringDamperHalf.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to SpringDamperHalf. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2158.SpringDamperHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_synchroniser(self) -> '_2159.Synchroniser':
        '''Synchroniser: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2159.Synchroniser.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Synchroniser. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2159.Synchroniser)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_synchroniser_half(self) -> '_2161.SynchroniserHalf':
        '''SynchroniserHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2161.SynchroniserHalf.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to SynchroniserHalf. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2161.SynchroniserHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_synchroniser_part(self) -> '_2162.SynchroniserPart':
        '''SynchroniserPart: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2162.SynchroniserPart.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to SynchroniserPart. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2162.SynchroniserPart)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_synchroniser_sleeve(self) -> '_2163.SynchroniserSleeve':
        '''SynchroniserSleeve: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2163.SynchroniserSleeve.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to SynchroniserSleeve. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2163.SynchroniserSleeve)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_torque_converter(self) -> '_2164.TorqueConverter':
        '''TorqueConverter: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2164.TorqueConverter.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to TorqueConverter. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2164.TorqueConverter)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_torque_converter_pump(self) -> '_2165.TorqueConverterPump':
        '''TorqueConverterPump: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2165.TorqueConverterPump.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to TorqueConverterPump. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2165.TorqueConverterPump)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_torque_converter_turbine(self) -> '_2167.TorqueConverterTurbine':
        '''TorqueConverterTurbine: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2167.TorqueConverterTurbine.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to TorqueConverterTurbine. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2167.TorqueConverterTurbine)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def single_mesh_whine_analysis(self) -> '_5526.SingleMeshWhineAnalysis':
        '''SingleMeshWhineAnalysis: 'SingleMeshWhineAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5526.SingleMeshWhineAnalysis)(self.wrapped.SingleMeshWhineAnalysis) if self.wrapped.SingleMeshWhineAnalysis else None

    @property
    def uncoupled_modal_analysis(self) -> '_4803.PartModalAnalysis':
        '''PartModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_4803.PartModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_abstract_assembly_modal_analysis(self) -> '_4723.AbstractAssemblyModalAnalysis':
        '''AbstractAssemblyModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4723.AbstractAssemblyModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to AbstractAssemblyModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4723.AbstractAssemblyModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_abstract_shaft_or_housing_modal_analysis(self) -> '_4724.AbstractShaftOrHousingModalAnalysis':
        '''AbstractShaftOrHousingModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4724.AbstractShaftOrHousingModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to AbstractShaftOrHousingModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4724.AbstractShaftOrHousingModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_agma_gleason_conical_gear_modal_analysis(self) -> '_4726.AGMAGleasonConicalGearModalAnalysis':
        '''AGMAGleasonConicalGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4726.AGMAGleasonConicalGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to AGMAGleasonConicalGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4726.AGMAGleasonConicalGearModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_agma_gleason_conical_gear_set_modal_analysis(self) -> '_4727.AGMAGleasonConicalGearSetModalAnalysis':
        '''AGMAGleasonConicalGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4727.AGMAGleasonConicalGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to AGMAGleasonConicalGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4727.AGMAGleasonConicalGearSetModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_assembly_modal_analysis(self) -> '_4728.AssemblyModalAnalysis':
        '''AssemblyModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4728.AssemblyModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to AssemblyModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4728.AssemblyModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_bearing_modal_analysis(self) -> '_4729.BearingModalAnalysis':
        '''BearingModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4729.BearingModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to BearingModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4729.BearingModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_belt_drive_modal_analysis(self) -> '_4731.BeltDriveModalAnalysis':
        '''BeltDriveModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4731.BeltDriveModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to BeltDriveModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4731.BeltDriveModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_bevel_differential_gear_modal_analysis(self) -> '_4733.BevelDifferentialGearModalAnalysis':
        '''BevelDifferentialGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4733.BevelDifferentialGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to BevelDifferentialGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4733.BevelDifferentialGearModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_bevel_differential_gear_set_modal_analysis(self) -> '_4734.BevelDifferentialGearSetModalAnalysis':
        '''BevelDifferentialGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4734.BevelDifferentialGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to BevelDifferentialGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4734.BevelDifferentialGearSetModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_bevel_differential_planet_gear_modal_analysis(self) -> '_4735.BevelDifferentialPlanetGearModalAnalysis':
        '''BevelDifferentialPlanetGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4735.BevelDifferentialPlanetGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to BevelDifferentialPlanetGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4735.BevelDifferentialPlanetGearModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_bevel_differential_sun_gear_modal_analysis(self) -> '_4736.BevelDifferentialSunGearModalAnalysis':
        '''BevelDifferentialSunGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4736.BevelDifferentialSunGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to BevelDifferentialSunGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4736.BevelDifferentialSunGearModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_bevel_gear_modal_analysis(self) -> '_4738.BevelGearModalAnalysis':
        '''BevelGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4738.BevelGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to BevelGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4738.BevelGearModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_bevel_gear_set_modal_analysis(self) -> '_4739.BevelGearSetModalAnalysis':
        '''BevelGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4739.BevelGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to BevelGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4739.BevelGearSetModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_bolted_joint_modal_analysis(self) -> '_4740.BoltedJointModalAnalysis':
        '''BoltedJointModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4740.BoltedJointModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to BoltedJointModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4740.BoltedJointModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_bolt_modal_analysis(self) -> '_4741.BoltModalAnalysis':
        '''BoltModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4741.BoltModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to BoltModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4741.BoltModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_clutch_half_modal_analysis(self) -> '_4743.ClutchHalfModalAnalysis':
        '''ClutchHalfModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4743.ClutchHalfModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ClutchHalfModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4743.ClutchHalfModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_clutch_modal_analysis(self) -> '_4744.ClutchModalAnalysis':
        '''ClutchModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4744.ClutchModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ClutchModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4744.ClutchModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_component_modal_analysis(self) -> '_4746.ComponentModalAnalysis':
        '''ComponentModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4746.ComponentModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ComponentModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4746.ComponentModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_concept_coupling_half_modal_analysis(self) -> '_4748.ConceptCouplingHalfModalAnalysis':
        '''ConceptCouplingHalfModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4748.ConceptCouplingHalfModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ConceptCouplingHalfModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4748.ConceptCouplingHalfModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_concept_coupling_modal_analysis(self) -> '_4749.ConceptCouplingModalAnalysis':
        '''ConceptCouplingModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4749.ConceptCouplingModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ConceptCouplingModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4749.ConceptCouplingModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_concept_gear_modal_analysis(self) -> '_4751.ConceptGearModalAnalysis':
        '''ConceptGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4751.ConceptGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ConceptGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4751.ConceptGearModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_concept_gear_set_modal_analysis(self) -> '_4752.ConceptGearSetModalAnalysis':
        '''ConceptGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4752.ConceptGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ConceptGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4752.ConceptGearSetModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_conical_gear_modal_analysis(self) -> '_4754.ConicalGearModalAnalysis':
        '''ConicalGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4754.ConicalGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ConicalGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4754.ConicalGearModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_conical_gear_set_modal_analysis(self) -> '_4755.ConicalGearSetModalAnalysis':
        '''ConicalGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4755.ConicalGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ConicalGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4755.ConicalGearSetModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_connector_modal_analysis(self) -> '_4757.ConnectorModalAnalysis':
        '''ConnectorModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4757.ConnectorModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ConnectorModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4757.ConnectorModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_coupling_half_modal_analysis(self) -> '_4760.CouplingHalfModalAnalysis':
        '''CouplingHalfModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4760.CouplingHalfModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to CouplingHalfModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4760.CouplingHalfModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_coupling_modal_analysis(self) -> '_4761.CouplingModalAnalysis':
        '''CouplingModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4761.CouplingModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to CouplingModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4761.CouplingModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_cvt_modal_analysis(self) -> '_4763.CVTModalAnalysis':
        '''CVTModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4763.CVTModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to CVTModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4763.CVTModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_cvt_pulley_modal_analysis(self) -> '_4764.CVTPulleyModalAnalysis':
        '''CVTPulleyModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4764.CVTPulleyModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to CVTPulleyModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4764.CVTPulleyModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_cylindrical_gear_modal_analysis(self) -> '_4766.CylindricalGearModalAnalysis':
        '''CylindricalGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4766.CylindricalGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to CylindricalGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4766.CylindricalGearModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_cylindrical_gear_set_modal_analysis(self) -> '_4767.CylindricalGearSetModalAnalysis':
        '''CylindricalGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4767.CylindricalGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to CylindricalGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4767.CylindricalGearSetModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_cylindrical_planet_gear_modal_analysis(self) -> '_4768.CylindricalPlanetGearModalAnalysis':
        '''CylindricalPlanetGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4768.CylindricalPlanetGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to CylindricalPlanetGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4768.CylindricalPlanetGearModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_datum_modal_analysis(self) -> '_4769.DatumModalAnalysis':
        '''DatumModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4769.DatumModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to DatumModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4769.DatumModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_external_cad_model_modal_analysis(self) -> '_4770.ExternalCADModelModalAnalysis':
        '''ExternalCADModelModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4770.ExternalCADModelModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ExternalCADModelModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4770.ExternalCADModelModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_face_gear_modal_analysis(self) -> '_4772.FaceGearModalAnalysis':
        '''FaceGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4772.FaceGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to FaceGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4772.FaceGearModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_face_gear_set_modal_analysis(self) -> '_4773.FaceGearSetModalAnalysis':
        '''FaceGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4773.FaceGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to FaceGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4773.FaceGearSetModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_flexible_pin_assembly_modal_analysis(self) -> '_4774.FlexiblePinAssemblyModalAnalysis':
        '''FlexiblePinAssemblyModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4774.FlexiblePinAssemblyModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to FlexiblePinAssemblyModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4774.FlexiblePinAssemblyModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_gear_modal_analysis(self) -> '_4777.GearModalAnalysis':
        '''GearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4777.GearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to GearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4777.GearModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_gear_set_modal_analysis(self) -> '_4778.GearSetModalAnalysis':
        '''GearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4778.GearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to GearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4778.GearSetModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_guide_dxf_model_modal_analysis(self) -> '_4779.GuideDxfModelModalAnalysis':
        '''GuideDxfModelModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4779.GuideDxfModelModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to GuideDxfModelModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4779.GuideDxfModelModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_hypoid_gear_modal_analysis(self) -> '_4781.HypoidGearModalAnalysis':
        '''HypoidGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4781.HypoidGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to HypoidGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4781.HypoidGearModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_hypoid_gear_set_modal_analysis(self) -> '_4782.HypoidGearSetModalAnalysis':
        '''HypoidGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4782.HypoidGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to HypoidGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4782.HypoidGearSetModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_imported_fe_component_modal_analysis(self) -> '_4783.ImportedFEComponentModalAnalysis':
        '''ImportedFEComponentModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4783.ImportedFEComponentModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ImportedFEComponentModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4783.ImportedFEComponentModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_klingelnberg_cyclo_palloid_conical_gear_modal_analysis(self) -> '_4786.KlingelnbergCycloPalloidConicalGearModalAnalysis':
        '''KlingelnbergCycloPalloidConicalGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4786.KlingelnbergCycloPalloidConicalGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to KlingelnbergCycloPalloidConicalGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4786.KlingelnbergCycloPalloidConicalGearModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis(self) -> '_4787.KlingelnbergCycloPalloidConicalGearSetModalAnalysis':
        '''KlingelnbergCycloPalloidConicalGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4787.KlingelnbergCycloPalloidConicalGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to KlingelnbergCycloPalloidConicalGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4787.KlingelnbergCycloPalloidConicalGearSetModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis(self) -> '_4789.KlingelnbergCycloPalloidHypoidGearModalAnalysis':
        '''KlingelnbergCycloPalloidHypoidGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4789.KlingelnbergCycloPalloidHypoidGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to KlingelnbergCycloPalloidHypoidGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4789.KlingelnbergCycloPalloidHypoidGearModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis(self) -> '_4790.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis':
        '''KlingelnbergCycloPalloidHypoidGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4790.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to KlingelnbergCycloPalloidHypoidGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4790.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis(self) -> '_4792.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis':
        '''KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4792.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4792.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis(self) -> '_4793.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis':
        '''KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4793.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4793.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_mass_disc_modal_analysis(self) -> '_4794.MassDiscModalAnalysis':
        '''MassDiscModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4794.MassDiscModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to MassDiscModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4794.MassDiscModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_measurement_component_modal_analysis(self) -> '_4795.MeasurementComponentModalAnalysis':
        '''MeasurementComponentModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4795.MeasurementComponentModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to MeasurementComponentModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4795.MeasurementComponentModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_mountable_component_modal_analysis(self) -> '_4800.MountableComponentModalAnalysis':
        '''MountableComponentModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4800.MountableComponentModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to MountableComponentModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4800.MountableComponentModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_oil_seal_modal_analysis(self) -> '_4801.OilSealModalAnalysis':
        '''OilSealModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4801.OilSealModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to OilSealModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4801.OilSealModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_part_to_part_shear_coupling_half_modal_analysis(self) -> '_4805.PartToPartShearCouplingHalfModalAnalysis':
        '''PartToPartShearCouplingHalfModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4805.PartToPartShearCouplingHalfModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to PartToPartShearCouplingHalfModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4805.PartToPartShearCouplingHalfModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_part_to_part_shear_coupling_modal_analysis(self) -> '_4806.PartToPartShearCouplingModalAnalysis':
        '''PartToPartShearCouplingModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4806.PartToPartShearCouplingModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to PartToPartShearCouplingModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4806.PartToPartShearCouplingModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_planetary_gear_set_modal_analysis(self) -> '_4808.PlanetaryGearSetModalAnalysis':
        '''PlanetaryGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4808.PlanetaryGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to PlanetaryGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4808.PlanetaryGearSetModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_planet_carrier_modal_analysis(self) -> '_4809.PlanetCarrierModalAnalysis':
        '''PlanetCarrierModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4809.PlanetCarrierModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to PlanetCarrierModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4809.PlanetCarrierModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_point_load_modal_analysis(self) -> '_4810.PointLoadModalAnalysis':
        '''PointLoadModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4810.PointLoadModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to PointLoadModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4810.PointLoadModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_power_load_modal_analysis(self) -> '_4811.PowerLoadModalAnalysis':
        '''PowerLoadModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4811.PowerLoadModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to PowerLoadModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4811.PowerLoadModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_pulley_modal_analysis(self) -> '_4812.PulleyModalAnalysis':
        '''PulleyModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4812.PulleyModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to PulleyModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4812.PulleyModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_rolling_ring_assembly_modal_analysis(self) -> '_4813.RollingRingAssemblyModalAnalysis':
        '''RollingRingAssemblyModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4813.RollingRingAssemblyModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to RollingRingAssemblyModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4813.RollingRingAssemblyModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_rolling_ring_modal_analysis(self) -> '_4815.RollingRingModalAnalysis':
        '''RollingRingModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4815.RollingRingModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to RollingRingModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4815.RollingRingModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_root_assembly_modal_analysis(self) -> '_4816.RootAssemblyModalAnalysis':
        '''RootAssemblyModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4816.RootAssemblyModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to RootAssemblyModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4816.RootAssemblyModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_shaft_hub_connection_modal_analysis(self) -> '_4817.ShaftHubConnectionModalAnalysis':
        '''ShaftHubConnectionModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4817.ShaftHubConnectionModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ShaftHubConnectionModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4817.ShaftHubConnectionModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_shaft_modal_analysis(self) -> '_4818.ShaftModalAnalysis':
        '''ShaftModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4818.ShaftModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ShaftModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4818.ShaftModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_specialised_assembly_modal_analysis(self) -> '_4821.SpecialisedAssemblyModalAnalysis':
        '''SpecialisedAssemblyModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4821.SpecialisedAssemblyModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to SpecialisedAssemblyModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4821.SpecialisedAssemblyModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_spiral_bevel_gear_modal_analysis(self) -> '_4823.SpiralBevelGearModalAnalysis':
        '''SpiralBevelGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4823.SpiralBevelGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to SpiralBevelGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4823.SpiralBevelGearModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_spiral_bevel_gear_set_modal_analysis(self) -> '_4824.SpiralBevelGearSetModalAnalysis':
        '''SpiralBevelGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4824.SpiralBevelGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to SpiralBevelGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4824.SpiralBevelGearSetModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_spring_damper_half_modal_analysis(self) -> '_4826.SpringDamperHalfModalAnalysis':
        '''SpringDamperHalfModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4826.SpringDamperHalfModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to SpringDamperHalfModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4826.SpringDamperHalfModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_spring_damper_modal_analysis(self) -> '_4827.SpringDamperModalAnalysis':
        '''SpringDamperModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4827.SpringDamperModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to SpringDamperModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4827.SpringDamperModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_straight_bevel_diff_gear_modal_analysis(self) -> '_4829.StraightBevelDiffGearModalAnalysis':
        '''StraightBevelDiffGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4829.StraightBevelDiffGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to StraightBevelDiffGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4829.StraightBevelDiffGearModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_straight_bevel_diff_gear_set_modal_analysis(self) -> '_4830.StraightBevelDiffGearSetModalAnalysis':
        '''StraightBevelDiffGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4830.StraightBevelDiffGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to StraightBevelDiffGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4830.StraightBevelDiffGearSetModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_straight_bevel_gear_modal_analysis(self) -> '_4832.StraightBevelGearModalAnalysis':
        '''StraightBevelGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4832.StraightBevelGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to StraightBevelGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4832.StraightBevelGearModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_straight_bevel_gear_set_modal_analysis(self) -> '_4833.StraightBevelGearSetModalAnalysis':
        '''StraightBevelGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4833.StraightBevelGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to StraightBevelGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4833.StraightBevelGearSetModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_straight_bevel_planet_gear_modal_analysis(self) -> '_4834.StraightBevelPlanetGearModalAnalysis':
        '''StraightBevelPlanetGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4834.StraightBevelPlanetGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to StraightBevelPlanetGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4834.StraightBevelPlanetGearModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_straight_bevel_sun_gear_modal_analysis(self) -> '_4835.StraightBevelSunGearModalAnalysis':
        '''StraightBevelSunGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4835.StraightBevelSunGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to StraightBevelSunGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4835.StraightBevelSunGearModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_synchroniser_half_modal_analysis(self) -> '_4836.SynchroniserHalfModalAnalysis':
        '''SynchroniserHalfModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4836.SynchroniserHalfModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to SynchroniserHalfModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4836.SynchroniserHalfModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_synchroniser_modal_analysis(self) -> '_4837.SynchroniserModalAnalysis':
        '''SynchroniserModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4837.SynchroniserModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to SynchroniserModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4837.SynchroniserModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_synchroniser_part_modal_analysis(self) -> '_4838.SynchroniserPartModalAnalysis':
        '''SynchroniserPartModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4838.SynchroniserPartModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to SynchroniserPartModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4838.SynchroniserPartModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_synchroniser_sleeve_modal_analysis(self) -> '_4839.SynchroniserSleeveModalAnalysis':
        '''SynchroniserSleeveModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4839.SynchroniserSleeveModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to SynchroniserSleeveModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4839.SynchroniserSleeveModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_torque_converter_modal_analysis(self) -> '_4841.TorqueConverterModalAnalysis':
        '''TorqueConverterModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4841.TorqueConverterModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to TorqueConverterModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4841.TorqueConverterModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_torque_converter_pump_modal_analysis(self) -> '_4842.TorqueConverterPumpModalAnalysis':
        '''TorqueConverterPumpModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4842.TorqueConverterPumpModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to TorqueConverterPumpModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4842.TorqueConverterPumpModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_torque_converter_turbine_modal_analysis(self) -> '_4843.TorqueConverterTurbineModalAnalysis':
        '''TorqueConverterTurbineModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4843.TorqueConverterTurbineModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to TorqueConverterTurbineModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4843.TorqueConverterTurbineModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_unbalanced_mass_modal_analysis(self) -> '_4844.UnbalancedMassModalAnalysis':
        '''UnbalancedMassModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4844.UnbalancedMassModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to UnbalancedMassModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4844.UnbalancedMassModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_virtual_component_modal_analysis(self) -> '_4845.VirtualComponentModalAnalysis':
        '''VirtualComponentModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4845.VirtualComponentModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to VirtualComponentModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4845.VirtualComponentModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_worm_gear_modal_analysis(self) -> '_4852.WormGearModalAnalysis':
        '''WormGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4852.WormGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to WormGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4852.WormGearModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_worm_gear_set_modal_analysis(self) -> '_4853.WormGearSetModalAnalysis':
        '''WormGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4853.WormGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to WormGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4853.WormGearSetModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_zerol_bevel_gear_modal_analysis(self) -> '_4855.ZerolBevelGearModalAnalysis':
        '''ZerolBevelGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4855.ZerolBevelGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ZerolBevelGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4855.ZerolBevelGearModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def uncoupled_modal_analysis_of_type_zerol_bevel_gear_set_modal_analysis(self) -> '_4856.ZerolBevelGearSetModalAnalysis':
        '''ZerolBevelGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4856.ZerolBevelGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ZerolBevelGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new(_4856.ZerolBevelGearSetModalAnalysis)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis else None

    @property
    def gear_whine_analysis_settings(self) -> '_5350.GearWhineAnalysisOptions':
        '''GearWhineAnalysisOptions: 'GearWhineAnalysisSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5350.GearWhineAnalysisOptions)(self.wrapped.GearWhineAnalysisSettings) if self.wrapped.GearWhineAnalysisSettings else None
