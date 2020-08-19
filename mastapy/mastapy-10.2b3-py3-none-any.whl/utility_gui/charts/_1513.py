'''_1513.py

CustomTableAndChart
'''


from mastapy.math_utility import _1062
from mastapy._internal import constructor
from mastapy.utility.report import _1309
from mastapy._internal.python_net import python_net_import

_CUSTOM_TABLE_AND_CHART = python_net_import('SMT.MastaAPI.UtilityGUI.Charts', 'CustomTableAndChart')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomTableAndChart',)


class CustomTableAndChart(_1309.CustomTable):
    '''CustomTableAndChart

    This is a mastapy class.
    '''

    TYPE = _CUSTOM_TABLE_AND_CHART

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CustomTableAndChart.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def primary_axis_range(self) -> '_1062.Range':
        '''Range: 'PrimaryAxisRange' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1062.Range)(self.wrapped.PrimaryAxisRange) if self.wrapped.PrimaryAxisRange else None
