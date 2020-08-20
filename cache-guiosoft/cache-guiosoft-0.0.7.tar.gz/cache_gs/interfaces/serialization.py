import base64
import pickle


def serialize(data) -> str:
    pickled = pickle.dumps(data)
    encoded = base64.b85encode(pickled).decode('ascii')
    return encoded


def deserialize(encoded) -> object:
    decoded = base64.b85decode(encoded)
    unpickled = pickle.loads(decoded)
    return unpickled
