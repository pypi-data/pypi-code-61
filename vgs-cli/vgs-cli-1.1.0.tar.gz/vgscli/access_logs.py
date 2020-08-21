import json

from vgscli.utils import dump_yaml


def fetch_logs(api, params, tail):
    data = []
    count = 0
    page_number = 1

    while True:
        params['page[number]'] = page_number
        result = api.access_logs.list(params=params)
        page_data = result.body['data']

        last_index = tail and tail - count
        data.extend(page_data[:last_index])

        count += len(page_data)
        page_number += 1

        if result.body['meta']['count'] <= count or (tail and tail <= count):
            break

    data.reverse()

    return {
        'version': 1,
        'data': data,
    }


def format_logs(logs, output_format):
    if output_format == 'json':
        return json.dumps(logs)
    else:
        return dump_yaml(logs)


def prepare_filter(filter_options):
    result = {}
    for pair in filter_options.items():
        result['filter[{}]'.format(pair[0])] = pair[1]
    return result
