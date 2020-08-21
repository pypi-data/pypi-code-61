def get_date(days=0, separator='-'):
    import datetime
    return (datetime.datetime.now() + datetime.timedelta(days=days)).strftime(f"%Y{separator}%m{separator}%d")


def get_today(separator='-'):
    return get_date(days=0, separator=separator)


def get_month(months=0, separator='-'):
    """获取月份，如2019-10"""
    import arrow
    return arrow.now().shift(months=months).format(f"YYYY{separator}MM")


def trans_datetime_to_java_timestamp(dt):
    return int(dt.timestamp()*1000)


def get_begin_datetime(year, month, day):
    return datetime.datetime(year=year, month=month, day=day, hour=0, minute=0, second=0, microsecond=0)


def get_end_datetime(year, month, day):
    return datetime.datetime(year=year, month=month, day=day, hour=23, minute=59, second=59, microsecond=999999)
