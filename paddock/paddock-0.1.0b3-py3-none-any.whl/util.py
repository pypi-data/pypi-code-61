import json


__all__ = [
    "format_results",
    "parse",
]


def format_results(results, header):
    newres = []
    for row in results:
        newr = {}
        for k, v in row.items():
            newr[header[k]] = v
        newres.append(newr)
    return newres


def parse(data):
    res = ''
    try:
        res = json.loads(data)  # iRacing responses are generally in JSON
    except:
        pass  # TODO raise error?

    return res
