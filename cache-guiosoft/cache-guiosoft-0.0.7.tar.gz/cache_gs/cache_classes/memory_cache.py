from cache_gs.cache_classes.cache_data import CacheData
from cache_gs.interfaces.super_cache import SuperCache
import time


class MemoryCache(SuperCache):

    def setup(self):
        self._data = {}
        self._last_purge = 0

    def _get_value(self, section: str, key: str, default=None) -> CacheData:
        self._purge()
        if section not in self._data or key not in self._data[section]:
            return CacheData(section, key, default, 0)
        else:
            return self._data[section][key]

    def _set_value(self, data: CacheData) -> bool:
        self._purge()

        if data.section not in self._data:
            self._data[data.section] = {}

        self._data[data.section][data.key] = data
        return True

    def _delete_value(self, data: CacheData) -> bool:
        self._purge()
        if data.section in self._data and \
                data.key in self._data[data.section]:
            del(self._data[data.section][data.key])

        return True

    def purge_expired(self) -> int:
        removed = 0
        for section in self._data:
            keys = [key for key in self._data[section].keys()]
            for key in keys:
                if self._data[section][key].expired:
                    del(self._data[section][key])
                    removed += 1
        self._last_purge = time.time()
        return removed

    def _purge(self):
        if time.time()-self._last_purge > 300:  # After 5 minutes, auto purge
            self.purge_expired()
