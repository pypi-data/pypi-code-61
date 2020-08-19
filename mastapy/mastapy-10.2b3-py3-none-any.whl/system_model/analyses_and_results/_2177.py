'''_2177.py

SingleAnalysis
'''


from mastapy._internal import constructor
from mastapy import _6529
from mastapy.system_model import _1816
from mastapy.system_model.analyses_and_results import _2205
from mastapy._internal.python_net import python_net_import

_SINGLE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'SingleAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SingleAnalysis',)


class SingleAnalysis:
    '''SingleAnalysis

    This is a mastapy class.
    '''

    TYPE = _SINGLE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SingleAnalysis.TYPE'):
        self.wrapped = instance_to_wrap
        self._freeze()

    __frozen = False

    def __setattr__(self, attr, value):
        prop = getattr(self.__class__, attr, None)
        if isinstance(prop, property):
            prop.fset(self, value)
        else:
            if self.__frozen and attr not in self.__dict__:
                raise AttributeError((
                    'Attempted to set unknown '
                    'attribute: \'{}\''.format(attr))) from None

            super().__setattr__(attr, value)

    def __delattr__(self, name):
        raise AttributeError(
            'Cannot delete the attributes of a mastapy object.') from None

    def _freeze(self):
        self.__frozen = True

    @property
    def results_ready(self) -> 'bool':
        '''bool: 'ResultsReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ResultsReady

    def perform_analysis(self):
        ''' 'PerformAnalysis' is the original name of this method.'''

        self.wrapped.PerformAnalysis()

    def perform_analysis_with_progress(self, task_progress: '_6529.TaskProgress'):
        ''' 'PerformAnalysis' is the original name of this method.

        Args:
            task_progress (mastapy.TaskProgress)
        '''

        self.wrapped.PerformAnalysis.Overloads[_6529.TaskProgress.TYPE](task_progress.wrapped if task_progress else None)

    def results_for(self, design_entity: '_1816.DesignEntity') -> '_2205.DesignEntityAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.DesignEntity)

        Returns:
            mastapy.system_model.analyses_and_results.DesignEntityAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_1816.DesignEntity.TYPE](design_entity.wrapped if design_entity else None)
        return constructor.new(_2205.DesignEntityAnalysis)(method_result) if method_result else None

    def results_for_design_entity_analysis(self, design_entity_analysis: '_2205.DesignEntityAnalysis') -> '_2205.DesignEntityAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.DesignEntityAnalysis)

        Returns:
            mastapy.system_model.analyses_and_results.DesignEntityAnalysis
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_2205.DesignEntityAnalysis.TYPE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_2205.DesignEntityAnalysis)(method_result) if method_result else None

    def initialize_lifetime_service(self) -> 'object':
        ''' 'InitializeLifetimeService' is the original name of this method.

        Returns:
            object
        '''

        method_result = self.wrapped.InitializeLifetimeService()
        return method_result
