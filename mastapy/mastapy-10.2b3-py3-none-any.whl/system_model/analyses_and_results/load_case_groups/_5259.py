'''_5259.py

ClutchEngagementStatus
'''


from mastapy.system_model.analyses_and_results.load_case_groups import _5263
from mastapy.system_model.connections_and_sockets.couplings import _1915
from mastapy._internal.python_net import python_net_import

_CLUTCH_ENGAGEMENT_STATUS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups', 'ClutchEngagementStatus')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchEngagementStatus',)


class ClutchEngagementStatus(_5263.GenericClutchEngagementStatus['_1915.ClutchConnection']):
    '''ClutchEngagementStatus

    This is a mastapy class.
    '''

    TYPE = _CLUTCH_ENGAGEMENT_STATUS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchEngagementStatus.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
