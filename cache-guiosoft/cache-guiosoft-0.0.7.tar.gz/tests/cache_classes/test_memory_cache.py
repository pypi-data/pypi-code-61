import time
import unittest

from cache_gs.cache_classes.memory_cache import MemoryCache


class TestMemoryCache(unittest.TestCase):

    def test_memory_cache(self):
        cache = MemoryCache('memory://')
        cache.set_value('sec', 'expiring', 123, 0.01)
        cache.set_value('sec', 'chave', 'Value')
        self.assertEqual(cache.get_value('sec', 'chave', '000'), 'Value')

        cache.delete_value('sec', 'chave')
        self.assertEqual(cache.get_value('sec', 'chave', '00'), '00')
        time.sleep(0.5)
        cache._last_purge = 0
        cache._purge()
