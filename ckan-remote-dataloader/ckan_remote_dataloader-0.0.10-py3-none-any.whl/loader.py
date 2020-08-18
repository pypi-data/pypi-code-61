import messytables
import itertools
from ckanapi import RemoteCKAN
from datetime import datetime

TYPE_MAPPING = {
    'String': 'text',
    'Integer': 'numeric',
    'Decimal': 'numeric',
    'DateUtil': 'timestamp'
}

TYPES = [messytables.StringType, messytables.DecimalType,
          messytables.IntegerType, messytables.DateUtilType]


def connect(ckan_url, api_key):
    ckan = RemoteCKAN(ckan_url, apikey=api_key)
    return ckan


def update_resource_details(ckan, resource_id):
    """
    Update webstore_url and webstore_last_updated in CKAN
    """
    url_type = 'datastore'
    url = f'{ckan.address}/datastore/dump/{resource_id}'
    modified = datetime.now().isoformat()
    format = 'Table'
    ckan.action.resource_update(id=resource_id, url=url, url_type=url_type, last_modified=modified, format=format)


def chunky(iterable, n):
    """
    Generates chunks of data that can be loaded into ckan
    :param n: Size of each chunks
    :type n: int
    """
    it = iter(iterable)
    item = list(itertools.islice(it, n))
    while item:
        yield item
        item = list(itertools.islice(it, n))


def parse_data(input):
    fh = open(input, 'rb')

    try:
        table_set = messytables.any_tableset(fh)
    except messytables.ReadError as e:
        print(e)
    
    get_row_set = lambda table_set: table_set.tables.pop()
    row_set = get_row_set(table_set)
    offset, headers = messytables.headers_guess(row_set.sample)
    # Some headers might have been converted from strings to floats and such.
    headers = [str(header) for header in headers]
    
    row_set.register_processor(messytables.headers_processor(headers))
    row_set.register_processor(messytables.offset_processor(offset + 1))
    types = messytables.type_guess(row_set.sample, types=TYPES, strict=True)
    
    row_set.register_processor(messytables.types_processor(types))

    headers = [header.strip() for header in headers if header.strip()]
    headers_set = set(headers)
    
    def row_iterator():
        for row in row_set:
            data_row = {}
            for index, cell in enumerate(row):
                column_name = cell.column.strip()
                if column_name not in headers_set:
                    continue
                data_row[column_name] = cell.value
            yield data_row
    result = row_iterator()
    
    headers_dicts = [dict(id=field[0], type=TYPE_MAPPING[str(field[1])])
                     for field in zip(headers, types)]
    
    print('Determined headers and types: {headers}'.format(
        headers=headers_dicts))
    
    return headers_dicts, result


def update_resource(ckan, input, resource_id):
    _, result = parse_data(input)
    count = 0
    for i, records in enumerate(chunky(result, 250)):
        count += len(records)
        print('Saving chunk {number}'.format(number=i))
        ckan.action.datastore_upsert(resource_id=resource_id, records=records, force=True, method='insert')

    print('Successfully pushed {n} entries to "{res_id}".'.format(
        n=count, res_id=resource_id))


def new_resource(ckan, existing, input, package_id, name):
    if existing:
        resource = ckan.action.resource_show(id=package_id)
    else:
        resource = ckan.action.resource_create(package_id=package_id, name=name)
    headers, result = parse_data(input)
    count = 0
    for i, records in enumerate(chunky(result, 250)):
        count += len(records)
        print('Saving chunk {number}'.format(number=i))
        ckan.action.datastore_create(resource_id=resource['id'], fields=headers, records=records, force=True)

    update_resource_details(ckan, resource['id'])

    print('Successfully pushed {n} entries to "{res_id}".'.format(
        n=count, res_id=resource['id']))
    return