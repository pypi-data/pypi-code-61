'''_2191.py

ModalAnalysisAnalysis
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
from mastapy.system_model.analyses_and_results.modal_analyses import (
    _4853, _4855, _4856, _4806,
    _4805, _4731, _4744, _4743,
    _4749, _4748, _4761, _4760,
    _4763, _4764, _4812, _4817,
    _4815, _4813, _4827, _4826,
    _4837, _4836, _4838, _4839,
    _4841, _4842, _4843, _4762,
    _4730, _4745, _4756, _4784,
    _4807, _4814, _4820, _4732,
    _4750, _4771, _4828, _4737,
    _4753, _4725, _4765, _4780,
    _4785, _4788, _4791, _4822,
    _4831, _4851, _4854, _4776,
    _4804, _4742, _4747, _4759,
    _4825, _4840, _4723, _4724,
    _4729, _4741, _4740, _4746,
    _4757, _4769, _4770, _4774,
    _4728, _4779, _4783, _4794,
    _4795, _4800, _4801, _4803,
    _4809, _4810, _4811, _4816,
    _4821, _4844, _4845, _4818,
    _4751, _4752, _4772, _4773,
    _4726, _4727, _4733, _4734,
    _4735, _4736, _4738, _4739,
    _4754, _4755, _4766, _4767,
    _4768, _4777, _4778, _4781,
    _4782, _4786, _4787, _4789,
    _4790, _4792, _4793, _4808,
    _4823, _4824, _4829, _4830,
    _4832, _4833, _4834, _4835,
    _4852
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

_MODAL_ANALYSIS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'ModalAnalysisAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ModalAnalysisAnalysis',)


class ModalAnalysisAnalysis(_2177.SingleAnalysis):
    '''ModalAnalysisAnalysis

    This is a mastapy class.
    '''

    TYPE = _MODAL_ANALYSIS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ModalAnalysisAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def results_for_worm_gear_set_load_case(self, design_entity_analysis: '_6238.WormGearSetLoadCase') -> '_4853.WormGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.WormGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6238.WormGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4853.WormGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear(self, design_entity: '_2116.ZerolBevelGear') -> '_4855.ZerolBevelGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ZerolBevelGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2116.ZerolBevelGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4855.ZerolBevelGearModalAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_load_case(self, design_entity_analysis: '_6239.ZerolBevelGearLoadCase') -> '_4855.ZerolBevelGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ZerolBevelGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6239.ZerolBevelGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4855.ZerolBevelGearModalAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_set(self, design_entity: '_2117.ZerolBevelGearSet') -> '_4856.ZerolBevelGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ZerolBevelGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2117.ZerolBevelGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4856.ZerolBevelGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_set_load_case(self, design_entity_analysis: '_6241.ZerolBevelGearSetLoadCase') -> '_4856.ZerolBevelGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ZerolBevelGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6241.ZerolBevelGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4856.ZerolBevelGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling(self, design_entity: '_2146.PartToPartShearCoupling') -> '_4806.PartToPartShearCouplingModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCoupling)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PartToPartShearCouplingModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2146.PartToPartShearCoupling.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4806.PartToPartShearCouplingModalAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_load_case(self, design_entity_analysis: '_6185.PartToPartShearCouplingLoadCase') -> '_4806.PartToPartShearCouplingModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PartToPartShearCouplingModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6185.PartToPartShearCouplingLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4806.PartToPartShearCouplingModalAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_half(self, design_entity: '_2147.PartToPartShearCouplingHalf') -> '_4805.PartToPartShearCouplingHalfModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PartToPartShearCouplingHalfModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2147.PartToPartShearCouplingHalf.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4805.PartToPartShearCouplingHalfModalAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_half_load_case(self, design_entity_analysis: '_6184.PartToPartShearCouplingHalfLoadCase') -> '_4805.PartToPartShearCouplingHalfModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PartToPartShearCouplingHalfModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6184.PartToPartShearCouplingHalfLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4805.PartToPartShearCouplingHalfModalAnalysis)(method_result) if method_result else None

    def results_for_belt_drive(self, design_entity: '_2135.BeltDrive') -> '_4731.BeltDriveModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BeltDriveModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2135.BeltDrive.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4731.BeltDriveModalAnalysis)(method_result) if method_result else None

    def results_for_belt_drive_load_case(self, design_entity_analysis: '_6083.BeltDriveLoadCase') -> '_4731.BeltDriveModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BeltDriveModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6083.BeltDriveLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4731.BeltDriveModalAnalysis)(method_result) if method_result else None

    def results_for_clutch(self, design_entity: '_2137.Clutch') -> '_4744.ClutchModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ClutchModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2137.Clutch.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4744.ClutchModalAnalysis)(method_result) if method_result else None

    def results_for_clutch_load_case(self, design_entity_analysis: '_6096.ClutchLoadCase') -> '_4744.ClutchModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ClutchModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6096.ClutchLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4744.ClutchModalAnalysis)(method_result) if method_result else None

    def results_for_clutch_half(self, design_entity: '_2138.ClutchHalf') -> '_4743.ClutchHalfModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ClutchHalfModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2138.ClutchHalf.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4743.ClutchHalfModalAnalysis)(method_result) if method_result else None

    def results_for_clutch_half_load_case(self, design_entity_analysis: '_6095.ClutchHalfLoadCase') -> '_4743.ClutchHalfModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ClutchHalfModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6095.ClutchHalfLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4743.ClutchHalfModalAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling(self, design_entity: '_2140.ConceptCoupling') -> '_4749.ConceptCouplingModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConceptCouplingModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2140.ConceptCoupling.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4749.ConceptCouplingModalAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_load_case(self, design_entity_analysis: '_6101.ConceptCouplingLoadCase') -> '_4749.ConceptCouplingModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConceptCouplingModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6101.ConceptCouplingLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4749.ConceptCouplingModalAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_half(self, design_entity: '_2141.ConceptCouplingHalf') -> '_4748.ConceptCouplingHalfModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConceptCouplingHalfModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2141.ConceptCouplingHalf.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4748.ConceptCouplingHalfModalAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_half_load_case(self, design_entity_analysis: '_6100.ConceptCouplingHalfLoadCase') -> '_4748.ConceptCouplingHalfModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConceptCouplingHalfModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6100.ConceptCouplingHalfLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4748.ConceptCouplingHalfModalAnalysis)(method_result) if method_result else None

    def results_for_coupling(self, design_entity: '_2142.Coupling') -> '_4761.CouplingModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CouplingModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2142.Coupling.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4761.CouplingModalAnalysis)(method_result) if method_result else None

    def results_for_coupling_load_case(self, design_entity_analysis: '_6114.CouplingLoadCase') -> '_4761.CouplingModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CouplingModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6114.CouplingLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4761.CouplingModalAnalysis)(method_result) if method_result else None

    def results_for_coupling_half(self, design_entity: '_2143.CouplingHalf') -> '_4760.CouplingHalfModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CouplingHalfModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2143.CouplingHalf.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4760.CouplingHalfModalAnalysis)(method_result) if method_result else None

    def results_for_coupling_half_load_case(self, design_entity_analysis: '_6113.CouplingHalfLoadCase') -> '_4760.CouplingHalfModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CouplingHalfModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6113.CouplingHalfLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4760.CouplingHalfModalAnalysis)(method_result) if method_result else None

    def results_for_cvt(self, design_entity: '_2144.CVT') -> '_4763.CVTModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CVTModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2144.CVT.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4763.CVTModalAnalysis)(method_result) if method_result else None

    def results_for_cvt_load_case(self, design_entity_analysis: '_6116.CVTLoadCase') -> '_4763.CVTModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CVTModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6116.CVTLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4763.CVTModalAnalysis)(method_result) if method_result else None

    def results_for_cvt_pulley(self, design_entity: '_2145.CVTPulley') -> '_4764.CVTPulleyModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CVTPulleyModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2145.CVTPulley.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4764.CVTPulleyModalAnalysis)(method_result) if method_result else None

    def results_for_cvt_pulley_load_case(self, design_entity_analysis: '_6117.CVTPulleyLoadCase') -> '_4764.CVTPulleyModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTPulleyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CVTPulleyModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6117.CVTPulleyLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4764.CVTPulleyModalAnalysis)(method_result) if method_result else None

    def results_for_pulley(self, design_entity: '_2148.Pulley') -> '_4812.PulleyModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PulleyModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2148.Pulley.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4812.PulleyModalAnalysis)(method_result) if method_result else None

    def results_for_pulley_load_case(self, design_entity_analysis: '_6194.PulleyLoadCase') -> '_4812.PulleyModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PulleyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PulleyModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6194.PulleyLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4812.PulleyModalAnalysis)(method_result) if method_result else None

    def results_for_shaft_hub_connection(self, design_entity: '_2156.ShaftHubConnection') -> '_4817.ShaftHubConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ShaftHubConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2156.ShaftHubConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4817.ShaftHubConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_shaft_hub_connection_load_case(self, design_entity_analysis: '_6200.ShaftHubConnectionLoadCase') -> '_4817.ShaftHubConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ShaftHubConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6200.ShaftHubConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4817.ShaftHubConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring(self, design_entity: '_2154.RollingRing') -> '_4815.RollingRingModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.RollingRingModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2154.RollingRing.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4815.RollingRingModalAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_load_case(self, design_entity_analysis: '_6198.RollingRingLoadCase') -> '_4815.RollingRingModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.RollingRingModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6198.RollingRingLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4815.RollingRingModalAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_assembly(self, design_entity: '_2155.RollingRingAssembly') -> '_4813.RollingRingAssemblyModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.RollingRingAssemblyModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2155.RollingRingAssembly.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4813.RollingRingAssemblyModalAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_assembly_load_case(self, design_entity_analysis: '_6196.RollingRingAssemblyLoadCase') -> '_4813.RollingRingAssemblyModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.RollingRingAssemblyModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6196.RollingRingAssemblyLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4813.RollingRingAssemblyModalAnalysis)(method_result) if method_result else None

    def results_for_spring_damper(self, design_entity: '_2157.SpringDamper') -> '_4827.SpringDamperModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SpringDamperModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2157.SpringDamper.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4827.SpringDamperModalAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_load_case(self, design_entity_analysis: '_6210.SpringDamperLoadCase') -> '_4827.SpringDamperModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SpringDamperModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6210.SpringDamperLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4827.SpringDamperModalAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_half(self, design_entity: '_2158.SpringDamperHalf') -> '_4826.SpringDamperHalfModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SpringDamperHalfModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2158.SpringDamperHalf.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4826.SpringDamperHalfModalAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_half_load_case(self, design_entity_analysis: '_6209.SpringDamperHalfLoadCase') -> '_4826.SpringDamperHalfModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SpringDamperHalfModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6209.SpringDamperHalfLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4826.SpringDamperHalfModalAnalysis)(method_result) if method_result else None

    def results_for_synchroniser(self, design_entity: '_2159.Synchroniser') -> '_4837.SynchroniserModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SynchroniserModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2159.Synchroniser.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4837.SynchroniserModalAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_load_case(self, design_entity_analysis: '_6221.SynchroniserLoadCase') -> '_4837.SynchroniserModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SynchroniserModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6221.SynchroniserLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4837.SynchroniserModalAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_half(self, design_entity: '_2161.SynchroniserHalf') -> '_4836.SynchroniserHalfModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SynchroniserHalfModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2161.SynchroniserHalf.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4836.SynchroniserHalfModalAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_half_load_case(self, design_entity_analysis: '_6220.SynchroniserHalfLoadCase') -> '_4836.SynchroniserHalfModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SynchroniserHalfModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6220.SynchroniserHalfLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4836.SynchroniserHalfModalAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_part(self, design_entity: '_2162.SynchroniserPart') -> '_4838.SynchroniserPartModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SynchroniserPartModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2162.SynchroniserPart.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4838.SynchroniserPartModalAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_part_load_case(self, design_entity_analysis: '_6222.SynchroniserPartLoadCase') -> '_4838.SynchroniserPartModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserPartLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SynchroniserPartModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6222.SynchroniserPartLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4838.SynchroniserPartModalAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_sleeve(self, design_entity: '_2163.SynchroniserSleeve') -> '_4839.SynchroniserSleeveModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SynchroniserSleeveModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2163.SynchroniserSleeve.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4839.SynchroniserSleeveModalAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_sleeve_load_case(self, design_entity_analysis: '_6223.SynchroniserSleeveLoadCase') -> '_4839.SynchroniserSleeveModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SynchroniserSleeveModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6223.SynchroniserSleeveLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4839.SynchroniserSleeveModalAnalysis)(method_result) if method_result else None

    def results_for_torque_converter(self, design_entity: '_2164.TorqueConverter') -> '_4841.TorqueConverterModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.TorqueConverterModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2164.TorqueConverter.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4841.TorqueConverterModalAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_load_case(self, design_entity_analysis: '_6227.TorqueConverterLoadCase') -> '_4841.TorqueConverterModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.TorqueConverterModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6227.TorqueConverterLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4841.TorqueConverterModalAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_pump(self, design_entity: '_2165.TorqueConverterPump') -> '_4842.TorqueConverterPumpModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.TorqueConverterPumpModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2165.TorqueConverterPump.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4842.TorqueConverterPumpModalAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_pump_load_case(self, design_entity_analysis: '_6228.TorqueConverterPumpLoadCase') -> '_4842.TorqueConverterPumpModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.TorqueConverterPumpModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6228.TorqueConverterPumpLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4842.TorqueConverterPumpModalAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_turbine(self, design_entity: '_2167.TorqueConverterTurbine') -> '_4843.TorqueConverterTurbineModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.TorqueConverterTurbineModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2167.TorqueConverterTurbine.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4843.TorqueConverterTurbineModalAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_turbine_load_case(self, design_entity_analysis: '_6229.TorqueConverterTurbineLoadCase') -> '_4843.TorqueConverterTurbineModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.TorqueConverterTurbineModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6229.TorqueConverterTurbineLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4843.TorqueConverterTurbineModalAnalysis)(method_result) if method_result else None

    def results_for_cvt_belt_connection(self, design_entity: '_1858.CVTBeltConnection') -> '_4762.CVTBeltConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CVTBeltConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1858.CVTBeltConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4762.CVTBeltConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_cvt_belt_connection_load_case(self, design_entity_analysis: '_6115.CVTBeltConnectionLoadCase') -> '_4762.CVTBeltConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTBeltConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CVTBeltConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6115.CVTBeltConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4762.CVTBeltConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_belt_connection(self, design_entity: '_1853.BeltConnection') -> '_4730.BeltConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BeltConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1853.BeltConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4730.BeltConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_belt_connection_load_case(self, design_entity_analysis: '_6082.BeltConnectionLoadCase') -> '_4730.BeltConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BeltConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6082.BeltConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4730.BeltConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_coaxial_connection(self, design_entity: '_1854.CoaxialConnection') -> '_4745.CoaxialConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CoaxialConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1854.CoaxialConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4745.CoaxialConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_coaxial_connection_load_case(self, design_entity_analysis: '_6097.CoaxialConnectionLoadCase') -> '_4745.CoaxialConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CoaxialConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6097.CoaxialConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4745.CoaxialConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_connection(self, design_entity: '_1857.Connection') -> '_4756.ConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1857.Connection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4756.ConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_connection_load_case(self, design_entity_analysis: '_6110.ConnectionLoadCase') -> '_4756.ConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6110.ConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4756.ConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_inter_mountable_component_connection(self, design_entity: '_1866.InterMountableComponentConnection') -> '_4784.InterMountableComponentConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.InterMountableComponentConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1866.InterMountableComponentConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4784.InterMountableComponentConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_inter_mountable_component_connection_load_case(self, design_entity_analysis: '_6165.InterMountableComponentConnectionLoadCase') -> '_4784.InterMountableComponentConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.InterMountableComponentConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.InterMountableComponentConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6165.InterMountableComponentConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4784.InterMountableComponentConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_planetary_connection(self, design_entity: '_1869.PlanetaryConnection') -> '_4807.PlanetaryConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PlanetaryConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1869.PlanetaryConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4807.PlanetaryConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_planetary_connection_load_case(self, design_entity_analysis: '_6186.PlanetaryConnectionLoadCase') -> '_4807.PlanetaryConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PlanetaryConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6186.PlanetaryConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4807.PlanetaryConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_connection(self, design_entity: '_1873.RollingRingConnection') -> '_4814.RollingRingConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.RollingRingConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1873.RollingRingConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4814.RollingRingConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_connection_load_case(self, design_entity_analysis: '_6197.RollingRingConnectionLoadCase') -> '_4814.RollingRingConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.RollingRingConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6197.RollingRingConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4814.RollingRingConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_shaft_to_mountable_component_connection(self, design_entity: '_1877.ShaftToMountableComponentConnection') -> '_4820.ShaftToMountableComponentConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ShaftToMountableComponentConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1877.ShaftToMountableComponentConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4820.ShaftToMountableComponentConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_shaft_to_mountable_component_connection_load_case(self, design_entity_analysis: '_6202.ShaftToMountableComponentConnectionLoadCase') -> '_4820.ShaftToMountableComponentConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftToMountableComponentConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ShaftToMountableComponentConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6202.ShaftToMountableComponentConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4820.ShaftToMountableComponentConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_mesh(self, design_entity: '_1883.BevelDifferentialGearMesh') -> '_4732.BevelDifferentialGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1883.BevelDifferentialGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4732.BevelDifferentialGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_mesh_load_case(self, design_entity_analysis: '_6085.BevelDifferentialGearMeshLoadCase') -> '_4732.BevelDifferentialGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6085.BevelDifferentialGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4732.BevelDifferentialGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_mesh(self, design_entity: '_1887.ConceptGearMesh') -> '_4750.ConceptGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConceptGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1887.ConceptGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4750.ConceptGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_mesh_load_case(self, design_entity_analysis: '_6103.ConceptGearMeshLoadCase') -> '_4750.ConceptGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConceptGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6103.ConceptGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4750.ConceptGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_face_gear_mesh(self, design_entity: '_1893.FaceGearMesh') -> '_4771.FaceGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.FaceGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1893.FaceGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4771.FaceGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_face_gear_mesh_load_case(self, design_entity_analysis: '_6141.FaceGearMeshLoadCase') -> '_4771.FaceGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.FaceGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6141.FaceGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4771.FaceGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_mesh(self, design_entity: '_1907.StraightBevelDiffGearMesh') -> '_4828.StraightBevelDiffGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelDiffGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1907.StraightBevelDiffGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4828.StraightBevelDiffGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_mesh_load_case(self, design_entity_analysis: '_6213.StraightBevelDiffGearMeshLoadCase') -> '_4828.StraightBevelDiffGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelDiffGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6213.StraightBevelDiffGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4828.StraightBevelDiffGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_mesh(self, design_entity: '_1885.BevelGearMesh') -> '_4737.BevelGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BevelGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1885.BevelGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4737.BevelGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6090.BevelGearMeshLoadCase') -> '_4737.BevelGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BevelGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6090.BevelGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4737.BevelGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_mesh(self, design_entity: '_1889.ConicalGearMesh') -> '_4753.ConicalGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConicalGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1889.ConicalGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4753.ConicalGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_mesh_load_case(self, design_entity_analysis: '_6107.ConicalGearMeshLoadCase') -> '_4753.ConicalGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConicalGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6107.ConicalGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4753.ConicalGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_mesh(self, design_entity: '_1881.AGMAGleasonConicalGearMesh') -> '_4725.AGMAGleasonConicalGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.AGMAGleasonConicalGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1881.AGMAGleasonConicalGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4725.AGMAGleasonConicalGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_mesh_load_case(self, design_entity_analysis: '_6077.AGMAGleasonConicalGearMeshLoadCase') -> '_4725.AGMAGleasonConicalGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.AGMAGleasonConicalGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6077.AGMAGleasonConicalGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4725.AGMAGleasonConicalGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_mesh(self, design_entity: '_1891.CylindricalGearMesh') -> '_4765.CylindricalGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CylindricalGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1891.CylindricalGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4765.CylindricalGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_mesh_load_case(self, design_entity_analysis: '_6120.CylindricalGearMeshLoadCase') -> '_4765.CylindricalGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CylindricalGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6120.CylindricalGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4765.CylindricalGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_mesh(self, design_entity: '_1897.HypoidGearMesh') -> '_4780.HypoidGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.HypoidGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1897.HypoidGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4780.HypoidGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_mesh_load_case(self, design_entity_analysis: '_6161.HypoidGearMeshLoadCase') -> '_4780.HypoidGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.HypoidGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6161.HypoidGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4780.HypoidGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(self, design_entity: '_1900.KlingelnbergCycloPalloidConicalGearMesh') -> '_4785.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1900.KlingelnbergCycloPalloidConicalGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4785.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(self, design_entity_analysis: '_6167.KlingelnbergCycloPalloidConicalGearMeshLoadCase') -> '_4785.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6167.KlingelnbergCycloPalloidConicalGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4785.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self, design_entity: '_1901.KlingelnbergCycloPalloidHypoidGearMesh') -> '_4788.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1901.KlingelnbergCycloPalloidHypoidGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4788.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(self, design_entity_analysis: '_6170.KlingelnbergCycloPalloidHypoidGearMeshLoadCase') -> '_4788.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6170.KlingelnbergCycloPalloidHypoidGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4788.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self, design_entity: '_1902.KlingelnbergCycloPalloidSpiralBevelGearMesh') -> '_4791.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1902.KlingelnbergCycloPalloidSpiralBevelGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4791.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6173.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase') -> '_4791.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6173.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4791.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_mesh(self, design_entity: '_1905.SpiralBevelGearMesh') -> '_4822.SpiralBevelGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SpiralBevelGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1905.SpiralBevelGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4822.SpiralBevelGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6206.SpiralBevelGearMeshLoadCase') -> '_4822.SpiralBevelGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SpiralBevelGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6206.SpiralBevelGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4822.SpiralBevelGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_mesh(self, design_entity: '_1909.StraightBevelGearMesh') -> '_4831.StraightBevelGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1909.StraightBevelGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4831.StraightBevelGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6216.StraightBevelGearMeshLoadCase') -> '_4831.StraightBevelGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6216.StraightBevelGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4831.StraightBevelGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_mesh(self, design_entity: '_1911.WormGearMesh') -> '_4851.WormGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.WormGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1911.WormGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4851.WormGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_mesh_load_case(self, design_entity_analysis: '_6237.WormGearMeshLoadCase') -> '_4851.WormGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.WormGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6237.WormGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4851.WormGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_mesh(self, design_entity: '_1913.ZerolBevelGearMesh') -> '_4854.ZerolBevelGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ZerolBevelGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1913.ZerolBevelGearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4854.ZerolBevelGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6240.ZerolBevelGearMeshLoadCase') -> '_4854.ZerolBevelGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ZerolBevelGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6240.ZerolBevelGearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4854.ZerolBevelGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_gear_mesh(self, design_entity: '_1895.GearMesh') -> '_4776.GearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.GearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1895.GearMesh.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4776.GearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_gear_mesh_load_case(self, design_entity_analysis: '_6147.GearMeshLoadCase') -> '_4776.GearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.GearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6147.GearMeshLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4776.GearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_connection(self, design_entity: '_1921.PartToPartShearCouplingConnection') -> '_4804.PartToPartShearCouplingConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PartToPartShearCouplingConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1921.PartToPartShearCouplingConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4804.PartToPartShearCouplingConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_connection_load_case(self, design_entity_analysis: '_6183.PartToPartShearCouplingConnectionLoadCase') -> '_4804.PartToPartShearCouplingConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PartToPartShearCouplingConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6183.PartToPartShearCouplingConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4804.PartToPartShearCouplingConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_clutch_connection(self, design_entity: '_1915.ClutchConnection') -> '_4742.ClutchConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ClutchConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1915.ClutchConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4742.ClutchConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_clutch_connection_load_case(self, design_entity_analysis: '_6094.ClutchConnectionLoadCase') -> '_4742.ClutchConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ClutchConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6094.ClutchConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4742.ClutchConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_connection(self, design_entity: '_1917.ConceptCouplingConnection') -> '_4747.ConceptCouplingConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConceptCouplingConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1917.ConceptCouplingConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4747.ConceptCouplingConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_connection_load_case(self, design_entity_analysis: '_6099.ConceptCouplingConnectionLoadCase') -> '_4747.ConceptCouplingConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConceptCouplingConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6099.ConceptCouplingConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4747.ConceptCouplingConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_coupling_connection(self, design_entity: '_1919.CouplingConnection') -> '_4759.CouplingConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CouplingConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1919.CouplingConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4759.CouplingConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_coupling_connection_load_case(self, design_entity_analysis: '_6112.CouplingConnectionLoadCase') -> '_4759.CouplingConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CouplingConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6112.CouplingConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4759.CouplingConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_connection(self, design_entity: '_1923.SpringDamperConnection') -> '_4825.SpringDamperConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SpringDamperConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1923.SpringDamperConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4825.SpringDamperConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_connection_load_case(self, design_entity_analysis: '_6208.SpringDamperConnectionLoadCase') -> '_4825.SpringDamperConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SpringDamperConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6208.SpringDamperConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4825.SpringDamperConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_connection(self, design_entity: '_1925.TorqueConverterConnection') -> '_4840.TorqueConverterConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.TorqueConverterConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1925.TorqueConverterConnection.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4840.TorqueConverterConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_connection_load_case(self, design_entity_analysis: '_6226.TorqueConverterConnectionLoadCase') -> '_4840.TorqueConverterConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.TorqueConverterConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6226.TorqueConverterConnectionLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4840.TorqueConverterConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_abstract_assembly(self, design_entity: '_2003.AbstractAssembly') -> '_4723.AbstractAssemblyModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.AbstractAssemblyModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2003.AbstractAssembly.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4723.AbstractAssemblyModalAnalysis)(method_result) if method_result else None

    def results_for_abstract_assembly_load_case(self, design_entity_analysis: '_6073.AbstractAssemblyLoadCase') -> '_4723.AbstractAssemblyModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.AbstractAssemblyModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6073.AbstractAssemblyLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4723.AbstractAssemblyModalAnalysis)(method_result) if method_result else None

    def results_for_abstract_shaft_or_housing(self, design_entity: '_2004.AbstractShaftOrHousing') -> '_4724.AbstractShaftOrHousingModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.AbstractShaftOrHousingModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2004.AbstractShaftOrHousing.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4724.AbstractShaftOrHousingModalAnalysis)(method_result) if method_result else None

    def results_for_abstract_shaft_or_housing_load_case(self, design_entity_analysis: '_6074.AbstractShaftOrHousingLoadCase') -> '_4724.AbstractShaftOrHousingModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractShaftOrHousingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.AbstractShaftOrHousingModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6074.AbstractShaftOrHousingLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4724.AbstractShaftOrHousingModalAnalysis)(method_result) if method_result else None

    def results_for_bearing(self, design_entity: '_2007.Bearing') -> '_4729.BearingModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BearingModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2007.Bearing.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4729.BearingModalAnalysis)(method_result) if method_result else None

    def results_for_bearing_load_case(self, design_entity_analysis: '_6081.BearingLoadCase') -> '_4729.BearingModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BearingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BearingModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6081.BearingLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4729.BearingModalAnalysis)(method_result) if method_result else None

    def results_for_bolt(self, design_entity: '_2009.Bolt') -> '_4741.BoltModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BoltModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2009.Bolt.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4741.BoltModalAnalysis)(method_result) if method_result else None

    def results_for_bolt_load_case(self, design_entity_analysis: '_6093.BoltLoadCase') -> '_4741.BoltModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BoltModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6093.BoltLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4741.BoltModalAnalysis)(method_result) if method_result else None

    def results_for_bolted_joint(self, design_entity: '_2010.BoltedJoint') -> '_4740.BoltedJointModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BoltedJointModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2010.BoltedJoint.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4740.BoltedJointModalAnalysis)(method_result) if method_result else None

    def results_for_bolted_joint_load_case(self, design_entity_analysis: '_6092.BoltedJointLoadCase') -> '_4740.BoltedJointModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltedJointLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BoltedJointModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6092.BoltedJointLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4740.BoltedJointModalAnalysis)(method_result) if method_result else None

    def results_for_component(self, design_entity: '_2011.Component') -> '_4746.ComponentModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Component)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ComponentModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2011.Component.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4746.ComponentModalAnalysis)(method_result) if method_result else None

    def results_for_component_load_case(self, design_entity_analysis: '_6098.ComponentLoadCase') -> '_4746.ComponentModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ComponentModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6098.ComponentLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4746.ComponentModalAnalysis)(method_result) if method_result else None

    def results_for_connector(self, design_entity: '_2014.Connector') -> '_4757.ConnectorModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Connector)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConnectorModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2014.Connector.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4757.ConnectorModalAnalysis)(method_result) if method_result else None

    def results_for_connector_load_case(self, design_entity_analysis: '_6111.ConnectorLoadCase') -> '_4757.ConnectorModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectorLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConnectorModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6111.ConnectorLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4757.ConnectorModalAnalysis)(method_result) if method_result else None

    def results_for_datum(self, design_entity: '_2015.Datum') -> '_4769.DatumModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Datum)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.DatumModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2015.Datum.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4769.DatumModalAnalysis)(method_result) if method_result else None

    def results_for_datum_load_case(self, design_entity_analysis: '_6126.DatumLoadCase') -> '_4769.DatumModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.DatumLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.DatumModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6126.DatumLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4769.DatumModalAnalysis)(method_result) if method_result else None

    def results_for_external_cad_model(self, design_entity: '_2018.ExternalCADModel') -> '_4770.ExternalCADModelModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ExternalCADModelModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2018.ExternalCADModel.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4770.ExternalCADModelModalAnalysis)(method_result) if method_result else None

    def results_for_external_cad_model_load_case(self, design_entity_analysis: '_6139.ExternalCADModelLoadCase') -> '_4770.ExternalCADModelModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ExternalCADModelModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6139.ExternalCADModelLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4770.ExternalCADModelModalAnalysis)(method_result) if method_result else None

    def results_for_flexible_pin_assembly(self, design_entity: '_2019.FlexiblePinAssembly') -> '_4774.FlexiblePinAssemblyModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.FlexiblePinAssemblyModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2019.FlexiblePinAssembly.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4774.FlexiblePinAssemblyModalAnalysis)(method_result) if method_result else None

    def results_for_flexible_pin_assembly_load_case(self, design_entity_analysis: '_6143.FlexiblePinAssemblyLoadCase') -> '_4774.FlexiblePinAssemblyModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.FlexiblePinAssemblyModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6143.FlexiblePinAssemblyLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4774.FlexiblePinAssemblyModalAnalysis)(method_result) if method_result else None

    def results_for_assembly(self, design_entity: '_2002.Assembly') -> '_4728.AssemblyModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.AssemblyModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2002.Assembly.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4728.AssemblyModalAnalysis)(method_result) if method_result else None

    def results_for_assembly_load_case(self, design_entity_analysis: '_6080.AssemblyLoadCase') -> '_4728.AssemblyModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.AssemblyModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6080.AssemblyLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4728.AssemblyModalAnalysis)(method_result) if method_result else None

    def results_for_guide_dxf_model(self, design_entity: '_2020.GuideDxfModel') -> '_4779.GuideDxfModelModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.GuideDxfModelModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2020.GuideDxfModel.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4779.GuideDxfModelModalAnalysis)(method_result) if method_result else None

    def results_for_guide_dxf_model_load_case(self, design_entity_analysis: '_6151.GuideDxfModelLoadCase') -> '_4779.GuideDxfModelModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.GuideDxfModelModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6151.GuideDxfModelLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4779.GuideDxfModelModalAnalysis)(method_result) if method_result else None

    def results_for_imported_fe_component(self, design_entity: '_2023.ImportedFEComponent') -> '_4783.ImportedFEComponentModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ImportedFEComponent)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ImportedFEComponentModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2023.ImportedFEComponent.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4783.ImportedFEComponentModalAnalysis)(method_result) if method_result else None

    def results_for_imported_fe_component_load_case(self, design_entity_analysis: '_6163.ImportedFEComponentLoadCase') -> '_4783.ImportedFEComponentModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ImportedFEComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ImportedFEComponentModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6163.ImportedFEComponentLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4783.ImportedFEComponentModalAnalysis)(method_result) if method_result else None

    def results_for_mass_disc(self, design_entity: '_2027.MassDisc') -> '_4794.MassDiscModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.MassDiscModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2027.MassDisc.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4794.MassDiscModalAnalysis)(method_result) if method_result else None

    def results_for_mass_disc_load_case(self, design_entity_analysis: '_6175.MassDiscLoadCase') -> '_4794.MassDiscModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MassDiscLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.MassDiscModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6175.MassDiscLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4794.MassDiscModalAnalysis)(method_result) if method_result else None

    def results_for_measurement_component(self, design_entity: '_2028.MeasurementComponent') -> '_4795.MeasurementComponentModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.MeasurementComponentModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2028.MeasurementComponent.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4795.MeasurementComponentModalAnalysis)(method_result) if method_result else None

    def results_for_measurement_component_load_case(self, design_entity_analysis: '_6176.MeasurementComponentLoadCase') -> '_4795.MeasurementComponentModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.MeasurementComponentModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6176.MeasurementComponentLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4795.MeasurementComponentModalAnalysis)(method_result) if method_result else None

    def results_for_mountable_component(self, design_entity: '_2029.MountableComponent') -> '_4800.MountableComponentModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.MountableComponentModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2029.MountableComponent.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4800.MountableComponentModalAnalysis)(method_result) if method_result else None

    def results_for_mountable_component_load_case(self, design_entity_analysis: '_6178.MountableComponentLoadCase') -> '_4800.MountableComponentModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MountableComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.MountableComponentModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6178.MountableComponentLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4800.MountableComponentModalAnalysis)(method_result) if method_result else None

    def results_for_oil_seal(self, design_entity: '_2031.OilSeal') -> '_4801.OilSealModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.OilSealModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2031.OilSeal.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4801.OilSealModalAnalysis)(method_result) if method_result else None

    def results_for_oil_seal_load_case(self, design_entity_analysis: '_6180.OilSealLoadCase') -> '_4801.OilSealModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.OilSealLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.OilSealModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6180.OilSealLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4801.OilSealModalAnalysis)(method_result) if method_result else None

    def results_for_part(self, design_entity: '_2033.Part') -> '_4803.PartModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Part)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PartModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2033.Part.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4803.PartModalAnalysis)(method_result) if method_result else None

    def results_for_part_load_case(self, design_entity_analysis: '_6182.PartLoadCase') -> '_4803.PartModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PartModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6182.PartLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4803.PartModalAnalysis)(method_result) if method_result else None

    def results_for_planet_carrier(self, design_entity: '_2034.PlanetCarrier') -> '_4809.PlanetCarrierModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PlanetCarrierModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2034.PlanetCarrier.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4809.PlanetCarrierModalAnalysis)(method_result) if method_result else None

    def results_for_planet_carrier_load_case(self, design_entity_analysis: '_6189.PlanetCarrierLoadCase') -> '_4809.PlanetCarrierModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PlanetCarrierModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6189.PlanetCarrierLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4809.PlanetCarrierModalAnalysis)(method_result) if method_result else None

    def results_for_point_load(self, design_entity: '_2036.PointLoad') -> '_4810.PointLoadModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PointLoadModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2036.PointLoad.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4810.PointLoadModalAnalysis)(method_result) if method_result else None

    def results_for_point_load_load_case(self, design_entity_analysis: '_6192.PointLoadLoadCase') -> '_4810.PointLoadModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PointLoadModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6192.PointLoadLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4810.PointLoadModalAnalysis)(method_result) if method_result else None

    def results_for_power_load(self, design_entity: '_2037.PowerLoad') -> '_4811.PowerLoadModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PowerLoadModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2037.PowerLoad.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4811.PowerLoadModalAnalysis)(method_result) if method_result else None

    def results_for_power_load_load_case(self, design_entity_analysis: '_6193.PowerLoadLoadCase') -> '_4811.PowerLoadModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PowerLoadModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6193.PowerLoadLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4811.PowerLoadModalAnalysis)(method_result) if method_result else None

    def results_for_root_assembly(self, design_entity: '_2039.RootAssembly') -> '_4816.RootAssemblyModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.RootAssemblyModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2039.RootAssembly.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4816.RootAssemblyModalAnalysis)(method_result) if method_result else None

    def results_for_root_assembly_load_case(self, design_entity_analysis: '_6199.RootAssemblyLoadCase') -> '_4816.RootAssemblyModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RootAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.RootAssemblyModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6199.RootAssemblyLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4816.RootAssemblyModalAnalysis)(method_result) if method_result else None

    def results_for_specialised_assembly(self, design_entity: '_2041.SpecialisedAssembly') -> '_4821.SpecialisedAssemblyModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SpecialisedAssemblyModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2041.SpecialisedAssembly.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4821.SpecialisedAssemblyModalAnalysis)(method_result) if method_result else None

    def results_for_specialised_assembly_load_case(self, design_entity_analysis: '_6203.SpecialisedAssemblyLoadCase') -> '_4821.SpecialisedAssemblyModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpecialisedAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SpecialisedAssemblyModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6203.SpecialisedAssemblyLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4821.SpecialisedAssemblyModalAnalysis)(method_result) if method_result else None

    def results_for_unbalanced_mass(self, design_entity: '_2042.UnbalancedMass') -> '_4844.UnbalancedMassModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.UnbalancedMassModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2042.UnbalancedMass.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4844.UnbalancedMassModalAnalysis)(method_result) if method_result else None

    def results_for_unbalanced_mass_load_case(self, design_entity_analysis: '_6234.UnbalancedMassLoadCase') -> '_4844.UnbalancedMassModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.UnbalancedMassModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6234.UnbalancedMassLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4844.UnbalancedMassModalAnalysis)(method_result) if method_result else None

    def results_for_virtual_component(self, design_entity: '_2043.VirtualComponent') -> '_4845.VirtualComponentModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.VirtualComponentModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2043.VirtualComponent.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4845.VirtualComponentModalAnalysis)(method_result) if method_result else None

    def results_for_virtual_component_load_case(self, design_entity_analysis: '_6235.VirtualComponentLoadCase') -> '_4845.VirtualComponentModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.VirtualComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.VirtualComponentModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6235.VirtualComponentLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4845.VirtualComponentModalAnalysis)(method_result) if method_result else None

    def results_for_shaft(self, design_entity: '_2046.Shaft') -> '_4818.ShaftModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ShaftModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2046.Shaft.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4818.ShaftModalAnalysis)(method_result) if method_result else None

    def results_for_shaft_load_case(self, design_entity_analysis: '_6201.ShaftLoadCase') -> '_4818.ShaftModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ShaftModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6201.ShaftLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4818.ShaftModalAnalysis)(method_result) if method_result else None

    def results_for_concept_gear(self, design_entity: '_2084.ConceptGear') -> '_4751.ConceptGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConceptGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2084.ConceptGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4751.ConceptGearModalAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_load_case(self, design_entity_analysis: '_6102.ConceptGearLoadCase') -> '_4751.ConceptGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConceptGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6102.ConceptGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4751.ConceptGearModalAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_set(self, design_entity: '_2085.ConceptGearSet') -> '_4752.ConceptGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConceptGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2085.ConceptGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4752.ConceptGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_set_load_case(self, design_entity_analysis: '_6104.ConceptGearSetLoadCase') -> '_4752.ConceptGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConceptGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6104.ConceptGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4752.ConceptGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_face_gear(self, design_entity: '_2091.FaceGear') -> '_4772.FaceGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.FaceGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2091.FaceGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4772.FaceGearModalAnalysis)(method_result) if method_result else None

    def results_for_face_gear_load_case(self, design_entity_analysis: '_6140.FaceGearLoadCase') -> '_4772.FaceGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.FaceGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6140.FaceGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4772.FaceGearModalAnalysis)(method_result) if method_result else None

    def results_for_face_gear_set(self, design_entity: '_2092.FaceGearSet') -> '_4773.FaceGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.FaceGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2092.FaceGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4773.FaceGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_face_gear_set_load_case(self, design_entity_analysis: '_6142.FaceGearSetLoadCase') -> '_4773.FaceGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.FaceGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6142.FaceGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4773.FaceGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear(self, design_entity: '_2076.AGMAGleasonConicalGear') -> '_4726.AGMAGleasonConicalGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.AGMAGleasonConicalGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2076.AGMAGleasonConicalGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4726.AGMAGleasonConicalGearModalAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_load_case(self, design_entity_analysis: '_6076.AGMAGleasonConicalGearLoadCase') -> '_4726.AGMAGleasonConicalGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.AGMAGleasonConicalGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6076.AGMAGleasonConicalGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4726.AGMAGleasonConicalGearModalAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_set(self, design_entity: '_2077.AGMAGleasonConicalGearSet') -> '_4727.AGMAGleasonConicalGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.AGMAGleasonConicalGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2077.AGMAGleasonConicalGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4727.AGMAGleasonConicalGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_set_load_case(self, design_entity_analysis: '_6078.AGMAGleasonConicalGearSetLoadCase') -> '_4727.AGMAGleasonConicalGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.AGMAGleasonConicalGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6078.AGMAGleasonConicalGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4727.AGMAGleasonConicalGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear(self, design_entity: '_2078.BevelDifferentialGear') -> '_4733.BevelDifferentialGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2078.BevelDifferentialGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4733.BevelDifferentialGearModalAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_load_case(self, design_entity_analysis: '_6084.BevelDifferentialGearLoadCase') -> '_4733.BevelDifferentialGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6084.BevelDifferentialGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4733.BevelDifferentialGearModalAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_set(self, design_entity: '_2079.BevelDifferentialGearSet') -> '_4734.BevelDifferentialGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2079.BevelDifferentialGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4734.BevelDifferentialGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_set_load_case(self, design_entity_analysis: '_6086.BevelDifferentialGearSetLoadCase') -> '_4734.BevelDifferentialGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6086.BevelDifferentialGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4734.BevelDifferentialGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_planet_gear(self, design_entity: '_2080.BevelDifferentialPlanetGear') -> '_4735.BevelDifferentialPlanetGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialPlanetGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2080.BevelDifferentialPlanetGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4735.BevelDifferentialPlanetGearModalAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_planet_gear_load_case(self, design_entity_analysis: '_6087.BevelDifferentialPlanetGearLoadCase') -> '_4735.BevelDifferentialPlanetGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialPlanetGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6087.BevelDifferentialPlanetGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4735.BevelDifferentialPlanetGearModalAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_sun_gear(self, design_entity: '_2081.BevelDifferentialSunGear') -> '_4736.BevelDifferentialSunGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialSunGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2081.BevelDifferentialSunGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4736.BevelDifferentialSunGearModalAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_sun_gear_load_case(self, design_entity_analysis: '_6088.BevelDifferentialSunGearLoadCase') -> '_4736.BevelDifferentialSunGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialSunGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialSunGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6088.BevelDifferentialSunGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4736.BevelDifferentialSunGearModalAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear(self, design_entity: '_2082.BevelGear') -> '_4738.BevelGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BevelGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2082.BevelGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4738.BevelGearModalAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_load_case(self, design_entity_analysis: '_6089.BevelGearLoadCase') -> '_4738.BevelGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BevelGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6089.BevelGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4738.BevelGearModalAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_set(self, design_entity: '_2083.BevelGearSet') -> '_4739.BevelGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BevelGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2083.BevelGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4739.BevelGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_set_load_case(self, design_entity_analysis: '_6091.BevelGearSetLoadCase') -> '_4739.BevelGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BevelGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6091.BevelGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4739.BevelGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_conical_gear(self, design_entity: '_2086.ConicalGear') -> '_4754.ConicalGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConicalGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2086.ConicalGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4754.ConicalGearModalAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_load_case(self, design_entity_analysis: '_6105.ConicalGearLoadCase') -> '_4754.ConicalGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConicalGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6105.ConicalGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4754.ConicalGearModalAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_set(self, design_entity: '_2087.ConicalGearSet') -> '_4755.ConicalGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConicalGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2087.ConicalGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4755.ConicalGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_set_load_case(self, design_entity_analysis: '_6109.ConicalGearSetLoadCase') -> '_4755.ConicalGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConicalGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6109.ConicalGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4755.ConicalGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear(self, design_entity: '_2088.CylindricalGear') -> '_4766.CylindricalGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CylindricalGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2088.CylindricalGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4766.CylindricalGearModalAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_load_case(self, design_entity_analysis: '_6118.CylindricalGearLoadCase') -> '_4766.CylindricalGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CylindricalGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6118.CylindricalGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4766.CylindricalGearModalAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_set(self, design_entity: '_2089.CylindricalGearSet') -> '_4767.CylindricalGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CylindricalGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2089.CylindricalGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4767.CylindricalGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_set_load_case(self, design_entity_analysis: '_6122.CylindricalGearSetLoadCase') -> '_4767.CylindricalGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CylindricalGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6122.CylindricalGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4767.CylindricalGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_planet_gear(self, design_entity: '_2090.CylindricalPlanetGear') -> '_4768.CylindricalPlanetGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CylindricalPlanetGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2090.CylindricalPlanetGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4768.CylindricalPlanetGearModalAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_planet_gear_load_case(self, design_entity_analysis: '_6123.CylindricalPlanetGearLoadCase') -> '_4768.CylindricalPlanetGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CylindricalPlanetGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6123.CylindricalPlanetGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4768.CylindricalPlanetGearModalAnalysis)(method_result) if method_result else None

    def results_for_gear(self, design_entity: '_2093.Gear') -> '_4777.GearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.GearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2093.Gear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4777.GearModalAnalysis)(method_result) if method_result else None

    def results_for_gear_load_case(self, design_entity_analysis: '_6145.GearLoadCase') -> '_4777.GearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.GearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6145.GearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4777.GearModalAnalysis)(method_result) if method_result else None

    def results_for_gear_set(self, design_entity: '_2095.GearSet') -> '_4778.GearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.GearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2095.GearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4778.GearSetModalAnalysis)(method_result) if method_result else None

    def results_for_gear_set_load_case(self, design_entity_analysis: '_6150.GearSetLoadCase') -> '_4778.GearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.GearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6150.GearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4778.GearSetModalAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear(self, design_entity: '_2097.HypoidGear') -> '_4781.HypoidGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.HypoidGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2097.HypoidGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4781.HypoidGearModalAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_load_case(self, design_entity_analysis: '_6160.HypoidGearLoadCase') -> '_4781.HypoidGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.HypoidGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6160.HypoidGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4781.HypoidGearModalAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_set(self, design_entity: '_2098.HypoidGearSet') -> '_4782.HypoidGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.HypoidGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2098.HypoidGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4782.HypoidGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_set_load_case(self, design_entity_analysis: '_6162.HypoidGearSetLoadCase') -> '_4782.HypoidGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.HypoidGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6162.HypoidGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4782.HypoidGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear(self, design_entity: '_2099.KlingelnbergCycloPalloidConicalGear') -> '_4786.KlingelnbergCycloPalloidConicalGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidConicalGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2099.KlingelnbergCycloPalloidConicalGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4786.KlingelnbergCycloPalloidConicalGearModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_load_case(self, design_entity_analysis: '_6166.KlingelnbergCycloPalloidConicalGearLoadCase') -> '_4786.KlingelnbergCycloPalloidConicalGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidConicalGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6166.KlingelnbergCycloPalloidConicalGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4786.KlingelnbergCycloPalloidConicalGearModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(self, design_entity: '_2100.KlingelnbergCycloPalloidConicalGearSet') -> '_4787.KlingelnbergCycloPalloidConicalGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidConicalGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2100.KlingelnbergCycloPalloidConicalGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4787.KlingelnbergCycloPalloidConicalGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set_load_case(self, design_entity_analysis: '_6168.KlingelnbergCycloPalloidConicalGearSetLoadCase') -> '_4787.KlingelnbergCycloPalloidConicalGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidConicalGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6168.KlingelnbergCycloPalloidConicalGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4787.KlingelnbergCycloPalloidConicalGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(self, design_entity: '_2101.KlingelnbergCycloPalloidHypoidGear') -> '_4789.KlingelnbergCycloPalloidHypoidGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidHypoidGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2101.KlingelnbergCycloPalloidHypoidGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4789.KlingelnbergCycloPalloidHypoidGearModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_load_case(self, design_entity_analysis: '_6169.KlingelnbergCycloPalloidHypoidGearLoadCase') -> '_4789.KlingelnbergCycloPalloidHypoidGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidHypoidGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6169.KlingelnbergCycloPalloidHypoidGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4789.KlingelnbergCycloPalloidHypoidGearModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(self, design_entity: '_2102.KlingelnbergCycloPalloidHypoidGearSet') -> '_4790.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2102.KlingelnbergCycloPalloidHypoidGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4790.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(self, design_entity_analysis: '_6171.KlingelnbergCycloPalloidHypoidGearSetLoadCase') -> '_4790.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6171.KlingelnbergCycloPalloidHypoidGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4790.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(self, design_entity: '_2103.KlingelnbergCycloPalloidSpiralBevelGear') -> '_4792.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2103.KlingelnbergCycloPalloidSpiralBevelGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4792.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(self, design_entity_analysis: '_6172.KlingelnbergCycloPalloidSpiralBevelGearLoadCase') -> '_4792.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6172.KlingelnbergCycloPalloidSpiralBevelGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4792.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, design_entity: '_2104.KlingelnbergCycloPalloidSpiralBevelGearSet') -> '_4793.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2104.KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4793.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(self, design_entity_analysis: '_6174.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase') -> '_4793.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6174.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4793.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_planetary_gear_set(self, design_entity: '_2105.PlanetaryGearSet') -> '_4808.PlanetaryGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PlanetaryGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2105.PlanetaryGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4808.PlanetaryGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_planetary_gear_set_load_case(self, design_entity_analysis: '_6187.PlanetaryGearSetLoadCase') -> '_4808.PlanetaryGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PlanetaryGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6187.PlanetaryGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4808.PlanetaryGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear(self, design_entity: '_2106.SpiralBevelGear') -> '_4823.SpiralBevelGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SpiralBevelGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2106.SpiralBevelGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4823.SpiralBevelGearModalAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_load_case(self, design_entity_analysis: '_6205.SpiralBevelGearLoadCase') -> '_4823.SpiralBevelGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SpiralBevelGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6205.SpiralBevelGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4823.SpiralBevelGearModalAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_set(self, design_entity: '_2107.SpiralBevelGearSet') -> '_4824.SpiralBevelGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SpiralBevelGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2107.SpiralBevelGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4824.SpiralBevelGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_set_load_case(self, design_entity_analysis: '_6207.SpiralBevelGearSetLoadCase') -> '_4824.SpiralBevelGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SpiralBevelGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6207.SpiralBevelGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4824.SpiralBevelGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear(self, design_entity: '_2108.StraightBevelDiffGear') -> '_4829.StraightBevelDiffGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelDiffGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2108.StraightBevelDiffGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4829.StraightBevelDiffGearModalAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_load_case(self, design_entity_analysis: '_6212.StraightBevelDiffGearLoadCase') -> '_4829.StraightBevelDiffGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelDiffGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6212.StraightBevelDiffGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4829.StraightBevelDiffGearModalAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_set(self, design_entity: '_2109.StraightBevelDiffGearSet') -> '_4830.StraightBevelDiffGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelDiffGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2109.StraightBevelDiffGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4830.StraightBevelDiffGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_set_load_case(self, design_entity_analysis: '_6214.StraightBevelDiffGearSetLoadCase') -> '_4830.StraightBevelDiffGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelDiffGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6214.StraightBevelDiffGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4830.StraightBevelDiffGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear(self, design_entity: '_2110.StraightBevelGear') -> '_4832.StraightBevelGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2110.StraightBevelGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4832.StraightBevelGearModalAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_load_case(self, design_entity_analysis: '_6215.StraightBevelGearLoadCase') -> '_4832.StraightBevelGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6215.StraightBevelGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4832.StraightBevelGearModalAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_set(self, design_entity: '_2111.StraightBevelGearSet') -> '_4833.StraightBevelGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2111.StraightBevelGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4833.StraightBevelGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_set_load_case(self, design_entity_analysis: '_6217.StraightBevelGearSetLoadCase') -> '_4833.StraightBevelGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6217.StraightBevelGearSetLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4833.StraightBevelGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_planet_gear(self, design_entity: '_2112.StraightBevelPlanetGear') -> '_4834.StraightBevelPlanetGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelPlanetGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2112.StraightBevelPlanetGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4834.StraightBevelPlanetGearModalAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_planet_gear_load_case(self, design_entity_analysis: '_6218.StraightBevelPlanetGearLoadCase') -> '_4834.StraightBevelPlanetGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelPlanetGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6218.StraightBevelPlanetGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4834.StraightBevelPlanetGearModalAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_sun_gear(self, design_entity: '_2113.StraightBevelSunGear') -> '_4835.StraightBevelSunGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelSunGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2113.StraightBevelSunGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4835.StraightBevelSunGearModalAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_sun_gear_load_case(self, design_entity_analysis: '_6219.StraightBevelSunGearLoadCase') -> '_4835.StraightBevelSunGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelSunGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelSunGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6219.StraightBevelSunGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4835.StraightBevelSunGearModalAnalysis)(method_result) if method_result else None

    def results_for_worm_gear(self, design_entity: '_2114.WormGear') -> '_4852.WormGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.WormGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2114.WormGear.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4852.WormGearModalAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_load_case(self, design_entity_analysis: '_6236.WormGearLoadCase') -> '_4852.WormGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.WormGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_6236.WormGearLoadCase.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4852.WormGearModalAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_set(self, design_entity: '_2115.WormGearSet') -> '_4853.WormGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.WormGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2115.WormGearSet.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_4853.WormGearSetModalAnalysis)(method_result) if method_result else None
