import os
import urllib.parse
import urllib.request


from dateutil.parser import parse as date_parse
from dateutil.rrule import YEARLY, MONTHLY, DAILY, rrule

from collections import namedtuple

DIR = os.path.dirname(__file__)

KIND = namedtuple('KIND', 'kind name interval directory')

kinds = None

def get_kinds():
    global kinds

    data_list = []

    lines = open(f'{DIR}/data_list.csv').read().splitlines()
    for line in lines:
        name, interval, directory = line.split(',')
        kind = directory.split('/')[-1]
        data_list.append(KIND(kind, name, interval, directory))

    kinds = {x.kind: x for x in data_list}

    return data_list


def download(kind, begin, until, output_dir):
    if not until:
        until = begin

    begin = date_parse(begin)
    until = date_parse(until)

    if kinds is None:
        get_kinds()

    kind = kinds.get(kind)

    if not kind:
        raise Exception(f'알 수 없는 kind: {kind}')

    interval = {
        'yearly': YEARLY,
        'monthly': MONTHLY,
        'daily': DAILY,
    }[kind.interval]

    dates = (x.date() for x in rrule(interval, begin, until=until))

    for dt in dates:
        remote_path_format = {
            'yearly': f'{kind.directory}/{kind.kind}.%Y.tiff',
            'monthly': f'{kind.directory}/%Y/{kind.kind}.%Y-%m.tiff',
            'daily': f'{kind.directory}/%Y/%m/%d/{kind.kind}.%Y-%m-%d.tiff',
        }[kind.interval]

        remote_path = dt.strftime(remote_path_format)

        src = f'https://agecoclim.agmet.kr{remote_path}'
        dst = f'{output_dir}/{os.path.basename(remote_path)}'

        urllib.request.urlretrieve(src, dst)

        print(dst)
