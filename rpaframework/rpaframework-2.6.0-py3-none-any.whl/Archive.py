import logging
from typing import Any
import zipfile
from RPA.core import notebook


class Archive:
    """[summary]
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def archive_folder_with_zip(self):
        pass

    def archive_folder_with_tar(self):
        pass

    def archive_folder_with_tar_and_gzip(self):
        pass

    def add_to_archive(self):
        pass

    def delete_from_archive(self):
        pass

    def list_archive(self, archive_name: str):
        """List files in a archive"""
        filelist = None
        if zipfile.is_zipfile(archive_name):
            with zipfile.ZipFile(archive_name, "r") as f:
                filelist = f.infolist()
        notebook.notebook_dir(filelist)
        return filelist

    def get_archive_info(self):
        pass

    def extract_archive(self, archive_name: str, path: str = None, members: Any = None):
        if zipfile.is_zipfile(archive_name):
            with zipfile.ZipFile(archive_name, "r") as f:
                f.extractall(path=path, members=members)

    def extract_file_from_archive(self):
        pass
