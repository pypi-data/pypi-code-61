from google.cloud import firestore

client = firestore.Client()


class Types:
    WORKSPACES = "workspaces"
    CONFIGURATIONS = "configurations"
    STATES = "states"
    PARAM_SETS = "paramSets"


def _workspace(wid=None):
    return client.collection(Types.WORKSPACES).document(wid)


def _configuration(wid, cid=None):
    return _workspace(wid).collection(Types.CONFIGURATIONS).document(cid)


def add_configuration(wid, name):
    ref = _configuration(wid)
    ref.set({"name": name})
    return ref.id


def get_configuration_by_name(wid, name):
    query = (
        _workspace(wid)
        .collection(Types.CONFIGURATIONS)
        .where("name", "==", name)
        .limit(1)
    )
    return next(query.stream(), None)
