import datetime
import unittest

from cache_gs.interfaces.serialization import deserialize, serialize


class TestSerialization(unittest.TestCase):

    def test_0(self):
        test_case = {
            'string': 'ABCD',
            'number': 1234,
            'date': datetime.datetime.now(),
            'bool': True
        }

        serialized = serialize(test_case)
        unserialized = deserialize(serialized)

        self.assertDictEqual(test_case, unserialized)
