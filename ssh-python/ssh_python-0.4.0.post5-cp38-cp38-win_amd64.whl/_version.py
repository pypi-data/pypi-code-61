
import json

version_json = '''
{"date": "2020-08-19T18:24:38.330147", "dirty": false, "error": null, "full-revisionid": "1747e32ba3ca6a51b70108f9aae3bc2291b09f61", "version": "0.4.0.post5"}'''  # END VERSION_JSON


def get_versions():
    return json.loads(version_json)

