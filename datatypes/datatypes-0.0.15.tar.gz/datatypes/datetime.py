# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division, print_function, absolute_import
import datetime


class Datetime(datetime.datetime):
    """Wrapper around standard datetime.datetime class that assures UTC time and
    full ISO8601 date strings with Z timezone.

    You can create an object multiple ways:

        d = Datetime() # current utc time
        d = Datetime("2019-10-01T23:26:22.079296Z") # parses ISO8601 date from string
        d = Datetime(2019, 10, 1) # standard creation syntax

    https://docs.python.org/3/library/datetime.html#datetime-objects
    """
    FORMAT_ISO_8601 = "%Y-%m-%dT%H:%M:%S.%fZ"
    FORMAT_PRECISION_SECONDS = "%Y-%m-%dT%H:%M:%SZ"
    FORMAT_PRECISION_DAY = "%Y-%m-%d"

    @property
    def yearname(self):
        """return the full 4 digit year"""

    @property
    def monthname(self):
        """return the full month name"""

    @property
    def dayname(self):
        """return the full day name"""


    @classmethod
    def formats(cls):
        is_valid = lambda k, v: k.startswith("FORMAT")
        formats = set(v for k, v in inspect.getmembers(cls) if is_valid(k, v))
        return formats


    @classmethod
    def parse(cls, d):

        # TODO: prom's interface.sqlite.TimestampType.convert has an ISO 8601 parser
        # that might be really handy right here if all our formats fail

        fs = cls.formats()
        for f in fs:
            try:
                return cls.strptime(args[0], f)

            except ValueError:
                pass

    def __new__(cls, *args, **kwargs):
        if not args and not kwargs:
            return cls.utcnow()

        elif len(args) == 1 and not kwargs:
            if isinstance(args[0], datetime.datetime):
                return super(Datetime, cls).__new__(
                    cls,
                    args[0].year,
                    args[0].month,
                    args[0].day,
                    args[0].hour,
                    args[0].minute,
                    args[0].second,
                    args[0].microsecond,
                )

            elif isinstance(args[0], datetime.date):
                return super(Datetime, cls).__new__(
                    cls,
                    args[0].year,
                    args[0].month,
                    args[0].day,
                    0,
                    0,
                    0,
                    0,
                )

            elif isinstance(args[0], datetime.timedelta):
                return cls.utcnow() + args[0]

            elif isinstance(args[0], (int, float)):
                return cls.fromtimestamp(args[0])

            else:
                if args[0]:
                    try:
                        # if the object is pickled we would get the pickled string
                        # as our one passed in value
                        return super(Datetime, cls).__new__(cls, *args, **kwargs)

                    except TypeError:
                        fs = cls.parse(args[0])
                        if fs is None:
                            raise

                        else:
                            return fs

                else:
                    return cls.utcnow()

        else:
            return super(Datetime, cls).__new__(cls, *args, **kwargs)

    def __str__(self):
        if self.has_time():
            if self.microsecond == 0:
                return self.strftime(self.FORMAT_PRECISION_SECONDS)

            else:
                return self.strftime(self.FORMAT_ISO_8601)

        else:
            return self.strftime(self.FORMAT_PRECISION_DAY)

    def __add__(self, other):
        return type(self)(super(Datetime, self).__add__(other))

    def __sub__(self, other):
        if isinstance(other, datetime.timedelta):
            return type(self)(super(Datetime, self).__sub__(other))
        else:
            return super(Datetime, self).__sub__(other)

    def has_time(self):
        return not (
            self.hour == 0 and
            self.minute == 0 and
            self.second == 0 and 
            self.microsecond == 0
        )

    def timestamp(self):
        """
        return the current utc timestamp

        http://crazytechthoughts.blogspot.com/2012/02/get-current-utc-timestamp-in-python.html

        return -- float -- the current utc timestamp with microsecond precision
        """
        # this only returns second precision, which is why we don't use it
        #now = calendar.timegm(datetime.datetime.utcnow().utctimetuple())

        # this returns microsecond precision
        # http://bugs.python.org/msg180110
        epoch = datetime.datetime(1970, 1, 1)
        return (self - epoch).total_seconds()

    def iso_date(self):
        """returns datetime as ISO-8601 string with just YYYY-MM-DD"""
        return self.strftime(self.FORMAT_PRECISION_DAY)
    iso_day = iso_date

    def iso_seconds(self):
        """returns datetime as ISO-8601 string with no milliseconds"""
        return self.strftime(self.FORMAT_PRECISION_SECONDS)

    def iso_8601(self):
        """returns datetime as a full ISO-8601 string with milliseconds"""
        return self.strftime(self.FORMAT_ISO_8601)

    def within(self, start, stop):
        """return True if this datetime is within start and stop dates"""
        # TODO -- use the Path modified_within that takes seconds and stuff like
        # that?

