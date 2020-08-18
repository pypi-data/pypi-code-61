# coding: utf8

__all__ = ["AverageInfo"]

from refinitiv.dataplatform.content.ipa.instrument._definition import ObjectDefinition
from ...enum_types.average_type import AverageType
from . import FxFixingInfo


class AverageInfo(ObjectDefinition):
    def __init__(
            self,
            average_type=None,
            fixing=None,
            average_so_far=None
    ):
        super().__init__()
        self.average_type = average_type
        self.fixing = fixing
        self.average_so_far = average_so_far

    @property
    def average_type(self):
        """
        The type of average used to compute. Possible values:
         - ArithmeticRate
         - ArithmeticStrike
         - GeometricRate
         - GeometricStrike
        :return: enum AverageType
        """
        return self._get_enum_parameter(AverageType, "averageType")

    @average_type.setter
    def average_type(self, value):
        self._set_enum_parameter(AverageType, "averageType", value)

    @property
    def fixing(self):
        """
        Fixing details for average options
        :return: object FxOptionFixingInfo
        """
        return self._get_object_parameter(FxFixingInfo, "fixing")

    @fixing.setter
    def fixing(self, value):
        self._set_object_parameter(FxFixingInfo, "fixing", value)

    @property
    def average_so_far(self):
        """
        The value of the AverageType
        :return: float
        """
        return self._get_parameter("averageSoFar")

    @average_so_far.setter
    def average_so_far(self, value):
        self._set_parameter("averageSoFar", value)
