'''_2194.py

ParametricStudyToolAnalysis
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
from mastapy.system_model.analyses_and_results.parametric_study_tools import (
    _3620, _3622, _3623, _3579,
    _3578, _3495, _3508, _3507,
    _3513, _3512, _3524, _3523,
    _3526, _3527, _3585, _3590,
    _3588, _3586, _3599, _3598,
    _3609, _3608, _3610, _3611,
    _3613, _3614, _3615, _3525,
    _3494, _3509, _3520, _3552,
    _3580, _3587, _3592, _3496,
    _3514, _3540, _3600, _3501,
    _3517, _3489, _3528, _3548,
    _3553, _3556, _3559, _3594,
    _3603, _3618, _3621, _3544,
    _3577, _3506, _3511, _3522,
    _3597, _3612, _3487, _3488,
    _3493, _3505, _3504, _3510,
    _3521, _3532, _3539, _3543,
    _3492, _3547, _3551, _3562,
    _3563, _3565, _3566, _3576,
    _3582, _3583, _3584, _3589,
    _3593, _3616, _3617, _3591,
    _3515, _3516, _3541, _3542,
    _3490, _3491, _3497, _3498,
    _3499, _3500, _3502, _3503,
    _3518, _3519, _3529, _3530,
    _3531, _3545, _3546, _3549,
    _3550, _3554, _3555, _3557,
    _3558, _3560, _3561, _3581,
    _3595, _3596, _3601, _3602,
    _3604, _3605, _3606, _3607,
    _3619
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

_PARAMETRIC_STUDY_TOOL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'ParametricStudyToolAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ParametricStudyToolAnalysis',)


class ParametricStudyToolAnalysis(_2177.SingleAnalysis):
    '''ParametricStudyToolAnalysis

    This is a mastapy class.
    '''

    TYPE = _PARAMETRIC_STUDY_TOOL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ParametricStudyToolAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def results_for_worm_gear_set_load_case(self, design_entity_analysis: '_6238.WormGearSetLoadCase') -> '_3620.WormGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.WormGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6238.WormGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3620.WormGearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_zerol_bevel_gear(self, design_entity: '_2116.ZerolBevelGear') -> '_3622.ZerolBevelGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ZerolBevelGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2116.ZerolBevelGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3622.ZerolBevelGearParametricStudyTool)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_load_case(self, design_entity_analysis: '_6239.ZerolBevelGearLoadCase') -> '_3622.ZerolBevelGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ZerolBevelGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6239.ZerolBevelGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3622.ZerolBevelGearParametricStudyTool)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_set(self, design_entity: '_2117.ZerolBevelGearSet') -> '_3623.ZerolBevelGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ZerolBevelGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2117.ZerolBevelGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3623.ZerolBevelGearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_set_load_case(self, design_entity_analysis: '_6241.ZerolBevelGearSetLoadCase') -> '_3623.ZerolBevelGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ZerolBevelGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6241.ZerolBevelGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3623.ZerolBevelGearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling(self, design_entity: '_2146.PartToPartShearCoupling') -> '_3579.PartToPartShearCouplingParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCoupling)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.PartToPartShearCouplingParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2146.PartToPartShearCoupling.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3579.PartToPartShearCouplingParametricStudyTool)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_load_case(self, design_entity_analysis: '_6185.PartToPartShearCouplingLoadCase') -> '_3579.PartToPartShearCouplingParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.PartToPartShearCouplingParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6185.PartToPartShearCouplingLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3579.PartToPartShearCouplingParametricStudyTool)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_half(self, design_entity: '_2147.PartToPartShearCouplingHalf') -> '_3578.PartToPartShearCouplingHalfParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.PartToPartShearCouplingHalfParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2147.PartToPartShearCouplingHalf.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3578.PartToPartShearCouplingHalfParametricStudyTool)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_half_load_case(self, design_entity_analysis: '_6184.PartToPartShearCouplingHalfLoadCase') -> '_3578.PartToPartShearCouplingHalfParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.PartToPartShearCouplingHalfParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6184.PartToPartShearCouplingHalfLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3578.PartToPartShearCouplingHalfParametricStudyTool)(method_result) if method_result else None

    def results_for_belt_drive(self, design_entity: '_2135.BeltDrive') -> '_3495.BeltDriveParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.BeltDriveParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2135.BeltDrive.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3495.BeltDriveParametricStudyTool)(method_result) if method_result else None

    def results_for_belt_drive_load_case(self, design_entity_analysis: '_6083.BeltDriveLoadCase') -> '_3495.BeltDriveParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.BeltDriveParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6083.BeltDriveLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3495.BeltDriveParametricStudyTool)(method_result) if method_result else None

    def results_for_clutch(self, design_entity: '_2137.Clutch') -> '_3508.ClutchParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ClutchParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2137.Clutch.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3508.ClutchParametricStudyTool)(method_result) if method_result else None

    def results_for_clutch_load_case(self, design_entity_analysis: '_6096.ClutchLoadCase') -> '_3508.ClutchParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ClutchParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6096.ClutchLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3508.ClutchParametricStudyTool)(method_result) if method_result else None

    def results_for_clutch_half(self, design_entity: '_2138.ClutchHalf') -> '_3507.ClutchHalfParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ClutchHalfParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2138.ClutchHalf.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3507.ClutchHalfParametricStudyTool)(method_result) if method_result else None

    def results_for_clutch_half_load_case(self, design_entity_analysis: '_6095.ClutchHalfLoadCase') -> '_3507.ClutchHalfParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ClutchHalfParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6095.ClutchHalfLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3507.ClutchHalfParametricStudyTool)(method_result) if method_result else None

    def results_for_concept_coupling(self, design_entity: '_2140.ConceptCoupling') -> '_3513.ConceptCouplingParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ConceptCouplingParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2140.ConceptCoupling.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3513.ConceptCouplingParametricStudyTool)(method_result) if method_result else None

    def results_for_concept_coupling_load_case(self, design_entity_analysis: '_6101.ConceptCouplingLoadCase') -> '_3513.ConceptCouplingParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ConceptCouplingParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6101.ConceptCouplingLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3513.ConceptCouplingParametricStudyTool)(method_result) if method_result else None

    def results_for_concept_coupling_half(self, design_entity: '_2141.ConceptCouplingHalf') -> '_3512.ConceptCouplingHalfParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ConceptCouplingHalfParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2141.ConceptCouplingHalf.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3512.ConceptCouplingHalfParametricStudyTool)(method_result) if method_result else None

    def results_for_concept_coupling_half_load_case(self, design_entity_analysis: '_6100.ConceptCouplingHalfLoadCase') -> '_3512.ConceptCouplingHalfParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ConceptCouplingHalfParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6100.ConceptCouplingHalfLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3512.ConceptCouplingHalfParametricStudyTool)(method_result) if method_result else None

    def results_for_coupling(self, design_entity: '_2142.Coupling') -> '_3524.CouplingParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.CouplingParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2142.Coupling.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3524.CouplingParametricStudyTool)(method_result) if method_result else None

    def results_for_coupling_load_case(self, design_entity_analysis: '_6114.CouplingLoadCase') -> '_3524.CouplingParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.CouplingParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6114.CouplingLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3524.CouplingParametricStudyTool)(method_result) if method_result else None

    def results_for_coupling_half(self, design_entity: '_2143.CouplingHalf') -> '_3523.CouplingHalfParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.CouplingHalfParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2143.CouplingHalf.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3523.CouplingHalfParametricStudyTool)(method_result) if method_result else None

    def results_for_coupling_half_load_case(self, design_entity_analysis: '_6113.CouplingHalfLoadCase') -> '_3523.CouplingHalfParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.CouplingHalfParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6113.CouplingHalfLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3523.CouplingHalfParametricStudyTool)(method_result) if method_result else None

    def results_for_cvt(self, design_entity: '_2144.CVT') -> '_3526.CVTParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.CVTParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2144.CVT.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3526.CVTParametricStudyTool)(method_result) if method_result else None

    def results_for_cvt_load_case(self, design_entity_analysis: '_6116.CVTLoadCase') -> '_3526.CVTParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.CVTParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6116.CVTLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3526.CVTParametricStudyTool)(method_result) if method_result else None

    def results_for_cvt_pulley(self, design_entity: '_2145.CVTPulley') -> '_3527.CVTPulleyParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.CVTPulleyParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2145.CVTPulley.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3527.CVTPulleyParametricStudyTool)(method_result) if method_result else None

    def results_for_cvt_pulley_load_case(self, design_entity_analysis: '_6117.CVTPulleyLoadCase') -> '_3527.CVTPulleyParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTPulleyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.CVTPulleyParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6117.CVTPulleyLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3527.CVTPulleyParametricStudyTool)(method_result) if method_result else None

    def results_for_pulley(self, design_entity: '_2148.Pulley') -> '_3585.PulleyParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.PulleyParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2148.Pulley.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3585.PulleyParametricStudyTool)(method_result) if method_result else None

    def results_for_pulley_load_case(self, design_entity_analysis: '_6194.PulleyLoadCase') -> '_3585.PulleyParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PulleyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.PulleyParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6194.PulleyLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3585.PulleyParametricStudyTool)(method_result) if method_result else None

    def results_for_shaft_hub_connection(self, design_entity: '_2156.ShaftHubConnection') -> '_3590.ShaftHubConnectionParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ShaftHubConnectionParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2156.ShaftHubConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3590.ShaftHubConnectionParametricStudyTool)(method_result) if method_result else None

    def results_for_shaft_hub_connection_load_case(self, design_entity_analysis: '_6200.ShaftHubConnectionLoadCase') -> '_3590.ShaftHubConnectionParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ShaftHubConnectionParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6200.ShaftHubConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3590.ShaftHubConnectionParametricStudyTool)(method_result) if method_result else None

    def results_for_rolling_ring(self, design_entity: '_2154.RollingRing') -> '_3588.RollingRingParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.RollingRingParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2154.RollingRing.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3588.RollingRingParametricStudyTool)(method_result) if method_result else None

    def results_for_rolling_ring_load_case(self, design_entity_analysis: '_6198.RollingRingLoadCase') -> '_3588.RollingRingParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.RollingRingParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6198.RollingRingLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3588.RollingRingParametricStudyTool)(method_result) if method_result else None

    def results_for_rolling_ring_assembly(self, design_entity: '_2155.RollingRingAssembly') -> '_3586.RollingRingAssemblyParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.RollingRingAssemblyParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2155.RollingRingAssembly.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3586.RollingRingAssemblyParametricStudyTool)(method_result) if method_result else None

    def results_for_rolling_ring_assembly_load_case(self, design_entity_analysis: '_6196.RollingRingAssemblyLoadCase') -> '_3586.RollingRingAssemblyParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.RollingRingAssemblyParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6196.RollingRingAssemblyLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3586.RollingRingAssemblyParametricStudyTool)(method_result) if method_result else None

    def results_for_spring_damper(self, design_entity: '_2157.SpringDamper') -> '_3599.SpringDamperParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.SpringDamperParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2157.SpringDamper.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3599.SpringDamperParametricStudyTool)(method_result) if method_result else None

    def results_for_spring_damper_load_case(self, design_entity_analysis: '_6210.SpringDamperLoadCase') -> '_3599.SpringDamperParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.SpringDamperParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6210.SpringDamperLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3599.SpringDamperParametricStudyTool)(method_result) if method_result else None

    def results_for_spring_damper_half(self, design_entity: '_2158.SpringDamperHalf') -> '_3598.SpringDamperHalfParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.SpringDamperHalfParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2158.SpringDamperHalf.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3598.SpringDamperHalfParametricStudyTool)(method_result) if method_result else None

    def results_for_spring_damper_half_load_case(self, design_entity_analysis: '_6209.SpringDamperHalfLoadCase') -> '_3598.SpringDamperHalfParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.SpringDamperHalfParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6209.SpringDamperHalfLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3598.SpringDamperHalfParametricStudyTool)(method_result) if method_result else None

    def results_for_synchroniser(self, design_entity: '_2159.Synchroniser') -> '_3609.SynchroniserParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.SynchroniserParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2159.Synchroniser.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3609.SynchroniserParametricStudyTool)(method_result) if method_result else None

    def results_for_synchroniser_load_case(self, design_entity_analysis: '_6221.SynchroniserLoadCase') -> '_3609.SynchroniserParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.SynchroniserParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6221.SynchroniserLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3609.SynchroniserParametricStudyTool)(method_result) if method_result else None

    def results_for_synchroniser_half(self, design_entity: '_2161.SynchroniserHalf') -> '_3608.SynchroniserHalfParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.SynchroniserHalfParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2161.SynchroniserHalf.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3608.SynchroniserHalfParametricStudyTool)(method_result) if method_result else None

    def results_for_synchroniser_half_load_case(self, design_entity_analysis: '_6220.SynchroniserHalfLoadCase') -> '_3608.SynchroniserHalfParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.SynchroniserHalfParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6220.SynchroniserHalfLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3608.SynchroniserHalfParametricStudyTool)(method_result) if method_result else None

    def results_for_synchroniser_part(self, design_entity: '_2162.SynchroniserPart') -> '_3610.SynchroniserPartParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.SynchroniserPartParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2162.SynchroniserPart.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3610.SynchroniserPartParametricStudyTool)(method_result) if method_result else None

    def results_for_synchroniser_part_load_case(self, design_entity_analysis: '_6222.SynchroniserPartLoadCase') -> '_3610.SynchroniserPartParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserPartLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.SynchroniserPartParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6222.SynchroniserPartLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3610.SynchroniserPartParametricStudyTool)(method_result) if method_result else None

    def results_for_synchroniser_sleeve(self, design_entity: '_2163.SynchroniserSleeve') -> '_3611.SynchroniserSleeveParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.SynchroniserSleeveParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2163.SynchroniserSleeve.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3611.SynchroniserSleeveParametricStudyTool)(method_result) if method_result else None

    def results_for_synchroniser_sleeve_load_case(self, design_entity_analysis: '_6223.SynchroniserSleeveLoadCase') -> '_3611.SynchroniserSleeveParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.SynchroniserSleeveParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6223.SynchroniserSleeveLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3611.SynchroniserSleeveParametricStudyTool)(method_result) if method_result else None

    def results_for_torque_converter(self, design_entity: '_2164.TorqueConverter') -> '_3613.TorqueConverterParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.TorqueConverterParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2164.TorqueConverter.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3613.TorqueConverterParametricStudyTool)(method_result) if method_result else None

    def results_for_torque_converter_load_case(self, design_entity_analysis: '_6227.TorqueConverterLoadCase') -> '_3613.TorqueConverterParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.TorqueConverterParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6227.TorqueConverterLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3613.TorqueConverterParametricStudyTool)(method_result) if method_result else None

    def results_for_torque_converter_pump(self, design_entity: '_2165.TorqueConverterPump') -> '_3614.TorqueConverterPumpParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.TorqueConverterPumpParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2165.TorqueConverterPump.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3614.TorqueConverterPumpParametricStudyTool)(method_result) if method_result else None

    def results_for_torque_converter_pump_load_case(self, design_entity_analysis: '_6228.TorqueConverterPumpLoadCase') -> '_3614.TorqueConverterPumpParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.TorqueConverterPumpParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6228.TorqueConverterPumpLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3614.TorqueConverterPumpParametricStudyTool)(method_result) if method_result else None

    def results_for_torque_converter_turbine(self, design_entity: '_2167.TorqueConverterTurbine') -> '_3615.TorqueConverterTurbineParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.TorqueConverterTurbineParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2167.TorqueConverterTurbine.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3615.TorqueConverterTurbineParametricStudyTool)(method_result) if method_result else None

    def results_for_torque_converter_turbine_load_case(self, design_entity_analysis: '_6229.TorqueConverterTurbineLoadCase') -> '_3615.TorqueConverterTurbineParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.TorqueConverterTurbineParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6229.TorqueConverterTurbineLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3615.TorqueConverterTurbineParametricStudyTool)(method_result) if method_result else None

    def results_for_cvt_belt_connection(self, design_entity: '_1858.CVTBeltConnection') -> '_3525.CVTBeltConnectionParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.CVTBeltConnectionParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1858.CVTBeltConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3525.CVTBeltConnectionParametricStudyTool)(method_result) if method_result else None

    def results_for_cvt_belt_connection_load_case(self, design_entity_analysis: '_6115.CVTBeltConnectionLoadCase') -> '_3525.CVTBeltConnectionParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTBeltConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.CVTBeltConnectionParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6115.CVTBeltConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3525.CVTBeltConnectionParametricStudyTool)(method_result) if method_result else None

    def results_for_belt_connection(self, design_entity: '_1853.BeltConnection') -> '_3494.BeltConnectionParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.BeltConnectionParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1853.BeltConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3494.BeltConnectionParametricStudyTool)(method_result) if method_result else None

    def results_for_belt_connection_load_case(self, design_entity_analysis: '_6082.BeltConnectionLoadCase') -> '_3494.BeltConnectionParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.BeltConnectionParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6082.BeltConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3494.BeltConnectionParametricStudyTool)(method_result) if method_result else None

    def results_for_coaxial_connection(self, design_entity: '_1854.CoaxialConnection') -> '_3509.CoaxialConnectionParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.CoaxialConnectionParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1854.CoaxialConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3509.CoaxialConnectionParametricStudyTool)(method_result) if method_result else None

    def results_for_coaxial_connection_load_case(self, design_entity_analysis: '_6097.CoaxialConnectionLoadCase') -> '_3509.CoaxialConnectionParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.CoaxialConnectionParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6097.CoaxialConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3509.CoaxialConnectionParametricStudyTool)(method_result) if method_result else None

    def results_for_connection(self, design_entity: '_1857.Connection') -> '_3520.ConnectionParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ConnectionParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1857.Connection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3520.ConnectionParametricStudyTool)(method_result) if method_result else None

    def results_for_connection_load_case(self, design_entity_analysis: '_6110.ConnectionLoadCase') -> '_3520.ConnectionParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ConnectionParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6110.ConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3520.ConnectionParametricStudyTool)(method_result) if method_result else None

    def results_for_inter_mountable_component_connection(self, design_entity: '_1866.InterMountableComponentConnection') -> '_3552.InterMountableComponentConnectionParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.InterMountableComponentConnectionParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1866.InterMountableComponentConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3552.InterMountableComponentConnectionParametricStudyTool)(method_result) if method_result else None

    def results_for_inter_mountable_component_connection_load_case(self, design_entity_analysis: '_6165.InterMountableComponentConnectionLoadCase') -> '_3552.InterMountableComponentConnectionParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.InterMountableComponentConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.InterMountableComponentConnectionParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6165.InterMountableComponentConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3552.InterMountableComponentConnectionParametricStudyTool)(method_result) if method_result else None

    def results_for_planetary_connection(self, design_entity: '_1869.PlanetaryConnection') -> '_3580.PlanetaryConnectionParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.PlanetaryConnectionParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1869.PlanetaryConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3580.PlanetaryConnectionParametricStudyTool)(method_result) if method_result else None

    def results_for_planetary_connection_load_case(self, design_entity_analysis: '_6186.PlanetaryConnectionLoadCase') -> '_3580.PlanetaryConnectionParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.PlanetaryConnectionParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6186.PlanetaryConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3580.PlanetaryConnectionParametricStudyTool)(method_result) if method_result else None

    def results_for_rolling_ring_connection(self, design_entity: '_1873.RollingRingConnection') -> '_3587.RollingRingConnectionParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.RollingRingConnectionParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1873.RollingRingConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3587.RollingRingConnectionParametricStudyTool)(method_result) if method_result else None

    def results_for_rolling_ring_connection_load_case(self, design_entity_analysis: '_6197.RollingRingConnectionLoadCase') -> '_3587.RollingRingConnectionParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.RollingRingConnectionParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6197.RollingRingConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3587.RollingRingConnectionParametricStudyTool)(method_result) if method_result else None

    def results_for_shaft_to_mountable_component_connection(self, design_entity: '_1877.ShaftToMountableComponentConnection') -> '_3592.ShaftToMountableComponentConnectionParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ShaftToMountableComponentConnectionParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1877.ShaftToMountableComponentConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3592.ShaftToMountableComponentConnectionParametricStudyTool)(method_result) if method_result else None

    def results_for_shaft_to_mountable_component_connection_load_case(self, design_entity_analysis: '_6202.ShaftToMountableComponentConnectionLoadCase') -> '_3592.ShaftToMountableComponentConnectionParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftToMountableComponentConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ShaftToMountableComponentConnectionParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6202.ShaftToMountableComponentConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3592.ShaftToMountableComponentConnectionParametricStudyTool)(method_result) if method_result else None

    def results_for_bevel_differential_gear_mesh(self, design_entity: '_1883.BevelDifferentialGearMesh') -> '_3496.BevelDifferentialGearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.BevelDifferentialGearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1883.BevelDifferentialGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3496.BevelDifferentialGearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_bevel_differential_gear_mesh_load_case(self, design_entity_analysis: '_6085.BevelDifferentialGearMeshLoadCase') -> '_3496.BevelDifferentialGearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.BevelDifferentialGearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6085.BevelDifferentialGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3496.BevelDifferentialGearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_concept_gear_mesh(self, design_entity: '_1887.ConceptGearMesh') -> '_3514.ConceptGearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ConceptGearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1887.ConceptGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3514.ConceptGearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_concept_gear_mesh_load_case(self, design_entity_analysis: '_6103.ConceptGearMeshLoadCase') -> '_3514.ConceptGearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ConceptGearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6103.ConceptGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3514.ConceptGearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_face_gear_mesh(self, design_entity: '_1893.FaceGearMesh') -> '_3540.FaceGearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.FaceGearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1893.FaceGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3540.FaceGearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_face_gear_mesh_load_case(self, design_entity_analysis: '_6141.FaceGearMeshLoadCase') -> '_3540.FaceGearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.FaceGearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6141.FaceGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3540.FaceGearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_mesh(self, design_entity: '_1907.StraightBevelDiffGearMesh') -> '_3600.StraightBevelDiffGearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.StraightBevelDiffGearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1907.StraightBevelDiffGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3600.StraightBevelDiffGearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_mesh_load_case(self, design_entity_analysis: '_6213.StraightBevelDiffGearMeshLoadCase') -> '_3600.StraightBevelDiffGearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.StraightBevelDiffGearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6213.StraightBevelDiffGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3600.StraightBevelDiffGearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_bevel_gear_mesh(self, design_entity: '_1885.BevelGearMesh') -> '_3501.BevelGearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.BevelGearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1885.BevelGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3501.BevelGearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6090.BevelGearMeshLoadCase') -> '_3501.BevelGearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.BevelGearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6090.BevelGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3501.BevelGearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_conical_gear_mesh(self, design_entity: '_1889.ConicalGearMesh') -> '_3517.ConicalGearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ConicalGearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1889.ConicalGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3517.ConicalGearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_conical_gear_mesh_load_case(self, design_entity_analysis: '_6107.ConicalGearMeshLoadCase') -> '_3517.ConicalGearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ConicalGearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6107.ConicalGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3517.ConicalGearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_mesh(self, design_entity: '_1881.AGMAGleasonConicalGearMesh') -> '_3489.AGMAGleasonConicalGearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.AGMAGleasonConicalGearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1881.AGMAGleasonConicalGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3489.AGMAGleasonConicalGearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_mesh_load_case(self, design_entity_analysis: '_6077.AGMAGleasonConicalGearMeshLoadCase') -> '_3489.AGMAGleasonConicalGearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.AGMAGleasonConicalGearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6077.AGMAGleasonConicalGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3489.AGMAGleasonConicalGearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_cylindrical_gear_mesh(self, design_entity: '_1891.CylindricalGearMesh') -> '_3528.CylindricalGearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.CylindricalGearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1891.CylindricalGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3528.CylindricalGearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_cylindrical_gear_mesh_load_case(self, design_entity_analysis: '_6120.CylindricalGearMeshLoadCase') -> '_3528.CylindricalGearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.CylindricalGearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6120.CylindricalGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3528.CylindricalGearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_hypoid_gear_mesh(self, design_entity: '_1897.HypoidGearMesh') -> '_3548.HypoidGearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.HypoidGearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1897.HypoidGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3548.HypoidGearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_hypoid_gear_mesh_load_case(self, design_entity_analysis: '_6161.HypoidGearMeshLoadCase') -> '_3548.HypoidGearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.HypoidGearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6161.HypoidGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3548.HypoidGearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(self, design_entity: '_1900.KlingelnbergCycloPalloidConicalGearMesh') -> '_3553.KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1900.KlingelnbergCycloPalloidConicalGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3553.KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(self, design_entity_analysis: '_6167.KlingelnbergCycloPalloidConicalGearMeshLoadCase') -> '_3553.KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6167.KlingelnbergCycloPalloidConicalGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3553.KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self, design_entity: '_1901.KlingelnbergCycloPalloidHypoidGearMesh') -> '_3556.KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1901.KlingelnbergCycloPalloidHypoidGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3556.KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(self, design_entity_analysis: '_6170.KlingelnbergCycloPalloidHypoidGearMeshLoadCase') -> '_3556.KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6170.KlingelnbergCycloPalloidHypoidGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3556.KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self, design_entity: '_1902.KlingelnbergCycloPalloidSpiralBevelGearMesh') -> '_3559.KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1902.KlingelnbergCycloPalloidSpiralBevelGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3559.KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6173.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase') -> '_3559.KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6173.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3559.KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_mesh(self, design_entity: '_1905.SpiralBevelGearMesh') -> '_3594.SpiralBevelGearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.SpiralBevelGearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1905.SpiralBevelGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3594.SpiralBevelGearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6206.SpiralBevelGearMeshLoadCase') -> '_3594.SpiralBevelGearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.SpiralBevelGearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6206.SpiralBevelGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3594.SpiralBevelGearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_straight_bevel_gear_mesh(self, design_entity: '_1909.StraightBevelGearMesh') -> '_3603.StraightBevelGearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.StraightBevelGearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1909.StraightBevelGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3603.StraightBevelGearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_straight_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6216.StraightBevelGearMeshLoadCase') -> '_3603.StraightBevelGearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.StraightBevelGearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6216.StraightBevelGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3603.StraightBevelGearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_worm_gear_mesh(self, design_entity: '_1911.WormGearMesh') -> '_3618.WormGearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.WormGearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1911.WormGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3618.WormGearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_worm_gear_mesh_load_case(self, design_entity_analysis: '_6237.WormGearMeshLoadCase') -> '_3618.WormGearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.WormGearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6237.WormGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3618.WormGearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_mesh(self, design_entity: '_1913.ZerolBevelGearMesh') -> '_3621.ZerolBevelGearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ZerolBevelGearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1913.ZerolBevelGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3621.ZerolBevelGearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6240.ZerolBevelGearMeshLoadCase') -> '_3621.ZerolBevelGearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ZerolBevelGearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6240.ZerolBevelGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3621.ZerolBevelGearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_gear_mesh(self, design_entity: '_1895.GearMesh') -> '_3544.GearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.GearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1895.GearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3544.GearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_gear_mesh_load_case(self, design_entity_analysis: '_6147.GearMeshLoadCase') -> '_3544.GearMeshParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.GearMeshParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6147.GearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3544.GearMeshParametricStudyTool)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_connection(self, design_entity: '_1921.PartToPartShearCouplingConnection') -> '_3577.PartToPartShearCouplingConnectionParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.PartToPartShearCouplingConnectionParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1921.PartToPartShearCouplingConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3577.PartToPartShearCouplingConnectionParametricStudyTool)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_connection_load_case(self, design_entity_analysis: '_6183.PartToPartShearCouplingConnectionLoadCase') -> '_3577.PartToPartShearCouplingConnectionParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.PartToPartShearCouplingConnectionParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6183.PartToPartShearCouplingConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3577.PartToPartShearCouplingConnectionParametricStudyTool)(method_result) if method_result else None

    def results_for_clutch_connection(self, design_entity: '_1915.ClutchConnection') -> '_3506.ClutchConnectionParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ClutchConnectionParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1915.ClutchConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3506.ClutchConnectionParametricStudyTool)(method_result) if method_result else None

    def results_for_clutch_connection_load_case(self, design_entity_analysis: '_6094.ClutchConnectionLoadCase') -> '_3506.ClutchConnectionParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ClutchConnectionParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6094.ClutchConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3506.ClutchConnectionParametricStudyTool)(method_result) if method_result else None

    def results_for_concept_coupling_connection(self, design_entity: '_1917.ConceptCouplingConnection') -> '_3511.ConceptCouplingConnectionParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ConceptCouplingConnectionParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1917.ConceptCouplingConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3511.ConceptCouplingConnectionParametricStudyTool)(method_result) if method_result else None

    def results_for_concept_coupling_connection_load_case(self, design_entity_analysis: '_6099.ConceptCouplingConnectionLoadCase') -> '_3511.ConceptCouplingConnectionParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ConceptCouplingConnectionParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6099.ConceptCouplingConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3511.ConceptCouplingConnectionParametricStudyTool)(method_result) if method_result else None

    def results_for_coupling_connection(self, design_entity: '_1919.CouplingConnection') -> '_3522.CouplingConnectionParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.CouplingConnectionParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1919.CouplingConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3522.CouplingConnectionParametricStudyTool)(method_result) if method_result else None

    def results_for_coupling_connection_load_case(self, design_entity_analysis: '_6112.CouplingConnectionLoadCase') -> '_3522.CouplingConnectionParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.CouplingConnectionParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6112.CouplingConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3522.CouplingConnectionParametricStudyTool)(method_result) if method_result else None

    def results_for_spring_damper_connection(self, design_entity: '_1923.SpringDamperConnection') -> '_3597.SpringDamperConnectionParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.SpringDamperConnectionParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1923.SpringDamperConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3597.SpringDamperConnectionParametricStudyTool)(method_result) if method_result else None

    def results_for_spring_damper_connection_load_case(self, design_entity_analysis: '_6208.SpringDamperConnectionLoadCase') -> '_3597.SpringDamperConnectionParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.SpringDamperConnectionParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6208.SpringDamperConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3597.SpringDamperConnectionParametricStudyTool)(method_result) if method_result else None

    def results_for_torque_converter_connection(self, design_entity: '_1925.TorqueConverterConnection') -> '_3612.TorqueConverterConnectionParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.TorqueConverterConnectionParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1925.TorqueConverterConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3612.TorqueConverterConnectionParametricStudyTool)(method_result) if method_result else None

    def results_for_torque_converter_connection_load_case(self, design_entity_analysis: '_6226.TorqueConverterConnectionLoadCase') -> '_3612.TorqueConverterConnectionParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.TorqueConverterConnectionParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6226.TorqueConverterConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3612.TorqueConverterConnectionParametricStudyTool)(method_result) if method_result else None

    def results_for_abstract_assembly(self, design_entity: '_2003.AbstractAssembly') -> '_3487.AbstractAssemblyParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.AbstractAssemblyParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2003.AbstractAssembly.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3487.AbstractAssemblyParametricStudyTool)(method_result) if method_result else None

    def results_for_abstract_assembly_load_case(self, design_entity_analysis: '_6073.AbstractAssemblyLoadCase') -> '_3487.AbstractAssemblyParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.AbstractAssemblyParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6073.AbstractAssemblyLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3487.AbstractAssemblyParametricStudyTool)(method_result) if method_result else None

    def results_for_abstract_shaft_or_housing(self, design_entity: '_2004.AbstractShaftOrHousing') -> '_3488.AbstractShaftOrHousingParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.AbstractShaftOrHousingParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2004.AbstractShaftOrHousing.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3488.AbstractShaftOrHousingParametricStudyTool)(method_result) if method_result else None

    def results_for_abstract_shaft_or_housing_load_case(self, design_entity_analysis: '_6074.AbstractShaftOrHousingLoadCase') -> '_3488.AbstractShaftOrHousingParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractShaftOrHousingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.AbstractShaftOrHousingParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6074.AbstractShaftOrHousingLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3488.AbstractShaftOrHousingParametricStudyTool)(method_result) if method_result else None

    def results_for_bearing(self, design_entity: '_2007.Bearing') -> '_3493.BearingParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.BearingParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2007.Bearing.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3493.BearingParametricStudyTool)(method_result) if method_result else None

    def results_for_bearing_load_case(self, design_entity_analysis: '_6081.BearingLoadCase') -> '_3493.BearingParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BearingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.BearingParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6081.BearingLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3493.BearingParametricStudyTool)(method_result) if method_result else None

    def results_for_bolt(self, design_entity: '_2009.Bolt') -> '_3505.BoltParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.BoltParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2009.Bolt.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3505.BoltParametricStudyTool)(method_result) if method_result else None

    def results_for_bolt_load_case(self, design_entity_analysis: '_6093.BoltLoadCase') -> '_3505.BoltParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.BoltParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6093.BoltLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3505.BoltParametricStudyTool)(method_result) if method_result else None

    def results_for_bolted_joint(self, design_entity: '_2010.BoltedJoint') -> '_3504.BoltedJointParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.BoltedJointParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2010.BoltedJoint.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3504.BoltedJointParametricStudyTool)(method_result) if method_result else None

    def results_for_bolted_joint_load_case(self, design_entity_analysis: '_6092.BoltedJointLoadCase') -> '_3504.BoltedJointParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltedJointLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.BoltedJointParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6092.BoltedJointLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3504.BoltedJointParametricStudyTool)(method_result) if method_result else None

    def results_for_component(self, design_entity: '_2011.Component') -> '_3510.ComponentParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Component)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ComponentParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2011.Component.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3510.ComponentParametricStudyTool)(method_result) if method_result else None

    def results_for_component_load_case(self, design_entity_analysis: '_6098.ComponentLoadCase') -> '_3510.ComponentParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ComponentParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6098.ComponentLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3510.ComponentParametricStudyTool)(method_result) if method_result else None

    def results_for_connector(self, design_entity: '_2014.Connector') -> '_3521.ConnectorParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Connector)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ConnectorParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2014.Connector.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3521.ConnectorParametricStudyTool)(method_result) if method_result else None

    def results_for_connector_load_case(self, design_entity_analysis: '_6111.ConnectorLoadCase') -> '_3521.ConnectorParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectorLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ConnectorParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6111.ConnectorLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3521.ConnectorParametricStudyTool)(method_result) if method_result else None

    def results_for_datum(self, design_entity: '_2015.Datum') -> '_3532.DatumParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Datum)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.DatumParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2015.Datum.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3532.DatumParametricStudyTool)(method_result) if method_result else None

    def results_for_datum_load_case(self, design_entity_analysis: '_6126.DatumLoadCase') -> '_3532.DatumParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.DatumLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.DatumParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6126.DatumLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3532.DatumParametricStudyTool)(method_result) if method_result else None

    def results_for_external_cad_model(self, design_entity: '_2018.ExternalCADModel') -> '_3539.ExternalCADModelParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ExternalCADModelParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2018.ExternalCADModel.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3539.ExternalCADModelParametricStudyTool)(method_result) if method_result else None

    def results_for_external_cad_model_load_case(self, design_entity_analysis: '_6139.ExternalCADModelLoadCase') -> '_3539.ExternalCADModelParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ExternalCADModelParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6139.ExternalCADModelLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3539.ExternalCADModelParametricStudyTool)(method_result) if method_result else None

    def results_for_flexible_pin_assembly(self, design_entity: '_2019.FlexiblePinAssembly') -> '_3543.FlexiblePinAssemblyParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.FlexiblePinAssemblyParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2019.FlexiblePinAssembly.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3543.FlexiblePinAssemblyParametricStudyTool)(method_result) if method_result else None

    def results_for_flexible_pin_assembly_load_case(self, design_entity_analysis: '_6143.FlexiblePinAssemblyLoadCase') -> '_3543.FlexiblePinAssemblyParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.FlexiblePinAssemblyParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6143.FlexiblePinAssemblyLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3543.FlexiblePinAssemblyParametricStudyTool)(method_result) if method_result else None

    def results_for_assembly(self, design_entity: '_2002.Assembly') -> '_3492.AssemblyParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.AssemblyParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2002.Assembly.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3492.AssemblyParametricStudyTool)(method_result) if method_result else None

    def results_for_assembly_load_case(self, design_entity_analysis: '_6080.AssemblyLoadCase') -> '_3492.AssemblyParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.AssemblyParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6080.AssemblyLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3492.AssemblyParametricStudyTool)(method_result) if method_result else None

    def results_for_guide_dxf_model(self, design_entity: '_2020.GuideDxfModel') -> '_3547.GuideDxfModelParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.GuideDxfModelParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2020.GuideDxfModel.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3547.GuideDxfModelParametricStudyTool)(method_result) if method_result else None

    def results_for_guide_dxf_model_load_case(self, design_entity_analysis: '_6151.GuideDxfModelLoadCase') -> '_3547.GuideDxfModelParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.GuideDxfModelParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6151.GuideDxfModelLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3547.GuideDxfModelParametricStudyTool)(method_result) if method_result else None

    def results_for_imported_fe_component(self, design_entity: '_2023.ImportedFEComponent') -> '_3551.ImportedFEComponentParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ImportedFEComponent)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ImportedFEComponentParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2023.ImportedFEComponent.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3551.ImportedFEComponentParametricStudyTool)(method_result) if method_result else None

    def results_for_imported_fe_component_load_case(self, design_entity_analysis: '_6163.ImportedFEComponentLoadCase') -> '_3551.ImportedFEComponentParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ImportedFEComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ImportedFEComponentParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6163.ImportedFEComponentLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3551.ImportedFEComponentParametricStudyTool)(method_result) if method_result else None

    def results_for_mass_disc(self, design_entity: '_2027.MassDisc') -> '_3562.MassDiscParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.MassDiscParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2027.MassDisc.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3562.MassDiscParametricStudyTool)(method_result) if method_result else None

    def results_for_mass_disc_load_case(self, design_entity_analysis: '_6175.MassDiscLoadCase') -> '_3562.MassDiscParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MassDiscLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.MassDiscParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6175.MassDiscLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3562.MassDiscParametricStudyTool)(method_result) if method_result else None

    def results_for_measurement_component(self, design_entity: '_2028.MeasurementComponent') -> '_3563.MeasurementComponentParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.MeasurementComponentParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2028.MeasurementComponent.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3563.MeasurementComponentParametricStudyTool)(method_result) if method_result else None

    def results_for_measurement_component_load_case(self, design_entity_analysis: '_6176.MeasurementComponentLoadCase') -> '_3563.MeasurementComponentParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.MeasurementComponentParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6176.MeasurementComponentLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3563.MeasurementComponentParametricStudyTool)(method_result) if method_result else None

    def results_for_mountable_component(self, design_entity: '_2029.MountableComponent') -> '_3565.MountableComponentParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.MountableComponentParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2029.MountableComponent.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3565.MountableComponentParametricStudyTool)(method_result) if method_result else None

    def results_for_mountable_component_load_case(self, design_entity_analysis: '_6178.MountableComponentLoadCase') -> '_3565.MountableComponentParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MountableComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.MountableComponentParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6178.MountableComponentLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3565.MountableComponentParametricStudyTool)(method_result) if method_result else None

    def results_for_oil_seal(self, design_entity: '_2031.OilSeal') -> '_3566.OilSealParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.OilSealParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2031.OilSeal.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3566.OilSealParametricStudyTool)(method_result) if method_result else None

    def results_for_oil_seal_load_case(self, design_entity_analysis: '_6180.OilSealLoadCase') -> '_3566.OilSealParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.OilSealLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.OilSealParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6180.OilSealLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3566.OilSealParametricStudyTool)(method_result) if method_result else None

    def results_for_part(self, design_entity: '_2033.Part') -> '_3576.PartParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Part)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.PartParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2033.Part.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3576.PartParametricStudyTool)(method_result) if method_result else None

    def results_for_part_load_case(self, design_entity_analysis: '_6182.PartLoadCase') -> '_3576.PartParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.PartParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6182.PartLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3576.PartParametricStudyTool)(method_result) if method_result else None

    def results_for_planet_carrier(self, design_entity: '_2034.PlanetCarrier') -> '_3582.PlanetCarrierParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.PlanetCarrierParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2034.PlanetCarrier.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3582.PlanetCarrierParametricStudyTool)(method_result) if method_result else None

    def results_for_planet_carrier_load_case(self, design_entity_analysis: '_6189.PlanetCarrierLoadCase') -> '_3582.PlanetCarrierParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.PlanetCarrierParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6189.PlanetCarrierLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3582.PlanetCarrierParametricStudyTool)(method_result) if method_result else None

    def results_for_point_load(self, design_entity: '_2036.PointLoad') -> '_3583.PointLoadParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.PointLoadParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2036.PointLoad.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3583.PointLoadParametricStudyTool)(method_result) if method_result else None

    def results_for_point_load_load_case(self, design_entity_analysis: '_6192.PointLoadLoadCase') -> '_3583.PointLoadParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.PointLoadParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6192.PointLoadLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3583.PointLoadParametricStudyTool)(method_result) if method_result else None

    def results_for_power_load(self, design_entity: '_2037.PowerLoad') -> '_3584.PowerLoadParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.PowerLoadParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2037.PowerLoad.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3584.PowerLoadParametricStudyTool)(method_result) if method_result else None

    def results_for_power_load_load_case(self, design_entity_analysis: '_6193.PowerLoadLoadCase') -> '_3584.PowerLoadParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.PowerLoadParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6193.PowerLoadLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3584.PowerLoadParametricStudyTool)(method_result) if method_result else None

    def results_for_root_assembly(self, design_entity: '_2039.RootAssembly') -> '_3589.RootAssemblyParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.RootAssemblyParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2039.RootAssembly.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3589.RootAssemblyParametricStudyTool)(method_result) if method_result else None

    def results_for_root_assembly_load_case(self, design_entity_analysis: '_6199.RootAssemblyLoadCase') -> '_3589.RootAssemblyParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RootAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.RootAssemblyParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6199.RootAssemblyLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3589.RootAssemblyParametricStudyTool)(method_result) if method_result else None

    def results_for_specialised_assembly(self, design_entity: '_2041.SpecialisedAssembly') -> '_3593.SpecialisedAssemblyParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.SpecialisedAssemblyParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2041.SpecialisedAssembly.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3593.SpecialisedAssemblyParametricStudyTool)(method_result) if method_result else None

    def results_for_specialised_assembly_load_case(self, design_entity_analysis: '_6203.SpecialisedAssemblyLoadCase') -> '_3593.SpecialisedAssemblyParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpecialisedAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.SpecialisedAssemblyParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6203.SpecialisedAssemblyLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3593.SpecialisedAssemblyParametricStudyTool)(method_result) if method_result else None

    def results_for_unbalanced_mass(self, design_entity: '_2042.UnbalancedMass') -> '_3616.UnbalancedMassParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.UnbalancedMassParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2042.UnbalancedMass.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3616.UnbalancedMassParametricStudyTool)(method_result) if method_result else None

    def results_for_unbalanced_mass_load_case(self, design_entity_analysis: '_6234.UnbalancedMassLoadCase') -> '_3616.UnbalancedMassParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.UnbalancedMassParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6234.UnbalancedMassLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3616.UnbalancedMassParametricStudyTool)(method_result) if method_result else None

    def results_for_virtual_component(self, design_entity: '_2043.VirtualComponent') -> '_3617.VirtualComponentParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.VirtualComponentParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2043.VirtualComponent.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3617.VirtualComponentParametricStudyTool)(method_result) if method_result else None

    def results_for_virtual_component_load_case(self, design_entity_analysis: '_6235.VirtualComponentLoadCase') -> '_3617.VirtualComponentParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.VirtualComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.VirtualComponentParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6235.VirtualComponentLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3617.VirtualComponentParametricStudyTool)(method_result) if method_result else None

    def results_for_shaft(self, design_entity: '_2046.Shaft') -> '_3591.ShaftParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ShaftParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2046.Shaft.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3591.ShaftParametricStudyTool)(method_result) if method_result else None

    def results_for_shaft_load_case(self, design_entity_analysis: '_6201.ShaftLoadCase') -> '_3591.ShaftParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ShaftParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6201.ShaftLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3591.ShaftParametricStudyTool)(method_result) if method_result else None

    def results_for_concept_gear(self, design_entity: '_2084.ConceptGear') -> '_3515.ConceptGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ConceptGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2084.ConceptGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3515.ConceptGearParametricStudyTool)(method_result) if method_result else None

    def results_for_concept_gear_load_case(self, design_entity_analysis: '_6102.ConceptGearLoadCase') -> '_3515.ConceptGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ConceptGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6102.ConceptGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3515.ConceptGearParametricStudyTool)(method_result) if method_result else None

    def results_for_concept_gear_set(self, design_entity: '_2085.ConceptGearSet') -> '_3516.ConceptGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ConceptGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2085.ConceptGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3516.ConceptGearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_concept_gear_set_load_case(self, design_entity_analysis: '_6104.ConceptGearSetLoadCase') -> '_3516.ConceptGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ConceptGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6104.ConceptGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3516.ConceptGearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_face_gear(self, design_entity: '_2091.FaceGear') -> '_3541.FaceGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.FaceGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2091.FaceGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3541.FaceGearParametricStudyTool)(method_result) if method_result else None

    def results_for_face_gear_load_case(self, design_entity_analysis: '_6140.FaceGearLoadCase') -> '_3541.FaceGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.FaceGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6140.FaceGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3541.FaceGearParametricStudyTool)(method_result) if method_result else None

    def results_for_face_gear_set(self, design_entity: '_2092.FaceGearSet') -> '_3542.FaceGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.FaceGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2092.FaceGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3542.FaceGearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_face_gear_set_load_case(self, design_entity_analysis: '_6142.FaceGearSetLoadCase') -> '_3542.FaceGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.FaceGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6142.FaceGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3542.FaceGearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear(self, design_entity: '_2076.AGMAGleasonConicalGear') -> '_3490.AGMAGleasonConicalGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.AGMAGleasonConicalGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2076.AGMAGleasonConicalGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3490.AGMAGleasonConicalGearParametricStudyTool)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_load_case(self, design_entity_analysis: '_6076.AGMAGleasonConicalGearLoadCase') -> '_3490.AGMAGleasonConicalGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.AGMAGleasonConicalGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6076.AGMAGleasonConicalGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3490.AGMAGleasonConicalGearParametricStudyTool)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_set(self, design_entity: '_2077.AGMAGleasonConicalGearSet') -> '_3491.AGMAGleasonConicalGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.AGMAGleasonConicalGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2077.AGMAGleasonConicalGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3491.AGMAGleasonConicalGearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_set_load_case(self, design_entity_analysis: '_6078.AGMAGleasonConicalGearSetLoadCase') -> '_3491.AGMAGleasonConicalGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.AGMAGleasonConicalGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6078.AGMAGleasonConicalGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3491.AGMAGleasonConicalGearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_bevel_differential_gear(self, design_entity: '_2078.BevelDifferentialGear') -> '_3497.BevelDifferentialGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.BevelDifferentialGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2078.BevelDifferentialGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3497.BevelDifferentialGearParametricStudyTool)(method_result) if method_result else None

    def results_for_bevel_differential_gear_load_case(self, design_entity_analysis: '_6084.BevelDifferentialGearLoadCase') -> '_3497.BevelDifferentialGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.BevelDifferentialGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6084.BevelDifferentialGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3497.BevelDifferentialGearParametricStudyTool)(method_result) if method_result else None

    def results_for_bevel_differential_gear_set(self, design_entity: '_2079.BevelDifferentialGearSet') -> '_3498.BevelDifferentialGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.BevelDifferentialGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2079.BevelDifferentialGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3498.BevelDifferentialGearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_bevel_differential_gear_set_load_case(self, design_entity_analysis: '_6086.BevelDifferentialGearSetLoadCase') -> '_3498.BevelDifferentialGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.BevelDifferentialGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6086.BevelDifferentialGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3498.BevelDifferentialGearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_bevel_differential_planet_gear(self, design_entity: '_2080.BevelDifferentialPlanetGear') -> '_3499.BevelDifferentialPlanetGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.BevelDifferentialPlanetGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2080.BevelDifferentialPlanetGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3499.BevelDifferentialPlanetGearParametricStudyTool)(method_result) if method_result else None

    def results_for_bevel_differential_planet_gear_load_case(self, design_entity_analysis: '_6087.BevelDifferentialPlanetGearLoadCase') -> '_3499.BevelDifferentialPlanetGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.BevelDifferentialPlanetGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6087.BevelDifferentialPlanetGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3499.BevelDifferentialPlanetGearParametricStudyTool)(method_result) if method_result else None

    def results_for_bevel_differential_sun_gear(self, design_entity: '_2081.BevelDifferentialSunGear') -> '_3500.BevelDifferentialSunGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.BevelDifferentialSunGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2081.BevelDifferentialSunGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3500.BevelDifferentialSunGearParametricStudyTool)(method_result) if method_result else None

    def results_for_bevel_differential_sun_gear_load_case(self, design_entity_analysis: '_6088.BevelDifferentialSunGearLoadCase') -> '_3500.BevelDifferentialSunGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialSunGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.BevelDifferentialSunGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6088.BevelDifferentialSunGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3500.BevelDifferentialSunGearParametricStudyTool)(method_result) if method_result else None

    def results_for_bevel_gear(self, design_entity: '_2082.BevelGear') -> '_3502.BevelGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.BevelGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2082.BevelGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3502.BevelGearParametricStudyTool)(method_result) if method_result else None

    def results_for_bevel_gear_load_case(self, design_entity_analysis: '_6089.BevelGearLoadCase') -> '_3502.BevelGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.BevelGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6089.BevelGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3502.BevelGearParametricStudyTool)(method_result) if method_result else None

    def results_for_bevel_gear_set(self, design_entity: '_2083.BevelGearSet') -> '_3503.BevelGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.BevelGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2083.BevelGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3503.BevelGearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_bevel_gear_set_load_case(self, design_entity_analysis: '_6091.BevelGearSetLoadCase') -> '_3503.BevelGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.BevelGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6091.BevelGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3503.BevelGearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_conical_gear(self, design_entity: '_2086.ConicalGear') -> '_3518.ConicalGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ConicalGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2086.ConicalGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3518.ConicalGearParametricStudyTool)(method_result) if method_result else None

    def results_for_conical_gear_load_case(self, design_entity_analysis: '_6105.ConicalGearLoadCase') -> '_3518.ConicalGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ConicalGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6105.ConicalGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3518.ConicalGearParametricStudyTool)(method_result) if method_result else None

    def results_for_conical_gear_set(self, design_entity: '_2087.ConicalGearSet') -> '_3519.ConicalGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ConicalGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2087.ConicalGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3519.ConicalGearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_conical_gear_set_load_case(self, design_entity_analysis: '_6109.ConicalGearSetLoadCase') -> '_3519.ConicalGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.ConicalGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6109.ConicalGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3519.ConicalGearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_cylindrical_gear(self, design_entity: '_2088.CylindricalGear') -> '_3529.CylindricalGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.CylindricalGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2088.CylindricalGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3529.CylindricalGearParametricStudyTool)(method_result) if method_result else None

    def results_for_cylindrical_gear_load_case(self, design_entity_analysis: '_6118.CylindricalGearLoadCase') -> '_3529.CylindricalGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.CylindricalGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6118.CylindricalGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3529.CylindricalGearParametricStudyTool)(method_result) if method_result else None

    def results_for_cylindrical_gear_set(self, design_entity: '_2089.CylindricalGearSet') -> '_3530.CylindricalGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.CylindricalGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2089.CylindricalGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3530.CylindricalGearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_cylindrical_gear_set_load_case(self, design_entity_analysis: '_6122.CylindricalGearSetLoadCase') -> '_3530.CylindricalGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.CylindricalGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6122.CylindricalGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3530.CylindricalGearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_cylindrical_planet_gear(self, design_entity: '_2090.CylindricalPlanetGear') -> '_3531.CylindricalPlanetGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.CylindricalPlanetGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2090.CylindricalPlanetGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3531.CylindricalPlanetGearParametricStudyTool)(method_result) if method_result else None

    def results_for_cylindrical_planet_gear_load_case(self, design_entity_analysis: '_6123.CylindricalPlanetGearLoadCase') -> '_3531.CylindricalPlanetGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.CylindricalPlanetGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6123.CylindricalPlanetGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3531.CylindricalPlanetGearParametricStudyTool)(method_result) if method_result else None

    def results_for_gear(self, design_entity: '_2093.Gear') -> '_3545.GearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.GearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2093.Gear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3545.GearParametricStudyTool)(method_result) if method_result else None

    def results_for_gear_load_case(self, design_entity_analysis: '_6145.GearLoadCase') -> '_3545.GearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.GearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6145.GearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3545.GearParametricStudyTool)(method_result) if method_result else None

    def results_for_gear_set(self, design_entity: '_2095.GearSet') -> '_3546.GearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.GearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2095.GearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3546.GearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_gear_set_load_case(self, design_entity_analysis: '_6150.GearSetLoadCase') -> '_3546.GearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.GearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6150.GearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3546.GearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_hypoid_gear(self, design_entity: '_2097.HypoidGear') -> '_3549.HypoidGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.HypoidGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2097.HypoidGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3549.HypoidGearParametricStudyTool)(method_result) if method_result else None

    def results_for_hypoid_gear_load_case(self, design_entity_analysis: '_6160.HypoidGearLoadCase') -> '_3549.HypoidGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.HypoidGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6160.HypoidGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3549.HypoidGearParametricStudyTool)(method_result) if method_result else None

    def results_for_hypoid_gear_set(self, design_entity: '_2098.HypoidGearSet') -> '_3550.HypoidGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.HypoidGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2098.HypoidGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3550.HypoidGearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_hypoid_gear_set_load_case(self, design_entity_analysis: '_6162.HypoidGearSetLoadCase') -> '_3550.HypoidGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.HypoidGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6162.HypoidGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3550.HypoidGearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear(self, design_entity: '_2099.KlingelnbergCycloPalloidConicalGear') -> '_3554.KlingelnbergCycloPalloidConicalGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.KlingelnbergCycloPalloidConicalGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2099.KlingelnbergCycloPalloidConicalGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3554.KlingelnbergCycloPalloidConicalGearParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_load_case(self, design_entity_analysis: '_6166.KlingelnbergCycloPalloidConicalGearLoadCase') -> '_3554.KlingelnbergCycloPalloidConicalGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.KlingelnbergCycloPalloidConicalGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6166.KlingelnbergCycloPalloidConicalGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3554.KlingelnbergCycloPalloidConicalGearParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(self, design_entity: '_2100.KlingelnbergCycloPalloidConicalGearSet') -> '_3555.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2100.KlingelnbergCycloPalloidConicalGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3555.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set_load_case(self, design_entity_analysis: '_6168.KlingelnbergCycloPalloidConicalGearSetLoadCase') -> '_3555.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6168.KlingelnbergCycloPalloidConicalGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3555.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(self, design_entity: '_2101.KlingelnbergCycloPalloidHypoidGear') -> '_3557.KlingelnbergCycloPalloidHypoidGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.KlingelnbergCycloPalloidHypoidGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2101.KlingelnbergCycloPalloidHypoidGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3557.KlingelnbergCycloPalloidHypoidGearParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_load_case(self, design_entity_analysis: '_6169.KlingelnbergCycloPalloidHypoidGearLoadCase') -> '_3557.KlingelnbergCycloPalloidHypoidGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.KlingelnbergCycloPalloidHypoidGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6169.KlingelnbergCycloPalloidHypoidGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3557.KlingelnbergCycloPalloidHypoidGearParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(self, design_entity: '_2102.KlingelnbergCycloPalloidHypoidGearSet') -> '_3558.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2102.KlingelnbergCycloPalloidHypoidGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3558.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(self, design_entity_analysis: '_6171.KlingelnbergCycloPalloidHypoidGearSetLoadCase') -> '_3558.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6171.KlingelnbergCycloPalloidHypoidGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3558.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(self, design_entity: '_2103.KlingelnbergCycloPalloidSpiralBevelGear') -> '_3560.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2103.KlingelnbergCycloPalloidSpiralBevelGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3560.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(self, design_entity_analysis: '_6172.KlingelnbergCycloPalloidSpiralBevelGearLoadCase') -> '_3560.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6172.KlingelnbergCycloPalloidSpiralBevelGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3560.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, design_entity: '_2104.KlingelnbergCycloPalloidSpiralBevelGearSet') -> '_3561.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2104.KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3561.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(self, design_entity_analysis: '_6174.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase') -> '_3561.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6174.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3561.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_planetary_gear_set(self, design_entity: '_2105.PlanetaryGearSet') -> '_3581.PlanetaryGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.PlanetaryGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2105.PlanetaryGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3581.PlanetaryGearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_planetary_gear_set_load_case(self, design_entity_analysis: '_6187.PlanetaryGearSetLoadCase') -> '_3581.PlanetaryGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.PlanetaryGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6187.PlanetaryGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3581.PlanetaryGearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_spiral_bevel_gear(self, design_entity: '_2106.SpiralBevelGear') -> '_3595.SpiralBevelGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.SpiralBevelGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2106.SpiralBevelGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3595.SpiralBevelGearParametricStudyTool)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_load_case(self, design_entity_analysis: '_6205.SpiralBevelGearLoadCase') -> '_3595.SpiralBevelGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.SpiralBevelGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6205.SpiralBevelGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3595.SpiralBevelGearParametricStudyTool)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_set(self, design_entity: '_2107.SpiralBevelGearSet') -> '_3596.SpiralBevelGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.SpiralBevelGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2107.SpiralBevelGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3596.SpiralBevelGearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_set_load_case(self, design_entity_analysis: '_6207.SpiralBevelGearSetLoadCase') -> '_3596.SpiralBevelGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.SpiralBevelGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6207.SpiralBevelGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3596.SpiralBevelGearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear(self, design_entity: '_2108.StraightBevelDiffGear') -> '_3601.StraightBevelDiffGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.StraightBevelDiffGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2108.StraightBevelDiffGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3601.StraightBevelDiffGearParametricStudyTool)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_load_case(self, design_entity_analysis: '_6212.StraightBevelDiffGearLoadCase') -> '_3601.StraightBevelDiffGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.StraightBevelDiffGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6212.StraightBevelDiffGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3601.StraightBevelDiffGearParametricStudyTool)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_set(self, design_entity: '_2109.StraightBevelDiffGearSet') -> '_3602.StraightBevelDiffGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.StraightBevelDiffGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2109.StraightBevelDiffGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3602.StraightBevelDiffGearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_set_load_case(self, design_entity_analysis: '_6214.StraightBevelDiffGearSetLoadCase') -> '_3602.StraightBevelDiffGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.StraightBevelDiffGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6214.StraightBevelDiffGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3602.StraightBevelDiffGearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_straight_bevel_gear(self, design_entity: '_2110.StraightBevelGear') -> '_3604.StraightBevelGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.StraightBevelGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2110.StraightBevelGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3604.StraightBevelGearParametricStudyTool)(method_result) if method_result else None

    def results_for_straight_bevel_gear_load_case(self, design_entity_analysis: '_6215.StraightBevelGearLoadCase') -> '_3604.StraightBevelGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.StraightBevelGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6215.StraightBevelGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3604.StraightBevelGearParametricStudyTool)(method_result) if method_result else None

    def results_for_straight_bevel_gear_set(self, design_entity: '_2111.StraightBevelGearSet') -> '_3605.StraightBevelGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.StraightBevelGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2111.StraightBevelGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3605.StraightBevelGearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_straight_bevel_gear_set_load_case(self, design_entity_analysis: '_6217.StraightBevelGearSetLoadCase') -> '_3605.StraightBevelGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.StraightBevelGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6217.StraightBevelGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3605.StraightBevelGearSetParametricStudyTool)(method_result) if method_result else None

    def results_for_straight_bevel_planet_gear(self, design_entity: '_2112.StraightBevelPlanetGear') -> '_3606.StraightBevelPlanetGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.StraightBevelPlanetGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2112.StraightBevelPlanetGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3606.StraightBevelPlanetGearParametricStudyTool)(method_result) if method_result else None

    def results_for_straight_bevel_planet_gear_load_case(self, design_entity_analysis: '_6218.StraightBevelPlanetGearLoadCase') -> '_3606.StraightBevelPlanetGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.StraightBevelPlanetGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6218.StraightBevelPlanetGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3606.StraightBevelPlanetGearParametricStudyTool)(method_result) if method_result else None

    def results_for_straight_bevel_sun_gear(self, design_entity: '_2113.StraightBevelSunGear') -> '_3607.StraightBevelSunGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.StraightBevelSunGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2113.StraightBevelSunGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3607.StraightBevelSunGearParametricStudyTool)(method_result) if method_result else None

    def results_for_straight_bevel_sun_gear_load_case(self, design_entity_analysis: '_6219.StraightBevelSunGearLoadCase') -> '_3607.StraightBevelSunGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelSunGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.StraightBevelSunGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6219.StraightBevelSunGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3607.StraightBevelSunGearParametricStudyTool)(method_result) if method_result else None

    def results_for_worm_gear(self, design_entity: '_2114.WormGear') -> '_3619.WormGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.WormGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2114.WormGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3619.WormGearParametricStudyTool)(method_result) if method_result else None

    def results_for_worm_gear_load_case(self, design_entity_analysis: '_6236.WormGearLoadCase') -> '_3619.WormGearParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.WormGearParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6236.WormGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3619.WormGearParametricStudyTool)(method_result) if method_result else None

    def results_for_worm_gear_set(self, design_entity: '_2115.WormGearSet') -> '_3620.WormGearSetParametricStudyTool':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.parametric_study_tools.WormGearSetParametricStudyTool
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2115.WormGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_3620.WormGearSetParametricStudyTool)(method_result) if method_result else None
