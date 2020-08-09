import os
import logging
import zipfile
from threading import Thread
from datetime import datetime

import bencode

from .methods import discover_bt_backup_path, convert_slashes


logger = logging.getLogger(__name__)


class QBTBatchMove(object):
    logger = logging.getLogger(__name__ + '.QBTBatchMove')

    def __init__(self, bt_backup_path: str = None):
        if bt_backup_path is None:
            bt_backup_path = discover_bt_backup_path()
        self.logger.debug('BT_backup Path: %s' % bt_backup_path)
        self.bt_backup_path = bt_backup_path
        self.discovered_files = None

    def run(self, existing_path: str, new_path: str, target_os: str = None, create_backup: bool = True):
        """
        Perform Batch Processing of path changes.
        :param existing_path: Existing path to look for
        :type existing_path: str
        :param new_path: New Path to replace with
        :type new_path: str
        :param target_os: If targeting a different OS than the source. Must be Windows, Linux, or Mac.
        :type target_os: str
        :param create_backup: Create a backup archive of the BT_Backup directory?
        :type create_backup: bool
        """
        if not os.path.exists(self.bt_backup_path) or not os.path.isdir(self.bt_backup_path):
            raise NotADirectoryError(self.bt_backup_path)
        if create_backup:
            backup_filename = 'fastresume_backup' + datetime.now().strftime('%Y%m%d%H%M%S') + '.zip'
            self.backup_folder(self.bt_backup_path,
                               os.path.join(os.path.dirname(self.bt_backup_path), backup_filename))

        self.logger.info('Searching for .fastresume files with path %s ...' % existing_path)
        for fast_resume in self.discover_relevant_fast_resume(self.bt_backup_path, existing_path):
            # Fire and forget
            Thread(target=self.update_fastresume, args=[fast_resume, existing_path, new_path,
                                                        target_os, True, False]).start()

    @staticmethod
    def discover_relevant_fast_resume(bt_backup_path: str, existing_path: str):
        """
        Find .fastresume files that contain the existing path.
        :param bt_backup_path: Path to BT_backup folder
        :type bt_backup_path: str
        :param existing_path: The existing path to look for
        :type existing_path: str
        :return: List of FastResume Objects
        :rtype: list[FastResume]
        """
        for file in os.listdir(bt_backup_path):
            if file.endswith('.fastresume'):
                fast_resume = FastResume(os.path.join(bt_backup_path, file))
                if existing_path in fast_resume.save_path or \
                        existing_path in fast_resume.qbt_save_path:
                    yield fast_resume
        return

    @classmethod
    def backup_folder(cls, folder_path, archive_path):
        cls.logger.info('Creating Archive %s ...' % archive_path)
        with zipfile.ZipFile(archive_path, 'w') as archive:
            for file in os.listdir(folder_path):
                archive.write(os.path.join(folder_path, file))
        cls.logger.info('Done!')

    @classmethod
    def update_fastresume(cls, fast_resume: 'FastResume', existing_path: str, new_path: str,
                          target_os: str = None, save_file: bool = True, create_backup: bool = True):
        cls.logger.info('Updating FastResume %s...' % fast_resume.file_path)
        new_save_path = fast_resume.save_path.replace(existing_path, new_path)
        fast_resume.set_save_paths(path=new_save_path, target_os=target_os,
                                   save_file=save_file, create_backup=create_backup)
        cls.logger.info('FastResume (%s) Updated!' % fast_resume.file_path)


class FastResume(object):
    logger = logging.getLogger(__name__ + '.FastResume')

    def __init__(self, file_path: str):
        self._file_path = os.path.realpath(file_path)
        if not os.path.exists(self.file_path) or not os.path.isfile(self.file_path):
            raise FileNotFoundError(self.file_path)
        self.logger.debug(f'Loading Fast Resume: {self.file_path}')
        self._data = bencode.bread(self.file_path)
        if 'save_path' not in self._data or 'qBt-savePath' not in self._data:
            raise ValueError('Missing required keys for a qBittorrent .fastresume file')
        self.logger.debug(f'Fast Resume ({self.file_path}) Init Complete.')

    @property
    def file_path(self):
        return self._file_path

    @property
    def backup_filename(self):
        return '%s.%s.%s' % (self.file_path,
                             datetime.now().strftime('%Y%m%d%H%M%S'),
                             'bkup')

    @property
    def save_path(self):
        return self._data['save_path']

    @property
    def qbt_save_path(self):
        return self._data['qBt-savePath']

    @property
    def mapped_files(self):
        if 'mapped_files' in self._data:
            return self._data['mapped_files']
        return None

    def set_save_path(self, path: str, key: str = 'save_path', target_os: str = None,
                      save_file: bool = True, create_backup: bool = True):
        if key not in ['save_path', 'qBt-savePath']:
            raise KeyError('When setting a save path, key must be `save_path` or `qBt-savePath`. '
                           f'Received {key}')
        if create_backup:
            self.save(self.backup_filename)
        if target_os is not None:
            path = convert_slashes(path, target_os)
        self.logger.debug(f'Setting {key}... Old: %s, New: %s, Target OS: %s'
                          % (self._data[key],
                             path,
                             target_os))
        self._data[key] = path
        if save_file:
            self.save()

    def set_save_paths(self, path: str, target_os: str = None,
                       save_file: bool = True, create_backup: bool = True):
        if create_backup:
            self.save(self.backup_filename)
        self.set_save_path(path, key='save_path', target_os=target_os, save_file=False, create_backup=False)
        self.set_save_path(path, key='qBt-savePath', target_os=target_os, save_file=False, create_backup=False)
        if self.mapped_files is not None and target_os is not None:
            self.logger.debug('Converting Slashes for mapped_files...')
            self._data['mapped_files'] = [convert_slashes(path, target_os) for path in self.mapped_files]
        if save_file:
            self.save()

    def save(self, file_name=None):
        if file_name is None:
            file_name = self.file_path
        self.logger.info('Saving File %s...' % file_name)
        bencode.bwrite(self._data, file_name)
