'''_2186.py

GearWhineAnalysisAnalysis
'''


from mastapy.system_model.analyses_and_results.static_loads import (
    _6238, _6239, _6241, _6185,
    _6184, _6083, _6096, _6095,
    _6101, _6100, _6114, _6113,
    _6116, _6117, _6194, _6200,
    _6198, _6196, _6210, _6209,
    _6221, _6220, _6222, _6223,
    _6227, _6228, _6229, _6115,
    _6082, _6097, _6110, _6165,
    _6186, _6197, _6202, _6085,
    _6103, _6141, _6213, _6090,
    _6107, _6077, _6120, _6161,
    _6167, _6170, _6173, _6206,
    _6216, _6237, _6240, _6147,
    _6183, _6094, _6099, _6112,
    _6208, _6226, _6073, _6074,
    _6081, _6093, _6092, _6098,
    _6111, _6126, _6139, _6143,
    _6080, _6151, _6163, _6175,
    _6176, _6178, _6180, _6182,
    _6189, _6192, _6193, _6199,
    _6203, _6234, _6235, _6201,
    _6102, _6104, _6140, _6142,
    _6076, _6078, _6084, _6086,
    _6087, _6088, _6089, _6091,
    _6105, _6109, _6118, _6122,
    _6123, _6145, _6150, _6160,
    _6162, _6166, _6168, _6169,
    _6171, _6172, _6174, _6187,
    _6205, _6207, _6212, _6214,
    _6215, _6217, _6218, _6219,
    _6236
)
from mastapy.system_model.analyses_and_results.gear_whine_analyses import (
    _5420, _5421, _5423, _5374,
    _5375, _5285, _5297, _5298,
    _5303, _5304, _5314, _5315,
    _5317, _5318, _5382, _5388,
    _5385, _5383, _5397, _5398,
    _5407, _5408, _5409, _5410,
    _5412, _5413, _5414, _5316,
    _5284, _5299, _5311, _5358,
    _5377, _5384, _5389, _5287,
    _5306, _5338, _5400, _5292,
    _5309, _5280, _5320, _5355,
    _5360, _5363, _5366, _5394,
    _5403, _5419, _5422, _5344,
    _5373, _5296, _5302, _5313,
    _5396, _5411, _5276, _5278,
    _5283, _5295, _5294, _5301,
    _5312, _5323, _5336, _5340,
    _5282, _5352, _5357, _5368,
    _5369, _5370, _5371, _5372,
    _5379, _5380, _5381, _5386,
    _5391, _5416, _5417, _5387,
    _5305, _5307, _5337, _5339,
    _5279, _5281, _5286, _5288,
    _5289, _5290, _5291, _5293,
    _5308, _5310, _5319, _5321,
    _5322, _5342, _5347, _5354,
    _5356, _5359, _5361, _5362,
    _5364, _5365, _5367, _5378,
    _5393, _5395, _5399, _5401,
    _5402, _5404, _5405, _5406,
    _5418
)
from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import (
    _2116, _2117, _2084, _2085,
    _2091, _2092, _2076, _2077,
    _2078, _2079, _2080, _2081,
    _2082, _2083, _2086, _2087,
    _2088, _2089, _2090, _2093,
    _2095, _2097, _2098, _2099,
    _2100, _2101, _2102, _2103,
    _2104, _2105, _2106, _2107,
    _2108, _2109, _2110, _2111,
    _2112, _2113, _2114, _2115
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
from mastapy.system_model.part_model import (
    _2003, _2004, _2007, _2009,
    _2010, _2011, _2014, _2015,
    _2018, _2019, _2002, _2020,
    _2023, _2027, _2028, _2029,
    _2031, _2033, _2034, _2036,
    _2037, _2039, _2041, _2042,
    _2043
)
from mastapy.system_model.part_model.shaft_model import _2046
from mastapy.system_model.analyses_and_results import _2177
from mastapy._internal.python_net import python_net_import

_GEAR_WHINE_ANALYSIS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'GearWhineAnalysisAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GearWhineAnalysisAnalysis',)


class GearWhineAnalysisAnalysis(_2177.SingleAnalysis):
    '''GearWhineAnalysisAnalysis

    This is a mastapy class.
    '''

    TYPE = _GEAR_WHINE_ANALYSIS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearWhineAnalysisAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def results_for_worm_gear_set_load_case(self, design_entity_analysis: '_6238.WormGearSetLoadCase') -> '_5420.WormGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.WormGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6238.WormGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5420.WormGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear(self, design_entity: '_2116.ZerolBevelGear') -> '_5421.ZerolBevelGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ZerolBevelGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2116.ZerolBevelGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5421.ZerolBevelGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_load_case(self, design_entity_analysis: '_6239.ZerolBevelGearLoadCase') -> '_5421.ZerolBevelGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ZerolBevelGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6239.ZerolBevelGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5421.ZerolBevelGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_set(self, design_entity: '_2117.ZerolBevelGearSet') -> '_5423.ZerolBevelGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ZerolBevelGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2117.ZerolBevelGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5423.ZerolBevelGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_set_load_case(self, design_entity_analysis: '_6241.ZerolBevelGearSetLoadCase') -> '_5423.ZerolBevelGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ZerolBevelGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6241.ZerolBevelGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5423.ZerolBevelGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling(self, design_entity: '_2146.PartToPartShearCoupling') -> '_5374.PartToPartShearCouplingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCoupling)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PartToPartShearCouplingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2146.PartToPartShearCoupling.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5374.PartToPartShearCouplingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_load_case(self, design_entity_analysis: '_6185.PartToPartShearCouplingLoadCase') -> '_5374.PartToPartShearCouplingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PartToPartShearCouplingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6185.PartToPartShearCouplingLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5374.PartToPartShearCouplingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_half(self, design_entity: '_2147.PartToPartShearCouplingHalf') -> '_5375.PartToPartShearCouplingHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PartToPartShearCouplingHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2147.PartToPartShearCouplingHalf.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5375.PartToPartShearCouplingHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_half_load_case(self, design_entity_analysis: '_6184.PartToPartShearCouplingHalfLoadCase') -> '_5375.PartToPartShearCouplingHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PartToPartShearCouplingHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6184.PartToPartShearCouplingHalfLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5375.PartToPartShearCouplingHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_belt_drive(self, design_entity: '_2135.BeltDrive') -> '_5285.BeltDriveGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BeltDriveGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2135.BeltDrive.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5285.BeltDriveGearWhineAnalysis)(method_result) if method_result else None

    def results_for_belt_drive_load_case(self, design_entity_analysis: '_6083.BeltDriveLoadCase') -> '_5285.BeltDriveGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BeltDriveGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6083.BeltDriveLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5285.BeltDriveGearWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch(self, design_entity: '_2137.Clutch') -> '_5297.ClutchGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ClutchGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2137.Clutch.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5297.ClutchGearWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch_load_case(self, design_entity_analysis: '_6096.ClutchLoadCase') -> '_5297.ClutchGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ClutchGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6096.ClutchLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5297.ClutchGearWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch_half(self, design_entity: '_2138.ClutchHalf') -> '_5298.ClutchHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ClutchHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2138.ClutchHalf.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5298.ClutchHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch_half_load_case(self, design_entity_analysis: '_6095.ClutchHalfLoadCase') -> '_5298.ClutchHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ClutchHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6095.ClutchHalfLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5298.ClutchHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling(self, design_entity: '_2140.ConceptCoupling') -> '_5303.ConceptCouplingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptCouplingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2140.ConceptCoupling.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5303.ConceptCouplingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_load_case(self, design_entity_analysis: '_6101.ConceptCouplingLoadCase') -> '_5303.ConceptCouplingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptCouplingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6101.ConceptCouplingLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5303.ConceptCouplingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_half(self, design_entity: '_2141.ConceptCouplingHalf') -> '_5304.ConceptCouplingHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptCouplingHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2141.ConceptCouplingHalf.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5304.ConceptCouplingHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_half_load_case(self, design_entity_analysis: '_6100.ConceptCouplingHalfLoadCase') -> '_5304.ConceptCouplingHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptCouplingHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6100.ConceptCouplingHalfLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5304.ConceptCouplingHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling(self, design_entity: '_2142.Coupling') -> '_5314.CouplingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CouplingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2142.Coupling.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5314.CouplingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling_load_case(self, design_entity_analysis: '_6114.CouplingLoadCase') -> '_5314.CouplingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CouplingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6114.CouplingLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5314.CouplingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling_half(self, design_entity: '_2143.CouplingHalf') -> '_5315.CouplingHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CouplingHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2143.CouplingHalf.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5315.CouplingHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling_half_load_case(self, design_entity_analysis: '_6113.CouplingHalfLoadCase') -> '_5315.CouplingHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CouplingHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6113.CouplingHalfLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5315.CouplingHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt(self, design_entity: '_2144.CVT') -> '_5317.CVTGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CVTGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2144.CVT.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5317.CVTGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt_load_case(self, design_entity_analysis: '_6116.CVTLoadCase') -> '_5317.CVTGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CVTGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6116.CVTLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5317.CVTGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt_pulley(self, design_entity: '_2145.CVTPulley') -> '_5318.CVTPulleyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CVTPulleyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2145.CVTPulley.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5318.CVTPulleyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt_pulley_load_case(self, design_entity_analysis: '_6117.CVTPulleyLoadCase') -> '_5318.CVTPulleyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTPulleyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CVTPulleyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6117.CVTPulleyLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5318.CVTPulleyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_pulley(self, design_entity: '_2148.Pulley') -> '_5382.PulleyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PulleyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2148.Pulley.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5382.PulleyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_pulley_load_case(self, design_entity_analysis: '_6194.PulleyLoadCase') -> '_5382.PulleyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PulleyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PulleyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6194.PulleyLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5382.PulleyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft_hub_connection(self, design_entity: '_2156.ShaftHubConnection') -> '_5388.ShaftHubConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ShaftHubConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2156.ShaftHubConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5388.ShaftHubConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft_hub_connection_load_case(self, design_entity_analysis: '_6200.ShaftHubConnectionLoadCase') -> '_5388.ShaftHubConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ShaftHubConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6200.ShaftHubConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5388.ShaftHubConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring(self, design_entity: '_2154.RollingRing') -> '_5385.RollingRingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.RollingRingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2154.RollingRing.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5385.RollingRingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_load_case(self, design_entity_analysis: '_6198.RollingRingLoadCase') -> '_5385.RollingRingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.RollingRingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6198.RollingRingLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5385.RollingRingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_assembly(self, design_entity: '_2155.RollingRingAssembly') -> '_5383.RollingRingAssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.RollingRingAssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2155.RollingRingAssembly.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5383.RollingRingAssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_assembly_load_case(self, design_entity_analysis: '_6196.RollingRingAssemblyLoadCase') -> '_5383.RollingRingAssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.RollingRingAssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6196.RollingRingAssemblyLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5383.RollingRingAssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper(self, design_entity: '_2157.SpringDamper') -> '_5397.SpringDamperGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpringDamperGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2157.SpringDamper.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5397.SpringDamperGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_load_case(self, design_entity_analysis: '_6210.SpringDamperLoadCase') -> '_5397.SpringDamperGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpringDamperGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6210.SpringDamperLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5397.SpringDamperGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_half(self, design_entity: '_2158.SpringDamperHalf') -> '_5398.SpringDamperHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpringDamperHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2158.SpringDamperHalf.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5398.SpringDamperHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_half_load_case(self, design_entity_analysis: '_6209.SpringDamperHalfLoadCase') -> '_5398.SpringDamperHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpringDamperHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6209.SpringDamperHalfLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5398.SpringDamperHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser(self, design_entity: '_2159.Synchroniser') -> '_5407.SynchroniserGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SynchroniserGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2159.Synchroniser.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5407.SynchroniserGearWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_load_case(self, design_entity_analysis: '_6221.SynchroniserLoadCase') -> '_5407.SynchroniserGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SynchroniserGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6221.SynchroniserLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5407.SynchroniserGearWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_half(self, design_entity: '_2161.SynchroniserHalf') -> '_5408.SynchroniserHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SynchroniserHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2161.SynchroniserHalf.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5408.SynchroniserHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_half_load_case(self, design_entity_analysis: '_6220.SynchroniserHalfLoadCase') -> '_5408.SynchroniserHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SynchroniserHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6220.SynchroniserHalfLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5408.SynchroniserHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_part(self, design_entity: '_2162.SynchroniserPart') -> '_5409.SynchroniserPartGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SynchroniserPartGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2162.SynchroniserPart.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5409.SynchroniserPartGearWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_part_load_case(self, design_entity_analysis: '_6222.SynchroniserPartLoadCase') -> '_5409.SynchroniserPartGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserPartLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SynchroniserPartGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6222.SynchroniserPartLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5409.SynchroniserPartGearWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_sleeve(self, design_entity: '_2163.SynchroniserSleeve') -> '_5410.SynchroniserSleeveGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SynchroniserSleeveGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2163.SynchroniserSleeve.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5410.SynchroniserSleeveGearWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_sleeve_load_case(self, design_entity_analysis: '_6223.SynchroniserSleeveLoadCase') -> '_5410.SynchroniserSleeveGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SynchroniserSleeveGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6223.SynchroniserSleeveLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5410.SynchroniserSleeveGearWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter(self, design_entity: '_2164.TorqueConverter') -> '_5412.TorqueConverterGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.TorqueConverterGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2164.TorqueConverter.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5412.TorqueConverterGearWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_load_case(self, design_entity_analysis: '_6227.TorqueConverterLoadCase') -> '_5412.TorqueConverterGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.TorqueConverterGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6227.TorqueConverterLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5412.TorqueConverterGearWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_pump(self, design_entity: '_2165.TorqueConverterPump') -> '_5413.TorqueConverterPumpGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.TorqueConverterPumpGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2165.TorqueConverterPump.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5413.TorqueConverterPumpGearWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_pump_load_case(self, design_entity_analysis: '_6228.TorqueConverterPumpLoadCase') -> '_5413.TorqueConverterPumpGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.TorqueConverterPumpGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6228.TorqueConverterPumpLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5413.TorqueConverterPumpGearWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_turbine(self, design_entity: '_2167.TorqueConverterTurbine') -> '_5414.TorqueConverterTurbineGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.TorqueConverterTurbineGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2167.TorqueConverterTurbine.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5414.TorqueConverterTurbineGearWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_turbine_load_case(self, design_entity_analysis: '_6229.TorqueConverterTurbineLoadCase') -> '_5414.TorqueConverterTurbineGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.TorqueConverterTurbineGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6229.TorqueConverterTurbineLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5414.TorqueConverterTurbineGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt_belt_connection(self, design_entity: '_1858.CVTBeltConnection') -> '_5316.CVTBeltConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CVTBeltConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1858.CVTBeltConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5316.CVTBeltConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt_belt_connection_load_case(self, design_entity_analysis: '_6115.CVTBeltConnectionLoadCase') -> '_5316.CVTBeltConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTBeltConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CVTBeltConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6115.CVTBeltConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5316.CVTBeltConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_belt_connection(self, design_entity: '_1853.BeltConnection') -> '_5284.BeltConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BeltConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1853.BeltConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5284.BeltConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_belt_connection_load_case(self, design_entity_analysis: '_6082.BeltConnectionLoadCase') -> '_5284.BeltConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BeltConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6082.BeltConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5284.BeltConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_coaxial_connection(self, design_entity: '_1854.CoaxialConnection') -> '_5299.CoaxialConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CoaxialConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1854.CoaxialConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5299.CoaxialConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_coaxial_connection_load_case(self, design_entity_analysis: '_6097.CoaxialConnectionLoadCase') -> '_5299.CoaxialConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CoaxialConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6097.CoaxialConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5299.CoaxialConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_connection(self, design_entity: '_1857.Connection') -> '_5311.ConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1857.Connection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5311.ConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_connection_load_case(self, design_entity_analysis: '_6110.ConnectionLoadCase') -> '_5311.ConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6110.ConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5311.ConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_inter_mountable_component_connection(self, design_entity: '_1866.InterMountableComponentConnection') -> '_5358.InterMountableComponentConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.InterMountableComponentConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1866.InterMountableComponentConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5358.InterMountableComponentConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_inter_mountable_component_connection_load_case(self, design_entity_analysis: '_6165.InterMountableComponentConnectionLoadCase') -> '_5358.InterMountableComponentConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.InterMountableComponentConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.InterMountableComponentConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6165.InterMountableComponentConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5358.InterMountableComponentConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_planetary_connection(self, design_entity: '_1869.PlanetaryConnection') -> '_5377.PlanetaryConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PlanetaryConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1869.PlanetaryConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5377.PlanetaryConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_planetary_connection_load_case(self, design_entity_analysis: '_6186.PlanetaryConnectionLoadCase') -> '_5377.PlanetaryConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PlanetaryConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6186.PlanetaryConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5377.PlanetaryConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_connection(self, design_entity: '_1873.RollingRingConnection') -> '_5384.RollingRingConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.RollingRingConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1873.RollingRingConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5384.RollingRingConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_connection_load_case(self, design_entity_analysis: '_6197.RollingRingConnectionLoadCase') -> '_5384.RollingRingConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.RollingRingConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6197.RollingRingConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5384.RollingRingConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft_to_mountable_component_connection(self, design_entity: '_1877.ShaftToMountableComponentConnection') -> '_5389.ShaftToMountableComponentConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ShaftToMountableComponentConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1877.ShaftToMountableComponentConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5389.ShaftToMountableComponentConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft_to_mountable_component_connection_load_case(self, design_entity_analysis: '_6202.ShaftToMountableComponentConnectionLoadCase') -> '_5389.ShaftToMountableComponentConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftToMountableComponentConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ShaftToMountableComponentConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6202.ShaftToMountableComponentConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5389.ShaftToMountableComponentConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_mesh(self, design_entity: '_1883.BevelDifferentialGearMesh') -> '_5287.BevelDifferentialGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelDifferentialGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1883.BevelDifferentialGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5287.BevelDifferentialGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_mesh_load_case(self, design_entity_analysis: '_6085.BevelDifferentialGearMeshLoadCase') -> '_5287.BevelDifferentialGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelDifferentialGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6085.BevelDifferentialGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5287.BevelDifferentialGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_mesh(self, design_entity: '_1887.ConceptGearMesh') -> '_5306.ConceptGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1887.ConceptGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5306.ConceptGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_mesh_load_case(self, design_entity_analysis: '_6103.ConceptGearMeshLoadCase') -> '_5306.ConceptGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6103.ConceptGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5306.ConceptGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear_mesh(self, design_entity: '_1893.FaceGearMesh') -> '_5338.FaceGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.FaceGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1893.FaceGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5338.FaceGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear_mesh_load_case(self, design_entity_analysis: '_6141.FaceGearMeshLoadCase') -> '_5338.FaceGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.FaceGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6141.FaceGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5338.FaceGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_mesh(self, design_entity: '_1907.StraightBevelDiffGearMesh') -> '_5400.StraightBevelDiffGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelDiffGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1907.StraightBevelDiffGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5400.StraightBevelDiffGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_mesh_load_case(self, design_entity_analysis: '_6213.StraightBevelDiffGearMeshLoadCase') -> '_5400.StraightBevelDiffGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelDiffGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6213.StraightBevelDiffGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5400.StraightBevelDiffGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_mesh(self, design_entity: '_1885.BevelGearMesh') -> '_5292.BevelGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1885.BevelGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5292.BevelGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6090.BevelGearMeshLoadCase') -> '_5292.BevelGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6090.BevelGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5292.BevelGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_mesh(self, design_entity: '_1889.ConicalGearMesh') -> '_5309.ConicalGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConicalGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1889.ConicalGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5309.ConicalGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_mesh_load_case(self, design_entity_analysis: '_6107.ConicalGearMeshLoadCase') -> '_5309.ConicalGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConicalGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6107.ConicalGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5309.ConicalGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_mesh(self, design_entity: '_1881.AGMAGleasonConicalGearMesh') -> '_5280.AGMAGleasonConicalGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AGMAGleasonConicalGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1881.AGMAGleasonConicalGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5280.AGMAGleasonConicalGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_mesh_load_case(self, design_entity_analysis: '_6077.AGMAGleasonConicalGearMeshLoadCase') -> '_5280.AGMAGleasonConicalGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AGMAGleasonConicalGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6077.AGMAGleasonConicalGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5280.AGMAGleasonConicalGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_mesh(self, design_entity: '_1891.CylindricalGearMesh') -> '_5320.CylindricalGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CylindricalGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1891.CylindricalGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5320.CylindricalGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_mesh_load_case(self, design_entity_analysis: '_6120.CylindricalGearMeshLoadCase') -> '_5320.CylindricalGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CylindricalGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6120.CylindricalGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5320.CylindricalGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_mesh(self, design_entity: '_1897.HypoidGearMesh') -> '_5355.HypoidGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.HypoidGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1897.HypoidGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5355.HypoidGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_mesh_load_case(self, design_entity_analysis: '_6161.HypoidGearMeshLoadCase') -> '_5355.HypoidGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.HypoidGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6161.HypoidGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5355.HypoidGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(self, design_entity: '_1900.KlingelnbergCycloPalloidConicalGearMesh') -> '_5360.KlingelnbergCycloPalloidConicalGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidConicalGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1900.KlingelnbergCycloPalloidConicalGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5360.KlingelnbergCycloPalloidConicalGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(self, design_entity_analysis: '_6167.KlingelnbergCycloPalloidConicalGearMeshLoadCase') -> '_5360.KlingelnbergCycloPalloidConicalGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidConicalGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6167.KlingelnbergCycloPalloidConicalGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5360.KlingelnbergCycloPalloidConicalGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self, design_entity: '_1901.KlingelnbergCycloPalloidHypoidGearMesh') -> '_5363.KlingelnbergCycloPalloidHypoidGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidHypoidGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1901.KlingelnbergCycloPalloidHypoidGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5363.KlingelnbergCycloPalloidHypoidGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(self, design_entity_analysis: '_6170.KlingelnbergCycloPalloidHypoidGearMeshLoadCase') -> '_5363.KlingelnbergCycloPalloidHypoidGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidHypoidGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6170.KlingelnbergCycloPalloidHypoidGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5363.KlingelnbergCycloPalloidHypoidGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self, design_entity: '_1902.KlingelnbergCycloPalloidSpiralBevelGearMesh') -> '_5366.KlingelnbergCycloPalloidSpiralBevelGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1902.KlingelnbergCycloPalloidSpiralBevelGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5366.KlingelnbergCycloPalloidSpiralBevelGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6173.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase') -> '_5366.KlingelnbergCycloPalloidSpiralBevelGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6173.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5366.KlingelnbergCycloPalloidSpiralBevelGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_mesh(self, design_entity: '_1905.SpiralBevelGearMesh') -> '_5394.SpiralBevelGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpiralBevelGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1905.SpiralBevelGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5394.SpiralBevelGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6206.SpiralBevelGearMeshLoadCase') -> '_5394.SpiralBevelGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpiralBevelGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6206.SpiralBevelGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5394.SpiralBevelGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_mesh(self, design_entity: '_1909.StraightBevelGearMesh') -> '_5403.StraightBevelGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1909.StraightBevelGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5403.StraightBevelGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6216.StraightBevelGearMeshLoadCase') -> '_5403.StraightBevelGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6216.StraightBevelGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5403.StraightBevelGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_mesh(self, design_entity: '_1911.WormGearMesh') -> '_5419.WormGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.WormGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1911.WormGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5419.WormGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_mesh_load_case(self, design_entity_analysis: '_6237.WormGearMeshLoadCase') -> '_5419.WormGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.WormGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6237.WormGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5419.WormGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_mesh(self, design_entity: '_1913.ZerolBevelGearMesh') -> '_5422.ZerolBevelGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ZerolBevelGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1913.ZerolBevelGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5422.ZerolBevelGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6240.ZerolBevelGearMeshLoadCase') -> '_5422.ZerolBevelGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ZerolBevelGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6240.ZerolBevelGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5422.ZerolBevelGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_gear_mesh(self, design_entity: '_1895.GearMesh') -> '_5344.GearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.GearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1895.GearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5344.GearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_gear_mesh_load_case(self, design_entity_analysis: '_6147.GearMeshLoadCase') -> '_5344.GearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.GearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6147.GearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5344.GearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_connection(self, design_entity: '_1921.PartToPartShearCouplingConnection') -> '_5373.PartToPartShearCouplingConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PartToPartShearCouplingConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1921.PartToPartShearCouplingConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5373.PartToPartShearCouplingConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_connection_load_case(self, design_entity_analysis: '_6183.PartToPartShearCouplingConnectionLoadCase') -> '_5373.PartToPartShearCouplingConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PartToPartShearCouplingConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6183.PartToPartShearCouplingConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5373.PartToPartShearCouplingConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch_connection(self, design_entity: '_1915.ClutchConnection') -> '_5296.ClutchConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ClutchConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1915.ClutchConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5296.ClutchConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch_connection_load_case(self, design_entity_analysis: '_6094.ClutchConnectionLoadCase') -> '_5296.ClutchConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ClutchConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6094.ClutchConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5296.ClutchConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_connection(self, design_entity: '_1917.ConceptCouplingConnection') -> '_5302.ConceptCouplingConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptCouplingConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1917.ConceptCouplingConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5302.ConceptCouplingConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_connection_load_case(self, design_entity_analysis: '_6099.ConceptCouplingConnectionLoadCase') -> '_5302.ConceptCouplingConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptCouplingConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6099.ConceptCouplingConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5302.ConceptCouplingConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling_connection(self, design_entity: '_1919.CouplingConnection') -> '_5313.CouplingConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CouplingConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1919.CouplingConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5313.CouplingConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling_connection_load_case(self, design_entity_analysis: '_6112.CouplingConnectionLoadCase') -> '_5313.CouplingConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CouplingConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6112.CouplingConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5313.CouplingConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_connection(self, design_entity: '_1923.SpringDamperConnection') -> '_5396.SpringDamperConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpringDamperConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1923.SpringDamperConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5396.SpringDamperConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_connection_load_case(self, design_entity_analysis: '_6208.SpringDamperConnectionLoadCase') -> '_5396.SpringDamperConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpringDamperConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6208.SpringDamperConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5396.SpringDamperConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_connection(self, design_entity: '_1925.TorqueConverterConnection') -> '_5411.TorqueConverterConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.TorqueConverterConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1925.TorqueConverterConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5411.TorqueConverterConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_connection_load_case(self, design_entity_analysis: '_6226.TorqueConverterConnectionLoadCase') -> '_5411.TorqueConverterConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.TorqueConverterConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6226.TorqueConverterConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5411.TorqueConverterConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_abstract_assembly(self, design_entity: '_2003.AbstractAssembly') -> '_5276.AbstractAssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AbstractAssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2003.AbstractAssembly.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5276.AbstractAssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_abstract_assembly_load_case(self, design_entity_analysis: '_6073.AbstractAssemblyLoadCase') -> '_5276.AbstractAssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AbstractAssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6073.AbstractAssemblyLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5276.AbstractAssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_abstract_shaft_or_housing(self, design_entity: '_2004.AbstractShaftOrHousing') -> '_5278.AbstractShaftOrHousingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AbstractShaftOrHousingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2004.AbstractShaftOrHousing.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5278.AbstractShaftOrHousingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_abstract_shaft_or_housing_load_case(self, design_entity_analysis: '_6074.AbstractShaftOrHousingLoadCase') -> '_5278.AbstractShaftOrHousingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractShaftOrHousingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AbstractShaftOrHousingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6074.AbstractShaftOrHousingLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5278.AbstractShaftOrHousingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bearing(self, design_entity: '_2007.Bearing') -> '_5283.BearingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BearingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2007.Bearing.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5283.BearingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bearing_load_case(self, design_entity_analysis: '_6081.BearingLoadCase') -> '_5283.BearingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BearingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BearingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6081.BearingLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5283.BearingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bolt(self, design_entity: '_2009.Bolt') -> '_5295.BoltGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BoltGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2009.Bolt.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5295.BoltGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bolt_load_case(self, design_entity_analysis: '_6093.BoltLoadCase') -> '_5295.BoltGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BoltGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6093.BoltLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5295.BoltGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bolted_joint(self, design_entity: '_2010.BoltedJoint') -> '_5294.BoltedJointGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BoltedJointGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2010.BoltedJoint.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5294.BoltedJointGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bolted_joint_load_case(self, design_entity_analysis: '_6092.BoltedJointLoadCase') -> '_5294.BoltedJointGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltedJointLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BoltedJointGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6092.BoltedJointLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5294.BoltedJointGearWhineAnalysis)(method_result) if method_result else None

    def results_for_component(self, design_entity: '_2011.Component') -> '_5301.ComponentGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Component)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ComponentGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2011.Component.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5301.ComponentGearWhineAnalysis)(method_result) if method_result else None

    def results_for_component_load_case(self, design_entity_analysis: '_6098.ComponentLoadCase') -> '_5301.ComponentGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ComponentGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6098.ComponentLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5301.ComponentGearWhineAnalysis)(method_result) if method_result else None

    def results_for_connector(self, design_entity: '_2014.Connector') -> '_5312.ConnectorGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Connector)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConnectorGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2014.Connector.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5312.ConnectorGearWhineAnalysis)(method_result) if method_result else None

    def results_for_connector_load_case(self, design_entity_analysis: '_6111.ConnectorLoadCase') -> '_5312.ConnectorGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectorLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConnectorGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6111.ConnectorLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5312.ConnectorGearWhineAnalysis)(method_result) if method_result else None

    def results_for_datum(self, design_entity: '_2015.Datum') -> '_5323.DatumGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Datum)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.DatumGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2015.Datum.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5323.DatumGearWhineAnalysis)(method_result) if method_result else None

    def results_for_datum_load_case(self, design_entity_analysis: '_6126.DatumLoadCase') -> '_5323.DatumGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.DatumLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.DatumGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6126.DatumLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5323.DatumGearWhineAnalysis)(method_result) if method_result else None

    def results_for_external_cad_model(self, design_entity: '_2018.ExternalCADModel') -> '_5336.ExternalCADModelGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ExternalCADModelGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2018.ExternalCADModel.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5336.ExternalCADModelGearWhineAnalysis)(method_result) if method_result else None

    def results_for_external_cad_model_load_case(self, design_entity_analysis: '_6139.ExternalCADModelLoadCase') -> '_5336.ExternalCADModelGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ExternalCADModelGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6139.ExternalCADModelLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5336.ExternalCADModelGearWhineAnalysis)(method_result) if method_result else None

    def results_for_flexible_pin_assembly(self, design_entity: '_2019.FlexiblePinAssembly') -> '_5340.FlexiblePinAssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.FlexiblePinAssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2019.FlexiblePinAssembly.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5340.FlexiblePinAssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_flexible_pin_assembly_load_case(self, design_entity_analysis: '_6143.FlexiblePinAssemblyLoadCase') -> '_5340.FlexiblePinAssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.FlexiblePinAssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6143.FlexiblePinAssemblyLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5340.FlexiblePinAssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_assembly(self, design_entity: '_2002.Assembly') -> '_5282.AssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2002.Assembly.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5282.AssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_assembly_load_case(self, design_entity_analysis: '_6080.AssemblyLoadCase') -> '_5282.AssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6080.AssemblyLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5282.AssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_guide_dxf_model(self, design_entity: '_2020.GuideDxfModel') -> '_5352.GuideDxfModelGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.GuideDxfModelGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2020.GuideDxfModel.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5352.GuideDxfModelGearWhineAnalysis)(method_result) if method_result else None

    def results_for_guide_dxf_model_load_case(self, design_entity_analysis: '_6151.GuideDxfModelLoadCase') -> '_5352.GuideDxfModelGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.GuideDxfModelGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6151.GuideDxfModelLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5352.GuideDxfModelGearWhineAnalysis)(method_result) if method_result else None

    def results_for_imported_fe_component(self, design_entity: '_2023.ImportedFEComponent') -> '_5357.ImportedFEComponentGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ImportedFEComponent)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ImportedFEComponentGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2023.ImportedFEComponent.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5357.ImportedFEComponentGearWhineAnalysis)(method_result) if method_result else None

    def results_for_imported_fe_component_load_case(self, design_entity_analysis: '_6163.ImportedFEComponentLoadCase') -> '_5357.ImportedFEComponentGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ImportedFEComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ImportedFEComponentGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6163.ImportedFEComponentLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5357.ImportedFEComponentGearWhineAnalysis)(method_result) if method_result else None

    def results_for_mass_disc(self, design_entity: '_2027.MassDisc') -> '_5368.MassDiscGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.MassDiscGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2027.MassDisc.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5368.MassDiscGearWhineAnalysis)(method_result) if method_result else None

    def results_for_mass_disc_load_case(self, design_entity_analysis: '_6175.MassDiscLoadCase') -> '_5368.MassDiscGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MassDiscLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.MassDiscGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6175.MassDiscLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5368.MassDiscGearWhineAnalysis)(method_result) if method_result else None

    def results_for_measurement_component(self, design_entity: '_2028.MeasurementComponent') -> '_5369.MeasurementComponentGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.MeasurementComponentGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2028.MeasurementComponent.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5369.MeasurementComponentGearWhineAnalysis)(method_result) if method_result else None

    def results_for_measurement_component_load_case(self, design_entity_analysis: '_6176.MeasurementComponentLoadCase') -> '_5369.MeasurementComponentGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.MeasurementComponentGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6176.MeasurementComponentLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5369.MeasurementComponentGearWhineAnalysis)(method_result) if method_result else None

    def results_for_mountable_component(self, design_entity: '_2029.MountableComponent') -> '_5370.MountableComponentGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.MountableComponentGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2029.MountableComponent.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5370.MountableComponentGearWhineAnalysis)(method_result) if method_result else None

    def results_for_mountable_component_load_case(self, design_entity_analysis: '_6178.MountableComponentLoadCase') -> '_5370.MountableComponentGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MountableComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.MountableComponentGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6178.MountableComponentLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5370.MountableComponentGearWhineAnalysis)(method_result) if method_result else None

    def results_for_oil_seal(self, design_entity: '_2031.OilSeal') -> '_5371.OilSealGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.OilSealGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2031.OilSeal.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5371.OilSealGearWhineAnalysis)(method_result) if method_result else None

    def results_for_oil_seal_load_case(self, design_entity_analysis: '_6180.OilSealLoadCase') -> '_5371.OilSealGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.OilSealLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.OilSealGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6180.OilSealLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5371.OilSealGearWhineAnalysis)(method_result) if method_result else None

    def results_for_part(self, design_entity: '_2033.Part') -> '_5372.PartGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Part)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PartGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2033.Part.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5372.PartGearWhineAnalysis)(method_result) if method_result else None

    def results_for_part_load_case(self, design_entity_analysis: '_6182.PartLoadCase') -> '_5372.PartGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PartGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6182.PartLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5372.PartGearWhineAnalysis)(method_result) if method_result else None

    def results_for_planet_carrier(self, design_entity: '_2034.PlanetCarrier') -> '_5379.PlanetCarrierGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PlanetCarrierGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2034.PlanetCarrier.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5379.PlanetCarrierGearWhineAnalysis)(method_result) if method_result else None

    def results_for_planet_carrier_load_case(self, design_entity_analysis: '_6189.PlanetCarrierLoadCase') -> '_5379.PlanetCarrierGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PlanetCarrierGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6189.PlanetCarrierLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5379.PlanetCarrierGearWhineAnalysis)(method_result) if method_result else None

    def results_for_point_load(self, design_entity: '_2036.PointLoad') -> '_5380.PointLoadGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PointLoadGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2036.PointLoad.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5380.PointLoadGearWhineAnalysis)(method_result) if method_result else None

    def results_for_point_load_load_case(self, design_entity_analysis: '_6192.PointLoadLoadCase') -> '_5380.PointLoadGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PointLoadGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6192.PointLoadLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5380.PointLoadGearWhineAnalysis)(method_result) if method_result else None

    def results_for_power_load(self, design_entity: '_2037.PowerLoad') -> '_5381.PowerLoadGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PowerLoadGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2037.PowerLoad.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5381.PowerLoadGearWhineAnalysis)(method_result) if method_result else None

    def results_for_power_load_load_case(self, design_entity_analysis: '_6193.PowerLoadLoadCase') -> '_5381.PowerLoadGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PowerLoadGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6193.PowerLoadLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5381.PowerLoadGearWhineAnalysis)(method_result) if method_result else None

    def results_for_root_assembly(self, design_entity: '_2039.RootAssembly') -> '_5386.RootAssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.RootAssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2039.RootAssembly.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5386.RootAssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_root_assembly_load_case(self, design_entity_analysis: '_6199.RootAssemblyLoadCase') -> '_5386.RootAssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RootAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.RootAssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6199.RootAssemblyLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5386.RootAssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_specialised_assembly(self, design_entity: '_2041.SpecialisedAssembly') -> '_5391.SpecialisedAssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpecialisedAssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2041.SpecialisedAssembly.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5391.SpecialisedAssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_specialised_assembly_load_case(self, design_entity_analysis: '_6203.SpecialisedAssemblyLoadCase') -> '_5391.SpecialisedAssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpecialisedAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpecialisedAssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6203.SpecialisedAssemblyLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5391.SpecialisedAssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_unbalanced_mass(self, design_entity: '_2042.UnbalancedMass') -> '_5416.UnbalancedMassGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.UnbalancedMassGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2042.UnbalancedMass.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5416.UnbalancedMassGearWhineAnalysis)(method_result) if method_result else None

    def results_for_unbalanced_mass_load_case(self, design_entity_analysis: '_6234.UnbalancedMassLoadCase') -> '_5416.UnbalancedMassGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.UnbalancedMassGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6234.UnbalancedMassLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5416.UnbalancedMassGearWhineAnalysis)(method_result) if method_result else None

    def results_for_virtual_component(self, design_entity: '_2043.VirtualComponent') -> '_5417.VirtualComponentGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.VirtualComponentGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2043.VirtualComponent.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5417.VirtualComponentGearWhineAnalysis)(method_result) if method_result else None

    def results_for_virtual_component_load_case(self, design_entity_analysis: '_6235.VirtualComponentLoadCase') -> '_5417.VirtualComponentGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.VirtualComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.VirtualComponentGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6235.VirtualComponentLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5417.VirtualComponentGearWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft(self, design_entity: '_2046.Shaft') -> '_5387.ShaftGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ShaftGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2046.Shaft.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5387.ShaftGearWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft_load_case(self, design_entity_analysis: '_6201.ShaftLoadCase') -> '_5387.ShaftGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ShaftGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6201.ShaftLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5387.ShaftGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear(self, design_entity: '_2084.ConceptGear') -> '_5305.ConceptGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2084.ConceptGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5305.ConceptGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_load_case(self, design_entity_analysis: '_6102.ConceptGearLoadCase') -> '_5305.ConceptGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6102.ConceptGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5305.ConceptGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_set(self, design_entity: '_2085.ConceptGearSet') -> '_5307.ConceptGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2085.ConceptGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5307.ConceptGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_set_load_case(self, design_entity_analysis: '_6104.ConceptGearSetLoadCase') -> '_5307.ConceptGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6104.ConceptGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5307.ConceptGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear(self, design_entity: '_2091.FaceGear') -> '_5337.FaceGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.FaceGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2091.FaceGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5337.FaceGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear_load_case(self, design_entity_analysis: '_6140.FaceGearLoadCase') -> '_5337.FaceGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.FaceGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6140.FaceGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5337.FaceGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear_set(self, design_entity: '_2092.FaceGearSet') -> '_5339.FaceGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.FaceGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2092.FaceGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5339.FaceGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear_set_load_case(self, design_entity_analysis: '_6142.FaceGearSetLoadCase') -> '_5339.FaceGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.FaceGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6142.FaceGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5339.FaceGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear(self, design_entity: '_2076.AGMAGleasonConicalGear') -> '_5279.AGMAGleasonConicalGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AGMAGleasonConicalGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2076.AGMAGleasonConicalGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5279.AGMAGleasonConicalGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_load_case(self, design_entity_analysis: '_6076.AGMAGleasonConicalGearLoadCase') -> '_5279.AGMAGleasonConicalGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AGMAGleasonConicalGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6076.AGMAGleasonConicalGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5279.AGMAGleasonConicalGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_set(self, design_entity: '_2077.AGMAGleasonConicalGearSet') -> '_5281.AGMAGleasonConicalGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AGMAGleasonConicalGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2077.AGMAGleasonConicalGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5281.AGMAGleasonConicalGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_set_load_case(self, design_entity_analysis: '_6078.AGMAGleasonConicalGearSetLoadCase') -> '_5281.AGMAGleasonConicalGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AGMAGleasonConicalGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6078.AGMAGleasonConicalGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5281.AGMAGleasonConicalGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear(self, design_entity: '_2078.BevelDifferentialGear') -> '_5286.BevelDifferentialGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelDifferentialGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2078.BevelDifferentialGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5286.BevelDifferentialGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_load_case(self, design_entity_analysis: '_6084.BevelDifferentialGearLoadCase') -> '_5286.BevelDifferentialGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelDifferentialGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6084.BevelDifferentialGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5286.BevelDifferentialGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_set(self, design_entity: '_2079.BevelDifferentialGearSet') -> '_5288.BevelDifferentialGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelDifferentialGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2079.BevelDifferentialGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5288.BevelDifferentialGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_set_load_case(self, design_entity_analysis: '_6086.BevelDifferentialGearSetLoadCase') -> '_5288.BevelDifferentialGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelDifferentialGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6086.BevelDifferentialGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5288.BevelDifferentialGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_planet_gear(self, design_entity: '_2080.BevelDifferentialPlanetGear') -> '_5289.BevelDifferentialPlanetGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelDifferentialPlanetGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2080.BevelDifferentialPlanetGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5289.BevelDifferentialPlanetGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_planet_gear_load_case(self, design_entity_analysis: '_6087.BevelDifferentialPlanetGearLoadCase') -> '_5289.BevelDifferentialPlanetGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelDifferentialPlanetGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6087.BevelDifferentialPlanetGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5289.BevelDifferentialPlanetGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_sun_gear(self, design_entity: '_2081.BevelDifferentialSunGear') -> '_5290.BevelDifferentialSunGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelDifferentialSunGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2081.BevelDifferentialSunGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5290.BevelDifferentialSunGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_sun_gear_load_case(self, design_entity_analysis: '_6088.BevelDifferentialSunGearLoadCase') -> '_5290.BevelDifferentialSunGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialSunGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelDifferentialSunGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6088.BevelDifferentialSunGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5290.BevelDifferentialSunGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear(self, design_entity: '_2082.BevelGear') -> '_5291.BevelGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2082.BevelGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5291.BevelGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_load_case(self, design_entity_analysis: '_6089.BevelGearLoadCase') -> '_5291.BevelGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6089.BevelGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5291.BevelGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_set(self, design_entity: '_2083.BevelGearSet') -> '_5293.BevelGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2083.BevelGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5293.BevelGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_set_load_case(self, design_entity_analysis: '_6091.BevelGearSetLoadCase') -> '_5293.BevelGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6091.BevelGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5293.BevelGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear(self, design_entity: '_2086.ConicalGear') -> '_5308.ConicalGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConicalGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2086.ConicalGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5308.ConicalGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_load_case(self, design_entity_analysis: '_6105.ConicalGearLoadCase') -> '_5308.ConicalGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConicalGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6105.ConicalGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5308.ConicalGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_set(self, design_entity: '_2087.ConicalGearSet') -> '_5310.ConicalGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConicalGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2087.ConicalGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5310.ConicalGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_set_load_case(self, design_entity_analysis: '_6109.ConicalGearSetLoadCase') -> '_5310.ConicalGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConicalGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6109.ConicalGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5310.ConicalGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear(self, design_entity: '_2088.CylindricalGear') -> '_5319.CylindricalGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CylindricalGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2088.CylindricalGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5319.CylindricalGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_load_case(self, design_entity_analysis: '_6118.CylindricalGearLoadCase') -> '_5319.CylindricalGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CylindricalGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6118.CylindricalGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5319.CylindricalGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_set(self, design_entity: '_2089.CylindricalGearSet') -> '_5321.CylindricalGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CylindricalGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2089.CylindricalGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5321.CylindricalGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_set_load_case(self, design_entity_analysis: '_6122.CylindricalGearSetLoadCase') -> '_5321.CylindricalGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CylindricalGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6122.CylindricalGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5321.CylindricalGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_planet_gear(self, design_entity: '_2090.CylindricalPlanetGear') -> '_5322.CylindricalPlanetGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CylindricalPlanetGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2090.CylindricalPlanetGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5322.CylindricalPlanetGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_planet_gear_load_case(self, design_entity_analysis: '_6123.CylindricalPlanetGearLoadCase') -> '_5322.CylindricalPlanetGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CylindricalPlanetGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6123.CylindricalPlanetGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5322.CylindricalPlanetGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_gear(self, design_entity: '_2093.Gear') -> '_5342.GearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.GearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2093.Gear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5342.GearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_gear_load_case(self, design_entity_analysis: '_6145.GearLoadCase') -> '_5342.GearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.GearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6145.GearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5342.GearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_gear_set(self, design_entity: '_2095.GearSet') -> '_5347.GearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.GearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2095.GearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5347.GearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_gear_set_load_case(self, design_entity_analysis: '_6150.GearSetLoadCase') -> '_5347.GearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.GearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6150.GearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5347.GearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear(self, design_entity: '_2097.HypoidGear') -> '_5354.HypoidGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.HypoidGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2097.HypoidGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5354.HypoidGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_load_case(self, design_entity_analysis: '_6160.HypoidGearLoadCase') -> '_5354.HypoidGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.HypoidGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6160.HypoidGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5354.HypoidGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_set(self, design_entity: '_2098.HypoidGearSet') -> '_5356.HypoidGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.HypoidGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2098.HypoidGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5356.HypoidGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_set_load_case(self, design_entity_analysis: '_6162.HypoidGearSetLoadCase') -> '_5356.HypoidGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.HypoidGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6162.HypoidGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5356.HypoidGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear(self, design_entity: '_2099.KlingelnbergCycloPalloidConicalGear') -> '_5359.KlingelnbergCycloPalloidConicalGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidConicalGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2099.KlingelnbergCycloPalloidConicalGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5359.KlingelnbergCycloPalloidConicalGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_load_case(self, design_entity_analysis: '_6166.KlingelnbergCycloPalloidConicalGearLoadCase') -> '_5359.KlingelnbergCycloPalloidConicalGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidConicalGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6166.KlingelnbergCycloPalloidConicalGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5359.KlingelnbergCycloPalloidConicalGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(self, design_entity: '_2100.KlingelnbergCycloPalloidConicalGearSet') -> '_5361.KlingelnbergCycloPalloidConicalGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidConicalGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2100.KlingelnbergCycloPalloidConicalGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5361.KlingelnbergCycloPalloidConicalGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set_load_case(self, design_entity_analysis: '_6168.KlingelnbergCycloPalloidConicalGearSetLoadCase') -> '_5361.KlingelnbergCycloPalloidConicalGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidConicalGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6168.KlingelnbergCycloPalloidConicalGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5361.KlingelnbergCycloPalloidConicalGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(self, design_entity: '_2101.KlingelnbergCycloPalloidHypoidGear') -> '_5362.KlingelnbergCycloPalloidHypoidGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidHypoidGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2101.KlingelnbergCycloPalloidHypoidGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5362.KlingelnbergCycloPalloidHypoidGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_load_case(self, design_entity_analysis: '_6169.KlingelnbergCycloPalloidHypoidGearLoadCase') -> '_5362.KlingelnbergCycloPalloidHypoidGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidHypoidGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6169.KlingelnbergCycloPalloidHypoidGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5362.KlingelnbergCycloPalloidHypoidGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(self, design_entity: '_2102.KlingelnbergCycloPalloidHypoidGearSet') -> '_5364.KlingelnbergCycloPalloidHypoidGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidHypoidGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2102.KlingelnbergCycloPalloidHypoidGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5364.KlingelnbergCycloPalloidHypoidGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(self, design_entity_analysis: '_6171.KlingelnbergCycloPalloidHypoidGearSetLoadCase') -> '_5364.KlingelnbergCycloPalloidHypoidGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidHypoidGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6171.KlingelnbergCycloPalloidHypoidGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5364.KlingelnbergCycloPalloidHypoidGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(self, design_entity: '_2103.KlingelnbergCycloPalloidSpiralBevelGear') -> '_5365.KlingelnbergCycloPalloidSpiralBevelGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2103.KlingelnbergCycloPalloidSpiralBevelGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5365.KlingelnbergCycloPalloidSpiralBevelGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(self, design_entity_analysis: '_6172.KlingelnbergCycloPalloidSpiralBevelGearLoadCase') -> '_5365.KlingelnbergCycloPalloidSpiralBevelGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6172.KlingelnbergCycloPalloidSpiralBevelGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5365.KlingelnbergCycloPalloidSpiralBevelGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, design_entity: '_2104.KlingelnbergCycloPalloidSpiralBevelGearSet') -> '_5367.KlingelnbergCycloPalloidSpiralBevelGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2104.KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5367.KlingelnbergCycloPalloidSpiralBevelGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(self, design_entity_analysis: '_6174.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase') -> '_5367.KlingelnbergCycloPalloidSpiralBevelGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6174.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5367.KlingelnbergCycloPalloidSpiralBevelGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_planetary_gear_set(self, design_entity: '_2105.PlanetaryGearSet') -> '_5378.PlanetaryGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PlanetaryGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2105.PlanetaryGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5378.PlanetaryGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_planetary_gear_set_load_case(self, design_entity_analysis: '_6187.PlanetaryGearSetLoadCase') -> '_5378.PlanetaryGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PlanetaryGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6187.PlanetaryGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5378.PlanetaryGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear(self, design_entity: '_2106.SpiralBevelGear') -> '_5393.SpiralBevelGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpiralBevelGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2106.SpiralBevelGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5393.SpiralBevelGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_load_case(self, design_entity_analysis: '_6205.SpiralBevelGearLoadCase') -> '_5393.SpiralBevelGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpiralBevelGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6205.SpiralBevelGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5393.SpiralBevelGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_set(self, design_entity: '_2107.SpiralBevelGearSet') -> '_5395.SpiralBevelGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpiralBevelGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2107.SpiralBevelGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5395.SpiralBevelGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_set_load_case(self, design_entity_analysis: '_6207.SpiralBevelGearSetLoadCase') -> '_5395.SpiralBevelGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpiralBevelGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6207.SpiralBevelGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5395.SpiralBevelGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear(self, design_entity: '_2108.StraightBevelDiffGear') -> '_5399.StraightBevelDiffGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelDiffGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2108.StraightBevelDiffGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5399.StraightBevelDiffGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_load_case(self, design_entity_analysis: '_6212.StraightBevelDiffGearLoadCase') -> '_5399.StraightBevelDiffGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelDiffGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6212.StraightBevelDiffGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5399.StraightBevelDiffGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_set(self, design_entity: '_2109.StraightBevelDiffGearSet') -> '_5401.StraightBevelDiffGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelDiffGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2109.StraightBevelDiffGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5401.StraightBevelDiffGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_set_load_case(self, design_entity_analysis: '_6214.StraightBevelDiffGearSetLoadCase') -> '_5401.StraightBevelDiffGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelDiffGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6214.StraightBevelDiffGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5401.StraightBevelDiffGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear(self, design_entity: '_2110.StraightBevelGear') -> '_5402.StraightBevelGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2110.StraightBevelGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5402.StraightBevelGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_load_case(self, design_entity_analysis: '_6215.StraightBevelGearLoadCase') -> '_5402.StraightBevelGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6215.StraightBevelGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5402.StraightBevelGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_set(self, design_entity: '_2111.StraightBevelGearSet') -> '_5404.StraightBevelGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2111.StraightBevelGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5404.StraightBevelGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_set_load_case(self, design_entity_analysis: '_6217.StraightBevelGearSetLoadCase') -> '_5404.StraightBevelGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6217.StraightBevelGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5404.StraightBevelGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_planet_gear(self, design_entity: '_2112.StraightBevelPlanetGear') -> '_5405.StraightBevelPlanetGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelPlanetGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2112.StraightBevelPlanetGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5405.StraightBevelPlanetGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_planet_gear_load_case(self, design_entity_analysis: '_6218.StraightBevelPlanetGearLoadCase') -> '_5405.StraightBevelPlanetGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelPlanetGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6218.StraightBevelPlanetGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5405.StraightBevelPlanetGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_sun_gear(self, design_entity: '_2113.StraightBevelSunGear') -> '_5406.StraightBevelSunGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelSunGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2113.StraightBevelSunGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5406.StraightBevelSunGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_sun_gear_load_case(self, design_entity_analysis: '_6219.StraightBevelSunGearLoadCase') -> '_5406.StraightBevelSunGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelSunGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelSunGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6219.StraightBevelSunGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5406.StraightBevelSunGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_worm_gear(self, design_entity: '_2114.WormGear') -> '_5418.WormGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.WormGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2114.WormGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5418.WormGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_load_case(self, design_entity_analysis: '_6236.WormGearLoadCase') -> '_5418.WormGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.WormGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6236.WormGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5418.WormGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_set(self, design_entity: '_2115.WormGearSet') -> '_5420.WormGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.WormGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2115.WormGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_5420.WormGearSetGearWhineAnalysis)(method_result) if method_result else None
