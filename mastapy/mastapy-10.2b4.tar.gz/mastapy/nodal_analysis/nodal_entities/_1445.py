'''_1445.py

LineContactStiffnessEntity
'''


from mastapy.nodal_analysis import _1391
from mastapy._internal import constructor
from mastapy.nodal_analysis.nodal_entities import _1430
from mastapy._internal.python_net import python_net_import

_LINE_CONTACT_STIFFNESS_ENTITY = python_net_import('SMT.MastaAPI.NodalAnalysis.NodalEntities', 'LineContactStiffnessEntity')


__docformat__ = 'restructuredtext en'
__all__ = ('LineContactStiffnessEntity',)


class LineContactStiffnessEntity(_1430.ArbitraryNodalComponent):
    '''LineContactStiffnessEntity

    This is a mastapy class.
    '''

    TYPE = _LINE_CONTACT_STIFFNESS_ENTITY

    __hash__ = None

    def __init__(self, instance_to_wrap: 'LineContactStiffnessEntity.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def stiffness_in_local_coordinate_system(self) -> '_1391.NodalMatrix':
        '''NodalMatrix: 'StiffnessInLocalCoordinateSystem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1391.NodalMatrix)(self.wrapped.StiffnessInLocalCoordinateSystem) if self.wrapped.StiffnessInLocalCoordinateSystem else None
