# coding: utf8


__all__ = ["EtiFixingInfo"]

from ._abstracted_class import FixingInfo
from ...enum_types.fixing_frequency import FixingFrequency
from ...enum_types.average_type import AverageType


class EtiFixingInfo(FixingInfo):
    def __init__(
            self,
            average_type=None,
            fixing_frequency=None,
            fixing_calendar=None,
            fixing_end_date=None,
            fixing_start_date=None
    ):
        super().__init__()
        self.average_type = average_type
        self.fixing_frequency = fixing_frequency
        self.fixing_calendar = fixing_calendar
        self.fixing_end_date = fixing_end_date
        self.fixing_start_date = fixing_start_date

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
    def fixing_frequency(self):
        """
        The fixing's frequency. Possible values:
         - Daily
         - Weekly
         - BiWeekly
         - Monthly
         - Quaterly
         - SemiAnnual
         - Annual
        :return: enum FixingFrequency
        """
        return self._get_enum_parameter(FixingFrequency, "fixingFrequency")

    @fixing_frequency.setter
    def fixing_frequency(self, value):
        self._set_enum_parameter(FixingFrequency, "fixingFrequency", value)

    @property
    def fixing_calendar(self):
        """
        The calendar of the underlying's currency.
        :return: str
        """
        return self._get_parameter("fixingCalendar")

    @fixing_calendar.setter
    def fixing_calendar(self, value):
        self._set_parameter("fixingCalendar", value)

    @property
    def fixing_end_date(self):
        """
        The end date of the fixing period. Should be less or equal to the expiry.
        :return: str
        """
        return self._get_parameter("fixingEndDate")

    @fixing_end_date.setter
    def fixing_end_date(self, value):
        self._set_parameter("fixingEndDate", value)

    @property
    def fixing_start_date(self):
        """
        The beginning date of the fixing period.
        :return: str
        """
        return self._get_parameter("fixingStartDate")

    @fixing_start_date.setter
    def fixing_start_date(self, value):
        self._set_parameter("fixingStartDate", value)
