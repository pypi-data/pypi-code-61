'''_2220.py

CompoundModalAnalysesatStiffnessesAnalysis
'''


from mastapy.system_model.analyses_and_results import _2176
from mastapy._internal.python_net import python_net_import

_COMPOUND_MODAL_ANALYSESAT_STIFFNESSES_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'CompoundModalAnalysesatStiffnessesAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CompoundModalAnalysesatStiffnessesAnalysis',)


class CompoundModalAnalysesatStiffnessesAnalysis(_2176.CompoundAnalysis):
    '''CompoundModalAnalysesatStiffnessesAnalysis

    This is a mastapy class.
    '''

    TYPE = _COMPOUND_MODAL_ANALYSESAT_STIFFNESSES_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CompoundModalAnalysesatStiffnessesAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
