"""Add utils_plus.NodeModulesFinder to STATICFILES_FINDERS to use static_files from node_modules during development."""
import os
from typing import Any, List

from django.contrib.staticfiles.finders import BaseFinder
from django.contrib.staticfiles.utils import matches_patterns, get_files
from django.core.files.storage import FileSystemStorage

from .utils import get_node_modules_dir

NODE_MODULES_USED = set()
'''list of paths used by django-templates.
While settings.DEBUG=True, these files will get collected under staticfiles.
'''


class NodeModulesFinder(BaseFinder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cached_list = None

        self.match_patterns = list(NODE_MODULES_USED)

        self.storage = FileSystemStorage(location=get_node_modules_dir())
        # filesystem_storage.prefix =

    def check(self, **kwargs: Any) -> List:
        raise NotImplementedError

    def find(self, path, all=False):
        relpath = os.path.relpath(path, get_node_modules_dir())
        if not matches_patterns(relpath, self.match_patterns):
            return []
        return super().find(path, all=all)

    def list(self, ignore_patterns=None):
        """List all files in all locations."""
        for path in get_files(self.storage, self.match_patterns, ignore_patterns):
            yield path, self.storage
