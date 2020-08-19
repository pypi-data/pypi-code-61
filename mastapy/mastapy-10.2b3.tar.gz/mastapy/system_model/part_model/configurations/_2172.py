'''_2172.py

BearingDetailConfiguration
'''


from mastapy.system_model.part_model.configurations import _2174, _2173
from mastapy.system_model.part_model import _2007
from mastapy.bearings.bearing_designs import _1750
from mastapy._internal.python_net import python_net_import

_BEARING_DETAIL_CONFIGURATION = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Configurations', 'BearingDetailConfiguration')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingDetailConfiguration',)


class BearingDetailConfiguration(_2174.PartDetailConfiguration['_2173.BearingDetailSelection', '_2007.Bearing', '_1750.BearingDesign']):
    '''BearingDetailConfiguration

    This is a mastapy class.
    '''

    TYPE = _BEARING_DETAIL_CONFIGURATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BearingDetailConfiguration.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
