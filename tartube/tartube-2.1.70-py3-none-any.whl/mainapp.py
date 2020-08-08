#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2019-2020 A S Lewis
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.


"""Main application class."""


# Import Gtk modules
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, GdkPixbuf


# Import Python standard modules
from gi.repository import Gio
import datetime
import json
import math
import os
import pickle
import re
import shutil
import sys
import threading
import time

import gettext
_ = gettext.gettext


# Import other Python modules
try:
    import feedparser
    HAVE_FEEDPARSER_FLAG = True
except:
    HAVE_FEEDPARSER_FLAG = False

try:
    import moviepy.editor
    HAVE_MOVIEPY_FLAG = True
except:
    HAVE_MOVIEPY_FLAG = False

try:
    import playsound
    HAVE_PLAYSOUND_FLAG = True
except:
    HAVE_PLAYSOUND_FLAG = False

if os.name != 'nt':
    try:
        from xdg_tartube import XDG_CONFIG_HOME
        HAVE_XDG_FLAG = True
    except:
        HAVE_XDG_FLAG = False
else:
    HAVE_XDG_FLAG = False

# Import our modules
import __main__
import config
import dialogue
import downloads
import files
import formats
import info
import mainwin
import media
import options
import refresh
import testing
import tidy
import updates
import utils


# Debugging flag (calls utils.debug_time at the start of every function)
DEBUG_FUNC_FLAG = False
# ...(but don't call utils.debug_time from the timer functions such as
#   self.script_slow_timer_callback() )
DEBUG_NO_TIMER_FUNC_FLAG = False


# Classes


class TartubeApp(Gtk.Application):

    """Main python class for the Tartube application."""


    # Standard class methods


    def __init__(self, *args, **kwargs):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('ap 113 __init__')

        # Register the application
        if not __main__.__multiple_instance_flag__:

            # Restrict Tartube to a single instance
            super(TartubeApp, self).__init__(
                *args,
                application_id=__main__.__app_id__,
                flags=Gio.ApplicationFlags.FLAGS_NONE,
                **kwargs,
            )

        else:

            # Permit multiple instances of Tartube
            super(TartubeApp, self).__init__(
                *args,
                application_id=None,
                flags=Gio.ApplicationFlags.FLAGS_NONE,
                **kwargs,
            )


        # Debugging flags
        # ---------------
        # After installation, don't show the dialogue windows prompting the
        #   user to choose Tartube's data directory; just use the default
        #   location
        self.debug_no_dialogue_flag = False
        # When loading a config/database file, if a lockfile is present, load
        #   the config/database file anyway (i.e., ignore lockfiles)
        self.debug_ignore_lockfile_flag = False
        # In the main window's menu, show a menu item for adding a set of
        #   media data objects for testing
        self.debug_test_media_menu_flag = False
        # In the main window's toolbar, show a toolbar item for adding a set of
        #   media data objects for testing
        self.debug_test_media_toolbar_flag = False
        # Open the main window in the top-left corner of the desktop
        self.debug_open_top_left_flag = False
        # Automatically open the system preferences window on startup
        self.debug_open_pref_win_flag = False
        # Automatically open the general download options window on startup
        self.debug_open_options_win_flag = False
        # Hide all the system folders (this is not reversible by setting the
        #   flag back to False)
        self.debug_hide_folders_flag = False


        # Instance variable (IV) list - class objects
        # -------------------------------------------
        # The main window object, set as soon as it's created
        self.main_win_obj = None
        # A fake main window object, temporarily created before the actual main
        #   window by self.start() (in certain situations)
        # The existence of the fake main window, which is always invisible,
        #   allows that code to create modal Gtk dialogue windows
        self.fake_main_win_obj = None
        # The system tray icon (a mainapp.StatusIcon object, inheriting from
        #   Gtk.StatusIcon)
        self.status_icon_obj = None
        #
        # At the moment, there are five operations - the download, update,
        #   refresh, info and tidy operations
        # Only one operation can be in progress at a time. When an operation is
        #   in progress, many functions (such as opening configuration windows)
        #   are not possible
        #
        # A download operation is handled by a downloads.DownloadManager
        #   object. It downloads files from a server (for example, it downloads
        #   videos from YouTube)
        # Although its not possible to run more than one download
        #   operation at a time, a single download operation can handle
        #   multiple simultaneous downloads
        # The current downloads.DownloadManager object, if a download operation
        #   is in progress (or None, if not)
        self.download_manager_obj = None
        # An update operation (to update youtube-dl) is handled by an
        #   updates.UpdateManager object. It updates youtube-dl to the latest
        #   version
        # The current updates.UpdateManager object, if an upload operation is
        #   in progress (or None, if not)
        self.update_manager_obj = None
        # A refresh operation compares the media registry with the contents of
        #   Tartube's data directories, adding new videos to the media registry
        #   and marking missing videos as not downloaded, as appropriate
        # The current refresh.RefreshManager object, if a refresh operation is
        #   in progress (or None, if not)
        self.refresh_manager_obj = None
        # An info operation fetches information about a particular video;
        #   currently, its available formats and available subtitles
        # The current info.InfoManager object, if an info operation is in
        #   progress (or None, if not)
        self.info_manager_obj = None
        # A tidy operation can check that videos still exist and aren't
        #   corrupted, or can remove all videos, or all thumbnails, and so on
        # The current tidy.TidyManager object, if a tidy operation is in
        #   progress (or None, if not)
        self.tidy_manager_obj = None
        # A livestream operation is handled by a downloads.LivestreamManager
        #   object. It checks media.Video objects marked as livestreams, to
        #   see whether have started or stopped broadcasting
        self.livestream_manager_obj = None
        #
        # When an operation is in progress, the manager object is stored here
        #   (so code can quickly check if an operation is in progress, or not)
        # Livestream operations run silently in the background, and no
        #   functionality is disabled. Therefore, this IV remains set to None
        #   when the livestream operation is running
        self.current_manager_obj = None
        #
        # The file manager, files.FileManager, for loading thumbnail, icon
        #   and JSON files safely (i.e. without causing a Gtk crash)
        self.file_manager_obj = files.FileManager()
        # The message dialogue manager, dialogue.DialogueManager, for showing
        #   message dialogue windows safely (i.e. without causing a Gtk crash)
        self.dialogue_manager_obj = None
        #
        # Media data classes are those specified in media.py. Those class
        #   objects are media.Video (for individual videos), media.Channel,
        #   media.Playlist and media.Folder (reprenting a sub-directory inside
        #   Tartube's data directory)
        # Some media data objects have a list of children which are themselves
        #   media data objects. In that way, the user can organise their videos
        #   in convenient folders
        # media.Folder objects can have any media data objects as their
        #   children (including other media.Folder objects). media.Channel and
        #   media.Playlist objects can have media.Video objects as their
        #   children. media.Video objects don't have any children
        # (Media data objects are stored in IVs below)
        #
        # During a download operation, youtube-dl is supplied with a set of
        #   download options. Those options are specified by an
        #   options.OptionsManager object
        # Each media data object may have its own options.OptionsManager
        #   object. If not, it uses the options.OptionsManager object of its
        #   parent (or of its parent's parent, and so on)
        # If this chain of family relationships doesn't provide an
        #   options.OptionsManager object, then this default object, known as
        #   the General Options Manager, is used
        self.general_options_obj = None
        # The options.OptionsManager object used in the Classic Mode Tab. If
        #   None, then self.general_options_obj is used
        self.classic_options_obj = None

        # Instance variable (IV) list - other
        # -----------------------------------
        # Custom locale (matches one of the values in formats.LOCALE_LIST)
        self.custom_locale = 'en_GB'

        # Default window sizes (in pixels)
        self.main_win_width = 800
        self.main_win_height = 600
        self.config_win_width = 650
        self.config_win_height = 450
        self.paned_min_size = 200
        # Default size (in pixels) of space between various widgets
        self.default_spacing_size = 5

        # Custom window sizes
        # Flag set to True if Tartube should remember the main window size
        #   when saving the config file, and then use that size when
        #   re-starting tartube
        self.main_win_save_size_flag = False
        # The size of the main window, when the config file was last saved...
        self.main_win_save_width = self.main_win_width
        self.main_win_save_height = self.main_win_height
        # ...and the position of the divider separating the Video Index and
        #   Video Catalogue in the Videos tab (the default value is also the
        #   minimum value saved)
        self.main_win_save_posn = self.paned_min_size

        # The current Gtk version
        self.gtk_version_major = Gtk.get_major_version()
        self.gtk_version_minor = Gtk.get_minor_version()
        self.gtk_version_micro = Gtk.get_micro_version()
        # Gtk produces numerous and endless error/warning messages when the
        #   Video Index and Video Catalogue are updated. These issues have
        #   still not been fixed by Gtk v3.24.18, and cause frequent crashes
        # Disable some cosmetic features by default. Most of these features
        #   involve updating the Video Index/Video Catalogue during a download
        #   operation (etc)
        # The user can enable the features themselves, if they are satisfied
        #   that Gtk has been fixed
        self.gtk_emulate_broken_flag = True

        # IVs used to place a lock on the loaded database file, so that
        #   competing instances of Tartube don't try to use it at the same time
        # Time to wait (in seconds) to save the config file, if a lockfile
        #   exists for it
        self.config_lock_time = 5
        # The path to the database lockfile created by this instance of
        #   Tartube (None if no lockfile has been created)
        self.db_lock_file_path = None

        # At all times (after initial setup), two GObject timers run - a fast
        #   one and a slow one
        # The slow timer's ID
        self.script_slow_timer_id = None
        # The slow timer interval time (in milliseconds)
        self.script_slow_timer_time = 30000
        # The fast timer's ID
        self.script_fast_timer_id = None
        # The fast timer interval time (in milliseconds)
        self.script_fast_timer_time = 1000

        # Flag set to True if the main toolbar should not be drawn when the
        #   main window is opened
        self.toolbar_hide_flag = False
        # Flag set to True if the main toolbar should be compressed (by
        #   removing the labels); ideal if the toolbar's contents won't fit in
        #   the standard-sized window (as it almost certainly won't on MS
        #   Windows)
        if os.name != 'nt':
            self.toolbar_squeeze_flag = False
        else:
            self.toolbar_squeeze_flag = True
        # Flag set to True if tooltips should be visible in the Video Index
        #   and the Video Catalogue
        self.show_tooltips_flag = True
        # Flag set to True if stock icons in the Videos/Classic Mode tabs
        #   should be replaced by a custom set of icons (in case the stock
        #   icons are not visible, for some reason)
        self.show_custom_icons_flag = False
        # Flag set to True if small icons should be used in the Video Index,
        #   False if large icons should be used
        self.show_small_icons_in_index_flag = False
        # Flag set to True if the Video Index treeview should auto-expand/
        #   auto-collapse when an item is clicked, to show/hide its children
        #   (only folders have children visible in the Video Index, though)
        self.auto_expand_video_index_flag = False
        # Flag set to True if the treeview should be fully expanded when an
        #   item is clicked; False if only the next level should be expanded
        #   (ignored if self.auto_expand_video_index_flag is False)
        self.full_expand_video_index_flag = False
        # Flag set to True if the 'Download all' buttons in the main window
        #   toolbar and in the Videos tab should be disabled (in case the u
        #   user is sure they only want to do simulated downloads)
        self.disable_dl_all_flag = False
        # Flag set to True if we should use 'Today' and 'Yesterday' in the
        #   Video Index, rather than a date
        self.show_pretty_dates_flag = True

        # Flag set to True if an icon should be displayed in the system tray
        self.show_status_icon_flag = True
        # Flag set to True if the main window should close to the tray, rather
        #   than halting the application altogether. Ignored if
        #   self.show_status_icon_flag is False
        self.close_to_tray_flag = False

        # Flag set to True if rows in the Progress List should be hidden once
        #   the download operation has finished with the corresponding media
        #   data object (so the user can see the media data objects currently
        #   being downloaded more easily)
        self.progress_list_hide_flag = False
        # Flag set to True if new rows should be added to the Results List
        #   at the top, False if they should be added at the bottom
        self.results_list_reverse_flag = False

        # Flag set to True if system error messages should be shown in the
        #   Errors/Warnings tab
        self.system_error_show_flag = True
        # Flag set to True if system warning messages should be shown in the
        #   Errors/Warnings tab
        self.system_warning_show_flag = True
        # Flag set to True if operation error messages should be shown in the
        #   Errors/Warnings tab
        self.operation_error_show_flag = True
        # Flag set to True if operation warning messages should be shown in the
        #   Errors/Warnings tab
        self.operation_warning_show_flag = True
        # Flag set to True if the total number of system error/warning messages
        #   shown in the tab label is not reset until the 'Clear the list'
        #   button is explicitly clicked (normally, the total numbers are
        #   reset when the user switches to a different tab)
        self.system_msg_keep_totals_flag = False

        # For quick lookup, the directory in which the 'tartube' executable
        #   file is found, and its parent directory
        self.script_dir = sys.path[0]
        self.script_parent_dir = os.path.abspath(
            os.path.join(self.script_dir, os.pardir),
        )

        # Tartube's data directory (platform-dependent), i.e. 'tartube-data'
        # Note that, using the MSWin installer, Cygwin gives file paths with
        #   both / and \ separators. Throughout the code, we use
        #   os.path.abspath to circumvent this problem
        self.default_data_dir = os.path.abspath(
            os.path.join(
                os.path.expanduser('~'),
                __main__.__packagename__ + '-data',
            ),
        )
        self.data_dir = self.default_data_dir
        # A list of data directories used recently by the user. The list
        #   includes the current value of self.data_dir, and can be
        #   customised by the user (to forget directories no longer needed)
        # Multiple instances of Tartube can use the same config file, but
        #   they cannot use the same database file at the same time
        # When Tartube starts, if the database file in the directory
        #   self.data_dir is locked, Tartube will try other directories in this
        #   list, in order, until finding one that isn't locked
        self.data_dir_alt_list = [ self.data_dir ]
        # self.data_dir records the path to the database file that was in
        #   memory, when the config file was last saved. Flag set to False to
        #   use this path (meaning that, on startup, the same database file is
        #   loaded), or True if the first path in self.data_dir_alt_list is
        #   loaded instead
        self.data_dir_use_first_flag = True
        # On startup (but not when switching databases), if the database file
        #   in self.data_dir is locked, when this flag is True Tartube will try
        #   other directories in self.data_dir_alt_list (as described above).
        #   If False, only self.data_dir is tried
        self.data_dir_use_list_flag = True
        # When switching to a new database file, the data directory (containing
        #   the file) is added to the list, if the flag it True
        self.data_dir_add_from_list_flag = True

        # The data directory is structured like this:
        #   /tartube-data
        #       tartube.db          [the Tartube database file]
        #       /.backups
        #           tartube_BU.db   [any number of database file backups]
        #       /.temp              [temporary directory, deleted on startup]
        #       /pewdiepie          [example of a custom media.Channel]
        #       /Temporary Videos   [standard media.Folder]
        #       /Unsorted Videos    [standard media.Folder]
        # Before v1.3.099, the data directory was structured like this:
        #   /tartube-data
        #       tartube.db
        #       tartube_BU.db
        #       /.temp
        #       /downloads
        #           /pewdiepie
        #           /Temporary Videos
        #           /Unsorted Videos
        # Tartube can read from both stcuctures although, when creating a new
        #   data directory, only the new structure is created
        #
        # The sub-directory into which videos are downloaded (new and old
        #   style)
        self.downloads_dir = os.path.abspath(
            os.path.join(
                os.path.expanduser('~'),
                __main__.__packagename__ + '-data',
            ),
        )
        self.alt_downloads_dir = os.path.abspath(
            os.path.join(
                os.path.expanduser('~'),
                __main__.__packagename__ + '-data',
                'downloads',
            ),
        )
        # A hidden directory, used for storing backups of the Tartube database
        #   file
        self.backup_dir = os.path.abspath(
            os.path.join(
                os.path.expanduser('~'),
                __main__.__packagename__ + '-data',
                '.backups',
            ),
        )

        # A temporary directory, deleted when Tartube starts and stops
        self.temp_dir = os.path.abspath(
            os.path.join(
                os.path.expanduser('~'),
                __main__.__packagename__ + '-data',
                '.temp',
            ),
        )
        # Inside the temporary directory, a downloads folder, replicating the
        #   layout of self.downloads_dir, and used for storing description,
        #   JSON and thumbnail files which the user doesn't want to store in
        #   self.downloads_dir
        self.temp_dl_dir = os.path.abspath(
            os.path.join(
                os.path.expanduser('~'),
                __main__.__packagename__ + '-data',
                '.temp',
                'downloads',
            ),
        )
        # Inside the temporary directory, a test folder into which an info
        #   operation can allow youtube-dl to download files
        self.temp_test_dir = os.path.abspath(
            os.path.join(
                os.path.expanduser('~'),
                __main__.__packagename__ + '-data',
                '.temp',
                'ytdl-test',
            ),
        )

        # The directory in which sound files are found, set in the call to
        #   self.find_sound_effects()
        self.sound_dir = None
        # List of sound files found in the ../sounds directory (e.g.
        #   'beep.mp3')
        self.sound_list = []
        # The user's preferred sound effect (for livestream alarms)
        self.sound_custom = 'bell.mp3'

        # Name of the Tartube config file
        self.config_file_name = 'settings.json'
        # The config file can be stored at one of two locations, depending on
        #   whether XDG is available, or not
        self.config_file_dir = os.path.abspath(self.script_parent_dir)
        self.config_file_path = os.path.abspath(
            os.path.join(self.script_parent_dir, self.config_file_name),
        )

        if not HAVE_XDG_FLAG:
            self.config_file_xdg_dir = None
            self.config_file_xdg_path = None
        else:
            self.config_file_xdg_dir = os.path.abspath(
                os.path.join(
                    XDG_CONFIG_HOME,
                    __main__.__packagename__,
                ),
            )

            self.config_file_xdg_path = os.path.abspath(
                os.path.join(
                    XDG_CONFIG_HOME,
                    __main__.__packagename__,
                    self.config_file_name,
                ),
            )

        # Name of the Tartube database file (storing media data objects). The
        #   database file is always found in self.data_dir
        self.db_file_name = __main__.__packagename__ + '.db'
        # Names of the database export files (one for JSON, for for plain text)
        self.export_json_file_name \
        = __main__.__packagename__ + '_db_export.json'
        self.export_text_file_name \
        = __main__.__packagename__ + '_db_export.txt'
        # How Tartube should make backups of its database file:
        #   'default' - make a backup file during a save procedure, but delete
        #       it when the save procedure is complete
        #   'single' - make a backup file during a save procedure, replacing
        #       any existing backup file, and don't delete it when the save
        #       procedure is complete
        #   'daily' - make a backup file once per day, the first time a save
        #       procedure is performed in that day. The file is labelled with
        #       the date, so backup files from previous days are not
        #       overwritten
        #   'always' - always make a backup file, labelled with the date and
        #       time, so that no backup file is ever overwritten
        self.db_backup_mode = 'single'
        # If loading/saving of a config or database file fails, this flag is
        #   set to True, which disables all loading/saving for the rest of the
        #   session
        self.disable_load_save_flag = False
        # Optional error message generated when self.disable_load_save_flag
        #   was set to True
        self.disable_load_save_msg = None
        # If loading a database file (only) fails because of a lock file, this
        #   flag is set to True, so the user is prompted to remove the possibly
        #   stale lock file. If the user declines, the error message stored in
        #   self.disable_load_save_msg is then displayed
        self.disable_load_save_lock_flag = False
        # Users have reported that the Tartube database file was corrupted. On
        #   inspection, it was almost completely empty, presumably because
        #   self.save_db had been called before .load_db
        # As the corruption was catastrophic, make sure that can never happen
        #   again with this flag, set to False until the code has either
        #   loaded a database file, or wants to call .save_db to create one
        self.allow_db_save_flag = False

        # Flag set to True if the Classic Mode Tab should be the visible one,
        #   when Tartube first starts (for the benefit of users who only want
        #   Classic Mode downloads)
        self.show_classic_tab_on_startup_flag = False
        # Users can add more destination directories to the combobox in the
        #   Classic Mode Tab. Tartube remembers those directories, up to the
        #   maximum number specified below
        self.classic_dir_list = [ os.path.expanduser('~') ]
        # The maximum size of the list. When a new directory is added by the
        #   user, it's moved to the top of the list. If the list is now too
        #   big, the last item is removed
        self.classic_dir_max = 8
        # The most recently-selected destination directory. On startup, if this
        #   directory still exists in self.classic_dir_list, it is moved to the
        #   top (and so it appears as the first item in the combobox). This IV
        #   is then reset
        self.classic_dir_previous = None

        # The youtube-dl binary to use (platform-dependent) - 'youtube-dl' or
        #   'youtube-dl.exe', depending on the platform. The default value is
        #   set by self.start()
        self.ytdl_bin = None
        # The default path to the youtube-dl binary. The value is set by
        #   self.start(). On MSWin, it is 'youtube-dl.exe'. On Linux, it is
        #   '/usr/bin/youtube-dl'
        self.ytdl_path_default = None
        # The path to the youtube-dl binary, after installation using PyPI.
        #   Not used on MS Windows. The initial ~ character must be substituted
        #   for os.path.expanduser('~'), before use
        self.ytdl_path_pypi = '~/.local/bin/youtube-dl'
        # The actual path to use in the shell command during a download or
        #   update operation. Initially given the same value as
        #   self.ytdl_path_default
        # On MSWin, this value doesn't change. On Linux, depending on how
        #   youtube-dl was installed, it might be '/usr/bin/youtube-dl' or just
        #   'youtube-dl'
        self.ytdl_path = None
        # The shell command to use during an update operation depends on how
        #   youtube-dl was installed
        # Depending on the operatin system, Tartube provides some of these
        #   methods (listed here with the description visible to the user):
        #
        # 'ytdl_update_default_path'
        #       Update using default youtube-dl path
        # 'ytdl_update_local_path'
        #       Update using local youtube-dl path
        # 'ytdl_update_pip'
        #       Update using pip
        # 'ytdl_update_pip_omit_user'
        #       Update using pip (omit --user option)
        # 'ytdl_update_pip3'
        #       Update using pip3
        # 'ytdl_update_pip3_omit_user'
        #       Update using pip3 (omit --user option)
        # 'ytdl_update_pip3_recommend'
        #       Update using pip3 (recommended)
        # 'ytdl_update_pypi_path'
        #       Update using PyPI youtube-dl path
        # 'ytdl_update_win_32',
        #       Windows 32-bit update (recommended)
        # 'ytdl_update_win_64',
        #       Windows 64-bit update (recommended)
        # 'ytdl_update_disabled'
        #       youtube-dl updates are disabled
        # A dictionary containing some possibilities, populated by self.start()
        # Dictionary in the form
        #   key: method name (one of those listed above)
        #   value: list of words to use in the shell command
        self.ytdl_update_dict = {}
        # A list of keys from self.ytdl_update_dict in a standard order (so the
        #   combobox in config.SystemPrefWin is in a standard order)
        self.ytdl_update_list = []
        # The user's choice of shell command; one of the keys in
        #   self.ytdl_update_dict, set by self.start()
        self.ytdl_update_current = None

        # Flag set to True if youtube-dl system commands should be displayed in
        #   the Output Tab
        self.ytdl_output_system_cmd_flag = True
        # Flag set to True if youtube-dl's STDOUT should be displayed in the
        #   Output Tab
        self.ytdl_output_stdout_flag = True
        # Flag set to True if we should ignore JSON output when displaying text
        #   in the Output Tab (ignored if self.ytdl_output_stdout_flag is
        #   False)
        self.ytdl_output_ignore_json_flag = True
        # Flag set to True if we should ignore download progress (as a
        #   percentage) when displaying text in the Output Tab (ignored if
        #   self.ytdl_output_stdout_flag is False)
        self.ytdl_output_ignore_progress_flag = True
        # Flag set to True if youtube-dl's STDERR should be displayed in the
        #   Output Tab
        self.ytdl_output_stderr_flag = True
        # Flag set to True if pages in the Output Tab should be emptied at the
        #   start of each operation
        self.ytdl_output_start_empty_flag = True
        # Flag set to True if a summary page should be visible in the Output
        #   Tab. Changes to this flag are applied when Tartube restarts
        self.ytdl_output_show_summary_flag = False

        # Flag set to True if youtube-dl system commands should be written to
        #   the terminal window
        self.ytdl_write_system_cmd_flag = False
        # Flag set to True if youtube-dl's STDOUT should be written to the
        #   terminal window
        self.ytdl_write_stdout_flag = False
        # Flag set to True if we should ignore JSON output when writing to the
        #   terminal window (ignored if self.ytdl_write_stdout_flag is False)
        self.ytdl_write_ignore_json_flag = True
        # Flag set to True if we should ignore download progress (as a
        #   percentage) when writing to the terminal window (ignored if
        #   self.ytdl_write_stdout_flag is False)
        self.ytdl_write_ignore_progress_flag = True
        # Flag set to True if youtube-dl's STDERR should be written to the
        #   terminal window
        self.ytdl_write_stderr_flag = False

        # Flag set to True if youtube-dl should show verbose output (using the
        #   --verbose option). The setting applies to both the Output Tab and
        #   the terminal window
        self.ytdl_write_verbose_flag = False

        # Flag set to True if, during a refresh operation, videos should be
        #   displayed in the Output Tab. Set to False if only channels,
        #   playlists and folders should be displayed there
        self.refresh_output_videos_flag = True
        # Flag set to True if, during a refresh operation, non-matching videos
        #   should be displayed in the Output Tab. Set to False if only
        #   matching videos should be displayed there. Ignore if
        #   self.refresh_output_videos_flag is False
        self.refresh_output_verbose_flag = False
        # The moviepy module hangs indefinitely, if it is used to open a
        #   corrupted video file
        #   (see https://github.com/Zulko/moviepy/issues/639)
        # To counter this, self.update_video_from_filesystem() moves the
        #   procedure into a thread, and applies a timeout to that thread
        # The timeout (in seconds) to apply. Must be an integer, 0 or above.
        #   If 0, the moviepy procedure is allowed to hang indefinitely
        self.refresh_moviepy_timeout = 10

        # Path to the ffmpeg/avconv binary (or the directory containing the
        #   binary). If set to any value besides None,
        #   downloads.VideoDownloader will pass the value to youtube-dl using
        #   its --ffmpeg-location option
        self.ffmpeg_path = None

        # Flag set to True if the General Options Manager
        #   (self.general_options_obj) should be cloned whenever the user
        #   applies a new options manager to a media data object (e.g. by
        #   right-clicking a channel in the Video Index, and selecting
        #   Downloads > Apply options manager)
        self.auto_clone_options_flag = True

        # During a download operation, a GObject timer runs, so that the
        #   Progress Tab and Output Tab can be updated at regular intervals
        # There is also a delay between the instant at which youtube-dl
        #   reports a video file has been downloaded, and the instant at which
        #   it appears in the filesystem. The timer checks for newly-existing
        #   files at regular intervals, too
        # The timer's ID (None when no timer is running)
        self.dl_timer_id = None
        # The timer interval time (in milliseconds)
        self.dl_timer_time = 500
        # At the end of the download operation, the timer continues running for
        #   a few seconds, to give new files a chance to appear in the
        #   filesystem. The maximum time to wait (in seconds)
        self.dl_timer_final_time = 10
        # Once that extra time has been applied, the time (matches time.time())
        #   at which to stop waiting
        self.dl_timer_check_time = None

        # During a download operation, we periodically check whether the device
        #   containing self.data_dir is running out of space
        # The check interval time (in seconds)
        self.dl_timer_disk_space_time = 60
        # The time (matchs time.time()) at which the next check takes place
        self.dl_timer_disk_space_check_time = None

        # Flag set to True if Tartube should warn if the system is running out
        #   of disk space (on the drive containing self.data_dir), False if
        #   not. The warning is issued at the start of a download operation
        self.disk_space_warn_flag = True
        # The amount of free disk space (in Mb) below which the warning is
        #   issued. If 0, no warning is issued. Ignored if
        #   self.disk_space_warn_flag is False
        self.disk_space_warn_limit = 1000
        # Flag set to True if Tartube should refuse to start a download
        #   operation, and halt an existing download operation, if the system
        #   is running out of disk space (on the drive containing
        #   self.data_dir), False if not
        self.disk_space_stop_flag = True
        # The amount of free disk space (in Mb) below which the refusal/halt
        #   is enacted. If 0, a download operation will continue downloading
        #   files until the device actually runs out of space. Ignored if
        #   self.disk_space_stop_flag is False
        self.disk_space_stop_limit = 500
        # The IVs above can be set to any number (0 or above), but the
        #   Gtk.SpinButtons in the system preferences window increment/
        #   decrement the value by this many Mb at a time
        self.disk_space_increment = 100
        # An absolute minimum of disk space, below which a download operation
        #   will not start, or will halt, regardless of the values of the IVs
        #   above (in Mb)
        self.disk_space_abs_limit = 50

        # Custom download operation settings
        # If True, during a custom download, download every video which is
        #   marked as not downloaded (often after a 'Check all' operation);
        #   don't download channels/playlists directly
        self.custom_dl_by_video_flag = False
        # During a custom download, any videos whose source URL is YouTube can
        #   be diverted to another website
        #       'default' - Use the original YouTube URL
        #       'hooktube' - Divert to hooktube.com
        #       'invidious' - Divert to invidio.us
        #       'other' - user enters their own alternative front-end website
        self.custom_dl_divert_mode = 'default'
        # If self.custom_dl_divert_mode is 'other', the address of the
        #   YouTube alternative. The string directly replaces the 'youtube.com'
        #   part of a URL; so the string must be something like 'hooktube.com'
        #   not 'http://hooktube.com' or anything like that
        # Ignored if it does not contain at least 3 characters. Ignored for any
        #   other value of self.custom_dl_divert_mode
        self.custom_dl_divert_website = ''
        # If True, during a custom download, a delay (in minutes) is applied
        #   between media data object downloads. When applied to a
        #   channel/playlist, the delay occurs after the whole channel/
        #   playlist. When applied directly to videos, the delay occurs after
        #   each video
        self.custom_dl_delay_flag = False
        # The maximum delay to apply (in minutes, minimum value 0.2).
        #   Ignored if self.custom_dl_delay_flag is False
        self.custom_dl_delay_max = 5
        # The minimum delay to apply (in minutes, minimum value 0, maximum
        #   value self.custom_dl_delay_max). If specified, the delay is a
        #   random length of time between this value and
        #   self.custom_dl_delay_max. Ignored if self.custom_dl_delay_flag is
        #   False
        self.custom_dl_delay_min = 0

        # During an update operation, a separate GObject timer runs, so that
        #   the Output Tab can be updated at regular intervals
        # The timer's ID (None when no timer is running)
        self.update_timer_id = None
        # The timer interval time (in milliseconds)
        self.update_timer_time = 500
        # At the end of the update operation, the timer continues running for
        #   a few seconds, to prevent various Gtk errors (and occasionally
        #   crashes) for systems with Gtk < 3.24. The maximum time to wait (in
        #   seconds)
        self.update_timer_final_time = 5
        # Once that extra time has been applied, the time (matches time.time())
        #   at which to stop waiting
        self.update_timer_check_time = None

        # During a refresh operation, a separate GObject timer runs, so that
        #   the Output Tab can be updated at regular intervals
        # The timer's ID (None when no timer is running)
        self.refresh_timer_id = None
        # The timer interval time (in milliseconds)
        self.refresh_timer_time = 500
        # At the end of the refresh operation, the timer continues running for
        #   a few seconds, to prevent various Gtk errors (and occasionally
        #   crashes) for systems with Gtk < 3.24. The maximum time to wait (in
        #   seconds)
        self.refresh_timer_final_time = 5
        # Once that extra time has been applied, the time (matches time.time())
        #   at which to stop waiting
        self.refresh_timer_check_time = None

        # During an info operation, a separate GObject timer runs, so that
        #   the Output Tab can be updated at regular intervals
        # The timer's ID (None when no timer is running)
        self.info_timer_id = None
        # The timer interval time (in milliseconds)
        self.info_timer_time = 500
        # At the end of the info operation, the timer continues running for
        #   a few seconds, to prevent various Gtk errors (and occasionally
        #   crashes) for systems with Gtk < 3.24. The maximum time to wait (in
        #   seconds)
        # (Shorter wait time than other operations, because this type of
        #   operation finishes quickly)
        self.info_timer_final_time = 2
        # Once that extra time has been applied, the time (matches time.time())
        #   at which to stop waiting
        self.info_timer_check_time = None

        # During a tidy operation, a separate GObject timer runs, so that
        #   the Output Tab can be updated at regular intervals
        # The timer's ID (None when no timer is running)
        self.tidy_timer_id = None
        # The timer interval time (in milliseconds)
        self.tidy_timer_time = 500
        # At the end of the tidy operation, the timer continues running for
        #   a few seconds, to prevent various Gtk errors (and occasionally
        #   crashes) for systems with Gtk < 3.24. The maximum time to wait (in
        #   seconds)
        # (Shorter wait time than other operations, because this type of
        #   operation might finish quickly)
        self.tidy_timer_final_time = 2
        # Once that extra time has been applied, the time (matches time.time())
        #   at which to stop waiting
        self.tidy_timer_check_time = None

        # During any operation (except livestream operations), a flag set to
        #   True if the operation was halted by the user, rather than being
        #   allowed to complete naturally
        self.operation_halted_flag = False
        # During a download operation, a flag set to True if Tartube must shut
        #   down when the operation is finished
        self.halt_after_operation_flag = False
        # During a download operation, a flag set to True if no dialogue
        #   window must be shown at the end of that operation (but not
        #   necessarily any future download operations)
        self.no_dialogue_this_time_flag = False

        # For a channel/playlist containing hundreds (or more!) videos, a
        #   download operation will take a very long time, even though we might
        #   only want to check for new videos
        # Flag set to True if the download operation should give up checking a
        #   channel or playlist when its starts receiving details of videos
        #   about which it already knows (from a previous download operation)
        # This works well if the website sends video in order, youngest first
        #   (as YouTube does), but won't work at all otherwise
        self.operation_limit_flag = False
        # During simulated video downloads (e.g. after clicking the 'Check all'
        #   button), stop checking the channel/playlist after receiving details
        #   for this many videos, when a media.Video object exists for them
        #   and the object's .file_name and .name IVs are set
        # Must be an positive integer or 0. If 0, no limit applies. Ignored if
        #   self.operation_limit_flag is False
        self.operation_check_limit = 3
        # During actual video downloads (e.g. after clicking the 'Download all'
        #   button), stop downloading the channel/playlist after receiving
        #   this many 'video already downloaded' messages, when a media.Video
        #   objects exists for them and the object's .dl_flag is set
        # Must be an positive integer or 0. If 0, no limit applies. Ignored if
        #   self.operation_limit_flag is False
        self.operation_download_limit = 3

        # The media data registry
        # Every media data object has a unique .dbid (which is an integer). The
        #   number of media data objects ever created (including any that have
        #   been deleted), used to give new media data objects their .dbid
        self.media_reg_count = 0
        # A dictionary containing all media data objects (but not those which
        #   have been deleted)
        # Dictionary in the form
        #   key = media data object's unique .dbid
        #   value = the media data object itself
        self.media_reg_dict = {}
        # media.Channel, media.Playlist and media.Folder objects must have
        #   unique .name IVs
        # (A channel and a playlist can't have the same name. Videos within a
        #   single channel, playlist or folder can't have the same name.
        #   Videos with different parent objects CAN have the same name)
        # A dictionary used to check that media.Channel, media.Playlist and
        #   media.Folder objects have unique .name IVs (and to look up names
        #   quickly)
        # Dictionary in the form
        #   key = media data object's .name
        #   value = media data object's unique .dbid
        self.media_name_dict = {}
        # An ordered list of media.Channel, media.Playlist and media.Folder
        #   objects which have no parents (in the order they're displayed)
        # This list, combined with each media data object's child list, is
        #   used to construct a family tree. A typical family tree looks
        #   something like this:
        #           Folder
        #               Channel
        #                   Video
        #                   Video
        #               Channel
        #                   Video
        #                   Video
        #           Folder
        #               Folder
        #                   Playlist
        #                       Video
        #                       Video
        #               Folder
        #                   Playlist
        #                       Video
        #                       Video
        #           Folder
        #               Video
        #               Video
        # A list of .dbid IVs for all top-level media.Channel, media.Playlist
        #   and media.Folder objects
        self.media_top_level_list = []
        # The maximum depth of the media registry. The diagram above shows
        #   channels on the 2nd level and playlists on the third level.
        #   Container objects cannot be added beyond the following level
        self.media_max_level = 8
        # Standard name for a media.Video object, when the actual name of the
        #   video is not yet known
        self.default_video_name = '(video with no name)'
        # The maximum length of channel, playlist and folder names (does not
        #   apply to video names)
        self.container_name_max_len = 64
        # Forbidden names for channels, playlists and folders. This is to
        #   prevent the user overwriting directories in self.data_dir, that
        #   Tartube uses for its own purposes, and to prevent the user fooling
        #   Tartube into thinking that the old file structure is being used
        # Every item in this list is a regex; a name for a channel, playlist
        #   or folder must not match any item in the list. (media.Video
        #   objects can still have any name)
        self.illegal_name_regex_list = [
            r'^\.',
            r'^downloads$',
            __main__.__packagename__,
        ]

        # A subset of self.media_reg_dict, containing only media.Videos which
        #   are marked as livestreams (and which must therefore be checked by
        #   livestream operations)
        self.media_reg_live_dict = {}
        # A subset of self.media_reg_live_dict, containing only media.Videos
        #   which are waiting live streams. When the livestream goes live, a
        #   desktop notification is shown for them
        self.media_reg_auto_notify_dict = {}
        # A subset of self.media_reg_live_dict, containing only media.Videos
        #   which are waiting live streams. When the livestream goes live, an
        #   alarm is sounded for them
        self.media_reg_auto_alarm_dict = {}
        # A subset of self.media_reg_live_dict, containing only media.Videos
        #   which are waiting live streams. When the livestream goes live, the
        #   video is opened in the system's web browser
        self.media_reg_auto_open_dict = {}
        # A subset of self.media_reg_live_dict, containing only media.Videos
        #   which should be downloaded, as soon as they start (as soon as this
        #   is processed, the entry is removed from the dictionary)
        self.media_reg_auto_dl_start_dict = {}
        # A subset of self.media_reg_live_dict, containing only media.Videos
        #   which should be downloaded, as soon as they stop (as soon as this
        #   is processed, the entry is removed from the dictionary)
        self.media_reg_auto_dl_stop_dict = {}

        # Some media data objects are fixed (i.e. are created when Tartube
        #   first starts, and cannot be deleted by the user). Shortcuts to
        #   those objects
        # Private folder containing all videos (users cannot add anything to a
        #   private folder, because it's used by Tartube for special purposes)
        self.fixed_all_folder = None
        # Private folder containing only bookmarked videos
        self.fixed_bookmark_folder = None
        # Private folder containing only favourite videos
        self.fixed_fav_folder = None
        # Private folder containing only videos marked as (waiting or
        #   broadcasting) livestreams
        self.fixed_live_folder = None
        # Private folder containing only videos that have been removed from
        #   a channel/playlist (by the creator); only updated when
        #   self.track_missing_videos_flag is enabled
        self.fixed_missing_folder = None
        # Private folder containing only new videos
        self.fixed_new_folder = None
        # Private folder containing only playlist videos (when the user
        #   watches one, online or locally, the video is removed from the
        #   playlist)
        self.fixed_waiting_folder = None
        # Public folder that's used as the second one in the 'Add video'
        #   dialogue window, in which the user can store any individual videos
        #   that are automatically deleted when Tartube shuts down
        self.fixed_temp_folder = None
        # Public folder that's used as the first one in the 'Add video'
        #   dialogue window, in which the user can store any individual videos
        self.fixed_misc_folder = None
        # The locale for which the fixed folders are named. When the database
        #   file is loaded, if this value no longer matches self.custom_locale,
        #   then the folder names are all updated for the new locale
        self.fixed_folder_locale = self.custom_locale

        # A list of media.Video objects the user wants to watch, as soon as
        #   they have been downloaded. Videos are added by a call to
        #   self.watch_after_dl_list(), and removed by a call to
        #   self.announce_video_download()
        self.watch_after_dl_list = []

        # Automatic 'Download all' download operations - 'none' to disable,
        #   'start' to perform the operation whenever Tartube starts, or
        #   'scheduled' to perform the operation at regular intervals
        self.scheduled_dl_mode = 'none'
        # The time between 'scheduled' 'Download all' operations, if enabled
        self.scheduled_dl_wait_value = 2
        # ...using this unit (any of the values in formats.TIME_METRIC_LIST)
        self.scheduled_dl_wait_unit = 'hours'
        # The time (system time, in seconds) at which the last 'Download all'
        #   operation started (regardless of whether it was 'scheduled' or not)
        self.scheduled_dl_last_time = 0
        # If self.scheduled_dl_mode is 'start', on startup we wait a few
        #   seconds (for aesthetic reasons). The number of seconds to wait
        self.scheduled_dl_start_wait_time = 3
        # The time (system time, in seconds) at which the scheduled download
        #   operation should start (if no other operation has started in the
        #   meantime)
        self.scheduled_dl_start_check_time = None

        # Automatic 'Check all' download operations - 'none' to disable,
        #   'start' to perform the operation whenever Tartube starts, or
        #   'scheduled' to perform the operation at regular intervals
        self.scheduled_check_mode = 'none'
        # The time between 'scheduled' 'Check all' operations, if enabled
        self.scheduled_check_wait_value = 2
        # ...using this unit (any of the values in formats.TIME_METRIC_LIST)
        self.scheduled_check_wait_unit = 'hours'
        # The time (system time, in seconds) at which the last 'Check all'
        #   operation started (regardless of whether it was scheduled or not)
        self.scheduled_check_last_time = 0
        # If self.scheduled_check_mode is 'start', on startup we wait a few
        #   seconds (for aesthetic reasons). The number of seconds to wait
        self.scheduled_check_start_wait_time = 3
        # The time (system time, in seconds) at which the scheduled download
        #   operation should start (if no other operation has started in the
        #   meantime)
        self.scheduled_check_start_check_time = None

        # Flag set to True if Tartube should shut down after a 'Download all'
        #   operation (if self.scheduled_dl_mode is not 'none'), and after a
        #   'Check all' operation (if self.scheduled_check_mode is not 'none')
        self.scheduled_shutdown_flag = False

        # Flag set to True if Tartube should try to detect livestreams (on
        #   compatible websites only)
        # This feature is only tested on YouTube. It might work on other
        #   websites, if the user has set the RSS feed for each channel/
        #   playlist individually
        # If enabled, the download operation checks a channel/playlist RSS for
        #   videos that weren't picked up by ytdl, and marks them as
        #   livestreams. If JSON data can't be downloaded from it, assume it's
        #   an upcoming livestream; otherwise assume the livestream is live
        self.enable_livestreams_flag = True
        # If enabled, Tartube will assume that the website lists videos in
        #   order of announcement time, and will stop checking the RSS feed
        #   when it finds videos which are at least this old (in days). If set
        #   to zero, Tartube stops checking the RSS feed when it finds the
        #   first non-livestream video
        self.livestream_max_days = 7
        # Flag set to True if livestream videos in the Video Catalogue should
        #   be drawn with a coloured background, False if not
        self.livestream_use_colour_flag = True
        # Flag set to True if a desktop notification should be shown when a
        #   waiting livestream goes live (the setting can then be enabled/
        #   disabled for each video individually in the Video Catalogue)
        self.livestream_auto_notify_flag = False
        # Flag set to True if a Tartube should play an alarm when a waiting
        #   livestream goes live (the setting can then be enabled/disabled for
        #   each video individually in the Video Catalogue)
        self.livestream_auto_alarm_flag = False
        # Flag set to True if a video should be opened in the system's web
        #   browser when it goes live (the setting can then be enabled/
        #   disabled for each video individually in the Video Catalogue)
        self.livestream_auto_open_flag = False
        # Flag set to True if a video should be downloaded as soon as the
        #   livestream starts (media.Video.live_mode was 0/1, set to 2; the
        #   setting can then be enabled/disabled for each video individually in
        #   the Video Catalogue)
        # The start of the download may be delayed if a download operation is
        #   already in progress
        self.livestream_auto_dl_start_flag = False
        # Flag set to True if a video should be downloaded as soon as the
        #   livestream stops (media.Video.live_mode was 2, set to 0; the
        #   setting can then be enabled/disabled for each video individually in
        #   the Video Catalogue)
        # The start of the download may be delayed if a download operation is
        #   already in progress
        # If both this flag and self.livestream_auto_dl_start_flag are set to
        #   True, then youtube-dl is instructed to overwrite the earlier file
        # (NB As of April 2020, this is still not possible; as a temporary
        #   measure, the earlier file is renamed instead)
        self.livestream_auto_dl_stop_flag = False
        # The livestream operation can run periodically and checks the
        #   status of videos marked as livestreams
        # Flag set to True if the livestream task should run periodically
        self.scheduled_livestream_flag = True
        # The time (in minutes) between scheduled livestream operations, if
        #   enabled (cannot be fractional, minimum value 1)
        self.scheduled_livestream_wait_mins = 3
        # The time (system time, in seconds) at which the last livestream
        #   operation started
        self.scheduled_livestream_last_time = 0

        # Flag set to True if a download operation should auto-stop after a
        #   certain period of time (applies to both real and simulated
        #   downloads)
        self.autostop_time_flag = False
        # Auto-stop after this amount of time (minimum value 1)...
        self.autostop_time_value = 1
        # ...in this many units (any of the values in
        #   formats.TIME_METRIC_LIST)
        self.autostop_time_unit = 'hours'
        # Flag set to True if a download operation should auto-stop after a
        #   certain number of videos (applies to both real and simulated
        #   downloads)
        self.autostop_videos_flag = False
        # Auto-stop after this many videos (minimum value 1)
        self.autostop_videos_value = 100
        # Flag set to True if a download operation should auto-stop after
        #   downloading videos of a certain combined size (applies to real
        #   downloads only; the specified size is approximate, because it
        #   relies on th video size reported by youtube-dl, and doesn't take
        #   account of thumbnails, JSON data, and so on)
        self.autostop_size_flag = False
        # Auto-stop after this amount of diskspace (minimum value 1)...
        self.autostop_size_value = 1
        # ...in this many units (any of the values in
        #   formats.FILESIZE_METRIC_LIST)
        self.autostop_size_unit = 'GiB'

        # Flag set to True if an update operation should be automatically
        #   started before the beginning of every download operation
        self.operation_auto_update_flag = False
        # When that flag is True, the following IVs are set by the initial
        #   call to self.download_manager_start(), reminding
        #   self.update_manager_finished() to start a download operation, and
        #   supplying it with the arguments from the original call to
        #   self.download_manager_start()
        self.operation_waiting_flag = False
        self.operation_waiting_type = None
        self.operation_waiting_list = []
        # Flag set to True if files should be saved at the end of every
        #   operation
        self.operation_save_flag = True
        # Flag set to True if, during download operations using simulated
        #   downloads, videos whose parent is a media.Folder (i.e. videos not
        #   in channels/playlists) should not be added to the downlist list,
        #   unless the location of the video file is not set and no thumbnail
        #   has been downloaded. If False, those videos are always added to
        #   the download list
        # (This does not affect real downloads, in which such videos are never
        #   added to the download list)
        self.operation_sim_shortcut_flag = True
        # How to notify the user at the end of each download/update/refresh
        #   operation: 'dialogue' to use a dialogue window, 'desktop' to use a
        #   desktop notification, or 'default' to do neither
        # NB Desktop notifications don't work on MS Windows
        self.operation_dialogue_mode = 'dialogue'
        # What to do when the user creates a media.Video object whose URL
        #   represents a channel or playlist
        # 'channel' to create a new media.Channel object, and place all the
        #   downloaded videos inside it (the original media.Video object is
        #   destroyed)
        # 'playlist' to create a new media.Playlist object, and place all the
        #   downloaded videos inside it (the original media.Video object is
        #   destroyed)
        # 'multi' to create a new media.Video object for each downloaded video,
        #   placed in the same folder as the original media.Video object (the
        #   original is destroyed)
        # 'disable' to download nothing from the URL
        # There are some restrictions. If the original media.Video object is
        #   contained in a folder whose .restrict_flag is False, and if the
        #   mode is 'channel' or 'playlist', then the new channel/playlist is
        #   not created in that folder. If the original media.Video object is
        #   contained in a channel or playlist, all modes to default to
        #   'disable'
        self.operation_convert_mode = 'channel'
        # Flag set to True if self.update_video_from_filesystem() should get
        #   the video duration, if not already known, using the moviepy.editor
        #   module (an optional dependency)
        self.use_module_moviepy_flag = True

        # Flag set to True if dialogue windows for adding videos, channels and
        #   playlists should copy the contents of the system clipboard
        self.dialogue_copy_clipboard_flag = True
        # Flag set to True if dialogue windows for adding channels and
        #   playlists should continually re-open, whenever the use clicks the
        #   OK button (so multiple channels etc can be added quickly)
        self.dialogue_keep_open_flag = False

        # Flag set to True if, when downloading videos, youtube-dl should be
        #   passed, --download-archive, creating the file ytdl-archive.txt
        # If the file exists, youtube-dl won't re-download a video a user has
        #   deleted
        # Ignored for system folders like 'Unsorted Videos'
        self.allow_ytdl_archive_flag = True
        # Flag set to True if an archive file should be created when
        #   downloading from the Classic Mode Tab (this is marked 'not
        #   recommended' in the edit window)
        self.classic_ytdl_archive_flag = False
        # If self.allow_ytdl_archive_flag is set, youtube-dl will have created
        #   a ytdl_archive.txt, recording every video ever downloaded in the
        #   parent directory
        # This will prevent a successful re-downloading of the video. In
        #   response, the archive file is temporarily renamed (in a call to
        #   self.set_backup_archive() ). The details are stored in these IVs,
        #   so the original file names can be restored at the end of the
        #   download operation (in a call to self.reset_backup_archive() )
        self.ytdl_archive_path_list = []
        self.ytdl_archive_backup_path_list = []
        # Flag set to True if, when checking videos/channels/playlists, we
        #   should timeout after 60 seconds (in case youtube-dl gets stuck
        #   downloading the JSON data)
        self.apply_json_timeout_flag = True
        # Flag set to True if, when checking/downloading channels/playlists,
        #   we should look out for previously-downloaded videos (that the
        #   creator has since removed from their channel/playlist), and add
        #   them to the system 'Missing videos' folder
        self.track_missing_videos_flag = False
        # Flag set to True if a time limit should be placed on missing videos.
        #   Ignored if self.track_missing_videos_flag is False
        self.track_missing_time_flag = False
        # The time limit (in days) to apply. If videos will only be marked as
        #   missing if uploaded within this many days. If set to 0, no videos
        #   are marked as missing. Ignored if self.track_missing_videos_flag or
        #   self.track_missing_time_flag is False
        self.track_missing_time_days = 14

        # Flag set to True if 'Child process exited with non-zero code'
        #   messages, generated by Tartube, should be ignored (in the
        #   Errors/Warnings tab)
        self.ignore_child_process_exit_flag = True
        # Flag set to True if 'unable to download video data: HTTP Error 404'
        #   messages from youtube-dl should be ignored (in the Errors/Warnings
        #   tab)
        self.ignore_http_404_error_flag = False
        # Flag set to True if 'Did not get any data blocks' messages from
        #   youtube-dl should be ignored (in the Errors/Warnings tab)
        self.ignore_data_block_error_flag = False
        # Flag set to True if 'Requested formats are incompatible for merge and
        #   will be merged into mkv' messages from youtube-dl should be ignored
        #   (in the Errors/Warnings tab)
        self.ignore_merge_warning_flag = False
        # Flag set to True if 'No video formats found; please report this
        #   issue on...' messages from youtube-dl should be ignored (in the
        #   Errors/Warnings tab)
        self.ignore_missing_format_error_flag = False
        # Flag set to True if 'There are no annotations to write' messages
        #   should be ignored (in the Errors/Warnings tab)
        self.ignore_no_annotations_flag = True
        # Flag set to True if 'video doesn't have subtitles' errors should be
        #   ignored (in the Errors/Warnings tab)
        self.ignore_no_subtitles_flag = True

        # Flag set to True if YouTube copyright messages should be ignored (in
        #   the Errors/Warnings tab)
        self.ignore_yt_copyright_flag = False
        # Flag set to True if YouTube age-restriction messages should be
        #   ignored (in the Errors/Warnings tab)
        self.ignore_yt_age_restrict_flag = False
        # Flag set to True if 'The uploader has not made this video available'
        #   messages should be ignored (in the Errors/Warnings tab)
        self.ignore_yt_uploader_deleted_flag = False

        # Websites other than YouTube typically use different error messages
        # A custom list of strings or regexes, which are matched against error
        #   messages. Any matching error messages are not displayed in the
        #   Errors/Warnings tab. The user can add
        self.ignore_custom_msg_list = []
        # Flag set to True if the contents of the list are regexes, False if
        #   they are ordinary strings
        self.ignore_custom_regex_flag = False

        # During a download operation, the number of simultaneous downloads
        #   allowed. (An instruction to youtube-dl to download video(s) from a
        #   single URL is called a download job)
        # NB Because Tartube just passes a set of instructions to youtube-dl
        #   and then waits for the results, an increase in this number is
        #   applied to a download operation immediately, but a decrease is not
        #   applied until one of the download jobs has finished
        self.num_worker_default = 2
        # (Absoute minimum and maximum values)
        self.num_worker_max = 10
        self.num_worker_min = 1
        # Flag set to True when the limit is actually applied, False when not
        self.num_worker_apply_flag = True

        # During a download operation, the bandwith limit (in KiB/s)
        # NB Because Tartube just passes a set of instructions to youtube-dl,
        #   any change in this value is not applied until one of the download
        #   jobs has finished
        self.bandwidth_default = 500
        # (Absolute minimum and maximum values)
        self.bandwidth_max = 10000
        self.bandwidth_min = 1
        # Flag set to True when the limit is currently applied, False when not
        self.bandwidth_apply_flag = False

        # During a download operation, the maximum video resolution to
        #   download. Must be one of the keys in formats.VIDEO_RESOLUTION_DICT
        #   (e.g. '720p')
        self.video_res_default = '720p'
        # Flag set to True when this maximum video resolution is applied. When
        #   applied, it overrides the download option 'video_format_list' (see
        #   the comments in options.OptionsManager)
        self.video_res_apply_flag = False

        # The method of matching downloaded videos against existing
        #   media.Video objects:
        #       'exact_match' - The video name must match exactly
        #       'match_first' - The first n characters of the video name must
        #           match exactly
        #       'ignore_last' - All characters before the last n characters of
        #           the video name must match exactly
        self.match_method = 'exact_match'
        # Default values for self.match_first_chars and .match_ignore_chars
        self.match_default_chars = 10
        # For 'match_first', the number of characters (n) to use. Set to the
        #   default value when self.match_method is not 'match_first'; range
        #   1-999
        self.match_first_chars = self.match_default_chars
        # For 'ignore_last', the number of characters (n) to ignore. Set to the
        #   default value of when self.match_method is not 'ignore_last'; range
        #   1-999
        self.match_ignore_chars = self.match_default_chars

        # Automatic video deletion. Applies only to downloaded videos (not to
        #   checked videos)
        # Flag set to True if videos should be deleted after a certain time
        self.auto_delete_flag = False
        # Flag set to True if videos are automatically deleted after a certain
        #   time, but only if they have been watched (media.Video.dl_flag is
        #   True, media.Video.new_flag is False; ignored if
        #   self.auto_delete_old_flag is False)
        self.auto_delete_watched_flag = False
        # Videos are automatically deleted after this many days (must be an
        #   integer, minimum value 1; ignored if self.auto_delete_old_flag is
        #   False)
        self.auto_delete_days = 30

        # Temporary folder emptying (applies to all media.Folder objects whose
        #   .temp_flag is True)
        # Temporary folders are always emptied when Tartube starts. Flag set to
        #   True if they should be emptied when Tartube shuts down, as well
        self.delete_on_shutdown_flag = False
        # Flag set to True if temporary folders should be opened (on the
        #   desktop) when Tartube shuts down, so the user can more conveniently
        #   copy things out of it (but only if videos actually exist in the
        #   folder(s). Ignored if self.delete_on_shutdown_flag is True
        self.open_temp_on_desktop_flag = False

        # How much information to show in the Video Index. False to show
        #   minimal video stats, True to show full video stats
        self.complex_index_flag = False
        # The Video Catalogue has two 'skins', a simple view (without
        #   thumbnails) and a more complex view (with thumbnails)
        # Each skin can be set to show the name of the parent channel/playlist/
        #   folder, or not
        # The current Video Catalogue mode:
        #   'simple_hide_parent' - No thumbnail, show description
        #   'simple_show_parent' - No thumbnail, show parent
        #   'complex_hide_parent' - Thumbnail, show description
        #   'complex_hide_parent_ext' - Thumbnail, description & extra labels
        #   'complex_show_parent' - Thumbnail, show parent
        #   'complex_show_parent_ext' - Thumbnail, parent & extra labels
        self.catalogue_mode = 'complex_show_parent'
        # The Video Catalogue splits its video list into pages (as Gtk
        #   struggles with a list of hundreds, or thousands, of videos)
        # The number of videos per page, or 0 to always use a single page
        self.catalogue_page_size = 50
        # Flag set to True if the Video Catalogue toolbar should show an
        #   extra row, containing video filter options
        self.catalogue_show_filter_flag = False
        # Flag set to True if videos in the catalogue are sorted alphabetically
        #   or False if they are sorted by date (default)
        self.catalogue_alpha_sort_flag = False
        # Flag set to True if the 'Regex' button is toggled on, meaning that
        #   when the searching the catalogue, we match videos using a regex,
        #   rather than a simple string
        self.catologue_use_regex_flag = False

        # Flag set to True if a smaller set of options should be shown in the
        #   download options edit window (for inexperienced users)
        self.simple_options_flag = True


    def do_startup(self):

        """Gio.Application standard function."""

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 1407 do_startup')

        GObject.threads_init()
        Gtk.Application.do_startup(self)

        # Menu actions
        # ------------

        # 'File' column
        change_db_menu_action = Gio.SimpleAction.new('change_db_menu', None)
        change_db_menu_action.connect('activate', self.on_menu_change_db)
        self.add_action(change_db_menu_action)

        save_db_menu_action = Gio.SimpleAction.new('save_db_menu', None)
        save_db_menu_action.connect('activate', self.on_menu_save_db)
        self.add_action(save_db_menu_action)

        save_all_menu_action = Gio.SimpleAction.new('save_all_menu', None)
        save_all_menu_action.connect('activate', self.on_menu_save_all)
        self.add_action(save_all_menu_action)

        close_tray_menu_action = Gio.SimpleAction.new('close_tray_menu', None)
        close_tray_menu_action.connect('activate', self.on_menu_close_tray)
        self.add_action(close_tray_menu_action)

        quit_menu_action = Gio.SimpleAction.new('quit_menu', None)
        quit_menu_action.connect('activate', self.on_menu_quit)
        self.add_action(quit_menu_action)

        # 'Edit' column
        system_prefs_action = Gio.SimpleAction.new('system_prefs_menu', None)
        system_prefs_action.connect(
            'activate',
            self.on_menu_system_preferences,
        )
        self.add_action(system_prefs_action)

        gen_options_action = Gio.SimpleAction.new('gen_options_menu', None)
        gen_options_action.connect('activate', self.on_menu_general_options)
        self.add_action(gen_options_action)

        # 'Media' column
        add_video_menu_action = Gio.SimpleAction.new('add_video_menu', None)
        add_video_menu_action.connect('activate', self.on_menu_add_video)
        self.add_action(add_video_menu_action)

        add_channel_menu_action = Gio.SimpleAction.new(
            'add_channel_menu',
            None,
        )
        add_channel_menu_action.connect('activate', self.on_menu_add_channel)
        self.add_action(add_channel_menu_action)

        add_playlist_menu_action = Gio.SimpleAction.new(
            'add_playlist_menu',
            None,
        )
        add_playlist_menu_action.connect(
            'activate',
            self.on_menu_add_playlist,
        )
        self.add_action(add_playlist_menu_action)

        add_folder_menu_action = Gio.SimpleAction.new('add_folder_menu', None)
        add_folder_menu_action.connect('activate', self.on_menu_add_folder)
        self.add_action(add_folder_menu_action)

        export_db_menu_action = Gio.SimpleAction.new('export_db_menu', None)
        export_db_menu_action.connect('activate', self.on_menu_export_db)
        self.add_action(export_db_menu_action)

        import_json_menu_action = Gio.SimpleAction.new(
            'import_json_menu',
            None,
        )
        import_json_menu_action.connect('activate', self.on_menu_import_json)
        self.add_action(import_json_menu_action)

        import_text_menu_action = Gio.SimpleAction.new(
            'import_text_menu',
            None,
        )
        import_text_menu_action.connect(
            'activate',
            self.on_menu_import_plain_text,
        )
        self.add_action(import_text_menu_action)

        switch_view_menu_action = Gio.SimpleAction.new(
            'switch_view_menu',
            None,
        )
        switch_view_menu_action.connect('activate', self.on_button_switch_view)
        self.add_action(switch_view_menu_action)

        show_hidden_menu_action = Gio.SimpleAction.new(
            'show_hidden_menu',
            None,
        )
        show_hidden_menu_action.connect('activate', self.on_menu_show_hidden)
        self.add_action(show_hidden_menu_action)

        if self.debug_test_media_menu_flag:
            test_menu_action = Gio.SimpleAction.new('test_menu', None)
            test_menu_action.connect('activate', self.on_menu_test)
            self.add_action(test_menu_action)

        # 'Operations' column
        check_all_menu_action = Gio.SimpleAction.new('check_all_menu', None)
        check_all_menu_action.connect(
            'activate',
            self.on_menu_check_all,
        )
        self.add_action(check_all_menu_action)

        download_all_menu_action = Gio.SimpleAction.new(
            'download_all_menu',
            None,
        )
        download_all_menu_action.connect(
            'activate',
            self.on_menu_download_all,
        )
        self.add_action(download_all_menu_action)

        custom_dl_all_menu_action = Gio.SimpleAction.new(
            'custom_dl_all_menu',
            None,
        )
        custom_dl_all_menu_action.connect(
            'activate',
            self.on_menu_custom_dl_all,
        )
        self.add_action(custom_dl_all_menu_action)

        refresh_db_menu_action = Gio.SimpleAction.new('refresh_db_menu', None)
        refresh_db_menu_action.connect('activate', self.on_menu_refresh_db)
        self.add_action(refresh_db_menu_action)

        ytdl_menu_action = Gio.SimpleAction.new('update_ytdl_menu', None)
        ytdl_menu_action.connect('activate', self.on_menu_update_ytdl)
        self.add_action(ytdl_menu_action)

        ytdl_test_menu_action = Gio.SimpleAction.new('test_ytdl_menu', None)
        ytdl_test_menu_action.connect('activate', self.on_menu_test_ytdl)
        self.add_action(ytdl_test_menu_action)

        ffmpeg_menu_action = Gio.SimpleAction.new('install_ffmpeg_menu', None)
        ffmpeg_menu_action.connect('activate', self.on_menu_install_ffmpeg)
        self.add_action(ffmpeg_menu_action)

        tidy_up_menu_action = Gio.SimpleAction.new('tidy_up_menu', None)
        tidy_up_menu_action.connect('activate', self.on_menu_tidy_up)
        self.add_action(tidy_up_menu_action)

        stop_operation_menu_action = Gio.SimpleAction.new(
            'stop_operation_menu',
            None,
        )
        stop_operation_menu_action.connect(
            'activate',
            self.on_button_stop_operation,
        )
        self.add_action(stop_operation_menu_action)

        # 'Livestreams' column
        live_prefs_menu_action = Gio.SimpleAction.new(
            'live_prefs_menu',
            None,
        )
        live_prefs_menu_action.connect(
            'activate',
            self.on_menu_live_preferences,
        )
        self.add_action(live_prefs_menu_action)

        update_live_menu_action = Gio.SimpleAction.new(
            'update_live_menu',
            None,
        )
        update_live_menu_action.connect('activate', self.on_menu_update_live)
        self.add_action(update_live_menu_action)

        cancel_live_menu_action = Gio.SimpleAction.new(
            'cancel_live_menu',
            None,
        )
        cancel_live_menu_action.connect('activate', self.on_menu_cancel_live)
        self.add_action(cancel_live_menu_action)

        # 'Help' column
        about_menu_action = Gio.SimpleAction.new('about_menu', None)
        about_menu_action.connect('activate', self.on_menu_about)
        self.add_action(about_menu_action)

        go_website_menu_action = Gio.SimpleAction.new('go_website_menu', None)
        go_website_menu_action.connect('activate', self.on_menu_go_website)
        self.add_action(go_website_menu_action)

        send_feedback_menu_action = Gio.SimpleAction.new(
            'send_feedback_menu',
            None,
        )
        send_feedback_menu_action.connect(
            'activate',
            self.on_menu_send_feedback,
        )
        self.add_action(send_feedback_menu_action)

        # Main toolbar actions
        # --------------------

        add_video_toolbutton_action = Gio.SimpleAction.new(
            'add_video_toolbutton',
            None,
        )
        add_video_toolbutton_action.connect(
            'activate',
            self.on_menu_add_video,
        )
        self.add_action(add_video_toolbutton_action)

        add_channel_toolbutton_action = Gio.SimpleAction.new(
            'add_channel_toolbutton',
            None,
        )
        add_channel_toolbutton_action.connect(
            'activate',
            self.on_menu_add_channel,
        )
        self.add_action(add_channel_toolbutton_action)

        add_playlist_toolbutton_action = Gio.SimpleAction.new(
            'add_playlist_toolbutton',
            None,
        )
        add_playlist_toolbutton_action.connect(
            'activate',
            self.on_menu_add_playlist,
        )
        self.add_action(add_playlist_toolbutton_action)

        add_folder_toolbutton_action = Gio.SimpleAction.new(
            'add_folder_toolbutton',
            None,
        )
        add_folder_toolbutton_action.connect(
            'activate',
            self.on_menu_add_folder,
        )
        self.add_action(add_folder_toolbutton_action)

        check_all_toolbutton_action = Gio.SimpleAction.new(
            'check_all_toolbutton',
            None,
        )
        check_all_toolbutton_action.connect(
            'activate',
            self.on_menu_check_all,
        )
        self.add_action(check_all_toolbutton_action)

        download_all_toolbutton_action = Gio.SimpleAction.new(
            'download_all_toolbutton',
            None,
        )
        download_all_toolbutton_action.connect(
            'activate',
            self.on_menu_download_all,
        )
        self.add_action(download_all_toolbutton_action)

        stop_operation_button_action = Gio.SimpleAction.new(
            'stop_operation_toolbutton',
            None,
        )
        stop_operation_button_action.connect(
            'activate',
            self.on_button_stop_operation,
        )
        self.add_action(stop_operation_button_action)

        switch_view_button_action = Gio.SimpleAction.new(
            'switch_view_toolbutton',
            None,
        )
        switch_view_button_action.connect(
            'activate',
            self.on_button_switch_view,
        )
        self.add_action(switch_view_button_action)

        if self.debug_test_media_toolbar_flag:
            test_button_action = Gio.SimpleAction.new('test_toolbutton', None)
            test_button_action.connect('activate', self.on_menu_test)
            self.add_action(test_button_action)

        quit_button_action = Gio.SimpleAction.new('quit_toolbutton', None)
        quit_button_action.connect('activate', self.on_menu_quit)
        self.add_action(quit_button_action)

        # Video catalogue toolbar actions
        # -------------------------------

        first_page_toolbutton_action = Gio.SimpleAction.new(
            'first_page_toolbutton',
            None,
        )
        first_page_toolbutton_action.connect(
            'activate',
            self.on_button_first_page,
        )
        self.add_action(first_page_toolbutton_action)

        previous_page_toolbutton_action = Gio.SimpleAction.new(
            'previous_page_toolbutton',
            None,
        )
        previous_page_toolbutton_action.connect(
            'activate',
            self.on_button_previous_page,
        )
        self.add_action(previous_page_toolbutton_action)

        next_page_toolbutton_action = Gio.SimpleAction.new(
            'next_page_toolbutton',
            None,
        )
        next_page_toolbutton_action.connect(
            'activate',
            self.on_button_next_page,
        )
        self.add_action(next_page_toolbutton_action)

        last_page_toolbutton_action = Gio.SimpleAction.new(
            'last_page_toolbutton',
            None,
        )
        last_page_toolbutton_action.connect(
            'activate',
            self.on_button_last_page,
        )
        self.add_action(last_page_toolbutton_action)

        scroll_up_toolbutton_action = Gio.SimpleAction.new(
            'scroll_up_toolbutton',
            None,
        )
        scroll_up_toolbutton_action.connect(
            'activate',
            self.on_button_scroll_up,
        )
        self.add_action(scroll_up_toolbutton_action)

        scroll_down_toolbutton_action = Gio.SimpleAction.new(
            'scroll_down_toolbutton',
            None,
        )
        scroll_down_toolbutton_action.connect(
            'activate',
            self.on_button_scroll_down,
        )
        self.add_action(scroll_down_toolbutton_action)

        show_filter_toolbutton_action = Gio.SimpleAction.new(
            'show_filter_toolbutton',
            None,
        )
        show_filter_toolbutton_action.connect(
            'activate',
            self.on_button_show_filter,
        )
        self.add_action(show_filter_toolbutton_action)

        # (Second row)

        sort_type_toolbutton_action = Gio.SimpleAction.new(
            'sort_type_toolbutton',
            None,
        )
        sort_type_toolbutton_action.connect(
            'activate',
            self.on_button_sort_type,
        )
        self.add_action(sort_type_toolbutton_action)

        use_regex_togglebutton_action = Gio.SimpleAction.new(
            'use_regex_togglebutton',
            None,
        )
        use_regex_togglebutton_action.connect(
            'activate',
            self.on_button_use_regex,
        )
        self.add_action(use_regex_togglebutton_action)

        apply_filter_button_action = Gio.SimpleAction.new(
            'apply_filter_toolbutton',
            None,
        )
        apply_filter_button_action.connect(
            'activate',
            self.on_button_apply_filter,
        )
        self.add_action(apply_filter_button_action)

        cancel_filter_button_action = Gio.SimpleAction.new(
            'cancel_filter_toolbutton',
            None,
        )
        cancel_filter_button_action.connect(
            'activate',
            self.on_button_cancel_filter,
        )
        self.add_action(cancel_filter_button_action)

        find_date_toolbutton_action = Gio.SimpleAction.new(
            'find_date_toolbutton',
            None,
        )
        find_date_toolbutton_action.connect(
            'activate',
            self.on_button_find_date,
        )
        self.add_action(find_date_toolbutton_action)

        # Videos Tab actions
        # ------------------

        # Buttons

        check_all_button_action = Gio.SimpleAction.new(
            'check_all_button',
            None,
        )
        check_all_button_action.connect('activate', self.on_menu_check_all)
        self.add_action(check_all_button_action)

        download_all_button_action = Gio.SimpleAction.new(
            'download_all_button',
            None,
        )
        download_all_button_action.connect(
            'activate',
            self.on_menu_download_all,
        )
        self.add_action(download_all_button_action)

        # Classic Mode Tab actions
        # ------------------------

        # Buttons

        classic_menu_button_action = Gio.SimpleAction.new(
            'classic_menu_button',
            None,
        )
        classic_menu_button_action.connect(
            'activate',
            self.on_button_classic_menu,
        )
        self.add_action(classic_menu_button_action)

        classic_dest_dir_button_action = Gio.SimpleAction.new(
            'classic_dest_dir_button',
            None,
        )
        classic_dest_dir_button_action.connect(
            'activate',
            self.on_button_classic_dest_dir,
        )
        self.add_action(classic_dest_dir_button_action)

        classic_dest_dir_open_action = Gio.SimpleAction.new(
            'classic_dest_dir_open_button',
            None,
        )
        classic_dest_dir_open_action.connect(
            'activate',
            self.on_button_classic_dest_dir_open,
        )
        self.add_action(classic_dest_dir_open_action)

        classic_add_urls_button_action = Gio.SimpleAction.new(
            'classic_add_urls_button',
            None,
        )
        classic_add_urls_button_action.connect(
            'activate',
            self.on_button_classic_add_urls,
        )
        self.add_action(classic_add_urls_button_action)

        classic_remove_button_action = Gio.SimpleAction.new(
            'classic_remove_button',
            None,
        )
        classic_remove_button_action.connect(
            'activate',
            self.on_button_classic_remove,
        )
        self.add_action(classic_remove_button_action)

        classic_play_button_action = Gio.SimpleAction.new(
            'classic_play_button',
            None,
        )
        classic_play_button_action.connect(
            'activate',
            self.on_button_classic_play,
        )
        self.add_action(classic_play_button_action)

        classic_move_up_button_action = Gio.SimpleAction.new(
            'classic_move_up_button',
            None,
        )
        classic_move_up_button_action.connect(
            'activate',
            self.on_button_classic_move_up,
        )
        self.add_action(classic_move_up_button_action)

        classic_move_down_button_action = Gio.SimpleAction.new(
            'classic_move_down_button',
            None,
        )
        classic_move_down_button_action.connect(
            'activate',
            self.on_button_classic_move_down,
        )
        self.add_action(classic_move_down_button_action)

        classic_redownload_button_action = Gio.SimpleAction.new(
            'classic_redownload_button',
            None,
        )
        classic_redownload_button_action.connect(
            'activate',
            self.on_button_classic_redownload,
        )
        self.add_action(classic_redownload_button_action)

        classic_stop_button_action = Gio.SimpleAction.new(
            'classic_stop_button',
            None,
        )
        classic_stop_button_action.connect(
            'activate',
            self.on_button_classic_stop,
        )
        self.add_action(classic_stop_button_action)

        classic_download_button_action = Gio.SimpleAction.new(
            'classic_download_button',
            None,
        )
        classic_download_button_action.connect(
            'activate',
            self.on_button_classic_download,
        )
        self.add_action(classic_download_button_action)


    def do_activate(self):

        """Gio.Application standard function."""

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 1986 do_activate')

        # If the flag is set, restrict Tartube to a single instance
        if not __main__.__multiple_instance_flag__ and self.main_win_obj:

            self.main_win_obj.present()

        # Otherwise permit multiple instances
        else:

            self.start()

            # Open the system preferences window, if the debugging flag is set
            if self.debug_open_pref_win_flag:
                config.SystemPrefWin(self)

            # Open the general download options window, if the debugging flag
            #   is set
            if self.debug_open_options_win_flag:
                config.OptionsEditWin(self, self.general_options_obj, None)


    def do_shutdown(self):

        """Gio.Application standard function.

        Clean shutdowns (for example, from the main window's toolbar) are
        handled by self.stop().

        N.B. When called by mainwin.MainWin.on_delete_event(), the config/
        database files have already been saved.
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 2009 do_shutdown')

        # Stop the GObject timers immediately
        if self.script_slow_timer_id:
            GObject.source_remove(self.script_slow_timer_id)
        if self.script_fast_timer_id:
            GObject.source_remove(self.script_fast_timer_id)
        if self.dl_timer_id:
            GObject.source_remove(self.dl_timer_id)
        if self.update_timer_id:
            GObject.source_remove(self.update_timer_id)
        if self.refresh_timer_id:
            GObject.source_remove(self.refresh_timer_id)
        if self.info_timer_id:
            GObject.source_remove(self.info_timer_id)
        if self.tidy_timer_id:
            GObject.source_remove(self.tidy_timer_id)

        # Don't prompt the user before halting a download/update/refresh/info/
        #   tidy operation, as we would do in calls to self.stop()
        if self.download_manager_obj:
            self.download_manager_obj.stop_download_operation()
        elif self.update_manager_obj:
            self.update_manager_obj.stop_update_operation()
        elif self.refresh_manager_obj:
            self.refresh_manager_obj.stop_refresh_operation()
        elif self.info_manager_obj:
            self.info_manager_obj.stop_info_operation()
        elif self.tidy_manager_obj:
            self.tidy_manager_obj.stop_tidy_operation()

        # If there is a lock on the database file, release it
        self.remove_db_lock_file()

        # Destroy the fake main window used temporarily by self.start(), if it
        #   exists
        if self.fake_main_win_obj:
            self.fake_main_win_obj.destroy()

        # Stop immediately
        Gtk.Application.do_shutdown(self)
        if os.name == 'nt':
            # Under MS Windows, all methods of shutting down after an update
            #   operation fail - except this method
            os._exit(0)

        # Still here? Do a brute-force exit
        exit()


    # Public class methods


    def start(self):

        """Called by self.do_activate().

        Performs general initialisation.
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 2070 start')

        # Part 1 - Give mainapp.TartubeApp IVs their initial values
        # ---------------------------------------------------------

        # Set youtube-dl path IVs
        if os.name == 'nt':

            if 'PROGRAMFILES(X86)' in os.environ:
                # 64-bit MS Windows
                recommended = 'ytdl_update_win_64'
                python_path = '..\\..\\..\\mingw64\\bin\python3.exe'
                pip_path = '..\\..\\..\\mingw64\\bin\pip3-script.py'
            else:
                # 32-bit MS Windows
                recommended = 'ytdl_update_win_32'
                python_path = '..\\..\\..\\mingw32\\bin\python3.exe'
                pip_path = '..\\..\\..\\mingw32\\bin\pip3-script.py'

            self.ytdl_bin = 'youtube-dl'
            self.ytdl_path_default = 'youtube-dl'
            self.ytdl_path = 'youtube-dl'
            self.ytdl_update_dict = {
                recommended: [
                    python_path,
                    pip_path,
                    'install',
                    '--upgrade',
                    'youtube-dl',
                ],
                'ytdl_update_pip3': [
                    'pip3', 'install', '--upgrade', 'youtube-dl',
                ],
                'ytdl_update_pip': [
                    'pip', 'install', '--upgrade', 'youtube-dl',
                ],
                'ytdl_update_default_path': [
                    self.ytdl_path_default, '-U',
                ],
                'ytdl_update_local_path': [
                    'youtube-dl', '-U',
                ],
            }
            self.ytdl_update_list = [
                recommended,
                'ytdl_update_pip3',
                'ytdl_update_pip',
                'ytdl_update_default_path',
                'ytdl_update_local_path',
            ]
            self.ytdl_update_current = recommended

        elif __main__.__pkg_strict_install_flag__:

            self.ytdl_bin = 'youtube-dl'
            self.ytdl_path_default = os.path.abspath(
                os.path.join(os.sep, 'usr', 'bin', self.ytdl_bin),
            )
            self.ytdl_path = self.ytdl_path_pypi

            self.ytdl_update_dict = {
                'ytdl_update_disabled': [],
            }
            self.ytdl_update_list = [
                'ytdl_update_disabled',
            ]
            self.ytdl_update_current = 'ytdl_update_disabled'

        else:

            self.ytdl_bin = 'youtube-dl'
            self.ytdl_path_default = os.path.abspath(
                os.path.join(os.sep, 'usr', 'bin', self.ytdl_bin),
            )

            if __main__.__pkg_install_flag__:
                self.ytdl_path = self.ytdl_path_pypi
            else:
                self.ytdl_path = 'youtube-dl'

            self.ytdl_update_dict = {
                'ytdl_update_pip3_recommend': [
                    'pip3', 'install', '--upgrade', '--user', 'youtube-dl',
                ],
                'ytdl_update_pip3_omit_user': [
                    'pip3', 'install', '--upgrade', 'youtube-dl',
                ],
                'ytdl_update_pip': [
                    'pip', 'install', '--upgrade', '--user', 'youtube-dl',
                ],
                'ytdl_update_pip_omit_user': [
                    'pip', 'install', '--upgrade', 'youtube-dl',
                ],
                'ytdl_update_default_path': [
                    self.ytdl_path_default, '-U',
                ],
                'ytdl_update_local_path': [
                    'youtube-dl', '-U',
                ],
                'ytdl_update_pypi_path': [
                    self.ytdl_path_pypi, '-U',
                ],
            }
            self.ytdl_update_list = [
                'ytdl_update_pip3_recommend',
                'ytdl_update_pip3_omit_user',
                'ytdl_update_pip',
                'ytdl_update_pip_omit_user',
                'ytdl_update_default_path',
                'ytdl_update_local_path',
                'ytdl_update_pypi_path',
            ]
            self.ytdl_update_current = 'ytdl_update_pip3_recommend'

        # Set the General Options Manager
        self.general_options_obj = options.OptionsManager()
        # Apply download options to the Classic Mode Tab, by default
        self.apply_classic_downoad_options()

        # Compile a list of available sound effects
        self.find_sound_effects()

        # Part 2 - Load the config file
        # -----------------------------

        # Make sure the directory containing the config file exists
        # v2.0.003 (amended v2.1.034) The user can force Tartube to use the
        #   config file in the script's directory (rather than the one in the
        #   location described by xdg) by placing a 'settings.json' file there.
        #   If that file is created when Tartube is already running, it can be
        #   an empty file (because Tartube overwrites it). Otherwise, it should
        #   be a copy of a legitimate config file
        if not os.path.isfile(self.config_file_path):

            config_dir = None
            if (
                self.config_file_xdg_dir is not None
                and not os.path.isdir(self.config_file_xdg_dir)
            ):
                config_dir = self.config_file_xdg_dir

            elif (
                self.config_file_xdg_dir is None
                and not os.path.isdir(self.config_file_dir)
            ):
                config_dir = self.config_file_dir

            if config_dir is not None and not self.make_directory(config_dir):

                # Can't use an ordinary message dialogue without a parent
                #   window, and most users won't see a message in the terminal,
                #   so use a special window for this purpose
                mainwin.StartErrorWin(
                    self,
                    _(
                    'Tartube can\'t create the folder in which its' \
                    + ' configuration file is saved',
                    ),
                )

                return

        # If the config file exists, load it. If not, create it
        new_config_flag = False
        if (
            self.config_file_xdg_path is not None \
            and os.path.isfile(self.config_file_xdg_path)
        ) or os.path.isfile(self.config_file_path):
            new_config_flag = self.load_config()

        elif self.debug_no_dialogue_flag:
            self.save_config()
            new_config_flag = True

        elif not self.disable_load_save_flag:

            # New Tartube installation
            new_config_flag = True
            # Prompt the user to set the location of the data directory
            self.prompt_on_new_install()

        # If file load/save has been disabled, shut down after the special
        #   window is shown
        if self.disable_load_save_flag:

            mainwin.StartErrorWin(self, self.disable_load_save_msg)

            return

        # Part 3 - Set up the main window
        # -------------------------------

        # Create the main window
        self.main_win_obj = mainwin.MainWin(self)

        # Set up widgets in the Video Catalogue toolbar
        self.main_win_obj.update_show_filter_widgets()
        self.main_win_obj.update_alpha_sort_widgets()
        # Add the right number of pages to the Output Tab
        self.main_win_obj.output_tab_setup_pages()
        # If the flag it set, switch to the Classic Mode Tab
        if self.show_classic_tab_on_startup_flag:
            self.main_win_obj.notebook.set_current_page(2)

        # Most main widgets are desensitised, until the database file has been
        #   loaded
        self.main_win_obj.sensitise_widgets_if_database(False)
        # Disable tooltips, if necessary
        if not self.show_tooltips_flag:
            self.main_win_obj.disable_tooltips()
        # Disable the 'Download all' button and related widgets, if necessary
        if self.disable_dl_all_flag:
            self.main_win_obj.disable_dl_all_buttons()

        # Resize the main window to match the previous size, if required (but
        #   don't bother if the previous size is the same as the standard one)
        if self.main_win_save_size_flag \
        and (
            self.main_win_save_width != self.main_win_width
            or self.main_win_save_height != self.main_win_height
            or self.main_win_save_posn != self.paned_min_size
        ):
            self.main_win_obj.resize(
                self.main_win_save_width,
                self.main_win_save_height,
            )

            self.main_win_obj.videos_paned.set_position(
                self.main_win_save_posn,
            )

        # If the debugging flag is set, move the window to the top-left corner
        #   of the desktop
        if self.debug_open_top_left_flag:
            self.main_win_obj.move(0, 0)

        # Make the main window visible
        self.main_win_obj.show_all()

        # Prepare to add an icon to the system tray, making it visible only if
        #   required
        self.status_icon_obj = mainwin.StatusIcon(self)
        if self.show_status_icon_flag:
            self.status_icon_obj.show_icon()

        # Start the dialogue manager (thread-safe code for Gtk message dialogue
        #   windows)
        self.dialogue_manager_obj = dialogue.DialogueManager(
            self,
            self.main_win_obj,
        )

        # Part 4 - Load a database file
        # -----------------------------

        # Multiple instances of Tartube can share the same config file, but not
        #   the same database file
        # If the database file specified by the config file we've just loaded
        #   is locked (meaning it's in use by another instance), we might be
        #   able to use an alternative data directory
        if self.data_dir_use_list_flag and not new_config_flag:
            self.choose_alt_db()

        # Check that the data directory specified by self.data_dir actually
        #   exists. If not, the most common reason is that the user has
        #   forgotten to mount an external drive
        if not new_config_flag \
        and not self.debug_no_dialogue_flag \
        and not os.path.exists(self.data_dir):

            # Ask the user what to do next. The False argument tells the
            #   dialogue window that it's a missing directory
            dialogue_win = mainwin.MountDriveDialogue(
                self.main_win_obj,
                False,
            )
            dialogue_win.run()

            # If the data directory now exists, or can be created in principle
            #   by the code just below (because the user wants to use the
            #   default location), then available_flag will be True
            available_flag = dialogue_win.available_flag
            dialogue_win.destroy()

            if not available_flag:

                # The user opted to shut down Tartube. Destroying the main
                #   window calls self.do_shutdown()
                return self.main_win_obj.destroy()

        # Create Tartube's data directories (if they don't already exist)
        if not os.path.isdir(self.data_dir):

            # React to a 'Permission denied' error by asking the user what to
            #   do next. If necessary, shut down Tartube
            if not self.make_directory(self.data_dir):
                return self.main_win_obj.destroy()

        # Create the directory for database file backups
        if not os.path.isdir(self.backup_dir):
            if not self.make_directory(self.backup_dir):
                return self.main_win_obj.destroy()

        # Create the temporary data directories (or empty them, if they already
        #   exist)
        if os.path.isdir(self.temp_dir):
            try:
                shutil.rmtree(self.temp_dir)

            except:
                if not self.make_directory(self.temp_dir):
                    return self.main_win_obj.destroy()
                else:
                    shutil.rmtree(self.temp_dir)

        if not os.path.isdir(self.temp_dir):
            if not self.make_directory(self.temp_dir):
                return self.main_win_obj.destroy()

        if not os.path.isdir(self.temp_dl_dir):
            if not self.make_directory(self.temp_dl_dir):
                return self.main_win_obj.destroy()

        # If the database file exists, load it. If not, create it
        db_path = os.path.abspath(
            os.path.join(self.data_dir, self.db_file_name),
        )

        if os.path.isfile(db_path):

            self.load_db()

        else:

            # New database. First create fixed media data objects (media.Folder
            #   objects) that can't be removed by the user (though they can be
            #   hidden)
            self.create_fixed_folders()

            # Populate the Video Index
            self.main_win_obj.video_index_populate()

            # Create the database file
            self.allow_db_save_flag = True
            self.save_db()

        # Part 5 - Warn user about broken Gtk
        # -----------------------------------

        # Display a warning about Gtk stability issues, if required
        if self.gtk_emulate_broken_flag:
            self.system_warning(
                102,
                _(
                'Tartube is assuming that Gtk v{0}.{1}.{2} is broken;' \
                + ' some minor cosmetic features are disabled',
                ).format(
                    str(self.gtk_version_major),
                    str(self.gtk_version_minor),
                    str(self.gtk_version_micro),
                ),
            )

        # Part 6 - Warn user about failed loads
        # -------------------------------------

        # If file load/save has been disabled, we can now show a dialogue
        #   window
        if self.disable_load_save_flag:

            remove_flag = False

            # (If self.show_classic_tab_on_startup_flag, then the Classic Mode
            #   Tab is visible. This looks weird, so quickly switch back to
            #   the Videos Tab)
            self.main_win_obj.notebook.set_current_page(0)

            if self.disable_load_save_lock_flag:

                dialogue_win = mainwin.RemoveLockFileDialogue(
                    self.main_win_obj,
                )

                dialogue_win.run()
                remove_flag = dialogue_win.remove_flag
                dialogue_win.destroy()

                if remove_flag:
                    self.remove_stale_lock_file()
                    # (Don't need to display the error messages just below)
                    self.disable_load_save_lock_flag = False

                    self.file_error_dialogue(
                        _(
                        'The Tartube database file was not loaded, but is no'\
                        + ' longer protected',
                        ) + '\n\n' \
                        + _('Restart Tartube to load it'),
                    )

            if not remove_flag:

                if self.disable_load_save_msg is None:

                    self.file_error_dialogue(
                        _(
                        'Because of an error, file load/save has been' \
                        + ' disabled',
                        ),
                    )

                else:

                    self.file_error_dialogue(
                        self.disable_load_save_msg + '\n\n' \
                        + _(
                        'Because of the error, file load/save has been' \
                        + ' disabled',
                        )
                    )

        # Part 7 - Start system timers
        # ----------------------------

        # Start the script's GObject slow timer
        self.script_slow_timer_id = GObject.timeout_add(
            self.script_slow_timer_time,
            self.script_slow_timer_callback,
        )

        # Start the script's GObject fast timer
        self.script_fast_timer_id = GObject.timeout_add(
            self.script_fast_timer_time,
            self.script_fast_timer_callback,
        )

        # Part 8 - Automatically start update/download operations, if required
        # --------------------------------------------------------------------

        if not self.disable_load_save_flag:

            # For new installations, MS Windows must be prompted to perform an
            #   update operation, which installs youtube-dl on their system
            if new_config_flag and os.name == 'nt':

                self.dialogue_manager_obj.show_msg_dialogue(
                    _(
                    'youtube-dl must be installed before you can use' \
                    + ' Tartube. Do you want to install youtube-dl now?',
                    ),
                    'question',
                    'yes-no',
                    None,                   # Parent window is main window
                    {
                        'yes': 'update_manager_start',
                        # Install youtube-dl, not FFmpeg
                        'data': 'ytdl',
                    },
                )

            # If a download operation (real or simulated) is scheduled to occur
            #   on startup, then set the time at which
            #   self.script_fast_timer_callback() should initiate it
            elif self.scheduled_dl_mode == 'start':

                self.scheduled_dl_start_check_time \
                = time.time() + self.scheduled_dl_start_wait_time

            elif self.scheduled_check_mode == 'start':

                self.scheduled_check_start_check_time \
                = time.time() + self.scheduled_check_start_wait_time


    def stop(self):

        """Called by self.on_menu_quit() and
        mainwin.MainWin.on_quit_menu_item().

        Before terminating the Tartube app, gets confirmation from the user (if
        a download/update/refresh/info/tidy operation is in progress).

        If no operation is in progress, calls self.stop_continue() to terminate
        the app now. Otherwise, self.stop_continue() is only called when the
        clicks the dialogue window's 'Yes' button.
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 2604 stop')

        # If a (silent) livestream operation is in progress, we can stop it
        #   immediately
        if self.livestream_manager_obj:

            self.livestream_manager_obj.stop_livestream_operation()
            self.stop_continue()

        # If a download/update/refresh/info/tidy operation is in progress, get
        #   confirmation before stopping
        elif self.current_manager_obj:

            if self.download_manager_obj:
                string = _('There is a download operation in progress.')
            elif self.update_manager_obj:
                string = _('There is an update operation in progress.')
            elif self.refresh_manager_obj:
                string = _('There is a refresh operation in progress.')
            elif self.info_manager_obj:
                string = _('There is an info operation in progress.')
            else:
                string = _('There is a tidy operation in progress.')

            # If the user clicks 'yes', call self.stop_continue() to complete
            #   the shutdown
            self.dialogue_manager_obj.show_msg_dialogue(
                string + ' ' + _('Are you sure you want to quit Tartube?'),
                'question',
                'yes-no',
                None,                   # Parent window is main window
                {
                    'yes': 'stop_continue',
                }
            )

        # No confirmation required, so call self.stop_continue() now
        else:
            self.stop_continue()


    def stop_continue(self):

        """Called by self.stop() or self.download_manager_finished().

        Terminates the Tartube app. Forced shutdowns (for example, by clicking
        the X in the top corner of the window) are handled by
        self.do_shutdown().
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 2655 stop_continue')

        # (No need to check the livestream operation here - it was stopped in
        #   the call to self.stop() )
        if self.download_manager_obj:
            self.download_manager_obj.stop_download_operation()

        elif self.update_manager_obj:
            self.update_manager_obj.stop_update_operation()

        elif self.refresh_manager_obj:
            self.refresh_manager_obj.stop_refresh_operation()

        elif self.info_manager_obj:
            self.info_manager_obj.stop_info_operation()

        elif self.tidy_manager_obj:
            self.tidy_manager_obj.stop_tidy_operation()

        # Stop the GObject timers immediately. So this action is not repeated
        #   in the standard call to self.do_shutdown, reset the IVs
        if self.script_slow_timer_id:
            GObject.source_remove(self.script_slow_timer_id)
            self.script_slow_timer_id = None

        if self.script_fast_timer_id:
            GObject.source_remove(self.script_fast_timer_id)
            self.script_fast_timer_id = None

        if self.dl_timer_id:
            GObject.source_remove(self.dl_timer_id)
            self.dl_timer_id = None

        if self.update_timer_id:
            GObject.source_remove(self.update_timer_id)
            self.update_timer_id = None

        if self.refresh_timer_id:
            GObject.source_remove(self.refresh_timer_id)
            self.refresh_timer_id = None

        if self.info_timer_id:
            GObject.source_remove(self.info_timer_id)
            self.info_timer_id = None

        if self.tidy_timer_id:
            GObject.source_remove(self.tidy_timer_id)
            self.tidy_timer_id = None

        # Empty any temporary folders from the database (if allowed; those
        #   temporary folders are always deleted when Tartube starts)
        # Otherwise, open the temporary folders on the desktop, if allowd
        if self.delete_on_shutdown_flag:
            self.delete_temp_folders()
        elif self.open_temp_on_desktop_flag:
            self.open_temp_folders()

        # Delete Tartube's temporary folder from the filesystem
        if os.path.isdir(self.temp_dir):
            shutil.rmtree(self.temp_dir)

        # Save the config and database files for the final time, and release
        #   the database lockfile
        self.save_config()
        self.save_db()
        self.remove_db_lock_file()

        # I'm outta here!
        self.quit()


    def system_error(self, error_code, msg):

        """Can be called by anything.

        Wrapper function for mainwin.MainWin.errors_list_add_system_error().

        Args:

            error_code (int): An error code in the range 100-999

            msg (str): A system error message to display in the main window's
                Errors List.

        Notes:

            Error codes for this function and for self.system_warning are
            currently assigned thus:

            100-199: mainapp.py     (in use: 101-163)
            200-299: mainwin.py     (in use: 201-256)
            300-399: downloads.py   (in use: 301-306)
            400-499: config.py      (in use: 401-404)

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 2752 system_error')

        if self.main_win_obj and self.system_error_show_flag:
            self.main_win_obj.errors_list_add_system_error(error_code, msg)
        else:
            # Emergency fallback: display in the terminal window
            print('SYSTEM ERROR ' + str(error_code) + ': ' + msg)


    def system_warning(self, error_code, msg):

        """Can be called by anything.

        Wrapper function for mainwin.MainWin.errors_list_add_system_warning().

        Args:

            error_code (int): An error code in the range 100-999. This function
                and self.system_error() share the same error codes

            msg (str): A system error message to display in the main window's
                Errors List.

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 2778 system_warning')

        if self.main_win_obj and self.system_warning_show_flag:
            self.main_win_obj.errors_list_add_system_warning(error_code, msg)
        else:
            # Emergency fallback: display in the terminal window
            print('SYSTEM WARNING ' + str(error_code) + ': ' + msg)


    # (Config/database files load/save)


    def load_config(self):

        """Called by self.start() (only).

        Loads the Tartube config file. If loading fails, disables all file
        loading/saving.

        Return values:

            True if this appears to be a new Tartube installation, False
                otherwise (regardless of whether loading the config file
                succeeds, or not)

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 2799 load_config')

        # Define global variables for this function
        global _

        # The config file can be stored at one of two locations, depending on
        #   whether xdg is available, or not
        # v2.0.003 (amended v2.1.034) The user can force Tartube to use the
        #   config file in the script's directory (rather than the one in the
        #   location described by xdg) by placing a 'settings.json' file there.
        #   If that file is created when Tartube is already running, it can be
        #   an empty file (because Tartube overwrites it). Otherwise, it should
        #   be a copy of a legitimate config file
        if self.config_file_xdg_path is None \
        or (
            os.path.isfile(self.config_file_path) \
            and not __main__.__pkg_strict_install_flag__
        ):
            config_file_path = self.config_file_path
        else:
            config_file_path = self.config_file_xdg_path

        # Sanity check
        if self.current_manager_obj \
        or not os.path.isfile(config_file_path) \
        or self.disable_load_save_flag:

            self.disable_load_save(
                _(
                'Failed to load the Tartube config file (failed sanity check)',
                ),
            )

            # Return False to mark this as not a new installation
            return False

        # In case a competing instance of Tartube is saving the same config
        #   file, check for the lockfile and, if it exists, wait a reasonable
        #   time for it to be released
        if not self.debug_ignore_lockfile_flag:

            lock_path = config_file_path + '.lock'
            if os.path.isfile(lock_path):

                check_time = time.time() + self.config_lock_time
                while time.time < check_time and os.path.isfile(lock_path):
                    time.sleep(0.1)

                if os.path.isfile(lock_path):

                    self.disable_load_save(
                        _(
                        'Failed to load the Tartube config file (file is' \
                        + ' locked)',
                        ),
                    )

                    # Return False to mark this as not a new installation
                    return False

        # Try to load the config file
        try:
            with open(config_file_path) as infile:
                json_dict = json.load(infile)

        except:

            # If we're loading a config file from the script's own directory,
            #   then treat it as if it were a blank file, waiting to be
            #   overwritten by the next call to self.save_config (as described
            #   above)
            if config_file_path == self.config_file_path:

                # A blank file probably means it's a new Tartube installation.
                #    Prompt the user to set the location of the data directory
                self.prompt_on_new_install()
                # Return True to mark this as a new installation
                return True

            else:

                self.disable_load_save(
                    _(
                    'Failed to load the Tartube config file (JSON load' \
                    + ' failure)',
                    ),
                )

                # Return False to mark this as not a new installation
                return False

        # Do some basic checks on the loaded data
        if not json_dict \
        or not 'script_name' in json_dict \
        or not 'script_version' in json_dict \
        or not 'save_date' in json_dict \
        or not 'save_time' in json_dict \
        or json_dict['script_name'] != __main__.__packagename__:

            self.disable_load_save(
                _(
                'Failed to load the Tartube config file (file is invalid)',
                ),
            )

            # Return False to mark this as not a new installation
            return False

        # Convert a version, e.g. 1.234.567, into a simple number, e.g.
        #   1234567, that can be compared with other versions
        version = self.convert_version(json_dict['script_version'])
        # Now check that the config file wasn't written by a more recent
        #   version of Tartube (which this older version might not be able to
        #   read)
        if version is None \
        or version > self.convert_version(__main__.__version__):

            self.disable_load_save(
                _(
                'Failed to load the Tartube config file (file cannot be read' \
                + ' by this version)',
                ),
            )

            # Return False to mark this as not a new installation
            return False

        # Since v1.0.008, config files have identified their file type
        if version >= 1000008 \
        and (
            not 'file_type' in json_dict or json_dict['file_type'] != 'config'
        ):
            self.disable_load_save(
                _(
                'Failed to load the Tartube config file (missing file type)',
                ),
            )

            # Return False to mark this as not a new installation
            return False

        # Set the locale
        if version >= 2000081:  # v2.0.081
            self.custom_locale = json_dict['custom_locale']

        if self.custom_locale != formats.LOCALE_DEFAULT:

            if not self.custom_locale in formats.LOCALE_LIST:
                # Invalid; use the default value
                self.custom_locale = formats.LOCALE_DEFAULT

            else:

                LOCALE = gettext.translation(
                    'base',
                    localedir='locale',
                    languages=[self.custom_locale],
                )
                LOCALE.install()

                # (Apply to this file)
                _ = LOCALE.gettext
                # (Apply to other files)
                mainwin._ = _
                config._ = _
                downloads._ = _
                formats._ = _
                info._ = _
                media._ = _
                refresh._ = _
                tidy._ = _
                updates._ = _
                # (Update download operation stages, e.g.
                #   formats.MAIN_STAGE_QUEUED
                formats.do_translate(True)

        # Set IVs to their new values
        if version >= 1004040:  # v1.4.040
            self.main_win_save_size_flag = json_dict['main_win_save_size_flag']
            self.main_win_save_width = json_dict['main_win_save_width']
            self.main_win_save_height = json_dict['main_win_save_height']
            self.main_win_save_posn = json_dict['main_win_save_posn']

        if version >= 1003122:  # v1.3.122
            self.gtk_emulate_broken_flag = json_dict['gtk_emulate_broken_flag']

        if version >= 2001024:  # v2.1.024
            self.toolbar_hide_flag = json_dict['toolbar_hide_flag']
        if version >= 5024:     # v0.5.024
            self.toolbar_squeeze_flag = json_dict['toolbar_squeeze_flag']
        if version >= 1001064:  # v1.1.064
            self.show_tooltips_flag = json_dict['show_tooltips_flag']
        if version >= 2001036:  # v2.1.036
            self.show_custom_icons_flag \
            = json_dict['show_custom_icons_flag']
        if version >= 2001036:  # v2.1.036
            self.show_small_icons_in_index_flag \
            = json_dict['show_small_icons_in_index_flag']
        elif version >= 1001075:  # v1.1.075
            self.show_small_icons_in_index_flag \
            = json_dict['show_small_icons_in_index']
        if version >= 1001077:  # v1.1.077
            self.auto_expand_video_index_flag \
            = json_dict['auto_expand_video_index_flag']
        if version >= 2000014:  # v2.0.014
            self.full_expand_video_index_flag \
            = json_dict['full_expand_video_index_flag']
        if version >= 1001064:  # v1.1.064
            self.disable_dl_all_flag = json_dict['disable_dl_all_flag']
        if version >= 1004011:  # v1.4.011
            self.show_pretty_dates_flag = json_dict['show_pretty_dates_flag']

        if version >= 1003024:  # v1.3.024
            self.show_status_icon_flag = json_dict['show_status_icon_flag']
            self.close_to_tray_flag = json_dict['close_to_tray_flag']

        if version >= 1003129:  # v1.3.129
            self.progress_list_hide_flag = json_dict['progress_list_hide_flag']
        if version >= 1000029:  # v1.0.029
            self.results_list_reverse_flag \
            = json_dict['results_list_reverse_flag']

        if version >= 1003069:  # v1.3.069
            self.system_error_show_flag = json_dict['system_error_show_flag']
        if version >= 6006:     # v0.6.006
            self.system_warning_show_flag \
            = json_dict['system_warning_show_flag']
        if version >= 1003079:  # v1.3.079
            self.operation_error_show_flag \
            = json_dict['operation_error_show_flag']
            self.operation_warning_show_flag \
            = json_dict['operation_warning_show_flag']

        if version >= 1000007:  # v1.0.007
            self.system_msg_keep_totals_flag \
            = json_dict['system_msg_keep_totals_flag']

        self.data_dir = json_dict['data_dir']

        if version >= 1004069:  # v1.4.069:
            self.data_dir_alt_list = json_dict['data_dir_alt_list']
            self.data_dir_use_first_flag = json_dict['data_dir_use_first_flag']
            self.data_dir_use_list_flag = json_dict['data_dir_use_list_flag']
            self.data_dir_add_from_list_flag \
            = json_dict['data_dir_add_from_list_flag']
        else:
            self.data_dir_alt_list = [ self.data_dir ]

        if version >= 2000069:  # v2.0.069:
            self.sound_custom = json_dict['sound_custom']

        if version >= 3014:     # v0.3.014
            self.db_backup_mode = json_dict['db_backup_mode']

        if version >= 2000029:  # v2.0.029
            self.show_classic_tab_on_startup_flag \
            = json_dict['show_classic_tab_on_startup_flag']
            self.classic_dir_list = json_dict['classic_dir_list']
            self.classic_dir_previous = json_dict['classic_dir_previous']

        # (In various versions between v0.5.027 and v2.0.097, the youtube
        #   update IVs were overhauled several times)
        self.load_config_ytdl_update(version, json_dict)

        if version >= 1003074:  # v1.3.074
            self.ytdl_output_system_cmd_flag \
            = json_dict['ytdl_output_system_cmd_flag']
        if version >= 1002030:  # v1.2.030
            self.ytdl_output_stdout_flag = json_dict['ytdl_output_stdout_flag']
            self.ytdl_output_ignore_json_flag \
            = json_dict['ytdl_output_ignore_json_flag']
            self.ytdl_output_ignore_progress_flag \
            = json_dict['ytdl_output_ignore_progress_flag']
            self.ytdl_output_stderr_flag = json_dict['ytdl_output_stderr_flag']
            self.ytdl_output_start_empty_flag \
            = json_dict['ytdl_output_start_empty_flag']
        if version >= 1003064:  # v1.3.064
            self.ytdl_output_show_summary_flag \
            = json_dict['ytdl_output_show_summary_flag']

        if version >= 1003074:  # v1.3.074
            self.ytdl_write_system_cmd_flag \
            = json_dict['ytdl_write_system_cmd_flag']
        self.ytdl_write_stdout_flag = json_dict['ytdl_write_stdout_flag']
        if version >= 5004:     # v0.5.004
            self.ytdl_write_ignore_json_flag \
            = json_dict['ytdl_write_ignore_json_flag']
        if version >= 1002030:  # v1.2.030
            self.ytdl_write_ignore_progress_flag \
            = json_dict['ytdl_write_ignore_progress_flag']
        self.ytdl_write_stderr_flag = json_dict['ytdl_write_stderr_flag']

        self.ytdl_write_verbose_flag = json_dict['ytdl_write_verbose_flag']

        if version >= 1002024:  # v1.2.024
            self.refresh_output_videos_flag \
            = json_dict['refresh_output_videos_flag']
        if version >= 1002027:  # v1.2.027
            self.refresh_output_verbose_flag \
            = json_dict['refresh_output_verbose_flag']
        if version >= 1003012:  # v1.3.012
            self.refresh_moviepy_timeout = json_dict['refresh_moviepy_timeout']

        if version >= 1003032:  # v1.3.032
            self.auto_clone_options_flag = json_dict['auto_clone_options_flag']

        if version >= 1002030:  # v1.2.037
            self.disk_space_warn_flag = json_dict['disk_space_warn_flag']
            self.disk_space_warn_limit = json_dict['disk_space_warn_limit']
            self.disk_space_stop_flag = json_dict['disk_space_stop_flag']
            self.disk_space_stop_limit = json_dict['disk_space_stop_limit']

        if version >= 1004024:  # v1.4.024
            self.custom_dl_by_video_flag = json_dict['custom_dl_by_video_flag']

        if version >= 1004052:  # v1.4.052
            self.custom_dl_divert_mode = json_dict['custom_dl_divert_mode']
        elif version >= 1004024:  # v1.4.024
            if json_dict['custom_dl_divert_hooktube_flag']:
                self.custom_dl_divert_mode = 'hooktube'
        if version >= 2001047:  # v2.1.047
            self.custom_dl_divert_website \
            = json_dict['custom_dl_divert_website']
        if version >= 1004024:  # v1.4.024
            self.custom_dl_delay_flag = json_dict['custom_dl_delay_flag']
            self.custom_dl_delay_max = json_dict['custom_dl_delay_max']
            self.custom_dl_delay_min = json_dict['custom_dl_delay_min']

        if version >= 1001054:  # v1.1.054
            self.ffmpeg_path = json_dict['ffmpeg_path']

        if version >= 3029:     # v0.3.029
            self.operation_limit_flag = json_dict['operation_limit_flag']
            self.operation_check_limit = json_dict['operation_check_limit']
            self.operation_download_limit \
            = json_dict['operation_download_limit']

        if version >= 1001067:  # v1.0.067
            self.scheduled_dl_mode = json_dict['scheduled_dl_mode']
            self.scheduled_check_mode = json_dict['scheduled_check_mode']

            # Renamed in v2.1.056
            if 'scheduled_dl_wait_value' in json_dict:
                self.scheduled_dl_wait_value \
                = json_dict['scheduled_dl_wait_value']
                self.scheduled_dl_wait_unit \
                = json_dict['scheduled_dl_wait_unit']
                self.scheduled_check_wait_value \
                = json_dict['scheduled_check_wait_value']
                self.scheduled_check_wait_unit \
                = json_dict['scheduled_check_wait_unit']
            else:
                self.scheduled_dl_wait_value \
                = json_dict['scheduled_dl_wait_hours']
                self.scheduled_dl_wait_unit = 'hours'
                self.scheduled_check_wait_value \
                = json_dict['scheduled_check_wait_hours']
                self.scheduled_check_wait_unit = 'hours'

            self.scheduled_dl_last_time \
            = json_dict['scheduled_dl_last_time']
            self.scheduled_check_last_time \
            = json_dict['scheduled_check_last_time']

            # Renamed in v1.3.120
            if 'scheduled_stop_flag' in json_dict:
                self.scheduled_shutdown_flag = json_dict['scheduled_stop_flag']
            else:
                self.scheduled_shutdown_flag \
                = json_dict['scheduled_shutdown_flag']

        if version >= 2000037:  # v2.0.037
            self.enable_livestreams_flag \
            = json_dict['enable_livestreams_flag']
        if version >= 2000047:  # v2.0.047
            self.livestream_max_days = json_dict['livestream_max_days']
            self.livestream_use_colour_flag \
            = json_dict['livestream_use_colour_flag']
        if version >= 2000052:  # v2.0.052
            self.livestream_auto_notify_flag \
            = json_dict['livestream_auto_notify_flag']
        if version >= 2000068:  # v2.0.068
            self.livestream_auto_alarm_flag \
            = json_dict['livestream_auto_alarm_flag']
        if version >= 2000052:  # v2.0.052
            self.livestream_auto_open_flag \
            = json_dict['livestream_auto_open_flag']
        if version >= 2000054:  # v2.0.054
            self.livestream_auto_dl_start_flag \
            = json_dict['livestream_auto_dl_start_flag']
            self.livestream_auto_dl_stop_flag \
            = json_dict['livestream_auto_dl_stop_flag']
        if version >= 2000037:  # v2.0.037
            self.scheduled_livestream_flag \
            = json_dict['scheduled_livestream_flag']
            self.scheduled_livestream_wait_mins \
            = json_dict['scheduled_livestream_wait_mins']
            self.scheduled_livestream_last_time \
            = json_dict['scheduled_livestream_last_time']

        if version >= 1003112:  # v1.3.112
            self.autostop_time_flag = json_dict['autostop_time_flag']
            self.autostop_time_value = json_dict['autostop_time_value']
            self.autostop_time_unit = json_dict['autostop_time_unit']
            self.autostop_videos_flag = json_dict['autostop_videos_flag']
            self.autostop_videos_value = json_dict['autostop_videos_value']
            self.autostop_size_flag = json_dict['autostop_size_flag']
            self.autostop_size_value = json_dict['autostop_size_value']
            self.autostop_size_unit = json_dict['autostop_size_unit']

        self.operation_auto_update_flag \
        = json_dict['operation_auto_update_flag']
        self.operation_save_flag = json_dict['operation_save_flag']
        if version >= 1004003:  # v1.4.003
            self.operation_sim_shortcut_flag \
            = json_dict['operation_sim_shortcut_flag']
#       # Removed v1.3.028
#        self.operation_dialogue_flag = json_dict['operation_dialogue_flag']
        if version >= 1003028:  # v1.3.028
            self.operation_dialogue_mode = json_dict['operation_dialogue_mode']
        if version >= 1003060:  # v1.3.060
            self.operation_convert_mode = json_dict['operation_convert_mode']

        self.use_module_moviepy_flag = json_dict['use_module_moviepy_flag']
#       # Removed v0.5.003
#        self.use_module_validators_flag \
#        = json_dict['use_module_validators_flag']

        if version >= 1000006:  # v1.0.006
            self.dialogue_copy_clipboard_flag \
            = json_dict['dialogue_copy_clipboard_flag']
            self.dialogue_keep_open_flag \
            = json_dict['dialogue_keep_open_flag']
            # Removed v1.3.022
#            self.dialogue_keep_container_flag \
#            = json_dict['dialogue_keep_container_flag']

        if version >= 1003018:  # v1.3.018
            self.allow_ytdl_archive_flag \
            = json_dict['allow_ytdl_archive_flag']
        if version >= 2001022:  # v2.1.022
            self.classic_ytdl_archive_flag \
            = json_dict['classic_ytdl_archive_flag']
        if version >= 5004:     # v0.5.004
            self.apply_json_timeout_flag \
            = json_dict['apply_json_timeout_flag']
        if version >= 2001060:  # v2.1.060
            self.track_missing_videos_flag \
            = json_dict['track_missing_videos_flag']
            self.track_missing_time_flag \
            = json_dict['track_missing_time_flag']
            self.track_missing_time_days \
            = json_dict['track_missing_time_days']

        if version >= 5004:     # v0.5.004
            self.ignore_child_process_exit_flag \
            = json_dict['ignore_child_process_exit_flag']
        if version >= 1003088:  # v1.3.088
            self.ignore_http_404_error_flag \
            = json_dict['ignore_http_404_error_flag']
            self.ignore_data_block_error_flag \
            = json_dict['ignore_data_block_error_flag']
        if version >= 1027:     # v0.1.028
            self.ignore_merge_warning_flag \
            = json_dict['ignore_merge_warning_flag']
        if version >= 1003088:  # v1.3.088
            self.ignore_missing_format_error_flag \
            = json_dict['ignore_missing_format_error_flag']
        if version >= 1001077:  # v1.1.077
            self.ignore_no_annotations_flag \
            = json_dict['ignore_no_annotations_flag']
        if version >= 1002004:  # v1.2.004
            self.ignore_no_subtitles_flag \
            = json_dict['ignore_no_subtitles_flag']

        if version >= 5004:     # v0.5.004
            self.ignore_yt_copyright_flag \
            = json_dict['ignore_yt_copyright_flag']
        if version >= 1003084:  # v1.3.084
            self.ignore_yt_age_restrict_flag \
            = json_dict['ignore_yt_age_restrict_flag']
        if version >= 1003088:  # v1.3.088
            self.ignore_yt_age_restrict_flag \
            = json_dict['ignore_yt_uploader_deleted_flag']

        if version >= 1003090:  # v1.3.090
            self.ignore_custom_msg_list \
            = json_dict['ignore_custom_msg_list']
            self.ignore_custom_regex_flag \
            = json_dict['ignore_custom_regex_flag']

        self.num_worker_default = json_dict['num_worker_default']
        self.num_worker_apply_flag = json_dict['num_worker_apply_flag']

        self.bandwidth_default = json_dict['bandwidth_default']
        self.bandwidth_apply_flag = json_dict['bandwidth_apply_flag']

        if version >= 1002011:  # v1.2.011
            self.video_res_default = json_dict['video_res_default']
            self.video_res_apply_flag = json_dict['video_res_apply_flag']

        self.match_method = json_dict['match_method']
        self.match_first_chars = json_dict['match_first_chars']
        self.match_ignore_chars = json_dict['match_ignore_chars']

        if version >= 1001029:  # v1.1.029
            self.auto_delete_flag = json_dict['auto_delete_flag']
            self.auto_delete_watched_flag \
            = json_dict['auto_delete_watched_flag']
            self.auto_delete_days = json_dict['auto_delete_days']

        if version >= 1002041:  # v1.2.041
            self.delete_on_shutdown_flag = json_dict['delete_on_shutdown_flag']
        if version >= 1004027:  # v1.4.027
            self.open_temp_on_desktop_flag \
            = json_dict['open_temp_on_desktop_flag']

        self.complex_index_flag = json_dict['complex_index_flag']
        if version >= 3019:  # v0.3.019
            self.catalogue_mode = json_dict['catalogue_mode']
        if version >= 3023:  # v0.3.023
            self.catalogue_page_size = json_dict['catalogue_page_size']
        if version >= 1004005:  # v1.4.005
            self.catalogue_show_filter_flag \
            = json_dict['catalogue_show_filter_flag']
            self.catalogue_alpha_sort_flag \
            = json_dict['catalogue_alpha_sort_flag']
            self.catologue_use_regex_flag \
            = json_dict['catologue_use_regex_flag']

        if version >= 1002013:  # v1.2.013
            self.simple_options_flag = json_dict['simple_options_flag']

        # Having loaded the config file, set various file paths...
        if self.data_dir_use_first_flag:
            self.data_dir = self.data_dir_alt_list[0]

        self.downloads_dir = self.data_dir
        self.alt_downloads_dir = os.path.abspath(
            os.path.join(self.data_dir, 'downloads'),
        )
        self.backup_dir = os.path.abspath(
            os.path.join(self.data_dir, '.backups'),
        )
        self.temp_dir = os.path.abspath(os.path.join(self.data_dir, '.temp'))
        self.temp_dl_dir = os.path.abspath(
            os.path.join(self.data_dir, '.temp', 'downloads'),
        )
        self.temp_test_dir = os.path.abspath(
            os.path.join(self.data_dir, '.temp', 'ytdl-test'),
        )

        # If the most-recently selected directory, self.classic_dir_previous,
        #   still exists in self.classic_dir_list, move it to the top, so it's
        #   the first item displayed in the combo
        if self.classic_dir_previous is not None \
        and self.classic_dir_previous in self.classic_dir_list:

            self.classic_dir_list.remove(self.classic_dir_previous)
            self.classic_dir_list.insert(0, self.classic_dir_previous)

        # In either case, we don't need to remember the previous session's
        #   destination directory any more
        self.classic_dir_previous = None

        # Return False to mark this as not a new installation
        return False


    def load_config_ytdl_update(self, version, json_dict):

        """"Called by self.load_config().

        The IVs handling youtube-dl updates have been overhauled several
        times.

        To keep the layout of self.load_config() reasonable, this function is
        called to import the IVs from the loaded config file, and update them
        as appropriate.

        Args:

            version (int): The config file's Tartube version, converted to a
                simple integer in a call to self.convert_version()

            json_dict: The data loaded from the config file

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 3329 load_config_ytdl_update')

        # (In version v0.5.027, the value of these IVs were overhauled. If
        #   loading from an earlier config file, replace those values with the
        #   new default values)
        if version >= 5027:
            self.ytdl_bin = json_dict['ytdl_bin']
            self.ytdl_path_default = json_dict['ytdl_path_default']
            self.ytdl_path = json_dict['ytdl_path']
            self.ytdl_update_dict = json_dict['ytdl_update_dict']
            self.ytdl_update_list = json_dict['ytdl_update_list']
            self.ytdl_update_current = json_dict['ytdl_update_current']

        # (In version v1.3.903, these IVs were modified a little, but not
        #   on MS Windows)
        if os.name != 'nt' and version <= 1003090:   # v1.3.090
            self.ytdl_update_dict['Update using pip3 (recommended)'] \
            = ['pip3', 'install', '--upgrade', '--user', 'youtube-dl']
            self.ytdl_update_dict['Update using pip3 (omit --user option)'] \
            = ['pip3', 'install', '--upgrade', 'youtube-dl']
            self.ytdl_update_dict['Update using pip'] \
            = ['pip', 'install', '--upgrade', '--user', 'youtube-dl']
            self.ytdl_update_dict['Update using pip (omit --user option)'] \
            = ['pip', 'install', '--upgrade', 'youtube-dl']
            self.ytdl_update_list = [
                'Update using pip3 (recommended)',
                'Update using pip3 (omit --user option)',
                'Update using pip',
                'Update using pip (omit --user option)',
                'Update using default youtube-dl path',
                'Update using local youtube-dl path',
            ]

        # (In version v1.5.012, these IVs were modified a little, but not on
        #   MS Windows)
        if os.name != 'nt' and version <= 1005012:   # v1.5.012
            self.ytdl_update_dict['Update using PyPI youtube-dl path'] \
            = [self.ytdl_path_pypi, '-U']
            self.ytdl_update_list.append('Update using PyPI youtube-dl path')


        # (In version v2.0.086, these IVs were completely overhauled on all
        #   operatin systems)
        if version < 2000096:  # v2.0.096

            update_dict = {
                'Update using default youtube-dl path':
                    'ytdl_update_default_path',
                'Update using local youtube-dl path':
                    'ytdl_update_local_path',
                'Update using pip':
                    'ytdl_update_pip',
                'Update using pip (omit --user option)':
                    'ytdl_update_pip_omit_user',
                'Update using pip3':
                    'ytdl_update_pip3',
                'Update using pip3 (omit --user option)':
                    'ytdl_update_pip3_omit_user',
                'Update using pip3 (recommended)':
                    'ytdl_update_pip3_recommend',
                'Update using PyPI youtube-dl path':
                    'ytdl_update_pypi_path',
                'Windows 32-bit update (recommended)':
                    'ytdl_update_win_32',
                'Windows 64-bit update (recommended)':
                    'ytdl_update_win_64',
                'youtube-dl updates are disabled':
                    'ytdl_update_disabled',
            }

            ytdl_update_dict = {}
            for key in self.ytdl_update_dict:
                ytdl_update_dict[update_dict[key]] = self.ytdl_update_dict[key]

            self.ytdl_update_dict = ytdl_update_dict

            ytdl_update_list = []
            for item in self.ytdl_update_list:
                ytdl_update_list.append(update_dict[item])

            self.ytdl_update_list = ytdl_update_list

            self.ytdl_update_current = update_dict[self.ytdl_update_current]

        # (In version v2.0.109, the directory location used by tartube_mswin.sh
        #   was changed)
        if version < 2000109 and os.name == 'nt':  # v2.0.109

            if 'PROGRAMFILES(X86)' in os.environ:
                recommended = 'ytdl_update_win_64'
            else:
                recommended = 'ytdl_update_win_32'

            recommended_list = self.ytdl_update_dict[recommended]
            mod_list = []

            for item in recommended_list:
                mod_list.append(re.sub(r'^..\\', '', item))

            self.ytdl_update_dict[recommended] = mod_list


    def save_config(self):

        """Called by self.start(), .stop_continue(), switch_db(),
        .download_manager_finished(), .update_manager_finished(),
        .refresh_manager_finished(), .info_manager_finished(),
        .tidy_manager_finished(), .on_menu_save_all(),

        Saves the Tartube config file. If saving fails, disables all file
        loading/saving.
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 3443 save_config')

        # The config file can be stored at one of two locations, depending on
        #   whether xdg is available, or not
        # v2.0.003 (amended v2.1.034) The user can force Tartube to use the
        #   config file in the script's directory (rather than the one in the
        #   location described by xdg) by placing a 'settings.json' file there.
        #   If that file is created when Tartube is already running, it can be
        #   an empty file (because Tartube overwrites it). Otherwise, it should
        #   be a copy of a legitimate config file
        if self.config_file_xdg_path is None \
        or (
            os.path.isfile(self.config_file_path) \
            and not __main__.__pkg_strict_install_flag__
        ):
            config_file_path = self.config_file_path
        else:
            config_file_path = self.config_file_xdg_path

        # Sanity check
        if self.current_manager_obj or self.disable_load_save_flag:

            # When called from self.start(), no main window object exists
            #   yet, and so Tartube will be shut down with this error message
            # When called from anything else, throughout this function the
            #   response is different
            if not self.main_win_obj:
                self.disable_load_save(
                    _(
                    'Failed to save the Tartube config file (failed sanity' \
                    + ' check)',
                    ),
                )

            return

        # Prepare values
        utc = datetime.datetime.utcfromtimestamp(time.time())

        # Remember the size of the main window, if required. The minimum
        #   size for the 'Videos Tab' paned is the standard paned position;
        #   the minimum size for the main window itself is half the standard
        #   size
        if self.main_win_obj and self.main_win_save_size_flag:
            (width, height) = self.main_win_obj.get_size()
            posn = self.main_win_obj.videos_paned.get_position()

            if width >= int(self.main_win_width / 2):
                self.main_win_save_width = width
            else:
                self.main_win_save_width = self.main_win_width

            if height >= int(self.main_win_height / 2):
                self.main_win_save_height = height
            else:
                self.main_win_save_height = self.main_win_height

            if posn >= self.paned_min_size:
                self.main_win_save_posn = posn
            else:
                self.main_win_save_posn = self.paned_min_size

        # Prepare a dictionary of data to save as a JSON file
        json_dict = {
            # Metadata
            'script_name': __main__.__packagename__,
            'script_version': __main__.__version__,
            'save_date': str(utc.strftime('%d %b %Y')),
            'save_time': str(utc.strftime('%H:%M:%S')),
            'file_type': 'config',
            # Data
            'custom_locale': self.custom_locale,

            'main_win_save_size_flag': self.main_win_save_size_flag,
            'main_win_save_width': self.main_win_save_width,
            'main_win_save_height': self.main_win_save_height,
            'main_win_save_posn': self.main_win_save_posn,

            'gtk_emulate_broken_flag': self.gtk_emulate_broken_flag,

            'toolbar_hide_flag': self.toolbar_hide_flag,
            'toolbar_squeeze_flag': self.toolbar_squeeze_flag,
            'show_tooltips_flag': self.show_tooltips_flag,
            'show_custom_icons_flag': self.show_custom_icons_flag,
            'show_small_icons_in_index_flag': \
            self.show_small_icons_in_index_flag,
            'auto_expand_video_index_flag': self.auto_expand_video_index_flag,
            'full_expand_video_index_flag': self.full_expand_video_index_flag,
            'disable_dl_all_flag': self.disable_dl_all_flag,
            'show_pretty_dates_flag': self.show_pretty_dates_flag,

            'show_status_icon_flag': self.show_status_icon_flag,
            'close_to_tray_flag': self.close_to_tray_flag,

            'progress_list_hide_flag': self.progress_list_hide_flag,
            'results_list_reverse_flag': self.results_list_reverse_flag,

            'system_error_show_flag': self.system_error_show_flag,
            'system_warning_show_flag': self.system_warning_show_flag,
            'operation_error_show_flag': self.operation_error_show_flag,
            'operation_warning_show_flag': self.operation_warning_show_flag,
            'system_msg_keep_totals_flag': self.system_msg_keep_totals_flag,

            'data_dir': self.data_dir,
            'data_dir_alt_list': self.data_dir_alt_list,
            'data_dir_use_first_flag': self.data_dir_use_first_flag,
            'data_dir_use_list_flag': self.data_dir_use_list_flag,
            'data_dir_add_from_list_flag': self.data_dir_add_from_list_flag,

            'sound_custom': self.sound_custom,

            'db_backup_mode': self.db_backup_mode,

            'show_classic_tab_on_startup_flag': \
            self.show_classic_tab_on_startup_flag,
            'classic_dir_list': self.classic_dir_list,
            'classic_dir_previous': self.classic_dir_previous,

            'ytdl_bin': self.ytdl_bin,
            'ytdl_path_default': self.ytdl_path_default,
            'ytdl_path': self.ytdl_path,
            'ytdl_update_dict': self.ytdl_update_dict,
            'ytdl_update_list': self.ytdl_update_list,
            'ytdl_update_current': self.ytdl_update_current,

            'ytdl_output_system_cmd_flag': self.ytdl_output_system_cmd_flag,
            'ytdl_output_stdout_flag': self.ytdl_output_stdout_flag,
            'ytdl_output_ignore_json_flag': self.ytdl_output_ignore_json_flag,
            'ytdl_output_ignore_progress_flag': \
            self.ytdl_output_ignore_progress_flag,
            'ytdl_output_stderr_flag': self.ytdl_output_stderr_flag,
            'ytdl_output_start_empty_flag': self.ytdl_output_start_empty_flag,
            'ytdl_output_show_summary_flag': \
            self.ytdl_output_show_summary_flag,

            'ytdl_write_system_cmd_flag': self.ytdl_write_system_cmd_flag,
            'ytdl_write_stdout_flag': self.ytdl_write_stdout_flag,
            'ytdl_write_ignore_json_flag': self.ytdl_write_ignore_json_flag,
            'ytdl_write_ignore_progress_flag': \
            self.ytdl_write_ignore_progress_flag,
            'ytdl_write_stderr_flag': self.ytdl_write_stderr_flag,

            'ytdl_write_verbose_flag': self.ytdl_write_verbose_flag,

            'refresh_output_videos_flag': self.refresh_output_videos_flag,
            'refresh_output_verbose_flag': self.refresh_output_verbose_flag,
            'refresh_moviepy_timeout': self.refresh_moviepy_timeout,

            'auto_clone_options_flag': self.auto_clone_options_flag,

            'disk_space_warn_flag': self.disk_space_warn_flag,
            'disk_space_warn_limit': self.disk_space_warn_limit,
            'disk_space_stop_flag': self.disk_space_stop_flag,
            'disk_space_stop_limit': self.disk_space_stop_limit,

            'custom_dl_by_video_flag': self.custom_dl_by_video_flag,
            'custom_dl_divert_mode': self.custom_dl_divert_mode,
            'custom_dl_divert_website': self.custom_dl_divert_website,
            'custom_dl_delay_flag': self.custom_dl_delay_flag,
            'custom_dl_delay_max': self.custom_dl_delay_max,
            'custom_dl_delay_min': self.custom_dl_delay_min,

            'ffmpeg_path': self.ffmpeg_path,

            'operation_limit_flag': self.operation_limit_flag,
            'operation_check_limit': self.operation_check_limit,
            'operation_download_limit': self.operation_download_limit,

            'scheduled_dl_mode': self.scheduled_dl_mode,
            'scheduled_dl_wait_value': self.scheduled_dl_wait_value,
            'scheduled_dl_wait_unit': self.scheduled_dl_wait_unit,
            'scheduled_dl_last_time': self.scheduled_dl_last_time,

            'scheduled_check_mode': self.scheduled_check_mode,
            'scheduled_check_wait_value': self.scheduled_check_wait_value,
            'scheduled_check_wait_unit': self.scheduled_check_wait_unit,
            'scheduled_check_last_time': self.scheduled_check_last_time,

            'scheduled_shutdown_flag': self.scheduled_shutdown_flag,

            'enable_livestreams_flag': \
            self.enable_livestreams_flag,
            'livestream_max_days': self.livestream_max_days,
            'livestream_use_colour_flag': self.livestream_use_colour_flag,
            'livestream_auto_notify_flag': self.livestream_auto_notify_flag,
            'livestream_auto_alarm_flag': self.livestream_auto_alarm_flag,
            'livestream_auto_open_flag': self.livestream_auto_open_flag,
            'livestream_auto_dl_start_flag': \
            self.livestream_auto_dl_start_flag,
            'livestream_auto_dl_stop_flag': self.livestream_auto_dl_stop_flag,
            'scheduled_livestream_flag': self.scheduled_livestream_flag,
            'scheduled_livestream_wait_mins': \
            self.scheduled_livestream_wait_mins,
            'scheduled_livestream_last_time': \
            self.scheduled_livestream_last_time,

            'autostop_time_flag': self.autostop_time_flag,
            'autostop_time_value': self.autostop_time_value,
            'autostop_time_unit': self.autostop_time_unit,
            'autostop_videos_flag': self.autostop_videos_flag,
            'autostop_videos_value': self.autostop_videos_value,
            'autostop_size_flag': self.autostop_size_flag,
            'autostop_size_value': self.autostop_size_value,
            'autostop_size_unit': self.autostop_size_unit,

            'operation_auto_update_flag': self.operation_auto_update_flag,
            'operation_save_flag': self.operation_save_flag,
            'operation_sim_shortcut_flag': self.operation_sim_shortcut_flag,
            'operation_dialogue_mode': self.operation_dialogue_mode,
            'operation_convert_mode': self.operation_convert_mode,
            'use_module_moviepy_flag': self.use_module_moviepy_flag,

            'dialogue_copy_clipboard_flag': self.dialogue_copy_clipboard_flag,
            'dialogue_keep_open_flag': self.dialogue_keep_open_flag,

            'allow_ytdl_archive_flag': self.allow_ytdl_archive_flag,
            'classic_ytdl_archive_flag': \
            self.classic_ytdl_archive_flag,
            'apply_json_timeout_flag': self.apply_json_timeout_flag,
            'track_missing_videos_flag': self.track_missing_videos_flag,
            'track_missing_time_flag': self.track_missing_time_flag,
            'track_missing_time_days': self.track_missing_time_days,

            'ignore_child_process_exit_flag': \
            self.ignore_child_process_exit_flag,
            'ignore_http_404_error_flag': self.ignore_http_404_error_flag,
            'ignore_data_block_error_flag': self.ignore_data_block_error_flag,
            'ignore_merge_warning_flag': self.ignore_merge_warning_flag,
            'ignore_missing_format_error_flag': \
            self.ignore_missing_format_error_flag,
            'ignore_no_annotations_flag': self.ignore_no_annotations_flag,
            'ignore_no_subtitles_flag': self.ignore_no_subtitles_flag,

            'ignore_yt_copyright_flag': self.ignore_yt_copyright_flag,
            'ignore_yt_age_restrict_flag': self.ignore_yt_age_restrict_flag,
            'ignore_yt_uploader_deleted_flag': \
            self.ignore_yt_uploader_deleted_flag,

            'ignore_custom_msg_list': self.ignore_custom_msg_list,
            'ignore_custom_regex_flag': self.ignore_custom_regex_flag,

            'num_worker_default': self.num_worker_default,
            'num_worker_apply_flag': self.num_worker_apply_flag,

            'bandwidth_default': self.bandwidth_default,
            'bandwidth_apply_flag': self.bandwidth_apply_flag,

            'video_res_default': self.video_res_default,
            'video_res_apply_flag': self.video_res_apply_flag,

            'match_method': self.match_method,
            'match_first_chars': self.match_first_chars,
            'match_ignore_chars': self.match_ignore_chars,

            'auto_delete_flag': self.auto_delete_flag,
            'auto_delete_watched_flag': self.auto_delete_watched_flag,
            'auto_delete_days': self.auto_delete_days,

            'delete_on_shutdown_flag': self.delete_on_shutdown_flag,
            'open_temp_on_desktop_flag': self.open_temp_on_desktop_flag,

            'complex_index_flag': self.complex_index_flag,
            'catalogue_mode': self.catalogue_mode,
            'catalogue_page_size': self.catalogue_page_size,
            'catalogue_show_filter_flag': self.catalogue_show_filter_flag,
            'catalogue_alpha_sort_flag': self.catalogue_alpha_sort_flag,
            'catologue_use_regex_flag': self.catologue_use_regex_flag,

            'simple_options_flag': self.simple_options_flag,
        }

        # In case a competing instance of Tartube is saving the same config
        #   file, check for the lockfile and, if it exists, wait a reasonable
        #   time for it to be released
        if not self.debug_ignore_lockfile_flag:

            lock_path = config_file_path + '.lock'
            if os.path.isfile(lock_path):

                check_time = time.time() + self.config_lock_time
                while time.time < check_time and os.path.isfile(lock_path):
                    time.sleep(0.1)

                if os.path.isfile(lock_path):

                    msg = _(
                        'Failed to save the Tartube config file (file is' \
                        + ' locked)',
                    ) + '\n\n' + _('File load/save has been disabled')

                    if not self.main_win_obj:
                        self.disable_load_save(msg)
                    else:
                        self.disable_load_save()
                        self.file_error_dialogue(msg)

                    return

        # Place our own lock on the config file
        if not self.debug_ignore_lockfile_flag:

            try:
                fh = open(lock_path, 'a').close()

            except:

                msg = _(
                    'Failed to save the Tartube config file (file already' \
                    + ' in use)'
                )

                if not self.main_win_obj:
                    self.disable_load_save(msg)
                else:
                    self.disable_load_save()
                    self.file_error_dialogue(msg)

                return

        # Try to save the config file
        try:
            with open(config_file_path, 'w') as outfile:
                json.dump(json_dict, outfile, indent=4)

        except:
            os.remove(lock_path)

            msg = _('Failed to save the Tartube config file') \
                + '\n\n' + _('File load/save has been disabled')

            if not self.main_win_obj:
                self.disable_load_save(msg)
            else:
                self.disable_load_save()
                self.file_error_dialogue(msg)

            return

        # Procedure successful; remove the lock
        if not self.debug_ignore_lockfile_flag:
            os.remove(lock_path)


    def load_db(self):

        """Called by self.start() and .switch_db().

        Loads the Tartube database file. If loading fails, disables all file
        loading/saving.

        Returns:

            True on success, False on failure

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 3789 load_db')

        # Sanity check
        path = os.path.abspath(os.path.join(self.data_dir, self.db_file_name))
        if self.current_manager_obj \
        or not os.path.isfile(path) \
        or self.disable_load_save_flag:
            return False

        # If a lockfile already exists, then another competing instance of
        #   Tartube is already using this database file
        if not self.debug_ignore_lockfile_flag:

            lock_path = path + '.lock'
            if os.path.isfile(lock_path):

                # (The True argument signals that the user should be prompted
                #   to artificially remove the lockfile)
                self.disable_load_save(
                    _('Failed to load the Tartube database file'),
                    True,
                )

                return False

            else:

                # Place our own lock on the database file
                try:
                    fh = open(lock_path, 'a').close()
                    self.db_lock_file_path = lock_path

                except:

                    # (The True argument signals that the user should be
                    #   prompted to artificially remove the lockfile)
                    self.disable_load_save(
                        _('Failed to load the Tartube database file'),
                        True,
                    )

                    return False

        # Reset main window tabs now so the user can't manipulate their widgets
        #   during the load
        # (Don't reset the Erors/Warnings tab, as failed attempts to load a
        #   database generate messages there)
        if self.main_win_obj:
            self.main_win_obj.video_index_reset()
            self.main_win_obj.video_catalogue_reset()
            self.main_win_obj.progress_list_reset()
            self.main_win_obj.results_list_reset()
            self.main_win_obj.show_all()

        # Most main widgets are desensitised, until the database file has been
        #   loaded
        self.main_win_obj.sensitise_widgets_if_database(False)

        # Try to load the database file
        try:
            fh = open(path, 'rb')
            load_dict = pickle.load(fh)
            fh.close()

        except:
            self.remove_db_lock_file()
            self.disable_load_save(
                _('Failed to load the Tartube database file'),
            )

            return False

        # Do some basic checks on the loaded data
        if not load_dict \
        or not 'script_name' in load_dict \
        or not 'script_version' in load_dict \
        or not 'save_date' in load_dict \
        or not 'save_time' in load_dict \
        or load_dict['script_name'] != __main__.__packagename__:

            self.remove_db_lock_file()
            self.file_error_dialogue(
                _('The Tartube database file is invalid'),
            )

            return False

        # Convert a version, e.g. 1.234.567, into a simple number, e.g.
        #   1234567, that can be compared with other versions
        version = self.convert_version(load_dict['script_version'])
        # Now check that the database file wasn't written by a more recent
        #   version of Tartube (which this older version might not be able to
        #   read)
        if version is None \
        or version > self.convert_version(__main__.__version__):

            self.remove_db_lock_file()
            self.disable_load_save(
                _('Database file can\'t be read by this version of Tartube'),
            )

            return False

        # Before v1.3.099, self.data_dir and self.downloads_dir were different
        # If a /downloads directory exists, then the data directory is using
        #   the old structure
        old_flag = False
        if os.path.isdir(self.alt_downloads_dir):

            # Use the old location of self.downloads_dir
            old_flag = True
            self.downloads_dir = self.alt_downloads_dir
            # Move any database backup files to their new location
            self.move_backup_files()

        else:

            # Use the new location
            self.downloads_dir = self.data_dir

        # Set IVs to their new values
        self.general_options_obj = load_dict['general_options_obj']
        if version >= 2001007:  # v2.1.007
            self.classic_options_obj = load_dict['classic_options_obj']
        self.media_reg_count = load_dict['media_reg_count']
        self.media_reg_dict = load_dict['media_reg_dict']
        self.media_name_dict = load_dict['media_name_dict']
        self.media_top_level_list = load_dict['media_top_level_list']
        if version >= 2000048:  # v2.0.048
            self.media_reg_live_dict = load_dict['media_reg_live_dict']
        if version >= 2000052:  # v2.0.052
            self.media_reg_auto_notify_dict \
            = load_dict['media_reg_auto_notify_dict']
        if version >= 2000068:  # v2.0.068
            self.media_reg_auto_alarm_dict \
            = load_dict['media_reg_auto_alarm_dict']
        if version >= 2000052:  # v2.0.052
            self.media_reg_auto_open_dict \
            = load_dict['media_reg_auto_open_dict']
        if version >= 2000054:  # v2.0.054
            self.media_reg_auto_dl_start_dict \
            = load_dict['media_reg_auto_dl_start_dict']
            self.media_reg_auto_dl_stop_dict \
            = load_dict['media_reg_auto_dl_stop_dict']
        self.fixed_all_folder = load_dict['fixed_all_folder']
        self.fixed_fav_folder = load_dict['fixed_fav_folder']
        self.fixed_new_folder = load_dict['fixed_new_folder']
        self.fixed_temp_folder = load_dict['fixed_temp_folder']
        self.fixed_misc_folder = load_dict['fixed_misc_folder']
        if version >= 1004028:  # v1.4.028
            self.fixed_bookmark_folder = load_dict['fixed_bookmark_folder']
            self.fixed_waiting_folder = load_dict['fixed_waiting_folder']
        if version >= 2000042:  # v2.0.042
            self.fixed_live_folder = load_dict['fixed_live_folder']
        if version >= 2001060:  # v2.1.060
            self.fixed_missing_folder = load_dict['fixed_missing_folder']
        if version >= 2000098:  # v2.0.098
            self.fixed_folder_locale = load_dict['fixed_folder_locale']

        # Update the loaded data for this version of Tartube
        self.update_db(version)

        # If the old directory structure is being used, the user might try to
        #   manually copy the contents of the /downloads directory into the
        #   directory above
        # To prevent problems when that happens, preemptively rename any media
        #   data object called 'downloads'
        if old_flag and 'downloads' in self.media_name_dict:

            dbid = self.media_name_dict['downloads']
            media_data_obj = self.media_reg_dict[dbid]

            # Generate a new name; the function returns None on failure
            new_name = utils.find_available_name(self, 'downloads')
            if new_name is not None:
                self.rename_container_silently(media_data_obj, new_name)

        # If the locale has changed since the loaded database file was last
        #   saved, update the names of fixed folders
        if self.fixed_folder_locale != self.custom_locale:

            self.rename_fixed_folders()
            self.fixed_folder_locale = self.custom_locale

        # Empty any temporary folders
        self.delete_temp_folders()

        # Auto-delete old downloaded videos
        self.auto_delete_old_videos()

        # If the debugging flag is set, hide all fixed folders
        if self.debug_hide_folders_flag:
            self.fixed_all_folder.set_hidden_flag(True)
            self.fixed_bookmark_folder.set_hidden_flag(True)
            self.fixed_fav_folder.set_hidden_flag(True)
            self.fixed_live_folder.set_hidden_flag(True)
            self.fixed_missing_folder.set_hidden_flag(True)
            self.fixed_new_folder.set_hidden_flag(True)
            self.fixed_waiting_folder.set_hidden_flag(True)
            self.fixed_temp_folder.set_hidden_flag(True)
            self.fixed_misc_folder.set_hidden_flag(True)

        # Now that a database file has been loaded, most main window widgets
        #   can be sensitised...
        self.main_win_obj.sensitise_widgets_if_database(True)
        # ...and saving the database file is now allowed
        self.allow_db_save_flag = True

        # Repopulate the Video Index, showing the new data
        if self.main_win_obj:
            self.main_win_obj.video_index_catalogue_reset()

        return True


    def update_db(self, version):

        """Called by self.load_db().

        When the Tartube database created by a previous version of Tartube is
        loaded, update IVs as required.

        Args:

            version (int): The version of Tartube that created the database,
                already converted to a simple integer by self.convert_version()

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 4014 update_db')

        # (Other system folders, having been added later, are not required by
        #   this list)
        fixed_folder_list = [
            self.fixed_all_folder,
            self.fixed_fav_folder,
            self.fixed_new_folder,
        ]

        options_obj_list = [self.general_options_obj]
        for media_data_obj in self.media_reg_dict.values():
            if media_data_obj.options_obj is not None \
            and not media_data_obj.options_obj in options_obj_list:
                options_obj_list.append(media_data_obj.options_obj)

        if version < 3012:  # v0.3.012

            # This version fixed some problems, in which the deletion of media
            #   data objects was not handled correctly
            # Repair the media data registry, as required
            for folder_obj in fixed_folder_list:

                # Check that videos in 'All Videos', 'New Videos' and
                #   'Favourite Videos' still exist in the media data registry
                copy_list = folder_obj.child_list.copy()
                for child_obj in copy_list:
                    if isinstance(child_obj, media.Video) \
                    and not child_obj.parent_obj.dbid in self.media_reg_dict:
                        folder_obj.del_child(child_obj)

                # Video counts in 'All Videos', 'New Videos' and 'Favourite
                #   Videos' might be wrong
                vid_count = new_count = fav_count = dl_count = 0

                for child_obj in folder_obj.child_list:
                    if isinstance(child_obj, media.Video):
                        vid_count += 1

                        if child_obj.new_flag:
                            new_count += 1

                        if child_obj.fav_flag:
                            fav_count += 1

                        if child_obj.dl_flag:
                            dl_count += 1

                folder_obj.reset_counts(
                    vid_count,
                    0,
                    dl_count,
                    fav_count,
                    0,
                    0,
                    new_count,
                    0,
                )

        if version < 4003:  # v0.4.002

            # This version fixes video format options, which were stored
            #   incorrectly in options.OptionsManager
            key_list = [
                'video_format',
                'second_video_format',
                'third_video_format',
            ]

            for options_obj in options_obj_list:
                for key in key_list:

                    val = options_obj.options_dict[key]
                    if val != '0':

                        if val in formats.VIDEO_OPTION_DICT:
                            # Invert the key-value pair used before v0.4.002
                            options_obj.options_dict[key] \
                            = formats.VIDEO_OPTION_DICT[val]

                        else:
                            # Completely invalid format description, so
                            #   just reset it
                            options_obj.options_dict[key] = '0'

#        if version < 4004:  # v0.4.004
#
#            # This version fixes a bug in which moving a channel, playlist or
#            #   folder to a new location in the media data registry's tree
#            #   failed to update all the videos that moved with it
#            # To be safe, update every video in the registry
#            for media_data_obj in self.media_reg_dict.values():
#                if isinstance(media_data_obj, media.Video):
#                    media_data_obj.reset_file_dir()

        if version < 4015:  # v0.4.015

            # This version fixes issues with sorting videos. Channels,
            #   playlists and folders in a loaded database might not be sorted
            #   correctly, so just sort them all using the new algorithms
            # (Other system folders, having been added later, are not required
            #   by this list)
            container_list = [
                self.fixed_all_folder,
                self.fixed_new_folder,
                self.fixed_fav_folder,
                self.fixed_misc_folder,
                self.fixed_temp_folder,
            ]

            for dbid in self.media_name_dict.values():
                container_list.append(self.media_reg_dict[dbid])

            for container_obj in container_list:
                container_obj.sort_children()

        if version < 4022:  # v0.4.022

            # This version fixes a rare issue in which media.Video.index was
            #   set to a string, rather than int, value
            # Update all existing videos
            for media_data_obj in self.media_reg_dict.values():
                if isinstance(media_data_obj, media.Video) \
                and media_data_obj.index is not None:
                    media_data_obj.index = int(media_data_obj.index)

        if version < 6003:  # v0.6.003

            # This version fixes an issue in which deleting an individual video
            #   and then re-adding the same video, downloading it then deleting
            #   it a second time, messes up the parent container's count IVs
            # Nothing for it but to recalculate them all, just in case
            for dbid in self.media_name_dict.values():
                container_obj = self.media_reg_dict[dbid]

                vid_count = new_count = fav_count = dl_count = 0

                for child_obj in container_obj.child_list:
                    if isinstance(child_obj, media.Video):
                        vid_count += 1

                        if child_obj.new_flag:
                            new_count += 1

                        if child_obj.fav_flag:
                            fav_count += 1

                        if child_obj.dl_flag:
                            dl_count += 1

                container_obj.reset_counts(
                    vid_count,
                    0,
                    dl_count,
                    fav_count,
                    0,
                    0,
                    new_count,
                    0,
                )

        if version < 1000013:  # v1.0.013

            # This version adds nicknames to channels, playlists and folders
            for dbid in self.media_name_dict.values():
                container_obj = self.media_reg_dict[dbid]
                container_obj.nickname = container_obj.name

        if version < 1000031:  # v1.0.031

            # This version adds nicknames to videos. If the database is large,
            #   warn the user before continuing
            if self.media_reg_dict.len() > 1000:

                dialogue_win = self.dialogue_manager_obj.show_msg_dialogue(
                    _('Tartube is applying an essential database update') \
                    + '\n\n' \
                    + _('This might take a few minutes, so please be patient'),
                    'info',
                    'ok',
                    self.main_win_obj,
                )

                dialogue_win.set_modal(True)

            for media_data_obj in self.media_reg_dict.values():
                if isinstance(media_data_obj, media.Video):

                    media_data_obj.nickname = media_data_obj.name

                    # If the video's JSON data has been saved, we can use that
                    #   to set the nickname
                    json_path = media_data_obj.get_actual_path_by_ext(
                        self,
                        '.info.json',
                    )

                    if os.path.isfile(json_path):
                        json_dict = self.file_manager_obj.load_json(json_path)
                        if 'title' in json_dict:
                            media_data_obj.nickname = json_dict['title']


        if version < 1001031:  # v1.1.031

            # This version adds the ability to disable checking/downloading for
            #   media data objects
            for dbid in self.media_name_dict.values():
                media_data_obj = self.media_reg_dict[dbid]
                media_data_obj.dl_disable_flag = False

        if version < 1001032:  # v1.1.032

            # This version adds video archiving. Archived videos cannot be
            #   auto-deleted
            for media_data_obj in self.media_reg_dict.values():
                if isinstance(media_data_obj, media.Video):
                    media_data_obj.archive_flag = False

        if version < 1001037:  # v1.1.037

            # This version adds alternative destination directories for a
            #   channel's/playlist's/folder's videos, thumbnails (etc)
            for dbid in self.media_name_dict.values():
                media_data_obj = self.media_reg_dict[dbid]
                media_data_obj.master_dbid = media_data_obj.dbid
                media_data_obj.slave_dbid_list = []

        if version < 1001045:  # v1.1.045

            # This version adds a new option to options.OptionsManager
            for options_obj in options_obj_list:
                options_obj.options_dict['use_fixed_folder'] = None

        if version < 1001060:  # v1.1.060

            # This version adds new options to options.OptionsManager
            for options_obj in options_obj_list:
                options_obj.options_dict['abort_on_error'] = False

                options_obj.options_dict['socket_timeout'] = ''
                options_obj.options_dict['source_address'] = ''
                options_obj.options_dict['force_ipv4'] = False
                options_obj.options_dict['force_ipv6'] = False

                options_obj.options_dict['geo_verification_proxy'] = ''
                options_obj.options_dict['geo_bypass'] = False
                options_obj.options_dict['no_geo_bypass'] = False
                options_obj.options_dict['geo_bypass_country'] = ''
                options_obj.options_dict['geo_bypass_ip_block'] = ''

                options_obj.options_dict['match_title_list'] = []
                options_obj.options_dict['reject_title_list'] = []

                options_obj.options_dict['date'] = ''
                options_obj.options_dict['date_before'] = ''
                options_obj.options_dict['date_after'] = ''
                options_obj.options_dict['min_views'] = 0
                options_obj.options_dict['max_views'] = 0
                options_obj.options_dict['match_filter'] = ''
                options_obj.options_dict['age_limit'] = ''
                options_obj.options_dict['include_ads'] = False

                options_obj.options_dict['playlist_reverse'] = False
                options_obj.options_dict['playlist_random'] = False
                options_obj.options_dict['prefer_ffmpeg'] = False
                options_obj.options_dict['external_downloader'] = ''
                options_obj.options_dict['external_arg_string'] = ''

                options_obj.options_dict['force_encoding'] = ''
                options_obj.options_dict['no_check_certificate'] = False
                options_obj.options_dict['prefer_insecure'] = False

                options_obj.options_dict['all_formats'] = False
                options_obj.options_dict['prefer_free_formats'] = False
                options_obj.options_dict['yt_skip_dash'] = False
                options_obj.options_dict['merge_output_format'] = ''

                options_obj.options_dict['subs_format'] = ''

                options_obj.options_dict['two_factor'] = ''
                options_obj.options_dict['net_rc'] = False

                options_obj.options_dict['recode_video'] = ''
                options_obj.options_dict['pp_args'] = ''
                options_obj.options_dict['fixup_policy'] = ''
                options_obj.options_dict['prefer_avconv'] = False
                options_obj.options_dict['prefer_ffmpeg'] = False

                options_obj.options_dict['write_annotations'] = True
                options_obj.options_dict['keep_annotations'] = False
                options_obj.options_dict['sim_keep_annotations'] = False

                # (Also rename one option)
                options_obj.options_dict['extract_audio'] \
                = options_obj.options_dict['to_audio']
                options_obj.options_dict.pop('to_audio')

#        if version < 1003004:  # v1.3.004
#
#            # The way that directories are stored in media.VideoObj.file_dir
#            #   has changed. Reset those values for all video objects
#            for media_data_obj in self.media_reg_dict.values():
#                if isinstance(media_data_obj, media.Video):
#
#                    media_data_obj.reset_file_dir()

        if version < 1003009:  # v1.3.009

            # In earlier versions,
            #   refresh.RefreshManager.refresh_from_default_destination() set a
            #   video's .name, but not its .nickname
            # The .refresh_from_default_destination() is already fixed, but we
            #   need to check every video in the database, and set its
            #   .nickname if not set
            for media_data_obj in self.media_reg_dict.values():
                if isinstance(media_data_obj, media.Video):
                    if (
                        media_data_obj.nickname is None \
                        or media_data_obj.nickname == self.default_video_name
                    ) and media_data_obj.name is not None \
                    and media_data_obj.name != self.default_video_name:
                        media_data_obj.nickname = media_data_obj.name

        if version < 1003017:  # v1.3.017

            for options_obj in options_obj_list:

                # In earlier versions, the 'prefer_ffmpeg' and
                #   'hls_prefer_ffmpeg' download options had been confused
                options_obj.options_dict['hls_prefer_ffmpeg'] = False

                # In earlier versions, MS Windows users could set the
                #   'prefer_ffmpeg' and 'prefer_avconv' options, even though
                #   the MS Windows installer does not provide AVConv. Reset
                #   both values
                options_obj.options_dict['prefer_ffmpeg'] = False
                options_obj.options_dict['prefer_avconv'] = False

                # In earlier versions, the download options 'video_format',
                #   'second_video_format' and/or 'third_video_format' could
                #   incorrectly be set to a sound format like 'mp3'. This is
                #   not the way youtube-dl-gui was supposed to implement its
                #   formats; remove them, if the user has specified them
                if not options_obj.options_dict['third_video_format'] \
                in formats.VIDEO_OPTION_DICT:
                    options_obj.options_dict['third_video_format'] = '0'

                if not options_obj.options_dict['second_video_format'] \
                in formats.VIDEO_OPTION_DICT:
                    options_obj.options_dict['second_video_format'] = '0'
                    if options_obj.options_dict['third_video_format'] != '0':
                        options_obj.options_dict['second_video_format'] \
                        = options_obj.options_dict['third_video_format']
                        options_obj.options_dict['third_video_format'] = '0'

                if not options_obj.options_dict['video_format'] \
                in formats.VIDEO_OPTION_DICT:
                    options_obj.options_dict['video_format'] = '0'
                    if options_obj.options_dict['second_video_format'] != '0':
                        options_obj.options_dict['video_format'] \
                        = options_obj.options_dict['second_video_format']
                        options_obj.options_dict['second_video_format'] \
                        = options_obj.options_dict['third_video_format']

        if version <= 1003099:      # v1.3.099

            # In this version, some container names have become illegal.
            #   Replace any illegal names with legal ones
            for old_name in self.media_name_dict.keys():
                if not self.check_container_name_is_legal(old_name):

                    dbid = self.media_name_dict[old_name]
                    media_data_obj = self.media_reg_dict[dbid]

                    # Generate a new name. The -1 argument means to keep going
                    #   indefinitely, until an available name is found
                    self.rename_container_silently(
                        media_data_obj,
                        utils.find_available_name(self, 'downloads', 2, -1),
                    )

        if version < 1003106:  # v1.3.106

            # This version adds a new option to options.OptionsManager
            for options_obj in options_obj_list:
                if options_obj.options_dict['subs_lang'] == '':
                    options_obj.options_dict['subs_lang_list'] = []
                else:
                    options_obj.options_dict['subs_lang_list'] \
                    = [ options_obj.options_dict['subs_lang'] ]

        if version < 1003110:  # v1.3.110

            # Before this version, the 'output_template' in
            #   options.OptionManager was completely broken, containing both
            #   the filepath to this file, and an '%(uploader)s string that
            #   broke the structure of Tartube's data directory
            # Reset the value if it seems to contain either
            for options_obj in options_obj_list:
                output_template = options_obj.options_dict['output_template']
                if re.search(sys.path[0], output_template) \
                or re.search('\%\(uploader\)s', output_template):
                    options_obj.options_dict['output_template'] \
                    = '%(title)s.%(ext)s'

        if version < 1003111:  # v1.3.111

            # In this version, formats.py.FILE_OUTPUT_NAME_DICT and
            #   .FILE_OUTPUT_CONVERT_DICT, so that the custom format's index
            #   is 0 (was 3)
            for options_obj in options_obj_list:
                output_format = options_obj.options_dict['output_format']
                if output_format == 3:
                    options_obj.options_dict['output_format'] = 0
                elif output_format < 3:
                    options_obj.options_dict['output_format'] \
                    = output_format + 1

        if version < 1004028:      # v1.4.028

            # This version adds two new fixed folders. If there are existing
            #   folders with the same name, they must be renamed
            old_list \
            = [formats.FOLDER_BOOKMARKS, formats.FOLDER_WAITING_VIDEOS]
            for old_name in old_list:

                if old_name in self.media_name_dict:

                    dbid = self.media_name_dict[old_name]
                    media_data_obj = self.media_reg_dict[dbid]

                    # Generate a new name. The -1 argument means to keep going
                    #   indefinitely, until an available name is found
                    self.rename_container_silently(
                        media_data_obj,
                        utils.find_available_name(self, 'downloads', 2, -1),
                    )

            # Now create the new fixed folders
            self.fixed_bookmark_folder = self.add_folder(
                formats.FOLDER_BOOKMARKS,
                None,           # No parent folder
                False,          # Allow downloads
                True,           # Fixed (folder cannot be removed)
                True,           # Private
                True,           # Can only contain videos
                False,          # Not temporary
            )

            self.fixed_waiting_folder = self.add_folder(
                formats.FOLDER_WAITING_VIDEOS,
                None,           # No parent folder
                False,          # Allow downloads
                True,           # Fixed (folder cannot be removed)
                True,           # Private
                True,           # Can only contain videos
                False,          # Not temporary
            )

        if version < 1004037:  # v1.4.037

            # Having added new fixed folders, add corresponding new IVs for
            #   each media.Video object
            for dbid in self.media_name_dict.values():
                container_obj = self.media_reg_dict[dbid]

                for child_obj in container_obj.child_list:
                    if isinstance(child_obj, media.Video):
                        child_obj.bookmark_flag = False
                        child_obj.waiting_flag = False

        if version < 1004037:  # v1.4.037

            # This version adds new IVs to channels, playlists and folders
            for dbid in self.media_name_dict.values():
                container_obj = self.media_reg_dict[dbid]

                container_obj.bookmark_count = 0
                container_obj.waiting_count = 0

                # Some of the count IVs were not working 100%, so we'll just
                #   recalculate them all
                container_obj.recalculate_counts()

        if version < 1004043:  # v1.4.043

            # This version removes an IV from media.Video objects
            for media_data_obj in self.media_reg_dict.values():
                if isinstance(media_data_obj, media.Video):
                    del media_data_obj.file_dir

        if version < 2000012:  # v2.0.012

            # This version does not add the ytdl-archive.txt file to system
            #   folders ('Unsorted Videos' and 'Temporary Videos'), but
            #   continues to add it to channels, playlists and non-system
            #   folders
            # Remove the archive file from system folders, if present

            # 'Temporary Videos'
            temp_path = os.path.abspath(
                os.path.join(
                    self.fixed_temp_folder.get_default_dir(self),
                    'ytdl-archive.txt',
                ),
            )

            if os.path.isfile(temp_path):
                os.remove(temp_path)

            # 'Unsorted Videos'
            unsorted_path = os.path.abspath(
                os.path.join(
                    self.fixed_misc_folder.get_default_dir(self),
                    'ytdl-archive.txt',
                ),
            )

            if os.path.isfile(unsorted_path):
                os.remove(unsorted_path)

        if version < 2000025:  # v2.0.025

            # This version adds the Classic Mode Tab, and new IVs used by it.
            #   Most of them are only created when needed
            for media_data_obj in self.media_reg_dict.values():
                if isinstance(media_data_obj, media.Video):
                    media_data_obj.dummy_flag = False

        if version < 2000035:  # v2.0.035

            # This version adds IVs for livestream detection on compatible
            #   websites
            for media_data_obj in self.media_reg_dict.values():
                if isinstance(media_data_obj, media.Video):
                    media_data_obj.live_mode = 0
                elif not isinstance(media_data_obj, media.Folder):
                    media_data_obj.rss = None

        if version < 2000042:  # v2.0.042

            # This version adds new IVs to channels, playlists and folders
            for dbid in self.media_name_dict.values():
                container_obj = self.media_reg_dict[dbid]

                container_obj.live_count = 0

            # This version also creates a new fixed folder. If there are
            #   existing folders with the same name, they must be renamed
            if formats.FOLDER_LIVESTREAMS in self.media_name_dict:

                dbid = self.media_name_dict[formats.FOLDER_LIVESTREAMS]
                media_data_obj = self.media_reg_dict[dbid]

                # Generate a new name. The -1 argument means to keep going
                #   indefinitely, until an available name is found
                self.rename_container_silently(
                    media_data_obj,
                    utils.find_available_name(self, 'downloads', 2, -1),
                )

            # Now create the new fixed folder
            self.fixed_live_folder = self.add_folder(
                formats.FOLDER_LIVESTREAMS,
                None,           # No parent folder
                False,          # Allow downloads
                True,           # Fixed (folder cannot be removed)
                True,           # Private
                True,           # Can only contain videos
                False,          # Not temporary
            )

        if version < 2000105:  # v2.0.105

            # This version adds new options to options.OptionsManager, and
            #   deletes some existing ones
            for options_obj in options_obj_list:

                options_obj.options_dict['video_format_list'] = []

                if options_obj.options_dict['all_formats']:
                    options_obj.options_dict['video_format_mode'] = 'all'
                    options_obj.options_dict['all_formats'] = False
                else:
                    options_obj.options_dict['video_format_mode'] = 'single'

                options_obj.options_dict.pop('second_video_format')
                options_obj.options_dict.pop('third_video_format')

        if version < 2001010:  # v2.1.010

            # This version adds a new IV to media.Video objects
            for media_data_obj in self.media_reg_dict.values():
                if isinstance(media_data_obj, media.Video):
                    media_data_obj.was_live_flag = False

        if version < 2001012:  # v2.1.012

            # v2.1.005 Addresses problems in which a media.Video might still
            #   exist inside the 'New videos' folder (etc), but not anywhere
            #   else in the database
            # Still not sure what the cause was, but assuming that it was some
            #   ancient issue, long since fixed, force a silent call to the
            #   check/fix functions
            self.check_integrity_db(True)


        if version < 2001037:  # v2.1.037

            # This version adds a new IV to media.Video objects
            for media_data_obj in self.media_reg_dict.values():
                if isinstance(media_data_obj, media.Video):
                    media_data_obj.orig_parent = None

        if version < 2001041:  # v2.1.041

            # This version fixes a problem in options.OptionsManager; when
            #   options were applied to a channel/playlist/folder, the cloned
            #   dictionary of options contained lists that were not copied
            #   properly; hence changing one list changed all of them
            for options_obj in options_obj_list:

                for key in [
                    'match_title_list', 'reject_title_list',
                    'video_format_list', 'subs_lang_list',
                ]:
                    options_obj.options_dict[key] \
                    = options_obj.options_dict[key].copy()

        if version < 2001060:      # v2.1.060

            # This version adds a new fixed folders. If there is an existing
            #   folder with the same name, it must be renamed
            if formats.FOLDER_MISSING_VIDEOS in self.media_name_dict:

                dbid = self.media_name_dict[formats.FOLDER_MISSING_VIDEOS]
                media_data_obj = self.media_reg_dict[dbid]

                # Generate a new name. The -1 argument means to keep going
                #   indefinitely, until an available name is found
                self.rename_container_silently(
                    media_data_obj,
                    utils.find_available_name(self, 'downloads', 2, -1),
                )

            # Now create the new fixed folder
            self.fixed_missing_folder = self.add_folder(
                formats.FOLDER_MISSING_VIDEOS,
                None,           # No parent folder
                False,          # Allow downloads
                True,           # Fixed (folder cannot be removed)
                True,           # Private
                True,           # Can only contain videos
                False,          # Not temporary
            )

            # Having added new the fixed folder, add a corresponding new IV for
            #   each media.Video object
            for dbid in self.media_name_dict.values():

                container_obj = self.media_reg_dict[dbid]
                container_obj.missing_count = 0

                for child_obj in container_obj.child_list:
                    if isinstance(child_obj, media.Video):
                        child_obj.missing_flag = False


    def save_db(self):

        """Called by self.start(), .stop_continue(), .switch_db(),
        .fix_integrity_db(), .download_manager_finished(),
        .update_manager_finished(), .refresh_manager_finished(),
        .info_manager_finished(), .tidy_manager_finished(),
        .move_container_to_top_continue(), .move_container_continue(),
        .rename_container(), .on_menu_save_all() and .on_menu_save_db().

        Saves the Tartube database file. If saving fails, disables all file
        loading/saving.

        Returns:

            True on success, False on failure

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 4622 save_db')

        # Sanity check
        if self.current_manager_obj \
        or self.disable_load_save_flag \
        or not self.allow_db_save_flag:
            return False

        # Prepare values
        utc = datetime.datetime.utcfromtimestamp(time.time())
        path = os.path.abspath(os.path.join(self.data_dir, self.db_file_name))
        bu_path = os.path.abspath(
            os.path.join(
                self.backup_dir,
                __main__.__packagename__ + '_BU.db',
            ),
        )
        temp_bu_path = os.path.abspath(
            os.path.join(
                self.backup_dir,
                __main__.__packagename__ + '_TEMP_BU.db',
            ),
        )

        # Prepare a dictionary of data to save, using Python pickle
        save_dict = {
            # Metadata
            'script_name': __main__.__packagename__,
            'script_version': __main__.__version__,
            'save_date': str(utc.strftime('%d %b %Y')),
            'save_time': str(utc.strftime('%H:%M:%S')),
            # Data
            'general_options_obj' : self.general_options_obj,
            'classic_options_obj' : self.classic_options_obj,
            'media_reg_count': self.media_reg_count,
            'media_reg_dict': self.media_reg_dict,
            'media_name_dict': self.media_name_dict,
            'media_top_level_list': self.media_top_level_list,
            'media_reg_live_dict': self.media_reg_live_dict,
            'media_reg_auto_notify_dict': self.media_reg_auto_notify_dict,
            'media_reg_auto_alarm_dict': self.media_reg_auto_alarm_dict,
            'media_reg_auto_open_dict': self.media_reg_auto_open_dict,
            'media_reg_auto_dl_start_dict': self.media_reg_auto_dl_start_dict,
            'media_reg_auto_dl_stop_dict': self.media_reg_auto_dl_stop_dict,
            'fixed_all_folder': self.fixed_all_folder,
            'fixed_bookmark_folder': self.fixed_bookmark_folder,
            'fixed_fav_folder': self.fixed_fav_folder,
            'fixed_live_folder': self.fixed_live_folder,
            'fixed_missing_folder': self.fixed_missing_folder,
            'fixed_new_folder': self.fixed_new_folder,
            'fixed_waiting_folder': self.fixed_waiting_folder,
            'fixed_temp_folder': self.fixed_temp_folder,
            'fixed_misc_folder': self.fixed_misc_folder,
            'fixed_folder_locale': self.fixed_folder_locale,
        }

        # Back up any existing file
        if os.path.isfile(path):
            try:
                shutil.copyfile(path, temp_bu_path)

            except:
                self.disable_load_save()
                self.file_error_dialogue(
                    _('Failed to save the Tartube database file') \
                    + '\n\n' \
                    + _(
                        '(Could not make a backup copy of the existing file)'
                    ) \
                    + '\n\n' \
                    + _('File load/save has been disabled'),
                )

                return False

        # If there is no lock already in place (for example, because this is a
        #   new database file), then create a lockfile
        if not self.debug_ignore_lockfile_flag:

            if self.db_lock_file_path is None:

                lock_path = path + '.lock'
                if os.path.isfile(lock_path):

                    self.system_error(
                        103,
                        'Database file \'' + lock_path + '\' already exists,' \
                        + ' and is locked',
                    )

                    return False

                else:

                    # Place our own lock on the database file
                    try:
                        fh = open(lock_path, 'a').close()
                        self.db_lock_file_path = lock_path

                    except:

                        self.disable_load_save(
                            _(
                            'Failed to save the Tartube database file (file' \
                            + ' already in use)',
                            ),
                        )

                        return False

        # Try to save the database file
        try:
            fh = open(path, 'wb')
            pickle.dump(save_dict, fh)
            fh.close()

        except:

            self.disable_load_save()

            if os.path.isfile(temp_bu_path):
                self.file_error_dialogue(
                    _('Failed to save the Tartube database file') \
                    + '\n\n' \
                    + _('A backup of the previous file can be found at:') \
                    + '\n\n   ' + temp_bu_path + '\n\n' \
                    + _('File load/save has been disabled'),
                )

            else:
                self.file_error_dialogue(
                    _('Failed to save the Tartube database file') \
                    + '\n\n' + _('File load/save has been disabled'),
                )

            return False

        # In the event that there was no database file to backup, then the
        #   following code isn't necessary
        if os.path.isfile(temp_bu_path):

            # Make the backup file permanent, or not, depending on settings
            if self.db_backup_mode == 'default':
                os.remove(temp_bu_path)

            elif self.db_backup_mode == 'single':

                # (On MSWin, can't do os.rename if the destination file already
                #   exists)
                if os.path.isfile(bu_path):
                    os.remove(bu_path)

                # (os.rename sometimes fails on external hard drives; this is
                #   safer)
                shutil.move(temp_bu_path, bu_path)

            elif self.db_backup_mode == 'daily':

                daily_bu_path = os.path.abspath(
                    os.path.join(
                        self.backup_dir,
                        __main__.__packagename__ + '_BU_' \
                        + str(utc.strftime('%Y_%m_%d')) + '.db',
                    ),
                )

                # Only make a new backup file once per day
                if not os.path.isfile(daily_bu_path):

                    if os.path.isfile(daily_bu_path):
                        os.remove(daily_bu_path)

                    shutil.move(temp_bu_path, daily_bu_path)

                else:

                    os.remove(temp_bu_path)

            elif self.db_backup_mode == 'always':

                always_bu_path = os.path.abspath(
                    os.path.join(
                        self.backup_dir,
                        __main__.__packagename__ + '_BU_' \
                        + str(utc.strftime('%Y_%m_%d_%H_%M_%S')) + '.db',
                    ),
                )

                if os.path.isfile(always_bu_path):
                    os.remove(always_bu_path)

                shutil.move(temp_bu_path, always_bu_path)

        # Saving a database file, in order to create a new file, is much like
        #   loading one: main window widgets can now be sensitised
        self.main_win_obj.sensitise_widgets_if_database(True)

        # Save succeeded
        return True


    def switch_db(self, data_list):

        """Called by config.SystemPrefWin.try_switch_db().

        When the user selects a new location for a data directory, first save
        our existing database.

        Then load the database at the new location, if exists, or create a new
        database there, if not.

        Args:

            data_list (list): A list containing two items: the full file path
                to the location of the new data directory, and the system
                preferences window (config.SystemPrefWin) that the user has
                open

        Returns:

            True on success, False on failure

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 4845 switch_db')

        # Extract values from the argument list
        path = data_list.pop(0)
        pref_win_obj = data_list.pop(0)

        # Sanity check
        if self.current_manager_obj or self.disable_load_save_flag:
            return False

        # If the old path is the same as the new one, we don't need to do
        #   anything
        if path == self.data_dir:
            return False

        # Save the existing database, and release its lockfile
        if not self.save_db():
            return False
        else:
            self.remove_db_lock_file()

        # Delete Tartube's temporary folder from the filesystem
        if os.path.isdir(self.temp_dir):
            shutil.rmtree(self.temp_dir)

        # Update IVs for the new location of the data directory
        self.data_dir = path
        self.downloads_dir = path
        self.alt_downloads_dir = os.path.abspath(
            os.path.join(path, 'downloads'),
        )
        self.backup_dir = os.path.abspath(os.path.join(path, '.backups'))
        self.temp_dir = os.path.abspath(os.path.join(path, '.temp'))
        self.temp_dl_dir = os.path.abspath(
            os.path.join(path, '.temp', 'downloads'),
        )
        self.temp_test_dir = os.path.abspath(
            os.path.join(path, '.temp', 'ytdl-test'),
        )

        if self.data_dir_add_from_list_flag \
        and not self.data_dir in self.data_dir_alt_list:
            self.data_dir_alt_list.append(self.data_dir)

        # Before v1.3.099, self.data_dir and self.downloads_dir were different
        # If a /downloads directory exists, then the data directory is using
        #   the old structure
        if os.path.isdir(self.alt_downloads_dir):

            # Use the old location of self.downloads_dir
            self.downloads_dir = self.alt_downloads_dir

        else:

            # Use the new location
            self.downloads_dir = self.data_dir

        # Any of those directories that don't exist should be created
        if not os.path.isdir(self.data_dir):
            # React to a 'Permission denied' error by asking the user what to
            #   do next. If necessary, shut down Tartube
            # The True argument means that the drive is unwriteable
            if not self.make_directory(self.data_dir):
                return False

        if not os.path.isdir(self.backup_dir):
            if not self.make_directory(self.backup_dir):
                return False

        # (The temporary data directory should be emptied, if it already
        #   exists)
        if os.path.isdir(self.temp_dir):
            try:
                shutil.rmtree(self.temp_dir)

            except:
                if not self.make_directory(self.temp_dir):
                    return False
                else:
                    shutil.rmtree(self.temp_dir)

        if not os.path.isdir(self.temp_dir):
            if not self.make_directory(self.temp_dir):
                return self.main_win_obj.destroy()

        if not os.path.isdir(self.temp_dl_dir):
            if not self.make_directory(self.temp_dl_dir):
                return self.main_win_obj.destroy()

        # If the database file itself exists; load it. If not, create it
        db_path = os.path.abspath(
            os.path.join(self.data_dir, self.db_file_name),
        )
        if not os.path.isfile(db_path):

            # Reset main window widgets
            # (Don't reset the Erors/Warnings tab, as failed attempts to load a
            #   database generate messages there)
            self.main_win_obj.video_index_reset()
            self.main_win_obj.video_catalogue_reset()
            self.main_win_obj.progress_list_reset()
            self.main_win_obj.results_list_reset()

            # Reset database IVs
            self.reset_db()

            # Create a new database file
            self.save_db()

            # Save the config file, to preserve the new location of the data
            #   directory
            self.save_config()

            # Repopulate the Video Index, showing the new data
            self.main_win_obj.video_index_populate()

            # If the system preferences window is open, reset it to show the
            #   new data directory
            if pref_win_obj and pref_win_obj.is_visible():

                pref_win_obj.reset_window()
                pref_win_obj.select_switch_db_tab()

                self.dialogue_manager_obj.show_msg_dialogue(
                    _('Database file created'),
                    'info',
                    'ok',
                    pref_win_obj,
                )

            else:

                # (Parent window is the main window)
                self.dialogue_manager_obj.show_msg_dialogue(
                    _('Database file created'),
                    'info',
                    'ok',
                )

            return True

        else:

            if not self.load_db():

                return False

            else:

                # Save the config file, to preserve the new location of the
                #   data directory
                self.save_config()
                return True


    def choose_alt_db(self):

        """Called by self.start() (only), shortly after loading (or creating)
        the config file.

        Multiple instances of Tartube can share the same config file, but not
        the same database file.

        If the database file specified by the config file we've just loaded
        is locked (meaning it's in use by another instance), we might be
        able to use one of the alternative data directories specified by the
        user.
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 5015 choose_alt_db')

        db_file_path = os.path.abspath(
            os.path.join(self.data_dir, self.db_file_name),
        )

        lock_file_path = db_file_path + '.lock'

        if os.path.exists(self.data_dir) \
        and os.path.isfile(db_file_path) \
        and os.path.isfile(lock_file_path) \
        and not self.debug_ignore_lockfile_flag:
            self.system_warning(
                104,
                _(
                'Tartube database \'{0}\' can\'t be loaded - another' \
                + ' instance of Tartube may be using it. If not, you can' \
                + ' fix this problem by deleting the lockfile \'{1}\'',
                ).format(self.data_dir, lock_file_path),
            )

            for alt_data_dir in self.data_dir_alt_list:

                if alt_data_dir == self.data_dir:
                    # Already tried this one
                    continue

                alt_db_file_path = os.path.abspath(
                    os.path.join(alt_data_dir, self.db_file_name),
                )

                alt_lock_file_path = alt_db_file_path + '.lock'

                if os.path.exists(alt_data_dir) \
                and os.path.isfile(alt_db_file_path) \
                and (
                    not os.path.isfile(alt_lock_file_path) \
                    or self.debug_ignore_lockfile_flag
                ):
                    # Try loading this database instead
                    self.data_dir = alt_data_dir
                    # (Update other IVs to match)
                    self.downloads_dir = self.data_dir

                    self.alt_downloads_dir = os.path.abspath(
                        os.path.join(self.data_dir, 'downloads'),
                    )
                    self.backup_dir = os.path.abspath(
                        os.path.join(self.data_dir, '.backups'),
                    )
                    self.temp_dir = os.path.abspath(
                        os.path.join(self.data_dir, '.temp'),
                    )
                    self.temp_dl_dir = os.path.abspath(
                        os.path.join(self.data_dir, '.temp', 'downloads'),
                    )
                    self.temp_test_dir = os.path.abspath(
                        os.path.join(self.data_dir, '.temp', 'ytdl-test'),
                    )

                    return

                else:

                    self.system_warning(
                        105,
                        _(
                        'Tartube database \'{0}\' can\'t be loaded - another' \
                        + ' instance of Tartube may be using it. If not, you' \
                        + ' can fix this problem by deleting the lockfile' \
                        + ' \'{1}\'',
                        ).format(alt_data_dir, alt_lock_file_path),
                    )


    def forget_db(self, data_list):

        """Called by config.SystemPrefWin.on_data_dir_forget_button_clicked().

        When the user selects a data directory to be forgotten (i.e. removed
        from self.data_dir_alt_list), perform that action.

        Args:

            data_list (list): A list containing two items: the full file path
                to the location of the selected data directory, and the system
                preferences window (config.SystemPrefWin) that the user has
                open

        Returns:

            True on success, False on failure

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 5113 forget_db')

        # Extract values from the argument list
        path = data_list.pop(0)
        pref_win_obj = data_list.pop(0)

        # Sanity check. It shouldn't be possible to select the current data
        #   directory, but we'll check anyway
        if self.current_manager_obj \
        or self.disable_load_save_flag \
        or path == self.data_dir:
            return False

        # Update the IV
        if path in self.data_dir_alt_list:
            self.data_dir_alt_list.remove(path)

        # If the system preferences window is open, reset it to show the new
        #   contents of the IV
        if pref_win_obj and pref_win_obj.is_visible():
            pref_win_obj.reset_window()
            pref_win_obj.select_switch_db_tab()

        # Procedure complete
        return True


    def forget_all_db(self, pref_win_obj=None):

        """Called by
        config.SystemPrefWin.on_data_dir_forget_all_button_clicked().

        When the user wants to forget all data directories except the current
        one, perform that action.

        Args:

            pref_win_obj (config.SystemPrefWin): The system preferences window
                that the user has open, if any

        Returns:

            True on success, False on failure

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 5160 forget_all_db')

        # Sanity check
        if self.current_manager_obj or self.disable_load_save_flag:
            return False

        # Update the IV
        self.data_dir_alt_list = [ self.data_dir ]

        # If the system preferences window is open, reset it to show the new
        #   contents of the IV
        if pref_win_obj and pref_win_obj.is_visible():
            pref_win_obj.reset_window()
            pref_win_obj.select_switch_db_tab()

        # Procedure complete
        return True


    def reset_db(self):

        """Called by self.switch_db().

        Resets media registry IVs, so that a new Tartube database file can be
        created.
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 5188 reset_db')

        # Reset IVs to their default states
        self.general_options_obj = options.OptionsManager()
        self.media_reg_count = 0
        self.media_reg_dict = {}
        self.media_name_dict = {}
        self.media_top_level_list = []
        self.media_reg_live_dict = {}
        self.media_reg_auto_notify_dict = {}
        self.media_reg_auto_alarm_dict = {}
        self.media_reg_auto_open_dict = {}
        self.media_reg_auto_dl_start_dict = {}
        self.media_reg_auto_dl_stop_dict = {}
        self.fixed_all_folder = None
        self.fixed_bookmark_folder = None
        self.fixed_fav_folder = None
        self.fixed_live_folder = None
        self.fixed_missing_folder = None
        self.fixed_new_folder = None
        self.fixed_waiting_folder = None
        self.fixed_temp_folder = None
        self.fixed_misc_folder = None

        # Create new fixed folders (which sets the values of
        #   self.fixed_all_folder, etc)
        self.create_fixed_folders()


    def check_integrity_db(self, no_prompt_flag=False):

        """Called by config.SystemPrefWin.on_data_check_button_clicked() and
        also by self.update_db().

        In case the Tartube database contains inconsistencies of any kind (for
        example, an earlier failure in mainwin.DeleteContainerDialogue left
        some channel/playlist/folder objects in a half-deleted state), check
        the database for inconsistencies.

        If inconsistencies are found, prompt the user for permission to
        repair them. The repair process only updates Tartube IVs; it doesn't
        delete any files or folders in the filesystem.

        Args:

            no_prompt_flag (bool): If True, don't prompt the user to repair
                errors; just go ahead and repair them

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 5231 check_integrity_db')

        # Basic checks
        if self.disable_load_save_flag:

            self.system_error(
                106,
                'Cannot check/fix database after load/save has been disabled',
            )

            return

        if self.current_manager_obj:

            self.dialogue_manager_obj.show_msg_dialogue(
                _(
                'Tartube\'s database can\'t be checked while an operation is' \
                + ' in progress',
                ),
                'error',
                'ok',
            )

            return

        # Check the database, looking for: media.Video, media.Channel,
        #   media.Playlist and media.Folder objects (or their .dbids) that,
        #   due to some problem or other, appear in one IV but not another
        # If inconsistencies are found, add them to this dictionary, and
        #   then apply the fixes once we've finished checking everything
        error_reg_dict = {}
        # (Two additional dictionaries for recording any errors in the
        #   .master_dbid and .slave_dbid_list IVs, which are fixed separately)
        error_master_dict = {}
        error_slave_dict = {}

        # Check that entries in self.media_name_dict appear in
        #   self.media_reg_dict
        for dbid in self.media_name_dict.values():
            if not dbid in self.media_reg_dict:
                error_reg_dict[dbid] = None

        # Check that entries in self.media_top_level_list appear in
        #   self.media_reg_dict
        for dbid in self.media_top_level_list:
            if not dbid in self.media_reg_dict:
                error_reg_dict[dbid] = None

        # Check that entries in self.media_reg_live_dict (and its subsets)
        #   appear in self.media_reg_dict
        for dbid in self.media_reg_live_dict.keys():
            if not dbid in self.media_reg_dict:
                error_reg_dict[dbid] = None

        for dbid in self.media_reg_auto_notify_dict.keys():
            if not dbid in self.media_reg_dict:
                error_reg_dict[dbid] = None

        for dbid in self.media_reg_auto_alarm_dict.keys():
            if not dbid in self.media_reg_dict:
                error_reg_dict[dbid] = None

        for dbid in self.media_reg_auto_open_dict.keys():
            if not dbid in self.media_reg_dict:
                error_reg_dict[dbid] = None

        for dbid in self.media_reg_auto_dl_start_dict.keys():
            if not dbid in self.media_reg_dict:
                error_reg_dict[dbid] = None

        for dbid in self.media_reg_auto_dl_stop_dict.keys():
            if not dbid in self.media_reg_dict:
                error_reg_dict[dbid] = None

        # self.media_reg_dict contains, in theory, every video/channel/
        #   playlist/folder object
        # Walk the tree whose top level is self.media_top_level_list to get a
        #   list of all containers
        toplevel_container_obj_list = []
        for dbid in self.media_top_level_list:
            if not dbid in error_reg_dict:
                toplevel_container_obj_list.append(self.media_reg_dict[dbid])

        full_container_obj_list = []
        for container_obj in toplevel_container_obj_list:

            full_container_obj_list.extend(
                container_obj.compile_all_containers( [] ),
            )

        # v2.1.029 In some older databases, a fixed folder called 'downloads_2'
        #   was created, containing a small number of videos. I'm still not
        #   sure under which circumstances that folder was created; in any
        #   case, such a folder should be deleted
        for container_obj in full_container_obj_list:
            if isinstance(container_obj, media.Folder) \
            and container_obj.fixed_flag \
            and not self.check_fixed_folder(container_obj):
                error_reg_dict[container_obj.dbid] = container_obj

        # Make a copy of self.media_reg_dict...
        check_reg_dict = self.media_reg_dict.copy()
        # ...then compare the list of containers (and their child videos),
        #   looking for any which don't appear in self.media_reg_dict
        for container_obj in full_container_obj_list:

            if container_obj.dbid in self.media_reg_dict:

                # Container OK
                if container_obj.dbid in check_reg_dict:
                    del check_reg_dict[container_obj.dbid]

                for child_obj in container_obj.child_list:
                    if isinstance(child_obj, media.Video):

                        if not child_obj.dbid in self.media_reg_dict \
                        or child_obj != self.media_reg_dict[child_obj.dbid]:
                            # Child video not OK
                            error_reg_dict[child_obj.dbid] = child_obj
                        else:
                            # Child video OK
                            if child_obj.dbid in check_reg_dict:
                                del check_reg_dict[child_obj.dbid]

            else:
                # Container not OK
                error_reg_dict[container_obj.dbid] = container_obj

        # Anything left in check_reg_dict shouldn't be there
        for dbid in check_reg_dict:
            error_reg_dict[dbid] = check_reg_dict[dbid]

        # Check every media data object's parent
        for media_data_obj in self.media_reg_dict.values():
            if media_data_obj.parent_obj is not None \
            and (
                not media_data_obj.parent_obj.dbid in self.media_reg_dict \
                or isinstance(media_data_obj.parent_obj, media.Video) \
                or not media_data_obj in media_data_obj.parent_obj.child_list
            ):
                error_reg_dict[media_data_obj.dbid] = media_data_obj

        # Check every media data object's children (but don't check private
        #   folders, as their children are also stored in a different
        #   channel/playlist/folder)
        for media_data_obj in self.media_reg_dict.values():

            if not isinstance(media_data_obj, media.Video) \
            and (
                not isinstance(media_data_obj, media.Folder) \
                or not media_data_obj.priv_flag
            ):
                for child_obj in media_data_obj.child_list:
                    if child_obj.parent_obj is None \
                    or child_obj.parent_obj != media_data_obj:
                        error_reg_dict[child_obj.dbid] = child_obj

        # Check alternative download destinations for each channel/playlist/
        #   folder
        for media_data_obj in self.media_reg_dict.values():
            if not isinstance(media_data_obj, media.Video):

                # (Check the destination still exists in the media data
                #   registry)
                if media_data_obj.master_dbid is not None \
                and not media_data_obj.master_dbid in self.media_reg_dict:

                    error_master_dict[media_data_obj.dbid] = media_data_obj

                for slave_dbid in media_data_obj.slave_dbid_list:
                    if not slave_dbid in self.media_reg_dict:
                        error_slave_dict[media_data_obj.dbid] = media_data_obj

        # Initial check complete. Any media data object in error_reg_dict
        #   must have its children added too (we can't remove an object from
        #   the database, and not its children)
        for dbid in list(error_reg_dict.keys()):

            media_data_obj = error_reg_dict[dbid]
            if media_data_obj is not None \
            and not isinstance(media_data_obj, media.Video):

                descendant_list = media_data_obj.compile_all_containers( [] )
                for descendant_obj in descendant_list:

                    error_reg_dict[descendant_obj.dbid] = descendant_obj
                    for child_obj in descendant_obj.child_list:
                        if isinstance(child_obj, media.Video):
                            error_reg_dict[child_obj.dbid] = child_obj

        # Failsafe check: it shouldn't be possible for system folders to be
        #   in error_reg_dict, but check anyway, and discard them if found
        mod_error_reg_dict = {}
        for dbid in list(error_reg_dict.keys()):

            media_data_obj = error_reg_dict[dbid]

            # (The corresponding media.Video, media.Channel, media.Playlist or
            #   media.Folder may be known, or not)
            if media_data_obj is None \
            or not isinstance(media_data_obj, media.Folder) \
            or not media_data_obj.fixed_flag \
            or not self.check_fixed_folder(media_data_obj):
                mod_error_reg_dict[dbid] = media_data_obj

        # Check complete
        if not mod_error_reg_dict \
        and not error_master_dict \
        and not error_slave_dict:

            if not no_prompt_flag:

                self.dialogue_manager_obj.show_msg_dialogue(
                    _('Database check complete, no inconsistencies found'),
                    'info',
                    'ok',
                )

            return

        elif no_prompt_flag:

            # Don't prompt the user to repair errors; just go ahead and repair
            #   them
            self.fix_integrity_db(
                [
                    mod_error_reg_dict,
                    error_master_dict,
                    error_slave_dict,
                ],
                no_prompt_flag,
            )

        else:

            total = len(error_reg_dict) + len(error_master_dict) \
            + len(error_slave_dict)

            # Prompt the user before deleting stuff
            self.dialogue_manager_obj.show_msg_dialogue(
                _('Database check complete, problems found:') \
                + ' ' + str(total) + '\n\n' \
                + _(
                'Do you want to repair these problems? (The database will be' \
                + ' fixed, but no files will be deleted)',
                ),
                'question',
                'yes-no',
                None,                   # Parent window is main window
                # Arguments passed directly to .fix_integrity_db()
                {
                    'yes': 'fix_integrity_db',
                    'data': [
                        mod_error_reg_dict,
                        error_master_dict,
                        error_slave_dict,
                    ],
                },
            )


    def fix_integrity_db(self, data_list, no_prompt_flag=False):

        """Called by self.check_integrity_db().

        After the user has given permission to fix inconsistencies in the
        Tartube database, perform the repairs, and save files.

        The repair process only updates Tartube IVs; it doesn't delete any
        files or folders in the filesystem.

        Args:

            data_list (list): A list containing three dictionaries; in the
                form:

                error_reg_dict[dbid] = media_data_obj
                error_reg_dict[dbid] = None

                    (A general dictionary of errors to fix. All references to
                    the media data objects in this dictionary are removed from
                    all IVs)

                error_master_dict[dbid] = media_data_obj

                    (A dictionary of errors in a channel/playlist/folder's
                        .master_dbid IV, which are fixed separately)

                error_slave_dict[dbid] = media_data_obj

                    (A dictionary of errors in a channel/playlist/folder's
                        .slave_dbid_list IV, which are fixed separately)

            no_prompt_flag (bool): If True, don't show a dialogue window at
                the end of the procedure

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 5501 fix_integrity_db')

        # Extract the arguments
        error_reg_dict = data_list.pop(0)
        error_master_dict = data_list.pop(0)
        error_slave_dict = data_list.pop(0)

        # Update mainapp.TartubeApp IVs
        for dbid in error_reg_dict.keys():

            # (The corresponding media.Video, media.Channel, media.Playlist or
            #   media.Folder may be known, or not)
            error_obj = error_reg_dict[dbid]

            if dbid in self.media_reg_dict:
                del self.media_reg_dict[dbid]

            if error_obj is not None \
            and error_obj.name in self.media_name_dict:
                del self.media_name_dict[error_obj.name]

            if dbid in self.media_top_level_list:
                self.media_top_level_list.remove(dbid)

            if dbid in self.media_reg_live_dict:
                del self.media_reg_live_dict[dbid]

            if dbid in self.media_reg_auto_notify_dict:
                del self.media_reg_auto_notify_dict[dbid]

            if dbid in self.media_reg_auto_alarm_dict:
                del self.media_reg_auto_alarm_dict[dbid]

            if dbid in self.media_reg_auto_open_dict:
                del self.media_reg_auto_open_dict[dbid]

            if dbid in self.media_reg_auto_dl_start_dict:
                del self.media_reg_auto_dl_start_dict[dbid]

            if dbid in self.media_reg_auto_dl_stop_dict:
                del self.media_reg_auto_dl_stop_dict[dbid]

        # Check each media data object's child list, and remove anything that
        #   should be removed
        for media_data_obj in self.media_reg_dict.values():
            if not isinstance(media_data_obj, media.Video):

                remove_list = []
                for child_obj in media_data_obj.child_list:

                    if child_obj.dbid in error_reg_dict:
                        remove_list.append(child_obj)

                for child_obj in remove_list:
                    media_data_obj.child_list.remove(child_obj)

        # Recalculate counts for all channels/playlists/folders
        for dbid in self.media_name_dict.values():
            media_data_obj = self.media_reg_dict[dbid]
            media_data_obj.recalculate_counts()

        # Deal with alternative download destinations
        for media_data_obj in error_master_dict.values():

            if not media_data_obj.master_dbid in self.media_reg_dict:
                media_data_obj.set_master_dbid(self, media_data_obj.dbid)

        for media_data_obj in error_slave_dict.values():

            del_list = []
            for slave_dbid in media_data_obj.slave_dbid_list:
                if not slave_dbid in self.media_reg_dict:
                    del_list.append(slave_dbid)

            for slave_dbid in del_list:
                media_data_obj.del_slave_dbid(slave_dbid)

        # Save the database file (unless load/save has been disabled very
        #   recently)
        if not self.disable_load_save_flag:
            self.save_db()

        # Redraw the Video Index and Video Catalogue
        self.main_win_obj.video_index_catalogue_reset()

        # Show confirmation (if allowed)
        if not no_prompt_flag:

            self.dialogue_manager_obj.show_msg_dialogue(
                _('Database inconsistencies repaired'),
                'info',
                'ok',
            )


    def auto_delete_old_videos(self):

        """Called by self.load_db().

        After loading the Tartube database, auto-delete any old downloaded
        videos (if auto-deletion is enabled)
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 5603 auto_delete_old_videos')

        if not self.auto_delete_flag:
            return

        # Calculate the system time before which any downloaded videos can be
        #   deleted
        time_limit = int(time.time()) - (self.auto_delete_days * 24 * 60 * 60)

        # Import a list of media data objects (as self.media_reg_dict will be
        #   modified during this procedure)
        media_list = list(self.media_reg_dict.values())

        # Auto-delete any videos as required
        for media_data_obj in media_list:

            if isinstance(media_data_obj, media.Video) \
            and media_data_obj.dl_flag \
            and not media_data_obj.archive_flag \
            and media_data_obj.receive_time < time_limit \
            and (
                not self.auto_delete_watched_flag \
                or not media_data_obj.new_flag
            ):
                # Ddelete this video
                self.delete_video(media_data_obj, True, True, True)


    def convert_version(self, version):

        """Can be called by anything, but mostly called by self.load_config()
        and load_db().

        Converts a Tartube version number, a string in the form '1.234.567',
        into a simple integer in the form 1234567.

        The calling function can then compare the version number for this
        installation of Tartube with the version number that created the file.

        Args:

            version (str): A string in the form '1.234.567'

        Returns:

            The simple integer, or None if the 'version' argument was invalid

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 5653 convert_version')

        num_list = version.split('.')
        if len(num_list) != 3:
            return None
        else:
            return (int(num_list[0]) * 1000000) + (int(num_list[1]) * 1000) \
            + int(num_list[2])


    def find_sound_effects(self):

        """Called by self.start().

        Set the directory in which sound files are stored.

        When installed via PyPI, the files are moved to ../tartube/sounds.

        When installed via a Debian/RPM package, the files are moved to
        /usr/share/tartube/sounds.

        Compiles a list of paths to sound effects found in the /sounds
        directory, and updates the IVs.
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 5679 find_sound_effects')

        sound_dir_list = []
        sound_dir_list.append(
            os.path.abspath(
                os.path.join(self.script_parent_dir, 'sounds'),
            ),
        )

        sound_dir_list.append(
            os.path.abspath(
                os.path.join(
                    os.path.dirname(os.path.realpath(__file__)),
                    'sounds',
                ),
            ),
        )

        sound_dir_list.append(
            os.path.join(
                '/', 'usr', 'share', __main__.__packagename__, 'sounds',
            )
        )

        for sound_dir_path in sound_dir_list:
            if os.path.isdir(sound_dir_path):
                self.sound_dir = sound_dir_path

                # Get a list of available sound files, and sort alphabetically
                for (dirpath, dir_list, file_list) in os.walk(self.sound_dir):
                    for filename in file_list:
                        if filename != 'COPYING':
                            self.sound_list.append(filename)

                self.sound_list.sort()

                return


    def create_fixed_folders(self):

        """Called by self.start() and .reset_db().

        Creates the fixed (system) media.Folder objects that can't be
        destroyed by the user.
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 5727 create_fixed_folders')

        self.fixed_all_folder = self.add_folder(
            formats.FOLDER_ALL_VIDEOS,
            None,           # No parent folder
            False,          # Allow downloads
            True,           # Fixed (folder cannot be removed)
            True,           # Private
            True,           # Can only contain videos
            False,          # Not temporary
        )

        self.fixed_bookmark_folder = self.add_folder(
            formats.FOLDER_BOOKMARKS,
            None,           # No parent folder
            False,          # Allow downloads
            True,           # Fixed (folder cannot be removed)
            True,           # Private
            True,           # Can only contain videos
            False,          # Not temporary
        )

        self.fixed_fav_folder = self.add_folder(
            formats.FOLDER_FAVOURITE_VIDEOS,
            None,           # No parent folder
            False,          # Allow downloads
            True,           # Fixed (folder cannot be removed)
            True,           # Private
            True,           # Can only contain videos
            False,          # Not temporary
        )
        self.fixed_fav_folder.set_fav_flag(True)

        self.fixed_live_folder = self.add_folder(
            formats.FOLDER_LIVESTREAMS,
            None,           # No parent folder
            False,          # Allow downloads
            True,           # Fixed (folder cannot be removed)
            True,           # Private
            True,           # Can only contain videos
            False,          # Not temporary
        )

        self.fixed_missing_folder = self.add_folder(
            formats.FOLDER_MISSING_VIDEOS,
            None,           # No parent folder
            False,          # Allow downloads
            True,           # Fixed (folder cannot be removed)
            True,           # Private
            True,           # Can only contain videos
            False,          # Not temporary
        )

        self.fixed_new_folder = self.add_folder(
            formats.FOLDER_NEW_VIDEOS,
            None,           # No parent folder
            False,          # Allow downloads
            True,           # Fixed (folder cannot be removed)
            True,           # Private
            True,           # Can only contain videos
            False,          # Not temporary
        )

        self.fixed_waiting_folder = self.add_folder(
            formats.FOLDER_WAITING_VIDEOS,
            None,           # No parent folder
            False,          # Allow downloads
            True,           # Fixed (folder cannot be removed)
            True,           # Private
            True,           # Can only contain videos
            False,          # Not temporary
        )

        self.fixed_temp_folder = self.add_folder(
            formats.FOLDER_TEMPORARY_VIDEOS,
            None,           # No parent folder
            False,          # Allow downloads
            True,           # Fixed (folder cannot be removed)
            False,          # Public
            False,          # Can contain any media data object
            True,           # Temporary
        )

        self.fixed_misc_folder = self.add_folder(
            formats.FOLDER_UNSORTED_VIDEOS,
            None,           # No parent folder
            False,          # Allow downloads
            True,           # Fixed (folder cannot be removed)
            False,          # Public
            True,           # Can only contain videos
            False,          # Not temporary
        )


    def rename_fixed_folders(self):

        """Called by self.load_db() (only).

        If the locale used when saving the database file has changed then,
        having loaded the file, we can rename all the fixed folders to match
        the new locale.

        This function must only be called for that reason; fixed folders cannot
        otherwise be renamed.

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 5825 rename_fixed_folders')

        self.rename_fixed_folder(
            self.fixed_all_folder,
            formats.FOLDER_ALL_VIDEOS,
        )

        self.rename_fixed_folder(
            self.fixed_bookmark_folder,
            formats.FOLDER_BOOKMARKS,
        )

        self.rename_fixed_folder(
            self.fixed_fav_folder,
            formats.FOLDER_FAVOURITE_VIDEOS,
        )

        self.rename_fixed_folder(
            self.fixed_live_folder,
            formats.FOLDER_LIVESTREAMS,
        )

        self.rename_fixed_folder(
            self.fixed_missing_folder,
            formats.FOLDER_MISSING_VIDEOS,
        )

        self.rename_fixed_folder(
            self.fixed_new_folder,
            formats.FOLDER_NEW_VIDEOS,
        )

        self.rename_fixed_folder(
            self.fixed_waiting_folder,
            formats.FOLDER_WAITING_VIDEOS,
        )

        self.rename_fixed_folder(
            self.fixed_temp_folder,
            formats.FOLDER_TEMPORARY_VIDEOS,
        )

        self.rename_fixed_folder(
            self.fixed_misc_folder,
            formats.FOLDER_UNSORTED_VIDEOS,
        )


    def rename_fixed_folder(self, media_data_obj, new_name):

        """Called by self.rename_fixed_folders() (only).

        Renames the specified media.Folder object to match the new locale.

        Args:

            media_data_obj (media.Folder): The folder to rename

            new_name (str): The folder's new name, matching (for example)
                formats.FOLDER_ALL_VIDEOS, formats.FOLDER_BOOKMARKS, etc

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 5884 rename_fixed_folder')

        # If there is (by chance) a folder with the same name, it must be
        #   renamed
        if new_name in self.media_name_dict:

            other_dbid = self.media_name_dict[new_name]
            other_obj = self.media_reg_dict[other_dbid]

            # Sanity check: don't rename another fixed folder
            if isinstance(other_obj, media.Folder) and other_obj.fixed_flag:
                return

            # Generate a new name. The -1 argument means to keep going
            #   indefinitely, until an available name is found
            self.rename_container_silently(
                other_obj,
                utils.find_available_name(self, other_obj.name, 2, -1),
            )

        # Now rename the specified folder
        self.rename_container_silently(media_data_obj, new_name)


    def check_fixed_folder(self, media_data_obj):

        """Called by self.check_fixed_folder() or .delete_container().

        Checks whether a specified media data object is one of the eight
        recognised fixed folders (i.e., a system folder that can't be deleted).

        Args:

            media_data_obj (media.Folder): The media data object to test

        Return values:

            True if it's one of the either recognised fixed folders, False
                otherwise

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 5885 check_fixed_folder')

        if media_data_obj is not None \
        and isinstance(media_data_obj, media.Folder) \
        and media_data_obj.fixed_flag \
        and (
            media_data_obj is self.fixed_all_folder \
            or media_data_obj is self.fixed_bookmark_folder \
            or media_data_obj is self.fixed_fav_folder \
            or media_data_obj is self.fixed_live_folder \
            or media_data_obj is self.fixed_missing_folder \
            or media_data_obj is self.fixed_new_folder \
            or media_data_obj is self.fixed_waiting_folder \
            or media_data_obj is self.fixed_temp_folder \
            or media_data_obj is self.fixed_misc_folder
        ):
            return True
        else:
            return False


    def delete_temp_folders(self):

        """Called by self.stop_continue() and self.load_db().

        Deletes the contents of any folders marked temporary, such as the
        'Temporary Videos' folder. (The folders themselves are not deleted).
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 5917 delete_temp_folders')

        # (Must compile a list of top-level container objects first, or Python
        #   will complain about the dictionary changing size)
        obj_list = []
        for dbid in self.media_name_dict.values():
            obj_list.append(self.media_reg_dict[dbid])

        for media_data_obj in obj_list:

            if isinstance(media_data_obj, media.Folder) \
            and media_data_obj.temp_flag:

                # Delete all child objects
                for child_obj in list(media_data_obj.child_list.copy()):
                    if isinstance(child_obj, media.Video):
                        self.delete_video(child_obj)
                    else:
                        self.delete_container(child_obj)

                # Remove files from the filesystem, leaving an empty directory
                dir_path = media_data_obj.get_default_dir(self)
                if os.path.isdir(dir_path):
                    shutil.rmtree(dir_path)

                try:
                    os.makedirs(dir_path)
                except:
                    pass


    def open_temp_folders(self):

        """Called by self.stop_continue().

        Checks all folders marked temporary. Any of them that contain videos
        are opened on the desktop (so the user can more conveniently copy
        things out of them, before they are deleted.)
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 5955 open_temp_folders')

        for dbid in self.media_name_dict.values():
            media_data_obj = self.media_reg_dict[dbid]

            if isinstance(media_data_obj, media.Folder) \
            and media_data_obj.temp_flag \
            and media_data_obj.child_list:

                utils.open_file(media_data_obj.get_default_dir(self))


    def disable_load_save(self, error_msg=None, lock_flag=False):

        """Called by self.load_config(), .save_config(), load_db() and
        .save_db().

        After an error, disables loading/saving, and desensitises many widgets
        in the main window.

        Args:

            error_msg (str or None): An optional error message that can be#
                retrieved later, if required

            lock_flag (bool): True when the error was caused by being unable to
                load a database file because of a lockfile; in which the user
                is prompted if they want to remove it, or not

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 5987 disable_load_save')

        # Ignore subsequent calls to this function; only the initial error
        #   is of interest
        if not self.disable_load_save_flag:

            self.disable_load_save_flag = True
            self.allow_db_save_flag = False
            self.disable_load_save_msg = error_msg
            self.disable_load_save_lock_flag = lock_flag

            if self.main_win_obj is not None:
                self.main_win_obj.sensitise_widgets_if_database(False)


    def remove_db_lock_file(self):

        """Called by self.do_shutdown(), .stop_continue(), .load_db() and
        .switch_db().

        Removes the lockfile protecting the Tartube database file, and updates
        IVs.
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 6012 remove_db_lock_file')

        if self.db_lock_file_path is not None:

            if os.path.isfile(self.db_lock_file_path):
                os.remove(self.db_lock_file_path)

            self.db_lock_file_path = None


    def remove_stale_lock_file(self):

        """Called by self.start() (only), after a call to
        mainwin.RemoveLockFileDialogue.

        The user has confirmed that the lockfile protecting a Tartube database
        file is stale, and can be removed; so remove it.
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 6032 remove_stale_lock_file')

        lock_path = os.path.abspath(
            os.path.join(self.data_dir, self.db_file_name + '.lock'),
        )

        if os.path.exists(lock_path):
            os.remove(lock_path)


    def file_error_dialogue(self, msg):

        """Called by self.start(), .save_config(), load_db() and .save_db().

        After a failure to load/save a file, display a dialogue window if the
        main window is open, or write to the terminal if not.

        Args:

            msg (str): The message to display

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 6056 file_error_dialogue')

        if self.main_win_obj and self.dialogue_manager_obj:
            self.dialogue_manager_obj.show_msg_dialogue(msg, 'error', 'ok')

        else:
            # Main window not open yet, so remove any newline characters
            #   (which look weird when printed to the terminal)
            msg = re.sub(
                r'\n',
                ' ',
                msg,
            )

            print('FILE ERROR: ' + msg)


    def make_directory(self, dir_path):

        """Can be called by anything.

        The call to os.makedirs() might fail with a 'Permission denied' error,
        meaning that the specified directory is unwriteable.

        Convenience function to intercept the error, and display a Tartube
        dialogue instead.

        Args:

            dir_path (str): The path to the directory to be created with a
                call to os.makedirs()

        Returns:

            True if the directory was created, False if not

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 6095 make_directory')

        try:
            os.makedirs(dir_path)
            return True

        except:

            # The True argument tells the dialogue window that it's an
            #   unwriteable directory
            dialogue_win = mainwin.MountDriveDialogue(self.main_win_obj, True)
            dialogue_win.run()
            available_flag = dialogue_win.available_flag
            dialogue_win.destroy()

            return available_flag


    def move_backup_files(self):

        """Called by self.load_db().

        Before v1.3.099, Tartube's data directory used a different structure,
        with the database backup files stored in self.data_dir itself.

        After v1.3.099, they are stored in self.backup_dir.

        The calling function has detected that the old file structure is being
        used. As a convenience to the user, move all the backup files to their
        new location.
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 6128 move_backup_files')

        for filename in os.listdir(path=self.data_dir):
            if re.search(r'^tartube_BU_.*\.db$', filename):

                old_path = os.path.abspath(
                    os.path.join(self.data_dir, filename),
                )

                new_path = os.path.abspath(
                    os.path.join(self.backup_dir, filename),
                )

                shutil.move(old_path, new_path)


    def prompt_on_new_install(self):

        """Called by self.start() when no configuration file exists (meaning
        this is probably a new Tartube installation).

        Called by self.load_config if the config file exists in the Tartube
        directory, but is unreadable (meaning that the user has created a
        blank config file there, in order to force the new Tartube installation
        to use that directory).

        Prompts the user for the location of Tartube's data directory.
        """

        # The main window hasn't been created yet, so create a temporary
        #   fake one (which never becomes visible)
        # (Without a parent window, Gtk will complain at being asked to
        #   create dialogue windows)
        self.fake_main_win_obj = mainwin.FakeMainWin(self)

        # On MS Windows, tell the user that they must set the location of
        #   the data directory, self.data_dir. On other operating systems,
        #   ask the user if they want to use the default location, or
        #   choose a custom one
        if self.notify_user_of_data_dir() \
        and not self.prompt_user_for_data_dir():

            self.disable_load_save(
                _(
                'The user declined to specify a data folder for Tartube',
                ),
            )

        else:

            # All done; create the config file, whether Tartube's data
            #   directory has been changed, or not
            self.save_config()

        # Destroy the fake main window
        self.fake_main_win_obj.destroy()
        self.fake_main_win_obj = None


    def notify_user_of_data_dir(self):

        """Called by self.start().

        On MS Windows, tell the user that they must set the location of the
        Tartube data directory, self.data_dir. On other operating systems, ask
        the user if they want to use the default location, or choose a custom
        one.

        Returns:

            True to choose a custom location for the data directory, False to
                use the default location.

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 6161 notify_user_of_data_dir')

        if os.name == 'nt':

            # On MS Windows, Cygwin creates a Tartube data directory at
            #   C:\msys64\home\USERNAME\tartube-data, which is not very
            #   convenient. Force the user to nominate the directory they want
            dialogue_win = mainwin.SetDirectoryDialogue_MSWin(
                self.fake_main_win_obj,
            )

            dialogue_win.run()
            dialogue_win.destroy()

            return True

        else:

            # On Linux/BSD, offer the user a choice between using the default
            #   data directory specified by self.data_dir, or specifying their
            #   own data directory
            dialogue_win = mainwin.SetDirectoryDialogue_LinuxBSD(
                self.fake_main_win_obj,
                self.data_dir,
            )

            response = dialogue_win.run()

            # Retrieve user choices from the dialogue window, before destroying
            #   it
            custom_flag = False
            if response == Gtk.ResponseType.OK \
            and dialogue_win.button2.get_active():
                custom_flag = True

            dialogue_win.destroy()

            return custom_flag


    def prompt_user_for_data_dir(self):

        """Called by self.start(), immediately after a call to
        self.notify_user_of_data_dir().

        Also called by mainwin.MountDriveDialogue.do_select_dir().

        When Tartube starts for the first time, and the user wants to specify
        a non-default location for Tartube's data directory, prompt the user to
        select/create a directory.

        Returns:

            True if the user selects a location, False if they do not.

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 6219 prompt_user_for_data_dir')

        # If the main window hasn't been created yet, use the fake main
        #   window created by self.start()
        if self.main_win_obj:
            parent_win_obj = self.main_win_obj
        else:
            parent_win_obj = self.fake_main_win_obj

        file_chooser_win = Gtk.FileChooserDialog(
            _('Please select Tartube\'s data folder'),
            parent_win_obj,
            Gtk.FileChooserAction.SELECT_FOLDER,
            (
                Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                Gtk.STOCK_OPEN, Gtk.ResponseType.OK,
            ),
        )

        # Get the user's response
        response = file_chooser_win.run()
        if response == Gtk.ResponseType.OK:

            self.data_dir = file_chooser_win.get_filename()
            self.data_dir_alt_list = [ self.data_dir ]

            self.downloads_dir = os.path.abspath(
                os.path.join(self.data_dir),
            )

            self.alt_downloads_dir = os.path.abspath(
                os.path.join(self.data_dir, 'downloads'),
            )

            self.backup_dir = os.path.abspath(
                os.path.join(self.data_dir, '.backups'),
            )

            self.temp_dir = os.path.abspath(
                os.path.join(self.data_dir, '.temp'),
            )

            self.temp_dl_dir = os.path.abspath(
                os.path.join(self.data_dir, '.temp', 'downloads'),
            )

            self.temp_test_dir = os.path.abspath(
                os.path.join(self.data_dir, '.temp', 'ytdl-test'),
            )

        file_chooser_win.destroy()
        if response == Gtk.ResponseType.OK:

            # Location selected; the remaining code in self.start() will
            #   create the data directory, if necessary
            return True

        else:

            # Location not selected. Tartube will now shut down
            return False


    # (Download/Update/Refresh/Info/Tidy operations)


    def download_manager_start(self, operation_type, \
    automatic_flag=False, media_data_list=[]):

        """Can be called by anything.

        Creates a new downloads.DownloadManager object to handle the download
        operation. When the operation is complete,
        self.download_manager_finished() is called.

        Args:

            operation_type (str): 'sim' if channels/playlists should just be
                checked for new videos, without downloading anything. 'real'
                if videos should be downloaded (or not) depending on each media
                data object's .dl_sim_flag IV. 'custom' is like 'real', but
                with additional options applied (specified by IVs like
                self.custom_dl_by_video_flag). 'classic' if the Classic Mode
                Tab is open, and the user has clicked the download button there

            automatic_flag (bool): True when called by
                self.script_fast_timer_callback() or
                self.script_slow_timer_callback(). If the download operation
                does not start, no dialogue window is displayed (as it normally
                would be)

            media_data_list (list): List of media.Video, media.Channel,
                media.Playlist and/or media.Folder objects. If not an empty
                list, only those media data objects and their descendants are
                checked/downloaded. If an empty list, all media data objects
                are checked/downloaded. If operation_type is 'classic', then
                the media_data_list contains a list of dummy media.Video
                objects from a previous call to this function. If an empty
                list, all dummy media.Video objects are downloaded

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 6322 download_manager_start')

        # The operation may have been scheduled to begin on startup. For
        #   aesthetic reasons, we actually wait a few seconds before
        #   initiatin those operations. If the user starts a download operation
        #   before that happens, then cancel the scheduled one
        self.scheduled_dl_start_check_time = None
        self.scheduled_check_start_check_time = None

        # If a livestream operation is running, tell it to stop immediately
        if self.livestream_manager_obj:
            self.livestream_manager_obj.stop_livestream_operation()

        # If a livestream operation was running, this IV should now be reset
        if self.current_manager_obj:

            # Download/update/refresh/info/tidy operation already in progress
            if not automatic_flag:
                self.system_error(
                    107,
                    'Download, update, refresh, info or tidy operation' \
                    + ' already in progress',
                )

            return

        elif self.main_win_obj.config_win_list:

            # Download operation is not allowed when a configuration window is
            #   open
            if not automatic_flag:
                self.dialogue_manager_obj.show_msg_dialogue(
                    _(
                    'A download operation cannot start if one or more' \
                    + ' configuration windows are still open',
                    ),
                    'error',
                    'ok',
                )

            return

        # If the device containing self.data_dir is running low on space,
        #   warn the user before proceeding
        disk_space = utils.disk_get_free_space(self.data_dir)
        total_space = utils.disk_get_total_space(self.data_dir)

        if (
            self.disk_space_stop_flag \
            and self.disk_space_stop_limit != 0 \
            and disk_space <= self.disk_space_stop_limit
        ) or disk_space < self.disk_space_abs_limit:

            # Refuse to proceed with the operation
            if not automatic_flag:
                self.dialogue_manager_obj.show_msg_dialogue(
                    _(
                    'You only have {0} / {1} Mb remaining on your device',
                    ).format(str(disk_space), str(total_space)),
                )

            return

        elif self.disk_space_warn_flag \
        and self.disk_space_warn_limit != 0 \
        and disk_space <= self.disk_space_warn_limit:

            if automatic_flag:

                # Don't perform a schedules download operation if disk space is
                #   below the limit at which a warning would normally be issued
                return

            else:

                # Warn the user that their free disk space is running low, and
                #   get confirmation before starting the download operation
                self.dialogue_manager_obj.show_msg_dialogue(
                    _(
                    'You only have {0} / {1} Mb remaining on your device',
                    ).format(str(disk_space), str(total_space)) \
                    + '\n\n' \
                    + _('Are you sure you want to continue?'),
                    'question',
                    'yes-no',
                    None,                   # Parent window is main window
                    # Arguments passed directly to .download_manager_continue()
                    {
                        'yes': 'download_manager_continue',
                        'data': [
                            operation_type,
                            automatic_flag,
                            media_data_list,
                        ],
                    },
                )

        else:

            # Start the download operation immediately
            self.download_manager_continue(
                [operation_type, automatic_flag, media_data_list],
            )


    def download_manager_continue(self, arg_list):

        """Called by self.download_manager_start() and
        .update_manager_finished().

        Having obtained confirmation from the user (if required), start the
        download operation.

        Args:

            arg_list (list): List of arguments originally supplied to
                self.download_manager_start(). A list in the form

                    [ operation_type, automatic_flag, media_data_list ]

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 6445 download_manager_continue')

        # Extract arguments from arg_list
        operation_type = arg_list.pop(0)
        automatic_flag = arg_list.pop(0)
        media_data_list = arg_list.pop(0)

        # When not called by the Classic Mode Tab:
        #
        # The media data registry consists of a collection of media data
        #   objects (media.Video, media.Channel, media.Playlist and
        #   media.Folder)
        # If a list of media data objects was specified by the calling
        #   function, those media data object and all of their descendants are
        #   are assigned a downloads.DownloadItem object
        # Otherwise, all media data objects are assigned a
        #   downloads.DownloadItem object
        # Those downloads.DownloadItem objects are collectively stored in a
        #   downloads.DownloadList object
        #
        # When called by the Classic Mode Tab:
        #
        # The user has added one or more URLs to the tab's download list and,
        #   in response, Tartube has created a number of dummy media.Video
        #   objects (which have not been added to the media data registry).
        #   Each dummy object corresponds to a single URL (which might
        #   represent a video, channel or playlist)
        # If a list of dummy media.Video objects was specified by the calling
        #   function, they are downloaded. Otherwise all dummy media.Video
        #   objects are downloaded
        download_list_obj = downloads.DownloadList(
            self,
            operation_type,
            media_data_list,
        )

        if not download_list_obj.download_item_list:

            if not automatic_flag:
                if operation_type == 'sim':
                    msg = _('There is nothing to check!')
                else:
                    msg = _('There is nothing to download!')

                self.dialogue_manager_obj.show_msg_dialogue(msg, 'error', 'ok')

            return

        # If the flag is set, do an update operation before starting the
        #   download operation
        if self.operation_auto_update_flag and not self.operation_waiting_flag:

            self.update_manager_start('ytdl')
            # These IVs tells self.update_manager_finished to start a download
            #   operation
            self.operation_waiting_flag = True
            self.operation_waiting_type = operation_type
            self.operation_waiting_list = media_data_list
            return

        # For the benefit of future scheduled download operations, set the
        #   time at which this operation began
        if not media_data_list:
            if operation_type == 'sim':
                self.scheduled_check_last_time = int(time.time())
            else:
                self.scheduled_dl_last_time = int(time.time())

        # If Tartube should shut down after this download operation, set a
        #   flag that self.download_manager_finished() can check
        if automatic_flag:
            if self.scheduled_shutdown_flag:
                self.halt_after_operation_flag = True
            else:
                self.no_dialogue_this_time_flag = True

        # During a download operation, show a progress bar in the Videos Tab
        #   (except when launched from the Classic Mode Tab, in which case we
        #   just desensitise the existing buttons)
        if operation_type != 'classic':
            if operation_type == 'sim':
                self.main_win_obj.show_progress_bar('check')
            else:
                self.main_win_obj.show_progress_bar('download')
        else:
            self.main_win_obj.sensitise_progress_bar(False)

        # Reset the Progress List
        self.main_win_obj.progress_list_reset()
        # Reset the Results List
        self.main_win_obj.results_list_reset()
        # Reset the Output Tab
        self.main_win_obj.output_tab_reset_pages()

        if operation_type != 'classic':

            # Initialise the Progress List with one row for each media data
            #   object in the downloads.DownloadList object
            # (The Classic Progress List, if in use, has already been
            #   initialised)
            self.main_win_obj.progress_list_init(download_list_obj)

        # (De)sensitise other widgets, as appropriate
        self.main_win_obj.sensitise_operation_widgets(False)
        # Make the widget changes visible
        self.main_win_obj.show_all()

        # During a download operation, a GObject timer runs, so that the
        #   Progress Tab and Output Tab can be updated at regular intervals
        # There is also a delay between the instant at which youtube-dl reports
        #   a video file has been downloaded, and the instant at which it
        #   appears in the filesystem. The timer checks for newly-existing
        #   files at regular intervals, too
        # (When called from the Classic Mode Tab, we use a similar GObject
        #   timer that updates only the list in that tab)
        #
        # Create the timer
        self.dl_timer_id = GObject.timeout_add(
            self.dl_timer_time,
            self.dl_timer_callback,
        )

        # Initiate the download operation. Any code can check whether a
        #   download, update or refresh operation is in progress, or not, by
        #   checking this IV
        self.current_manager_obj = downloads.DownloadManager(
            self,
            operation_type,
            download_list_obj,
        )
        self.download_manager_obj = self.current_manager_obj

        # Update the status icon in the system tray
        self.status_icon_obj.update_icon()


    def download_manager_halt_timer(self):

        """Called by downloads.DownloadManager.run() when that function has
        finished.

        During a download operation, a GObject timer was running. Let it
        continue running for a few seconds more.
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 6591 download_manager_halt_timer')

        if self.dl_timer_id:
            self.dl_timer_check_time \
            = int(time.time()) + self.dl_timer_final_time


    def download_manager_finished(self):

        """Called by self.dl_timer_callback() and
        downloads.DownloadManager.run().

        The download operation has finished, so update IVs and main window
        widgets.
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 6608 download_manager_finished')

        # This function behaves differently, if the download operation was
        #   launched from the Classic Mode Tab
        if self.download_manager_obj.operation_type != 'classic':
            classic_mode_flag = False
        else:
            classic_mode_flag = True

        # Get the time taken by the download operation, so we can convert it
        #   into a nice string below (e.g. '05:15')
        # For refresh operations, RefreshManager.stop_time() might not have
        #   been set at this point (for some reason), so we need to check for
        #   the equivalent problem
        if self.download_manager_obj.stop_time is not None:
            time_num = int(
                self.download_manager_obj.stop_time \
                - self.download_manager_obj.start_time
            )
        else:
            time_num = int(time.time() - self.download_manager_obj.start_time)

        # Any code can check whether a download/update/refresh/info/tidy
        #   operation is in progress, or not, by checking this IV
        self.current_manager_obj = None
        self.download_manager_obj = None

        # Stop the timer and reset IVs
        GObject.source_remove(self.dl_timer_id)
        self.dl_timer_id = None
        self.dl_timer_check_time = None
        # (All videos marked to be launched in the system's default media
        #   player should have been launched already, but just to be safe,
        #   empty this list)
        self.watch_after_dl_list = []

        # After a download operation, save files, if allowed (but don't bother
        #   when launched from the Classic Mode Tab)
        if not classic_mode_flag and self.operation_save_flag:
            self.save_config()
            self.save_db()

        # After a download operation, update the status icon in the system tray
        self.status_icon_obj.update_icon()

        if not classic_mode_flag:

            # Remove the progress bar in the Videos Tab
            self.main_win_obj.hide_progress_bar()

            # If remaining lines in the Progress List should be hidden, hide
            #   them
            if self.progress_list_hide_flag:
                self.main_win_obj.progress_list_check_hide_rows(True)

        else:

            # No progress bar exists; just resensitise the existing buttons
            self.main_win_obj.sensitise_progress_bar(True)

        # (De)sensitise other widgets, as appropriate
        self.main_win_obj.sensitise_operation_widgets(True)
        # Make the widget changes visible (not necessary if the main window has
        #   been closed to the system tray)
        if self.main_win_obj.is_visible():
            self.main_win_obj.show_all()

        # If updates to the Video Index were disabled because of Gtk issues, we
        #   must now redraw the Video Index and Video Catalogue from scratch
        if not classic_mode_flag and self.gtk_emulate_broken_flag:

            # Redraw the Video Index and Video Catalogue, re-selecting the
            #   current selection, if any
            self.main_win_obj.video_index_catalogue_reset(True)

        # If the youtube-dl archive file(s) were temporarily renamed to enable
        #   video(s) to be re-downloaded (by
        #   mainwin.MainWin.on_video_catalogue_re_download() ), restore the
        #   archive file(s) original names
        self.reset_backup_archive()

        # If Tartube is due to shut down, then shut it down
        if self.halt_after_operation_flag:
            self.stop_continue()

        # Otherwise, show a dialogue window or desktop notification, if allowed
        elif not self.no_dialogue_this_time_flag:

            if not self.operation_halted_flag:
                msg = _('Download operation complete')
            else:
                msg = _('Download operation halted')

            if time_num >= 10:
                msg += '\n\n' + _('Time taken:') + ' ' \
                + utils.convert_seconds_to_string(time_num, True)

            if self.operation_dialogue_mode == 'dialogue':
                self.dialogue_manager_obj.show_msg_dialogue(msg, 'info', 'ok')
            elif self.operation_dialogue_mode == 'desktop':
                self.main_win_obj.notify_desktop(None, msg)

        # In any case, reset those IVs
        self.halt_after_operation_flag = False
        self.no_dialogue_this_time_flag = False
        # Also reset operation IVs
        self.operation_halted_flag = False


    def update_manager_start(self, update_type):

        """Can be called by anything.

        Initiates an update operation to do one of two jobs:

        1. Install FFmpeg (on MS Windows only)

        2. Install youtube-dl, or update it to its most recent version.

        Creates a new updates.UpdateManager object to handle the update
        operation. When the operation is complete,
        self.update_manager_finished() is called.

        Args:

            update_type (str): 'ffmpeg' to install FFmpeg, or 'ytdl' to
                install/update youtube-dl

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 6740 update_manager_start')

        # If a livestream operation is running, tell it to stop immediately
        if self.livestream_manager_obj:
            self.livestream_manager_obj.stop_livestream_operation()

        # If a livestream operation was running, this IV should now be reset
        if self.current_manager_obj:

            # Download/update/refresh/info/tidy operation already in progress
            return self.system_error(
                108,
                'Download, update, refresh, info or tidy operation already' \
                + ' in progress',
            )

        elif self.main_win_obj.config_win_list:
            # Update operation is not allowed when a configuration window is
            #   open
            self.dialogue_manager_obj.show_msg_dialogue(
                _(
                'An update operation cannot start if one or more' \
                + ' configuration windows are still open',
                ),
                'error',
                'ok',
            )

            return

        elif __main__.__pkg_strict_install_flag__:
            # Update operation is disabled in the Debian/RPM package. It should
            #   not be possible to call this function, but we'll show an error
            #   message anyway
            return self.system_error(
                109,
                'Update operations are disabled in this version of Tartube',
            )

        elif update_type == 'ffmpeg' and os.name != 'nt':
            # The Update operation can only install FFmpeg on the MS Windows
            #   installation of Tartube. It should not be possible to call this
            #   function, but we'll show an error message anyway
            return self.system_error(
                110,
                'Update operation cannot install FFmpeg on your operating' \
                + ' system',
            )

        # During an update operation, certain widgets are modified and/or
        #   desensitised
        self.main_win_obj.output_tab_reset_pages()
        self.main_win_obj.sensitise_check_dl_buttons(False, update_type)

        # During an update operation, a GObject timer runs, so that the Output
        #   Tab can be updated at regular intervals
        # Create the timer
        self.update_timer_id = GObject.timeout_add(
            self.update_timer_time,
            self.update_timer_callback,
        )

        # Initiate the update operation. Any code can check whether a
        #   download, update or refresh operation is in progress, or not, by
        #   checking this IV
        self.current_manager_obj = updates.UpdateManager(self, update_type)
        self.update_manager_obj = self.current_manager_obj

        # Update the status icon in the system tray
        self.status_icon_obj.update_icon()


    def update_manager_halt_timer(self):

        """Called by updates.UpdateManager.install_ffmpeg() or
        .install_ytdl() when those functions have finished.

        During an update operation, a GObject timer was running. Let it
        continue running for a few seconds more.
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 6822 update_manager_halt_timer')

        if self.update_timer_id:
            self.update_timer_check_time \
            = int(time.time()) + self.update_timer_final_time


    def update_manager_finished(self):

        """Called by self.update_timer_callback().

        The update operation has finished, so update IVs and main window
        widgets.
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 6838 update_manager_finished')

        # Import IVs from updates.UpdateManager, before it is destroyed
        update_type = self.update_manager_obj.update_type
        success_flag = self.update_manager_obj.success_flag
        ytdl_version = self.update_manager_obj.ytdl_version

        # Any code can check whether a download/update/refresh/info/tidy
        #   operation is in progress, or not, by checking this IV
        self.current_manager_obj = None
        self.update_manager_obj = None

        # Stop the timer and reset IVs
        GObject.source_remove(self.update_timer_id)
        self.update_timer_id = None
        self.update_timer_check_time = None

        # After an update operation, save files, if allowed
        if self.operation_save_flag:
            self.save_config()
            self.save_db()

        # During an update operation, certain widgets are modified and/or
        #   desensitised; restore them to their original state
        self.main_win_obj.sensitise_check_dl_buttons(True)
        # Update the status icon in the system tray
        self.status_icon_obj.update_icon()

        # Then show a dialogue window/desktop notification, if allowed (and if
        #   a download operation is not waiting to start)
        if self.operation_dialogue_mode != 'default' \
        and not self.operation_waiting_flag:

            if update_type == 'ffmpeg':

                if not success_flag:
                    msg = _('Installation failed')
                else:
                    msg = _('Installation complete')

            else:
                if not success_flag:
                    msg = _('Update operation failed')
                elif self.operation_halted_flag:
                    msg = _('Update operation halted')
                else:
                    msg = _('Update operation complete') \
                    + '\n\n' + _('youtube-dl version:') + ' '
                    if ytdl_version is not None:
                        msg += ytdl_version
                    else:
                        msg += _('(unknown)')

            if self.operation_dialogue_mode == 'dialogue':
                self.dialogue_manager_obj.show_msg_dialogue(msg, 'info', 'ok')
            elif self.operation_dialogue_mode == 'desktop':
                self.main_win_obj.notify_desktop(None, msg)

        # Reset operation IVs
        self.operation_halted_flag = False

        # If a download operation is waiting to start, start it
        if self.operation_waiting_flag:
            self.download_manager_continue(
                [
                    self.operation_waiting_type,
                    False,
                    self.operation_waiting_list,
                ],
            )

            # Reset those IVs, ready for any future download operations
            self.operation_waiting_flag = False
            self.operation_waiting_type = None
            self.operation_waiting_list = []


    def refresh_manager_start(self, media_data_obj=None):

        """Can be called by anything.

        Initiates a refresh operation to compare Tartube's data directory with
        the media registry, updating the registry as appropriate.

        Creates a new refresh.RefreshManager object to handle the refresh
        operation. When the operation is complete,
        self.refresh_manager_finished() is called.

        Args:

            media_data_obj (media.Channel, media.Playlist, media.Folder or
                None): If specified, only this channel/playlist/folder is
                refreshed. If not specified, the entire media registry is
                refreshed

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 6936 refresh_manager_start')

        # If a livestream operation is running, tell it to stop immediately
        if self.livestream_manager_obj:
            self.livestream_manager_obj.stop_livestream_operation()

        # If a livestream operation was running, this IV should now be reset
        if self.current_manager_obj:
            # Download/update/refresh/info/tidy operation already in progress
            return self.system_error(
                111,
                'Download, update, refresh, info or tidy operation already' \
                + ' in progress',
            )

        elif media_data_obj is not None \
        and isinstance(media_data_obj, media.Video):
            return self.system_error(
                112,
                'Refresh operation cannot be applied to an individual video',
            )

        elif self.main_win_obj.config_win_list:
            # Refresh operation is not allowed when a configuration window is
            #   open
            self.dialogue_manager_obj.show_msg_dialogue(
                _(
                'A refresh operation cannot start if one or more' \
                + ' configuration windows are still open',
                ),
                'error',
                'ok',
            )

            return

        # The user might not be aware of what a refresh operation is, or the
        #   effect it might have on Tartube's database
        # Warn them, and give them the opportunity to back out
        msg = _(
            'During a refresh operation, Tartube analyses its data folder,' \
            + ' looking for videos that haven\'t yet been added to its' \
            + ' database',
        ) + '\n\n' + _(
            'You only need to perform a refresh operation if you have' \
            + ' manually copied videos into Tartube\'s data folder',
        ) + '\n\n'

        if not media_data_obj:

            msg += _(
                'Before starting a refresh operation, you should click the' \
                + ' \'Check all\' button in the main window',
            )

        elif isinstance(media_data_obj, media.Channel):

            msg += _(
                'Before starting a refresh operation, you should right-click' \
                + ' the channel and select \'Check channel\'',
            )

        elif isinstance(media_data_obj, media.Playlist):

            msg += _(
                'Before starting a refresh operation, you should right-click' \
                + ' the playlist and select \'Check playlist\'',
            )

        else:

            msg += _(
                'Before starting a refresh operation, you should right-click' \
                + ' the folder and select \'Check folder\'',
            )

        msg += '\n\n' + _(
            'Are you sure you want to proceed with the refresh operation?',
        )


        self.dialogue_manager_obj.show_msg_dialogue(
            msg,
            'question',
            'yes-no',
            None,                   # Parent window is main window
            # Arguments passed directly to .move_container_to_top_continue()
            {
                'yes': 'refresh_manager_continue',
                'data': media_data_obj,
            },
        )


    def refresh_manager_continue(self, media_data_obj=None):

        """Called by self.refresh_manager_start().

        Having obtained confirmation from the user, start the refresh
        operation.

        Args:

            media_data_obj (media.Channel, media.Playlist, media.Folder or
                None): If specified, only this channel/playlist/folder is
                refreshed. If not specified, the entire media registry is
                refreshed

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 7047 refresh_manager_continue')

        # Because of Gtk stability issues, refresh operations on a channel/
        #   playlist/folder cause frequent crashes. We can work around that by
        #   resetting the Video Index and Video Catalogue
        if self.gtk_emulate_broken_flag:

            # Redraw the Video Index and Video Catalogue
            self.main_win_obj.video_index_catalogue_reset()

        # During a refresh operation, show a progress bar in the Videos Tab
        self.main_win_obj.show_progress_bar('refresh')
        # Reset the Output Tab
        self.main_win_obj.output_tab_reset_pages()
        # (De)sensitise other widgets, as appropriate
        self.main_win_obj.sensitise_operation_widgets(False, True)
        # Make the widget changes visible
        self.main_win_obj.show_all()

        # During a refresh operation, a GObject timer runs, so that the Output
        #   Tab can be updated at regular intervals
        # Create the timer
        self.refresh_timer_id = GObject.timeout_add(
            self.refresh_timer_time,
            self.refresh_timer_callback,
        )

        # Initiate the refresh operation. Any code can check whether a
        #   download, update or refresh operation is in progress, or not, by
        #   checking this IV
        self.current_manager_obj = refresh.RefreshManager(self, media_data_obj)
        self.refresh_manager_obj = self.current_manager_obj

        # Update the status icon in the system tray
        self.status_icon_obj.update_icon()


    def refresh_manager_halt_timer(self):

        """Called by refresh.RefreshManager.run() when that function has
        finished.

        During a refresh operation, a GObject timer was running. Let it
        continue running for a few seconds more.
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 7094 refresh_manager_halt_timer')

        if self.refresh_timer_id:
            self.refresh_timer_check_time \
            = int(time.time()) + self.refresh_timer_final_time


    def refresh_manager_finished(self):

        """Called by self.refresh_timer_callback().

        The refresh operation has finished, so update IVs and main window
        widgets.
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 7110 refresh_manager_finished')

        # Get the time taken by the refresh operation, so we can convert it
        #   into a nice string below (e.g. '05:15')
        # For some reason, RefreshManager.stop_time() might not be set, so we
        #   need to check for that
        if self.refresh_manager_obj.stop_time is not None:
            time_num = int(
                self.refresh_manager_obj.stop_time \
                - self.refresh_manager_obj.start_time
            )
        else:
            time_num = int(time.time() - self.refresh_manager_obj.start_time)

        # Any code can check whether a download/update/refresh/info/tidy
        #   operation is in progress, or not, by checking this IV
        self.current_manager_obj = None
        self.refresh_manager_obj = None

        # Stop the timer and reset IVs
        GObject.source_remove(self.refresh_timer_id)
        self.refresh_timer_id = None
        self.refresh_timer_check_time = None

        # After a refresh operation, save files, if allowed
        if self.operation_save_flag:
            self.save_config()
            self.save_db()

        # Update the status icon in the system tray
        self.status_icon_obj.update_icon()
        # Remove the progress bar in the Videos Tab
        self.main_win_obj.hide_progress_bar()
        # Any remaining messages generated by refresh.RefreshManager should be
        #   shown in the Output Tab immediately
        self.main_win_obj.output_tab_update_pages()
        # (De)sensitise other widgets, as appropriate
        self.main_win_obj.sensitise_operation_widgets(True)
        # Make the widget changes visible (not necessary if the main window has
        #   been closed to the system tray)
        if self.main_win_obj.is_visible():
            self.main_win_obj.show_all()

        # If updates to the Video Index were disabled because of Gtk issues,
        #   we must now redraw the Video Index and Video Catalogue from
        #   scratch
        if self.gtk_emulate_broken_flag:

            # Redraw the Video Index and Video Catalogue
            self.main_win_obj.video_index_catalogue_reset()

        # Then show a dialogue window/desktop notification, if allowed
        if self.operation_dialogue_mode != 'default':

            if not self.operation_halted_flag:
                msg = _('Refresh operation complete')
            else:
                msg = _('Refresh operation halted')

            if time_num >= 10:
                msg += '\n\n' + _('Time taken:') + ' ' \
                + utils.convert_seconds_to_string(time_num, True)

            if self.operation_dialogue_mode == 'dialogue':
                self.dialogue_manager_obj.show_msg_dialogue(msg, 'info', 'ok')
            elif self.operation_dialogue_mode == 'desktop':
                self.main_win_obj.notify_desktop(None, msg)

        # Reset operation IVs
        self.operation_halted_flag = False


    def info_manager_start(self, info_type, media_data_obj=None,
    url_string=None, options_string=None):

        """Can be called by anything.

        Initiates an info operation to do one of three jobs:

        1. Fetch a list of available formats for a video, directly from
            youtube-dl

        2. Fetch a list of available subtitles for a video, directly from
            youtube-dl

        3. Test youtube-dl with specified download options; everything is
            downloaded into a temporary folder

        Creates a new info.InfoManager object to handle the info operation.
        When the operation is complete, self.info_manager_finished() is
        called.

        Args:

            info_type (str): 'formats' to fetch a list of formats, 'subs' to
                fetch a list of subtitles, or 'test_ytdl' to test youtube-dl
                with specified options

            media_data_obj (media.Video): For 'formats' and 'subs', the
                media.Video object for which formats/subtitles should be
                fetched. For 'test_ytdl', set to None

            url_string (str): For 'test_ytdl', the video URL to download (can
                be None or an empty string, if no download is required, for
                example 'youtube-dl --version'. For 'formats' and 'subs',
                set to None

            options_string (str): For 'test_ytdl', a string containing one or
                more youtube-dl download options. The string, generated by a
                Gtk.TextView, typically contains newline and/or multiple
                whitespace characters; the info.InfoManager code deals with
                that. Can be None or an empty string, if no download options
                are required. For 'formats' and 'subs', set to None

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 7227 info_manager_start')

        # If a livestream operation is running, tell it to stop immediately
        if self.livestream_manager_obj:
            self.livestream_manager_obj.stop_livestream_operation()

        # If a livestream operation was running, this IV should now be reset
        if self.current_manager_obj:
            # Download/update/refresh/info/tidy operation already in progress
            return self.system_error(
                113,
                'Download, update, refresh, info or tidy operation already' \
                + ' in progress',
            )

        elif info_type != 'formats' \
        and info_type != 'subs' \
        and info_type != 'test_ytdl':
            # Unrecognised argument
            return self.system_error(
                114,
                'Invalid info operation argument',
            )

        elif media_data_obj is not None \
        and (
            not isinstance(media_data_obj, media.Video)
            or not media_data_obj.source
        ):
            # Unusable media data object
            return self.system_error(
                115,
                'Wrong media data object type or missing source',
            )

        elif self.main_win_obj.config_win_list:

            # Info operation is not allowed when a configuration window is open
            self.dialogue_manager_obj.show_msg_dialogue(
                _(
                'An info operation cannot start if one or more' \
                + ' configuration windows are still open',
                ),
                'error',
                'ok',
            )

            return

        # During an info operation, certain widgets are modified and/or
        #   desensitised
        self.main_win_obj.output_tab_reset_pages()
        self.main_win_obj.sensitise_check_dl_buttons(False, info_type)

        # During an info operation, a GObject timer runs, so that the Output
        #   Tab can be updated at regular intervals
        # Create the timer
        self.info_timer_id = GObject.timeout_add(
            self.info_timer_time,
            self.info_timer_callback,
        )

        # If testing youtube-dl, empty the temporary directory into which
        #   anything is downloaded
        if info_type == 'test_ytdl':

            if os.path.isdir(self.temp_test_dir):
                try:
                    shutil.rmtree(self.temp_test_dir)
                    os.makedirs(self.temp_test_dir)
                except:
                    pass

        # Initiate the info operation. Any code can check whether a
        #   download/update/refresh/info/tidy operation is in progress, or not,
        #   by checking this IV
        self.current_manager_obj = info.InfoManager(
            self,
            info_type,
            media_data_obj,
            url_string,
            options_string,
        )

        self.info_manager_obj = self.current_manager_obj

        # Update the status icon in the system tray
        self.status_icon_obj.update_icon()


    def info_manager_halt_timer(self):

        """Called by info.InfoManager.run() when that function has finished.

        During an info operation, a GObject timer was running. Let it
        continue running for a few seconds more.
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 7326 info_manager_halt_timer')

        if self.info_timer_id:
            self.info_timer_check_time \
            = int(time.time()) + self.info_timer_final_time


    def info_manager_finished(self):

        """Called by self.info_timer_callback().

        The info operation has finished, so update IVs and main window widgets.
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 7341 info_manager_finished')

        # Import IVs from info.InfoManager, before it is destroyed
        info_type = self.info_manager_obj.info_type
        success_flag = self.info_manager_obj.success_flag
        output_list = self.info_manager_obj.output_list.copy()
        url_string = self.info_manager_obj.url_string

        # Any code can check whether a download/update/refresh/info/tidy
        #   operation is in progress, or not, by checking this IV
        self.current_manager_obj = None
        self.info_manager_obj = None

        # Stop the timer and reset IVs
        GObject.source_remove(self.info_timer_id)
        self.info_timer_id = None
        self.info_timer_check_time = None

        # After an info operation, save files, if allowed
        if self.operation_save_flag:
            self.save_config()
            self.save_db()

        # During an info operation, certain widgets are modified and/or
        #   desensitised; restore them to their original state
        self.main_win_obj.sensitise_check_dl_buttons(True)
        # Update the status icon in the system tray
        self.status_icon_obj.update_icon()

        # When testing youtube-dl, and a source URL was specified by the user,
        #   open the temporary directory so the user can see what (if
        #   anything) was downloaded
        if url_string is not None and url_string != '':
             utils.open_file(self.temp_test_dir)

        # Then show a dialogue window/desktop notification, if allowed
        if self.operation_dialogue_mode != 'default':

            if not success_flag:
                msg = _('Operation failed')
            else:
                msg = _('Operation complete')

            msg += '\n\n' + _('Click the Output Tab to see the results')

            if self.operation_dialogue_mode == 'dialogue':
                self.dialogue_manager_obj.show_msg_dialogue(msg, 'info', 'ok')
            elif self.operation_dialogue_mode == 'desktop':
                self.main_win_obj.notify_desktop(None, msg)

        # Reset operation IVs
        self.operation_halted_flag = False


    def tidy_manager_start(self, choices_dict):

        """Can be called by anything.

        Initiates a tidy operation to tidy up the directories used by each of
        one or more media.Channel, media.Playlist and media.Folder objects.
        The tidy-up process consists of one or more of the following jobs:

        1. Check video files are not corrupted (and optionally delete any
            that are)

        2. Check that video files which should exist, actually do (and
            vice-versa)

        3. Delete video files, audio files, description files, metadata (JSON)
            files, annotation files, thumbnail files and/or youtube-dl
            archive files

        Creates a new tidy.TidyManager object to handle the tidy operation.
        When the operation is complete, self.tidy_manager_finished() is
        called.

        Args:

            choices_dict (dict): A dictionary specifying the choices made by
                the user in mainwin.TidyDialogue. The dictionary is in the
                following format:

                media_data_obj: A media.Channel, media.Playlist or media.Folder
                    object, or None if all channels/playlists/folders are to be
                    tidied up. If specified, the channel/playlist/folder and
                    all of its descendants are checked

                corrupt_flag: True if video files should be checked for
                    corruption

                del_corrupt_flag: True if corrupted video files should be
                    deleted

                exist_Flag: True if video files that should exist should be
                    checked, in case they don't (and vice-versa)

                del_video_flag: True if downloaded video files should be
                    deleted

                del_others_flag: True if all video/audio files with the same
                    name should be deleted (as artefacts of post-processing
                    with FFmpeg or AVConv)

                del_descrip_flag: True if all description files should be
                    deleted

                del_json_flag: True if all metadata (JSON) files should be
                    deleted

                del_xml_flag: True if all annotation files should be deleted

                del_thumb_flag: True if all thumbnail files should be deleted

                del_archive_flag: True if all youtube-dl archive files should
                    be deleted

        """


        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 7461 tidy_manager_start')

        # If a livestream operation is running, tell it to stop immediately
        if self.livestream_manager_obj:
            self.livestream_manager_obj.stop_livestream_operation()

        # If a livestream operation was running, this IV should now be reset
        if self.current_manager_obj:
            # Download/update/refresh/info/tidy operation already in progress
            return self.system_error(
                116,
                'Download, update, refresh, info or tidy operation already' \
                + ' in progress',
            )

        elif self.main_win_obj.config_win_list:

            # Tidy operation is not allowed when a configuration window is open
            if not automatic_flag:
                self.dialogue_manager_obj.show_msg_dialogue(
                    _(
                    'A tidy operation cannot start if one or more' \
                    + ' configuration windows are still open',
                    ),
                    'error',
                    'ok',
                )

            return

        # Because of Gtk stability issues, tidy operations on a channel/
        #   playlist/folder cause frequent crashes. We can work around that by
        #   resetting the Video Index and Video Catalogue
        if self.gtk_emulate_broken_flag:

            # Redraw the Video Index and Video Catalogue
            self.main_win_obj.video_index_catalogue_reset()

        # During a tidy operation, show a progress bar in the Videos Tab
        self.main_win_obj.show_progress_bar('tidy')
        # Reset the Output Tab
        self.main_win_obj.output_tab_reset_pages()
        # (De)sensitise other widgets, as appropriate
        self.main_win_obj.sensitise_operation_widgets(False, True)
        # Make the widget changes visible
        self.main_win_obj.show_all()

        # During a tidy operation, a GObject timer runs, so that the Output Tab
        #   can be updated at regular intervals
        # Create the timer
        self.tidy_timer_id = GObject.timeout_add(
            self.tidy_timer_time,
            self.tidy_timer_callback,
        )

        # Initiate the tidy operation. Any code can check whether a
        #   download/update/refresh/info/tidy operation is in progress, or not,
        #   by checking this IV
        self.current_manager_obj = tidy.TidyManager(self, choices_dict)
        self.tidy_manager_obj = self.current_manager_obj

        # Update the status icon in the system tray
        self.status_icon_obj.update_icon()


    def tidy_manager_halt_timer(self):

        """Called by tidy.TidyManager.run() when that function has finished.

        During a tidy operation, a GObject timer was running. Let it continue
        running for a few seconds more.
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 7535 tidy_manager_halt_timer')

        if self.tidy_timer_id:
            self.tidy_timer_check_time \
            = int(time.time()) + self.tidy_timer_final_time


    def tidy_manager_finished(self):

        """Called by self.tidy_timer_callback().

        The tidy operation has finished, so update IVs and main window widgets.
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 7550 tidy_manager_finished')

        # Get the time taken by the tidy operation, so we can convert it into a
        #   nice string below (e.g. '05:15')
        # For some reason, TidyManager.stop_time() might not be set, so we need
        #   to check for that
        if self.tidy_manager_obj.stop_time is not None:
            time_num = int(
                self.tidy_manager_obj.stop_time \
                - self.tidy_manager_obj.start_time
            )
        else:
            time_num = int(time.time() - self.tidy_manager_obj.start_time)

        # Any code can check whether a download/update/refresh/info/tidy
        #   operation is in progress, or not, by checking this IV
        self.current_manager_obj = None
        self.tidy_manager_obj = None

        # Stop the timer and reset IVs
        GObject.source_remove(self.tidy_timer_id)
        self.tidy_timer_id = None
        self.tidy_timer_check_time = None

        # After a tidy operation, save files, if allowed
        if self.operation_save_flag:
            self.save_config()
            self.save_db()

        # Update the status icon in the system tray
        self.status_icon_obj.update_icon()
        # Remove the progress bar in the Videos Tab
        self.main_win_obj.hide_progress_bar()
        # Any remaining messages generated by tidy.TidyManager should be shown
        #   in the Output Tab immediately
        self.main_win_obj.output_tab_update_pages()
        # (De)sensitise other widgets, as appropriate
        self.main_win_obj.sensitise_operation_widgets(True)
        # Make the widget changes visible (not necessary if the main window has
        #   been closed to the system tray)
        if self.main_win_obj.is_visible():
            self.main_win_obj.show_all()

        # If updates to the Video Index were disabled because of Gtk stability
        #   issues, we must now redraw the Video Index and Video Catalogue from
        #   scratch
        if self.gtk_emulate_broken_flag:

            # Redraw the Video Index and Video Catalogue
            self.main_win_obj.video_index_catalogue_reset()

        # ...but if not, the Video Catalogue must be redrawn anyway
        else:
            self.main_win_obj.video_catalogue_redraw_all(
                self.main_win_obj.video_index_current,
            )

        # Show a dialogue window/desktop notification, if allowed
        if self.operation_dialogue_mode != 'default':

            if not self.operation_halted_flag:
                msg = _('Tidy operation complete')
            else:
                msg = _('Tidy operation halted')

            if time_num >= 10:
                msg += '\n\n' + _('Time taken:') + ' ' \
                + utils.convert_seconds_to_string(time_num, True)

            if self.operation_dialogue_mode == 'dialogue':
                self.dialogue_manager_obj.show_msg_dialogue(msg, 'info', 'ok')
            elif self.operation_dialogue_mode == 'desktop':
                self.main_win_obj.notify_desktop(None, msg)

        # Reset operation IVs
        self.operation_halted_flag = False


    def livestream_manager_start(self):

        """Can be called by anything.

        Initiates a livestream operation to check the status of all media.Video
        objects marked as livestreams (everything in self.media_reg_live_dict).

        This is one by telling youtube-dl to fetch the video's JSON data.

        If a waiting livestream has started, the data is received (otherwise an
        error is received).

        If a current livestream has finished, the JSON data will say so.

        Creates a new downloads.LivestreamManager object to handle the
        livestream operation. When the operation is complete,
        self.livestream_manager_finished() is called.

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 7649 livestream_manager_start')

        # Download/update/refresh/info/tidy/livestream operation already in
        #   progress, or a configuration window is open, or there are no
        #   livestreams to check:
        if self.current_manager_obj \
        or self.livestream_manager_obj \
        or self.main_win_obj.config_win_list \
        or not self.media_reg_live_dict:

            # Don't show a dialogue window as we would for other operations, as
            #   the livestream operation occurs silently
            return

        # For the benefit of future scheduled livestream operations, set the
        #   time at which this operation began
        self.scheduled_livestream_last_time = int(time.time())

        # Initiate the livestream operation. Any code can check whether a
        #   download/update/refresh/info/tidy/livestream operation is in
        #   progress, or not, by checking this IV
        # (NB Since livestream operations run silently in the background and
        #   since no functionality is disabled during a livestream operation,
        #   self.current_manager_obj remains set to None)
        self.livestream_manager_obj = downloads.LivestreamManager(self)

        # Update the status icon in the system tray
        self.status_icon_obj.update_icon()


    def livestream_manager_finished(self):

        """Called by downloads.LivestreamManager.run().

        The livestream operation has finished, so update IVs and main window
        widgets.
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 7685 livestream_manager_finished')

        # The operation generated three dictionaries of videos whose livestream
        #   status has changed
        # Before destroying the downloads.LivestreamManager object, import them
        video_started_dict \
        = self.livestream_manager_obj.video_started_dict.copy()
        video_stopped_dict \
        = self.livestream_manager_obj.video_stopped_dict.copy()
        video_missing_dict \
        = self.livestream_manager_obj.video_missing_dict.copy()

        # Any videos marked as missing can be removed from the media registry
        for video_obj in video_missing_dict.values():

            # The True argument tells the function to delete files associated
            #   with the video (the thumbnail, in this case)
            self.delete_video(video_obj, True)

        # Any videos whose livestream status has changed must be redrawn in
        #   the Video catalogue
        if self.main_win_obj.video_index_current \
        == self.fixed_live_folder.name:

            # Livestreams folder visible; just redraw it
            self.main_win_obj.video_catalogue_redraw_all(
                self.fixed_live_folder.name,
            )

        else:

            for video_obj in video_started_dict.values():

                if video_obj.dbid in self.media_reg_dict:
                    self.main_win_obj.video_catalogue_update_row(video_obj)

            for video_obj in video_stopped_dict.values():

                if video_obj.dbid in self.media_reg_dict:
                    self.main_win_obj.video_catalogue_update_row(video_obj)

        # Any code can check whether livestream operation is in progress, or
        #   not, by checking this IV
        self.livestream_manager_obj = None
        # If the automatic sort function in
        #   mainwin.MainWin.video_catalogue_update_row was suppressed, perform
        #   it now
        if self.gtk_emulate_broken_flag:
            self.main_win_obj.catalogue_listbox.invalidate_sort()
            self.main_win_obj.catalogue_listbox.show_all()

        # Update the status icon in the system tray
        self.status_icon_obj.update_icon()

        # Notify the user and/or open videos in the system's web browser, if
        #   a waiting livestream has just gone live (and if allowed to do so)
        for video_obj in video_started_dict.values():

            if video_obj.dbid in self.media_reg_dict:

                # Use the video's thumbnail as the notification icon, if
                #   available (or None, if not, in which case a generic icon is
                #   automatically used)
                if video_obj.dbid in self.media_reg_auto_notify_dict:
                    self.main_win_obj.notify_desktop(
                        _('Livestream has started'),
                        video_obj.name,
                        utils.find_thumbnail(self, video_obj),
                        video_obj.source,
                    )

                if video_obj.dbid in self.media_reg_auto_open_dict \
                and video_obj.source:
                    utils.open_file(video_obj.source)

        # Play a sound effect (but only one) if any waiting livestream has
        #   gone live
        if video_started_dict:
            self.play_sound()

        # If the livestream has just started or just stopped, download it (if
        #   required to do so)
        # First compile a dictionary to eliminate duplicate videos
        dl_dict = {}
        for video_obj in video_started_dict.values():
            if video_obj.dbid in self.media_reg_auto_dl_start_dict:
                dl_dict[video_obj.dbid] = video_obj

        for video_obj in video_stopped_dict.values():
            if video_obj.dbid in self.media_reg_auto_dl_stop_dict:
                dl_dict[video_obj.dbid] = video_obj

                # If the livestream was downloaded when it was still
                #   broadcasting, then a new download must overwrite the
                #   original file
                # As of April 2020, the youtube-dl --yes-overwrites option is
                #   still not available, so as a temporary measure we will
                #   rename the original file (in case the download fails)
                self.prepare_overwrite_video(video_obj)

        # Then download the videos
        if dl_dict:

            if not self.download_manager_obj:

                # Start a new download operation
                self.download_manager_start(
                    'real',
                    False,
                    list(dl_dict.values()),
                )

            else:

                # Download operation already in progress (unlikely, but
                #   possible)
                for video_obj in dl_dict.values():

                    download_item_obj \
                    = self.download_manager_obj.download_list_obj.create_item(
                        video_obj,
                        'real',
                        True,
                    )

                    if download_item_obj:

                        # Add a row to the Progress List
                        self.main_win_obj.progress_list_add_row(
                            download_item_obj.item_id,
                            video_obj,
                        )

                        # Update the main window's progress bar
                        self.download_manager_obj.nudge_progress_bar()


    # (Download operation support functions)

    def create_video_from_download(self, download_item_obj, dir_path, \
    filename, extension, no_sort_flag=False):

        """Called downloads.VideoDownloader.confirm_new_video(),
        .confirm_old_video() and .confirm_sim_video().

        When an individual video has been downloaded, this function is called
        to create a new media.Video object.

        Args:

            download_item_obj (downloads.DownloadItem) - The object used to
                track the download status of a media data object (media.Video,
                media.Channel or media.Playlist)

            dir_path (str): The full path to the directory in which the video
                is saved, e.g. '/home/yourname/tartube/downloads/Videos'

            filename (str): The video's filename, e.g. 'My Video'

            extension (str): The video's extension, e.g. '.mp4'

            no_sort_flag (bool): True when called by
                downloads.VideoDownloader.confirm_sim_video(), because the
                video's parent containers (including the 'All Videos' folder)
                should delay sorting their lists of child objects until that
                calling function is ready. False when called by anything else

        Returns:

            video_obj (media.Video) - The video object created

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 7849 create_video_from_download')

        # The downloads.DownloadItem handles a download for a video, a channel
        #   or a playlist
        media_data_obj = download_item_obj.media_data_obj

        if isinstance(media_data_obj, media.Video):

            # The downloads.DownloadItem object is handling a single video
            video_obj = media_data_obj
            # If the video was added manually (for example, using the 'Add
            #   videos' button), then its filepath won't be set yet
            if not video_obj.file_name:
                video_obj.set_file(filename, extension)

        else:

            # The downloads.DownloadItem object is handling a channel or
            #   playlist
            # Does a media.Video object already exist?
            video_obj = None
            for child_obj in media_data_obj.child_list:

                child_file_dir = None
                if child_obj.file_name is not None:
                    child_file_dir = media_data_obj.get_actual_dir(self)

                if isinstance(child_obj, media.Video) \
                and child_file_dir \
                and child_file_dir == dir_path \
                and child_obj.file_name \
                and child_obj.file_name == filename:
                    video_obj = child_obj

            if video_obj is None:

                # Create a new media data object for the video
                options_manager_obj = download_item_obj.options_manager_obj
                override_name \
                = options_manager_obj.options_dict['use_fixed_folder']
                if override_name is not None \
                and override_name in self.media_name_dict:

                    other_dbid = self.media_name_dict[override_name]
                    other_parent_obj = self.media_reg_dict[other_dbid]

                    video_obj = self.add_video(
                        other_parent_obj,
                        None,
                        False,
                        no_sort_flag,
                    )

                else:
                    video_obj = self.add_video(
                        media_data_obj,
                        None,
                        False,
                        no_sort_flag,
                    )

                # Since we have them to hand, set the video's file path IVs
                #   immediately
                video_obj.set_file(filename, extension)

        # If the video is marked as a livestream, then the livestream has
        #   finished
        if video_obj.live_mode:

            self.mark_video_live(
                video_obj,
                0,                   # Not a livestream
                True,                # Don't update Video Index yet
                True,                # Don't update Video Catalogue yet
                no_sort_flag,
            )

        # If the video is in a channel or a playlist, assume that youtube-dl is
        #   supplying a list of videos in the order of upload, newest first -
        #   in which case, now is a good time to set the video's .receive_time
        #   IV
        # (If not, the IV is set by media.Video.set_dl_flag when the video is
        #   actually downloaded)
        if isinstance(video_obj.parent_obj, media.Channel) \
        or isinstance(video_obj.parent_obj, media.Playlist):
            video_obj.set_receive_time()

        return video_obj


    def convert_video_from_download(self, container_obj, options_manager_obj,
    dir_path, filename, extension, no_sort_flag=False):

        """Called downloads.VideoDownloader.confirm_new_video() and
        .confirm_sim_video().

        A modified version of self.create_video_from_download, called when
        youtube-dl is about to download a channel or playlist into a
        media.Video object.

        Args:

            container_obj (media.Folder): The folder into which a replacement
                media.Video object is to be created

            options_manager_obj (options.OptionsManager): The download options
                for this media data object

            dir_path (str): The full path to the directory in which the video
                is saved, e.g. '/home/yourname/tartube/downloads/Videos'

            filename (str): The video's filename, e.g. 'My Video'

            extension (str): The video's extension, e.g. '.mp4'

            no_sort_flag (bool): True when called by
                downloads.VideoDownloader.confirm_sim_video(), because the
                video's parent containers (including the 'All Videos' folder)
                should delay sorting their lists of child objects until that
                calling function is ready. False when called by anything else

        Returns:

            video_obj (media.Video) - The video object created

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 7977 convert_video_from_download')

        # Does the container object already contain this video?
        video_obj = None
        for child_obj in container_obj.child_list:

            child_file_dir = None
            if child_obj.file_dir is not None:
                child_file_dir = container_obj.get_actual_dir(self)

            if isinstance(child_obj, media.Video) \
            and child_file_dir \
            and child_file_dir == dir_path \
            and child_obj.file_name \
            and child_obj.file_name == filename:
                video_obj = child_obj

        if video_obj is None:

            # Create a new media data object for the video
            override_name \
            = options_manager_obj.options_dict['use_fixed_folder']
            if override_name is not None \
            and override_name in self.media_name_dict:

                other_dbid = self.media_name_dict[override_name]
                other_container_obj = self.media_reg_dict[other_dbid]

                video_obj = self.add_video(
                    other_container_obj,
                    None,
                    False,
                    no_sort_flag,
                )

            else:
                video_obj = self.add_video(
                    container_obj,
                    None,
                    False,
                    no_sort_flag,
                )

            # Since we have them to hand, set the video's file path IVs
            #   immediately
            video_obj.set_file(filename, extension)

        return video_obj


    def announce_video_download(self, download_item_obj, video_obj, \
    keep_description=None, keep_info=None, keep_annotations=None,
    keep_thumbnail=None):

        """Called by downloads.VideoDownloader.confirm_new_video(),
        .confirm_old_video() and .confirm_sim_video().

        Updates the main window.

        Args:

            download_item_obj (downloads.DownloadItem): The download item
                object describing the URL from which youtube-dl should download
                video(s).

            video_obj (media.Video): The video object for the downloaded video

            keep_description (True, False, None):
            keep_info (True, False, None):
            keep_annotations (True, False, None):
            keep_thumbnail (True, False, None):
                Settings from the options.OptionsManager object used to
                    download the video (set to 'None' for a simulated download)

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 8054 announce_video_download')

        # If the video's parent media data object (a channel, playlist or
        #   folder) is selected in the Video Index, update the Video Catalogue
        #   for the downloaded video
        self.main_win_obj.video_catalogue_update_row(video_obj)

        # Update the Results List
        self.main_win_obj.results_list_add_row(
            download_item_obj,
            video_obj,
            keep_description,
            keep_info,
            keep_annotations,
            keep_thumbnail,
        )


    def create_livestream_from_download(self, container_obj, live_mode,
    video_name, video_source, video_descrip, video_upload_time):

        """Called by downloads.JSONFetcher.do_fetch().

        A modified form of self.create_video_from_download(), called at the end
        of a download operation when the RSS feed for a channel or playlist is
        checked, and contains an unfamiliar video (indicating that it's a
        livestream).

        Creates a new media.Video object for the livestream.

        Args:

            containe_obj (media.Channel or media.Playlist): The channel or
                playlist in which a livestream has been detected

            live_mode (int): Matches media.Video.live_mode: 1 for a waiting
                livestream, 2 for a livestream that has started

            video_name, video_source, video_descrip (str): Information about
                the detected livestream, grabbed from the RSS feed itself

            video_upload_time (int): The video's upload time (in Unix time, to
                match media.Video.upload_time)

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 8101 create_livestream_from_download')

        # Fetch the options.OptionsManager object that applies to the container
        options_manager_obj = utils.get_options_manager(self, container_obj)

        # Create a new media data object for the video
        override_name = options_manager_obj.options_dict['use_fixed_folder']
        if override_name is not None and override_name in self.media_name_dict:

            other_dbid = self.media_name_dict[override_name]
            container_obj = self.media_reg_dict[other_dbid]

        video_obj = self.add_video(
            container_obj,
            video_source,
            False,              # Not a simulated download
            True,               # Let the calling function sort the container
        )

        # Update its IVs
        video_obj.set_receive_time()
        video_obj.set_name(video_name)
        video_obj.set_nickname(video_name)
        video_obj.set_video_descrip(
            video_descrip,
            self.main_win_obj.descrip_line_max_len,
        )
        video_obj.set_upload_time(video_upload_time)

        # Give it a fake filename/extension, so that the Video Catalogue can
        #   find the thumbnail
        # (If a youtube-dl output template is applied, the file that might be
        #   downloaded later will have a modified name and/or extension)
        video_obj.set_file(video_name, '.mp4')

        # Mark it as a livestream
        self.mark_video_live(video_obj, live_mode)

        # We can now sort the parent containers
        video_obj.parent_obj.sort_children()
        self.fixed_all_folder.sort_children()
        self.fixed_live_folder.sort_children()


    def update_video_when_file_found(self, video_obj, video_path, temp_dict, \
    mkv_flag=False):

        """Called by mainwin.MainWin.results_list_update_row().

        When youtube-dl reports it is finished, there is a short delay before
        the final downloaded video(s) actually exist in the filesystem.

        Once the calling function has confirmed the file exists, it calls this
        function to update the media.Video object's IVs.

        Args:

            video_obj (media.Video): The video object to update

            video_path (str): The full filepath to the video file that has been
                confirmed to exist

            temp_dict (dict): Dictionary of values used to update the video
                object, in the form:

                'video_obj': not required by this function, as we already have
                    it
                'row_num': not required by this function
                'keep_description', 'keep_info', 'keep_annotations',
                    'keep_thumbnail': flags from the options.OptionsManager
                    object used for to download the video (not added to the
                    dictionary at all for simulated downloads)

            mkv_flag (bool): If the warning 'Requested formats are incompatible
                for merge and will be merged into mkv' has been seen, the
                calling function has found an .mkv file rather than the .mp4
                file it was expecting, and has set this flag to True

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 8182 update_video_when_file_found')

        # Only set the .name IV if the video is currently unnamed
        if video_obj.name == self.default_video_name:
            video_obj.set_name(video_obj.file_name)
            # (The video's title, stored in the .nickname IV, will be updated
            #   from the JSON data in a momemnt)
            video_obj.set_nickname(video_obj.file_name)

        # If it's an .mkv file because of a failed merge, update the IV
        if mkv_flag:
            video_obj.set_mkv()

        # Set the file size
        video_obj.set_file_size(os.path.getsize(video_path))

        # If the JSON file was downloaded, we can extract video statistics from
        #   it
        self.update_video_from_json(video_obj)

        # For any of those statistics that haven't been set (because the JSON
        #   file was missing or didn't contain the right statistics), set them
        #   directly
        self.update_video_from_filesystem(video_obj, video_path)

        # Delete the description, JSON, annotations and thumbnail files, if
        #   required to do so
        if 'keep_description' in temp_dict \
        and not temp_dict['keep_description']:

            old_path = video_obj.get_actual_path_by_ext(self, '.description')

            if os.path.isfile(old_path):
                utils.convert_path_to_temp(
                    self,
                    old_path,
                    True,               # Move the file
                )

        if 'keep_info' in temp_dict and not temp_dict['keep_info']:

            old_path = video_obj.get_actual_path_by_ext(self, '.info.json')

            if os.path.isfile(old_path):
                utils.convert_path_to_temp(
                    self,
                    old_path,
                    True,               # Move the file
                )

        if 'keep_annotations' in temp_dict \
        and not temp_dict['keep_annotations']:

            old_path = video_obj.get_actual_path_by_ext(
                self,
                '.annotations.xml',
            )

            if os.path.isfile(old_path):
                utils.convert_path_to_temp(
                    self,
                    old_path,
                    True,               # Move the file
                )

        if 'keep_thumbnail' in temp_dict and not temp_dict['keep_thumbnail']:

            old_path = utils.find_thumbnail(self, video_obj)

            if old_path is not None:
                utils.convert_path_to_temp(
                    self,
                    old_path,
                    True,               # Move the file
                )

        # Mark the video as (fully) downloaded (and update everything else)
        self.mark_video_downloaded(video_obj, True)

        # Register the video's size with the download manager, so that disk
        #   space limits can be applied, if required
        if self.download_manager_obj and video_obj.dl_flag:
            self.download_manager_obj.register_video_size(video_obj.file_size)

        # If required, launch this video in the system's default media player
        if video_obj in self.watch_after_dl_list:

            self.watch_after_dl_list.remove(video_obj)
            self.watch_video_in_player(video_obj)
            self.mark_video_new(video_obj, False)
            if video_obj.waiting_flag:
                self.mark_video_waiting(video_obj, False)


    def announce_video_clone(self, video_obj):

        """Called by downloads.VideoDownloader.confirm_old_video().

        This is a modified version of self.update_video_when_file_found(),
        called when a channel/playlist/folder is using an alternative
        download destination for its videos (in which case,
        self.update_video_when_file_found() can't be called).

        Args:

            video_obj (media.Video): The video which already exists on the
                user's filesystem (in the alternative download destination)

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 8293 announce_video_clone')

        video_path = video_obj.get_actual_path(self)

        # Only set the .name IV if the video is currently unnamed
        if video_obj.name == self.default_video_name:
            video_obj.set_name(video_obj.file_name)
            # (The video's title, stored in the .nickname IV, will be updated
            #   from the JSON data in a momemnt)
            video_obj.set_nickname(video_obj.file_name)

        # Set the file size
        video_obj.set_file_size(os.path.getsize(video_path))

        # If the JSON file was downloaded, we can extract video statistics from
        #   it
        self.update_video_from_json(video_obj)

        # For any of those statistics that haven't been set (because the JSON
        #   file was missing or didn't contain the right statistics), set them
        #   directly
        self.update_video_from_filesystem(video_obj, video_path)

        # Mark the video as (fully) downloaded (and update everything else)
        self.mark_video_downloaded(video_obj, True)


    def update_video_from_json(self, video_obj):

        """Called by self.update_video_when_file_found(),
        .announce_video_clone() and
        refresh.RefreshManager.refresh_from_default_destination().

        If a video's JSON file exists, extract video statistics from it, and
        use them to update the video object.

        Args:

            video_obj (media.Video): The video object to update

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 8336 update_video_from_json')

        json_path = video_obj.get_actual_path_by_ext(self, '.info.json')

        if os.path.isfile(json_path):

            json_dict = self.file_manager_obj.load_json(json_path)

            if 'title' in json_dict:
                video_obj.set_nickname(json_dict['title'])

            if 'upload_date' in json_dict:
                # date_string in form YYYYMMDD
                date_string = json_dict['upload_date']
                dt_obj = datetime.datetime.strptime(date_string, '%Y%m%d')
                video_obj.set_upload_time(dt_obj.timestamp())

            if 'duration' in json_dict:
                video_obj.set_duration(json_dict['duration'])

            if 'webpage_url' in json_dict:
                video_obj.set_source(json_dict['webpage_url'])

            if 'description' in json_dict:
                video_obj.set_video_descrip(
                    json_dict['description'],
                    self.main_win_obj.descrip_line_max_len,
                )


    def update_video_from_filesystem(self, video_obj, video_path):

        """Called by self.update_video_when_file_found(),
        .announce_video_clone() and
        refresh.RefreshManager.refresh_from_default_destination().

        If a video's JSON file does not exist, or did not contain the
        statistics we were looking for, we can set some of them directly from
        the filesystem.

        Args:

            video_obj (media.Video): The video object to update

            video_path (str): The full path to the video's file

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 8385 update_video_from_filesystem')

        if video_obj.upload_time is None:
            video_obj.set_upload_time(os.path.getmtime(video_path))

        if video_obj.duration is None \
        and HAVE_MOVIEPY_FLAG \
        and self.use_module_moviepy_flag:

            # When the video file is corrupted, moviepy freezes indefinitely
            # Instead, let's try placing the procedure inside a thread (unless
            #   the user has specified a timeout of zero; in which case, don't
            #   use a thread and let moviepy freeze indefinitely)
            if not self.refresh_moviepy_timeout:

                clip = moviepy.editor.VideoFileClip(video_path)
                video_obj.set_duration(clip.duration)

            else:

                this_thread = threading.Thread(
                    target=self.set_duration_from_moviepy,
                    args=(video_obj, video_path,),
                )

                this_thread.daemon = True
                this_thread.start()
                this_thread.join(self.refresh_moviepy_timeout)
                if this_thread.is_alive():
                    self.system_error(
                        117,
                        '\'' + video_obj.parent_obj.name \
                        + '\': moviepy module failed to fetch duration' \
                        + ' of video \'' + video_obj.name + '\'',
                    )

        # (Can't set the video source directly)

        if video_obj.descrip is None:
            video_obj.read_video_descrip(
                self,
                self.main_win_obj.descrip_line_max_len,
            )


    def set_duration_from_moviepy(self, video_obj, video_path):

        """Called by self.update_video_from_filesystem().

        When we call moviepy.editor.VideoFileClip() on a corrupted video file,
        moviepy freezes indefinitely.

        This function is called inside a thread, so a timeout of (by default)
        ten seconds can be applied.

        Args:

            video_obj (media.Video): The video object being updated

            video_path (str): The path to the video file itself

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 8449 set_duration_from_moviepy')

        try:
            clip = moviepy.editor.VideoFileClip(video_path)
            video_obj.set_duration(clip.duration)
        except:
            self.system_error(
                118,
                '\'' + video_obj.parent_obj.name + '\': moviepy module' \
                + 'failed to fetch duration of video \'' \
                + video_obj.name + '\'',
            )


    def prepare_overwrite_video(self, video_obj):

        """Called by self.livestream_manager_finished() and
        mainwin.MainWin.on_click_watch_player_label().

        If the specified video is a livestream that was downloaded when it was
        still broadcasting, then a new download must overwrite the original
        file.

        As of April 2020, the youtube-dl --yes-overwrites option is still not
        available, so as a temporary measure we will rename the original file
        (in case the download fails).

        Args:

            video_obj (media.Video): The video which this function assumes is
                (or was) a livestream

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 8484 prepare_overwrite_video')

        path = os.path.abspath(
            os.path.join(
                video_obj.parent_obj.get_actual_dir(self),
                video_obj.file_name + video_obj.file_ext,
            ),
        )

        bu_path = path + '_BU'

        if os.path.isfile(path):

            # (On MSWin, can't do os.rename if the destination file already
            #   exists)
            if os.path.isfile(bu_path):
                os.remove(bu_path)

            # (os.rename sometimes fails on external hard drives; this is safer
            shutil.move(path, bu_path)


    def set_backup_archive(self, dir_path):

        """Called by mainwin.MainWin.on_video_catalogue_re_download().

        If self.allow_ytdl_archive_flag is set, youtube-dl will have created a
        ytdl_archive.txt, recording every video ever downloaded in the parent
        directory.

        This will prevent a successful re-downloading of the video.

        Change the name of the archive file temporarily. After the download
        operation is complete, self.reset_backup_archive() is called to
        restore its original name.

        Args:

            dir_path (str): The full path to the directory containing the
                video(s) to be re-downloaded

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 8528 set_backup_archive')

        archive_path = os.path.abspath(
            os.path.join(dir_path, 'ytdl-archive.txt'),
        )

        if os.path.isfile(archive_path) \
        and not archive_path in self.ytdl_archive_path_list:

            bu_path = os.path.abspath(
                os.path.join(dir_path, 'bu_archive.txt'),
            )

            # (On MSWin, can't do os.rename if the destination file already
            #   exists)
            if os.path.isfile(bu_path):
                os.remove(bu_path)

            # (os.rename sometimes fails on external hard drives; this is
            #   safer)
            shutil.move(archive_path, bu_path)

            # Store both paths, so self.reset_backup_archive() can retrieve
            #   them
            self.ytdl_archive_path_list.append(archive_path)
            self.ytdl_archive_backup_path_list.append(bu_path)


    def reset_backup_archive(self):

        """Called by self.download_manager_finished().

        If youtube-dl archive file(s) were temporarily renamed (in a call to
        self.set_backup_archive()) in order to enable the video to be
        re-downloaded, then restore the archive files to their original names.
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 8566 reset_backup_archive')

        while self.ytdl_archive_path_list:

            archive_path = self.ytdl_archive_path_list.pop()
            bu_path = self.ytdl_archive_backup_path_list.pop()

            if os.path.isfile(bu_path):

                # (On MSWin, can't do os.rename if the destination file already
                #   exists)
                if os.path.isfile(archive_path):
                    os.remove(archive_path)

                # (os.rename sometimes fails on external hard drives; this is
                #   safer)
                shutil.move(bu_path, archive_path)

        # Regardless of whether backup archive file(s) were created during a
        #   re-download operation, or not, reset the IVs
        self.ytdl_archive_path_list = []
        self.ytdl_archive_backup_path_list = []


    # (Add media data objects)


    def add_video(self, parent_obj, source=None, dl_sim_flag=False,
    no_sort_flag=False):

        """Can be called by anything.

        Creates a new media.Video object, and updates IVs.

        Args:

            parent_obj (media.Channel, media.Playlist or media.Folder): The
                media data object for which the new media.Video object is the
                child (all videos have a parent)

            source (str): The video's source URL, if known

            dl_sim_flag (bool): If True, the video object's .dl_sim_flag IV is
                set to True, which forces simulated downloads

            no_sort_flag (bool): True when
                self.create_video_from_download() is called by
                downloads.VideoDownloader.confirm_sim_video(), because the
                video's parent containers (including the 'All Videos' folder)
                should delay sorting their lists of child objects until that
                calling function is ready. False when called by anything else

        Returns:

            The new media.Video object

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 8625 add_video')

        # Videos can't be placed inside other videos
        if parent_obj and isinstance(parent_obj, media.Video):
            return self.system_error(
                119,
                'Videos cannot be placed inside other videos',
            )

        # Videos can't be added directly to a private folder
        elif parent_obj and isinstance(parent_obj, media.Folder) \
        and parent_obj.priv_flag:
            return self.system_error(
                120,
                'Videos cannot be placed inside a private folder',
            )

        # Create a new media.Video object
        video_obj = media.Video(
            self.media_reg_count,
            self.default_video_name,
            parent_obj,
            None,                   # Use default download options
            no_sort_flag,
        )

        if source is not None:
            video_obj.set_source(source)

        if dl_sim_flag:
            video_obj.set_dl_sim_flag(True)

        # Update IVs
        self.media_reg_count += 1
        self.media_reg_dict[video_obj.dbid] = video_obj

        # The private 'All Videos' folder also has this video as a child object
        self.fixed_all_folder.add_child(video_obj, no_sort_flag)

        # Update the row in the Video Index for both the parent and private
        #   folder
        self.main_win_obj.video_index_update_row_text(video_obj.parent_obj)
        self.main_win_obj.video_index_update_row_text(self.fixed_all_folder)

        # If the video's parent is the one visible in the Video Catalogue (or
        #   if 'Unsorted Videos' or 'Temporary Videos', etc, is the one visible
        #   in the Video Catalogue), the new video itself won't be visible
        #   there yet
        # Make sure the video is visible, if appropriate
        self.main_win_obj.video_catalogue_update_row(video_obj)

        return video_obj


    def add_channel(self, name, parent_obj=None, source=None, \
    dl_sim_flag=None):

        """Can be called by anything.

        Creates a new media.Channel object, and updates IVs.

        Args:

            name (str): The channel name

            parent_obj (media.Folder): The media data object for which the new
                media.Channel object is a child (if any)

            source (str): The channel's source URL, if known

            dl_sim_flag (bool): True if we should simulate downloads for videos
                in this channel, False if we should actually download them
                (when allowed)

        Returns:

            The new media.Channel object

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 8706 add_channel')

        # Channels can only be placed inside an unrestricted media.Folder
        #   object (if they have a parent at all)
        if parent_obj \
        and (
            not isinstance(parent_obj, media.Folder) \
            or parent_obj.restrict_flag
        ):
            return self.system_error(
                121,
                'Channels cannot be added to a restricted folder',
            )

        # There is a limit to the number of levels allowed in the media
        #   registry
        if parent_obj and parent_obj.get_depth() >= self.media_max_level:
            return self.system_error(
                122,
                'Channel exceeds maximum depth of media registry',
            )

        # Some names are not allowed at all
        if name is None \
        or re.match('\s*$', name) \
        or not self.check_container_name_is_legal(name):
            return self.system_error(
                123,
                'Illegal channel name',
            )

        # Create a new media.Channel object
        channel_obj = media.Channel(
            self,
            self.media_reg_count,
            name,
            parent_obj,
            None,                   # Use default download options
        )

        if source is not None:
            channel_obj.set_source(source)

        if dl_sim_flag is not None:
            channel_obj.set_dl_sim_flag(dl_sim_flag)

        # Update IVs
        self.media_reg_count += 1
        self.media_reg_dict[channel_obj.dbid] = channel_obj
        self.media_name_dict[channel_obj.name] = channel_obj.dbid
        if not parent_obj:
            self.media_top_level_list.append(channel_obj.dbid)

        # Create the directory used by this channel (if it doesn't already
        #   exist)
        dir_path = channel_obj.get_default_dir(self)
        if not os.path.exists(dir_path):
            self.make_directory(dir_path)

        return channel_obj


    def add_playlist(self, name, parent_obj=None, source=None, \
    dl_sim_flag=None):

        """Can be called by anything.

        Creates a new media.Playlist object, and updates IVs.

        Args:

            name (str): The playlist name

            parent_obj (media.Folder): The media data object for which the new
                media.Playlist object is a child (if any)

            source (str): The playlist's source URL, if known

            dl_sim_flag (bool): True if we should simulate downloads for videos
                in this playlist, False if we should actually download them
                (when allowed)

        Returns:

            The new media.Playlist object

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 8795 add_playlist')

        # Playlists can only be place inside an unrestricted media.Folder
        #   object (if they have a parent at all)
        if parent_obj \
        and (
            not isinstance(parent_obj, media.Folder) \
            or parent_obj.restrict_flag
        ):
            return self.system_error(
                124,
                'Playlists cannot be added to a restricted folder',
            )

        # There is a limit to the number of levels allowed in the media
        #   registry
        if parent_obj and parent_obj.get_depth() >= self.media_max_level:
            return self.system_error(
                125,
                'Playlist exceeds maximum depth of media registry',
            )

        # Some names are not allowed at all
        if name is None \
        or re.match('\s*$', name) \
        or not self.check_container_name_is_legal(name):
            return self.system_error(
                126,
                'Illegal playlist name',
            )

        # Create a new media.Playlist object
        playlist_obj = media.Playlist(
            self,
            self.media_reg_count,
            name,
            parent_obj,
            None,                   # Use default download options
        )

        if source is not None:
            playlist_obj.set_source(source)

        if dl_sim_flag is not None:
            playlist_obj.set_dl_sim_flag(dl_sim_flag)

        # Update IVs
        self.media_reg_count += 1
        self.media_reg_dict[playlist_obj.dbid] = playlist_obj
        self.media_name_dict[playlist_obj.name] = playlist_obj.dbid
        if not parent_obj:
            self.media_top_level_list.append(playlist_obj.dbid)

        # Create the directory used by this playlist (if it doesn't already
        #   exist)
        dir_path = playlist_obj.get_default_dir(self)
        if not os.path.exists(dir_path):
            self.make_directory(dir_path)

        # Procedure complete
        return playlist_obj


    def add_folder(self, name, parent_obj=None, dl_sim_flag=False,
    fixed_flag=False, priv_flag=False, restrict_flag=False, temp_flag=False):

        """Can be called by anything.

        Creates a new media.Folder object, and updates IVs.

        Args:

            name (str): The folder name

            parent_obj (media.Folder): The media data object for which the new
                media.Channel object is a child (if any)

            dl_sim_flag (bool): If True, the folders .dl_sim_flag IV is set to
                True, which forces simulated downloads for any videos,
                channels or playlists contained in the folder

            fixed_flag, priv_flag, restrict_flag, temp_flag (bool): Flags sent
                to the object's .__init__() function

        Returns:

            The new media.Folder object

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 8886 add_folder')

        # Folders can only be placed inside an unrestricted media.Folder object
        #   (if they have a parent at all)
        if parent_obj \
        and (
            not isinstance(parent_obj, media.Folder) \
            or parent_obj.restrict_flag
        ):
            return self.system_error(
                127,
                'Folders cannot be added to another restricted folder',
            )

        # There is a limit to the number of levels allowed in the media
        #   registry
        if parent_obj and parent_obj.get_depth() >= self.media_max_level:
            return self.system_error(
                128,
                'Folder exceeds maximum depth of media registry',
            )

        # Some names are not allowed at all
        if name is None \
        or re.match('\s*$', name) \
        or not self.check_container_name_is_legal(name):
            return self.system_error(
                129,
                'Illegal folder name',
            )

        folder_obj = media.Folder(
            self,
            self.media_reg_count,
            name,
            parent_obj,
            None,                   # Use default download options
            fixed_flag,
            priv_flag,
            restrict_flag,
            temp_flag,
        )

        if dl_sim_flag:
            folder_obj.set_dl_sim_flag(True)

        # Update IVs
        self.media_reg_count += 1
        self.media_reg_dict[folder_obj.dbid] = folder_obj
        self.media_name_dict[folder_obj.name] = folder_obj.dbid
        if not parent_obj:
            self.media_top_level_list.append(folder_obj.dbid)

        # Create the directory used by this folder (if it doesn't already
        #   exist)
        # Obviously don't do that for private folders
        dir_path = folder_obj.get_default_dir(self)
        if not folder_obj.priv_flag and not os.path.exists(dir_path):
            self.make_directory(dir_path)

        # Procedure complete
        return folder_obj


    # (Move media data objects)


    def move_container_to_top(self, media_data_obj):

        """Called by mainwin.MainWin.on_video_index_move_to_top().

        Before moving a channel, playlist or folder, get confirmation from the
        user.

        After getting confirmation, call self.move_container_to_top_continue()
        to move the channel, playlist or folder to the top level (in other
        words, removes its parent folder).

        Args:

            media_data_obj (media.Channel, media.Playlist, media.Folder): The
                moving media data object

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 8972 move_container_to_top')

        # Do some basic checks
        if media_data_obj is None or isinstance(media_data_obj, media.Video) \
        or self.current_manager_obj or not media_data_obj.parent_obj:
            return self.system_error(
                130,
                'Move container to top request failed sanity check',
            )

        # Check that the target directory doesn't already exist (unlikely, but
        #   possible if the user has been copying files manually)
        target_path = os.path.abspath(
            os.path.join(
                self.downloads_dir,
                media_data_obj.name,
            ),
        )

        if os.path.isdir(target_path) or os.path.isfile(target_path):

            # (The same error message appears in self.move_container() )
            self.dialogue_manager_obj.show_msg_dialogue(
                _('Cannot move anything to:') + '\n\n' + target_path + '\n\n' \
                + _(
                    'because a file or folder with the same name already' \
                    + ' exists (although Tartube\'s database doesn\'t know' \
                    + ' anything about it)',
                ) + '\n\n' + _(
                    + 'You probably created that file/folder accidentally,' \
                    + ' in which case you should delete it manually before' \
                    + ' trying again',
                ),
                'error',
                'ok',
            )

            return

        # Prompt the user for confirmation. If the user clicks 'yes', call
        #   self.move_container_to_top_continue() to complete the move
        media_type = media_data_obj.get_type()
        if media_type == 'channel':
            msg = _('Are you sure you want to move this channel:')
        elif media_type == 'playlist':
            msg = _('Are you sure you want to move this playlist:')
        else:
            msg = _('Are you sure you want to move this folder:')

        msg += '\n\n   ' + media_data_obj.name + '\n\n'

        msg += _(
            + 'This procedure will move all downloaded files to the top' \
            + ' level of Tartube\'s data folder',
        )

        self.dialogue_manager_obj.show_msg_dialogue(
            msg,
            'question',
            'yes-no',
            None,                   # Parent window is main window
            # Arguments passed directly to .move_container_to_top_continue()
            {
                'yes': 'move_container_to_top_continue',
                'data': media_data_obj,
            },
        )


    def move_container_to_top_continue(self, media_data_obj):

        """Called by self.move_container_to_top().

        Moves a channel, playlist or folder to the top level (in other words,
        removes its parent folder).

        Args:

            media_data_obj (media.Channel, media.Playlist, media.Folder): The
                moving media data object

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 9056 move_container_to_top_continue')

        # Move the sub-directories to their new location
        shutil.move(media_data_obj.get_default_dir(self), self.downloads_dir)

        # Update IVs
        media_data_obj.parent_obj.del_child(media_data_obj)
        media_data_obj.set_parent_obj(None)
        self.media_top_level_list.append(media_data_obj.dbid)

        # Save the database (because, if the user terminates Tartube and then
        #   restarts it, then tries to perform a download operation, a load of
        #   Python error messages will be generated, complaining that
        #   directories don't exist)
        self.save_db()

        # Remove the moving object from the Video Index, and put it back there
        #   at its new location
        self.main_win_obj.video_index_delete_row(media_data_obj)
        self.main_win_obj.video_index_add_row(media_data_obj)

        # Select the moving object, which redraws the Video Catalogue
        self.main_win_obj.video_index_select_row(media_data_obj)


    def move_container(self, source_obj, dest_obj):

        """Called by mainwin.MainWin.on_video_index_drag_data_received().

        Before moving a channel, playlist or folder, get confirmation from the
        user.

        After getting confirmation, call self.move_container_continue() to move
        the channel, playlist or folder into another folder.

        Args:

            source_obj (media.Channel, media.Playlist, media.Folder): The
                moving media data object

            dest_obj (media.Folder): The destination folder

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 9101 move_container')

        # Do some basic checks
        if source_obj is None or isinstance(source_obj, media.Video) \
        or dest_obj is None or isinstance(dest_obj, media.Video):
            return self.system_error(
                131,
                'Move container request failed sanity check',
            )

        elif source_obj == dest_obj:
            # No need for a system error message if the user drags a folder
            #   onto itself; just do nothing
            return

        # Ignore Video Index drag-and-drop during an download/update/refresh/
        #   info/tidy operation
        elif self.current_manager_obj:
            return

        elif not isinstance(dest_obj, media.Folder):

            self.dialogue_manager_obj.show_msg_dialogue(
                _(
                'Channels, playlists and folders can only be dragged into' \
                + ' a folder',
                ),
                'error',
                'ok',
            )

            return

        elif isinstance(source_obj, media.Folder) and source_obj.fixed_flag:

            self.dialogue_manager_obj.show_msg_dialogue(
                _(
                'The fixed folder \'{0}\' cannot be moved (but it can still' \
                + ' be hidden)',
                ).format(dest_obj.name),
                'error',
                'ok',
            )

            return

        elif dest_obj.restrict_flag:

            self.dialogue_manager_obj.show_msg_dialogue(
                _(
                'The folder \'{0}\' can only contain videos',
                ).format(dest_obj.name),
                'error',
                'ok',
            )

            return

        # Check that the target directory doesn't already exist (unlikely, but
        #   possible if the user has been copying files manually)
        target_path = os.path.abspath(
            os.path.join(
                dest_obj.get_default_dir(self),
                source_obj.name,
            ),
        )

        if os.path.isdir(target_path) or os.path.isfile(target_path):

            self.dialogue_manager_obj.show_msg_dialogue(
                _('Cannot move anything to:') + '\n\n' + target_path + '\n\n' \
                + _(
                'because a file or folder with the same name already exists' \
                + ' (although Tartube\'s database doesn\'t know anything' \
                + ' about it)',
                ) + '\n\n' \
                + _(
                + 'You probably created that file/folder accidentally, in' \
                + ' which case, you should delete it manually before trying' \
                + ' again',
                ),
                'error',
                'ok',
            )

            return

        # Prompt the user for confirmation
        source_type = source_obj.get_type()
        if source_type == 'channel':
            msg = _('Are you sure you want to move this channel:')
        elif source_type == 'playlist':
            msg = _('Are you sure you want to move this playlist:')
        else:
            msg = _('Are you sure you want to move this folder:')

        msg += '\n\n   ' + source_obj.name + '\n\n' + _('into this folder:') \
            + '\n\n   ' + dest_obj.name + '\n\n'

        msg += _(
            'This procedure will move all downloaded files to the new' \
            + ' location',
        )

        if dest_obj.temp_flag:
            msg = '\n\n' + _(
                'WARNING: The destination folder is marked as temporary, so' \
                + ' everything inside it will be DELETED when Tartube' \
                + ' restarts!',
            )

        # If the user clicks 'yes', call self.move_container_continue() to
        #   complete the move
        self.dialogue_manager_obj.show_msg_dialogue(
            msg,
            'question',
            'yes-no',
            None,                   # Parent window is main window
            # Arguments passed directly to .move_container_continue()
            {
                'yes': 'move_container_continue',
                'data': [source_obj, dest_obj],
            },
        )


    def move_container_continue(self, media_list):

        """Called by self.move_container().

        Moves a channel, playlist or folder into another folder.

        Args:

            media_list (list): List in the form (destination, source), where
                both are media.Folder objects

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 9241 move_container_continue')

        source_obj = media_list[0]
        dest_obj = media_list[1]

        # Move the sub-directories to their new location
        shutil.move(
            source_obj.get_default_dir(self),
            dest_obj.get_default_dir(self),
        )

        # Update both media data objects' IVs
        if source_obj.parent_obj:
            source_obj.parent_obj.del_child(source_obj)

        dest_obj.add_child(source_obj)
        source_obj.set_parent_obj(dest_obj)

        if source_obj.dbid in self.media_top_level_list:
            index = self.media_top_level_list.index(source_obj.dbid)
            del self.media_top_level_list[index]

        # Save the database (because, if the user terminates Tartube and then
        #   restarts it, then tries to perform a download operation, a load of
        #   Python error messages will be generated, complaining that
        #   directories don't exist)
        self.save_db()

        # Remove the moving object from the Video Index, and put it back there
        #   at its new location
        self.main_win_obj.video_index_delete_row(source_obj)
        self.main_win_obj.video_index_add_row(source_obj)
        # Select the moving object, which redraws the Video Catalogue
        self.main_win_obj.video_index_select_row(source_obj)


    # (Convert channels to playlists, and vice-versa)


    def convert_remote_container(self, old_obj):

        """Called by mainwin.MainWin.on_video_index_convert_container().

        Converts a media.Channel object into a media.Playlist object, or vice-
        versa.

        Usually called after the user has copy-pasted a list of URLs into the
        mainwin.AddVideoDialogue window, some of which actually represent
        channels or playlists, not individual videos. During the next
        download operation, new channels or playlists can be automatically
        created (depending on the value of self.operation_convert_mode

        The user can then convert a channel to a playlist, and back again, as
        required.

        Args:

            old_obj (media.Channel, media.Playlist): The media data object to
                convert

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 9304 convert_remote_container')

        if (
            not isinstance(old_obj, media.Channel) \
            and not isinstance(old_obj, media.Playlist)
        ) or self.current_manager_obj:
            return self.system_error(
                132,
                'Convert container request failed sanity check',
            )

        # If old_obj is a media.Channel, create a playlist. If old_obj is
        #   a media.Playlist, create a channel
        if isinstance(old_obj, media.Channel):

            new_obj = self.add_playlist(
                old_obj.name,
                old_obj.parent_obj,
                old_obj.source,
                old_obj.dl_sim_flag,
            )

        elif isinstance(old_obj, media.Playlist):

            new_obj = self.add_channel(
                old_obj.name,
                old_obj.parent_obj,
                old_obj.source,
                old_obj.dl_sim_flag,
            )

        # Move any children from the old object to the new one
        for child_obj in old_obj.child_list:

            # The True argument means to delay sorting the child list
            new_obj.add_child(child_obj, True)
            child_obj.set_parent_obj(new_obj)

        # Deal with alternative download destinations
        if old_obj.master_dbid:
            new_obj.set_master_dbid(self, old_obj.master_dbid)
            master_obj = self.media_reg_dict[old_obj.master_dbid]
            master_obj.del_slave_dbid(old_obj.dbid)

        for slave_dbid in old_obj.slave_dbid_list:
            slave_obj = self.media_reg_dict[slave_dbid]
            slave_obj.set_master_dbid(self, new_obj.dbid)

        # Copy remaining properties from the old object to the new one
        new_obj.clone_properties(old_obj)

        # Remove the old object from the media data registry.
        #   self.media_name_dict should already be updated
        del self.media_reg_dict[old_obj.dbid]
        if old_obj.dbid in self.media_top_level_list:
            self.media_top_level_list.remove(old_obj.dbid)

        # Remove the old object from the Video Index...
        self.main_win_obj.video_index_delete_row(old_obj)
        # ...and add the new one, selecting it at the same time
        self.main_win_obj.video_index_add_row(new_obj)


    # (Delete media data objects)


    def delete_video(self, video_obj, delete_files_flag=False,
    no_update_index_flag=False, no_update_catalogue_flag=False):

        """Can be called by anything.

        Deletes a video object from the media registry.

        Args:

            video_obj (media.Video): The media.Video object to delete

            delete_files_flag (bool): True when called by
                mainwin.MainWin.on_video_catalogue_delete_video, in which case
                the video and its associated files are deleted from the
                filesystem

            no_update_index_flag (bool): True when called by
                self.delete_old_videos() or self.delete_container(), in which
                case the Video Index is not updated

            no_update_catalogue_flag (bool): True when called by
                self.delete_old_videos(), in which case the Video Catalogue is
                not updated

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 9397 delete_video')

        if not isinstance(video_obj, media.Video):
            return self.system_error(
                133,
                'Delete video request failed sanity check',
            )

        # Remove the video from its parent object
        video_obj.parent_obj.del_child(video_obj)

        # Remove the corresponding entry in each private folder's child list
        update_list = [video_obj.parent_obj]
        if self.fixed_all_folder.del_child(video_obj):
            update_list.append(self.fixed_all_folder)

        if self.fixed_bookmark_folder.del_child(video_obj):
            update_list.append(self.fixed_bookmark_folder)

        if self.fixed_fav_folder.del_child(video_obj):
            update_list.append(self.fixed_fav_folder)

        if self.fixed_live_folder.del_child(video_obj):
            update_list.append(self.fixed_live_folder)

        if self.fixed_missing_folder.del_child(video_obj):
            update_list.append(self.fixed_missing_folder)

        if self.fixed_new_folder.del_child(video_obj):
            update_list.append(self.fixed_new_folder)

        if self.fixed_waiting_folder.del_child(video_obj):
            update_list.append(self.fixed_waiting_folder)

        # Remove the video from our IVs
        # v1.2.017 When deleting folders containing thousands of videos, I
        #   noticed that a small number of video DBIDs didn't exist in the
        #   media data registry. Not sure what the cause is, but the following
        #   lines prevent a python error
        if video_obj.dbid in self.media_reg_dict:
            del self.media_reg_dict[video_obj.dbid]

        if video_obj.dbid in self.media_reg_live_dict:
            del self.media_reg_live_dict[video_obj.dbid]

        if video_obj.dbid in self.media_reg_auto_notify_dict:
            del self.media_reg_auto_notify_dict[video_obj.dbid]

        if video_obj.dbid in self.media_reg_auto_alarm_dict:
            del self.media_reg_auto_alarm_dict[video_obj.dbid]

        if video_obj.dbid in self.media_reg_auto_open_dict:
            del self.media_reg_auto_open_dict[video_obj.dbid]

        if video_obj.dbid in self.media_reg_auto_dl_start_dict:
            del self.media_reg_auto_dl_start_dict[video_obj.dbid]

        if video_obj.dbid in self.media_reg_auto_dl_stop_dict:
            del self.media_reg_auto_dl_stop_dict[video_obj.dbid]

        # Delete files from the filesystem, if required
        # If the parent container has an alternative download destination set,
        #   the files are in the corresponding directory. We don't delete the
        #   files because another channel/playlist/folder might be using them
        if delete_files_flag \
        and video_obj.file_name \
        and video_obj.parent_obj.dbid == video_obj.parent_obj.master_dbid:

            # There might be thousands of files in the directory, so using
            #   os.walk() or something like that might be too expensive
            # Also, post-processing might create various artefacts, all of
            #   which must be deleted
            ext_list = [
                'description',
                'info.json',
                'annotations.xml',
            ]
            ext_list.extend(formats.VIDEO_FORMAT_LIST)
            ext_list.extend(formats.AUDIO_FORMAT_LIST)

            for ext in ext_list:

                file_path = video_obj.get_default_path_by_ext(self, ext)
                if os.path.isfile(file_path):
                    os.remove(file_path)

            # (Thumbnails might be in one of two locations, so are handled
            #   separately)
            thumb_path = utils.find_thumbnail(self, video_obj)
            if thumb_path and os.path.isfile(thumb_path):
                os.remove(thumb_path)

        # Remove the video from the catalogue, if present
        if not no_update_catalogue_flag:
            self.main_win_obj.video_catalogue_delete_row(video_obj)

        # Update rows in the Video Index, first checking that the parent
        #   container object is currently drawn there (which it might not be,
        #   if emptying temporary folders on startup)
        if not no_update_index_flag:
            for container_obj in update_list:

                if container_obj.name \
                in self.main_win_obj.video_index_row_dict:
                    self.main_win_obj.video_index_update_row_text(
                        container_obj,
                    )


    def delete_container(self, media_data_obj, empty_flag=False):

        """Can be called by anything.

        Before deleting a channel, playlist or folder object from the media
        data registry, get confirmation from the user.

        The process is split across three functions.

        This functions obtains confirmation from the user. If deleting files,
        a second confirmation is required, and self.delete_container_continue()
        is called in response.

        In either case, self.delete_container_complete() is then called to
        update the media data registry.

        Args:

            media_data_obj (media.Channel, media.Playlist, media.Folder):
                The container media data object

            empty_flag (bool): If True, the container media data object is to
                be emptied, rather than being deleted

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 9530 delete_container')

        # Check this isn't a video or a fixed folder (which cannot be removed)
        # v2.1.029 In some older databases, a fixed folder called 'downloads_2'
        #   was created, containing a small number of videos. I'm still not
        #   sure under which circumstances that folder was created; in any
        #   case, such a folder needs to be deleteable
        if isinstance(media_data_obj, media.Video) \
        or (
            isinstance(media_data_obj, media.Folder)
            and media_data_obj.fixed_flag
            and self.check_fixed_folder(media_data_obj)
        ):
            return self.system_error(
                134,
                'Delete container request failed sanity check',
            )

        # Prompt the user for confirmation, even if the container object has no
        #   children
        # (Even though there are no children, we can't guarantee that the
        #   sub-directories in Tartube's data directory are empty)
        # Exception: don't prompt for confirmation if media_data_obj is
        #   somewhere inside a temporary folder
        confirm_flag = True
        delete_file_flag = False
        parent_obj = media_data_obj.parent_obj

        while parent_obj is not None:
            if isinstance(parent_obj, media.Folder) and parent_obj.temp_flag:
                # The media data object is somewhere inside a temporary folder;
                #   no need to prompt for confirmation
                confirm_flag = False

            parent_obj = parent_obj.parent_obj

        if confirm_flag:

            # Prompt the user for confirmation
            dialogue_win = mainwin.DeleteContainerDialogue(
                self.main_win_obj,
                media_data_obj,
                empty_flag,
            )

            response = dialogue_win.run()

            # Retrieve user choices from the dialogue window...
            if dialogue_win.button2.get_active():
                delete_file_flag = True
            else:
                delete_file_flag = False

            # ...before destroying it
            dialogue_win.destroy()

            if response != Gtk.ResponseType.OK:
                return

        # Get a second confirmation, if required to delete files
        if delete_file_flag:

            self.dialogue_manager_obj.show_msg_dialogue(
                _(
                'Are you SURE you want to delete files? This procedure' \
                ' cannot be reversed!',
                ),
                'question',
                'yes-no',
                None,                   # Parent window is main window
                # Arguments passed directly to .delete_container_continue()
                {
                    'yes': 'delete_container_continue',
                    'data': [media_data_obj, empty_flag],
                }
            )

        # No second confirmation required, so we can proceed directly to the
        #   call to self.delete_container_complete()
        else:
            self.delete_container_complete(media_data_obj, empty_flag)


    def delete_container_continue(self, data_list):

        """Called by self.delete_container().

        When deleting a container, after the user has specified that files
        should be deleted too, this function is called to delete those files.

        Args:

            data_list (list): A list of two items. The first is the container
                media data object; the second is a flag set to True if the
                container should be emptied, rather than being deleted

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 9624 delete_container_continue')

        # Unpack the arguments
        media_data_obj = data_list[0]
        empty_flag = data_list[1]

        # Confirmation obtained, so delete the files
        container_dir = media_data_obj.get_default_dir(self)
        if os.path.isdir(container_dir):
            shutil.rmtree(container_dir)

        # If emptying the container rather than deleting it, just create a
        #   replacement (empty) directory on the filesystem
        if empty_flag:
            try:
                os.makedirs(container_dir)
            except:
                pass

        # Now call self.delete_container_complete() to handle the media data
        #   registry
        self.delete_container_complete(media_data_obj, empty_flag)


    def delete_container_complete(self, media_data_obj, empty_flag,
    recursive_flag=False):

        """Called by self.delete_container() and .delete_container_continue().
        Subsequently called by this function recursively.

        Deletes a channel, playlist or folder object from the media data
        registry.

        This function calls itself recursively to delete all of the container
        object's descendants.

        Args:

            media_data_obj (media.Channel, media.Playlist, media.Folder):
                The container media data object

            empty_flag (bool): If True, the container media data object is to
                be emptied, rather than being deleted

            recursive_flag (bool): Set to False on the initial call to this
                function from some other part of the code, and True when this
                function calls itself recursively

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 9672 delete_container_complete')

        # Confirmation has been obtained, and any files have been deleted (if
        #   required), so now deal with the media data registry

        # Recursively remove all of the container object's children. The code
        #   doesn't work as intended, unless we make a copy of the list of
        #   child objects first
        copy_list = media_data_obj.child_list.copy()
        for child_obj in copy_list:
            if isinstance(child_obj, media.Video):
                self.delete_video(child_obj, False, True)
            else:
                self.delete_container_complete(child_obj, False, True)

        if not empty_flag or recursive_flag:

            # Remove the container object from its own parent object (if it has
            #   one)
            if media_data_obj.parent_obj:
                media_data_obj.parent_obj.del_child(media_data_obj)

            # Reset alternative download destinations
            media_data_obj.set_master_dbid(self, media_data_obj.dbid)

            # Remove the media data object from our IVs
            del self.media_reg_dict[media_data_obj.dbid]
            del self.media_name_dict[media_data_obj.name]
            if media_data_obj.dbid in self.media_top_level_list:
                index = self.media_top_level_list.index(media_data_obj.dbid)
                del self.media_top_level_list[index]

        # During the initial call to this function, delete the container
        #   object from the Video Index (which automatically resets the Video
        #   Catalogue)
        # (If deleting the contents of temporary folders while loading a
        #   Tartube database, the Video Index may not yet have been drawn, so
        #   we have to check for that)
        if not recursive_flag and not empty_flag \
        and media_data_obj.name in self.main_win_obj.video_index_row_dict:

            self.main_win_obj.video_index_delete_row(media_data_obj)

            # Also redraw the private folders in the Video Index, to show the
            #   correct number of downloaded/new videos, etc
            self.main_win_obj.video_index_update_row_text(
                self.fixed_all_folder,
            )

            self.main_win_obj.video_index_update_row_text(
                self.fixed_bookmark_folder,
            )

            self.main_win_obj.video_index_update_row_text(
                self.fixed_fav_folder,
            )

            self.main_win_obj.video_index_update_row_text(
                self.fixed_live_folder,
            )

            self.main_win_obj.video_index_update_row_text(
                self.fixed_missing_folder,
            )

            self.main_win_obj.video_index_update_row_text(
                self.fixed_new_folder,
            )

            self.main_win_obj.video_index_update_row_text(
                self.fixed_waiting_folder,
            )

        elif not recursive_flag and empty_flag:

            # When emptying the container, the quickest way to update the Video
            #   Index is just to redraw it from scratch
            self.main_win_obj.video_index_catalogue_reset()


    # (Change media data object settings, updating all related things)


    def prepare_mark_video(self, data_list):

        """Called by self.mark_container_favourite(),
        .mark_container_missing(), .mark_container_new() and
        mainwin.MainWin.on_video_index_mark_bookmark(), etc.

        The operation to mark a container's video as bookmarked or not
        bookmarked (etc) can take a very long time, especially if there are
        thousands of videos.

        This function takes some shortcuts to reduce the time to a few
        seconds.

        Args:

            data_list (list): List in the form

                (action_type, action_flag, container_obj, video_list)

            ...where 'action_type' is one of the strings 'bookmark',
                'favourite', 'missing', 'new' or 'waiting', 'action_flag' is
                True (e,g. to bookmark a video) or False (e.g. to unbookmark a
                video), 'container_obj' is a media.Channel, media.Playlist or
                media.Folder object, and 'video_list' is a list of media.Video
                objects to update (only specified when 'action_type' is
                'favourite', 'missing' or 'new')

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 9780 prepare_mark_video')

        action_type = data_list.pop(0)
        action_flag = data_list.pop(0)
        container_obj = data_list.pop(0)
        if action_type == 'favourite' or action_type == 'missing' \
        or action_type == 'new':
            video_list = data_list.pop(0)
        else:
            video_list = container_obj.child_list

        # Take some shortcuts
        for child_obj in video_list:

            if isinstance(child_obj, media.Video):

                if action_type == 'bookmark':
                    self.mark_video_bookmark(
                        child_obj,
                        action_flag,    # Mark video bookmarked
                        True,           # Don't update the Video Index
                        True,           # Don't update the Video Catalogue
                        True,           # Don't sort the child list each time
                    )

                elif action_type == 'favourite':

                    self.mark_video_favourite(
                        child_obj,
                        action_flag,    # Mark video favourite (or not)
                        True,           # Don't update the Video Index
                        True,           # Don't update the Video Catalogue
                        True,           # Don't sort the child list each time
                    )

                elif action_type == 'missing':

                    self.mark_video_missing(
                        child_obj,
                        action_flag,    # Mark video missing (or not)
                        True,           # Don't update the Video Index
                        True,           # Don't update the Video Catalogue
                        True,           # Don't sort the child list each time
                    )

                elif action_type == 'new':

                    self.mark_video_new(
                        child_obj,
                        action_flag,    # Mark video favourite (or not)
                        True,           # Don't update the Video Index
                        True,           # Don't update the Video Catalogue
                        True,           # Don't sort the child list each time
                    )

                elif action_type == 'waiting':

                    self.mark_video_waiting(
                        child_obj,
                        action_flag,    # Mark video waiting (or not)
                        True,           # Don't update the Video Index
                        True,           # Don't update the Video Catalogue
                        True,           # Don't sort the child list each time
                    )

        # Now we can sort the system folder's child list...
        if action_type == 'bookmark':
            self.fixed_bookmark_folder.sort_children()
        elif action_type == 'favourite':
            self.fixed_fav_folder.sort_children()
        elif action_type == 'missing':
            self.fixed_missing_folder.sort_children()
        elif action_type == 'new':
            self.fixed_new_folder.sort_children()
        elif action_type == 'waiting':
            self.fixed_waiting_folder.sort_children()

        # ...and then can redraw the Video Index and Video Catalogue,
        #   re-selecting the current selection, if any
        self.main_win_obj.video_index_catalogue_reset(True)


    def mark_video_bookmark(self, video_obj, bookmark_flag, \
    no_update_index_flag=False, no_update_catalogue_flag=False, \
    no_sort_flag=False):

        """Can be called by anything.

        Marks a video object as bookmarked or not bookmarked.

        The video object's .bookmark_flag IV is updated.

        Args:

            video_obj (media.Video): The media.Video object to mark

            bookmark_flag (bool): True to mark the video as bookmarked, False
                to mark it as not bookmarked

            no_update_index_flag (bool): True if the Video Index should not be
                updated (except for the system 'Bookmarks' folder), because the
                calling function wants to do that itself

            no_update_catalogue_flag (bool): True if rows in the Video
                Catalogue should not be updated, because the calling function
                wants to redraw the whole catalogue itself

            no_sort_flag (bool): True if the parent container's .child_list
                should not be sorted, because the calling function wants to do
                that itself

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 9881 mark_video_bookmark')

        # (List of Video Index rows to update, at the end of this function)
        update_list = [self.fixed_bookmark_folder]
        if not no_update_index_flag:
            update_list.append(video_obj.parent_obj)
            update_list.append(self.fixed_all_folder)
            if video_obj.fav_flag:
                update_list.append(self.fixed_fav_folder)
            if video_obj.live_mode:
                update_list.append(self.fixed_live_folder)
            if video_obj.missing_flag:
                update_list.append(self.fixed_missing_folder)
            if video_obj.new_flag:
                update_list.append(self.fixed_new_folder)
            if video_obj.waiting_flag:
                update_list.append(self.fixed_waiting_folder)

        # Mark the video as bookmarked or not bookmarked
        if not isinstance(video_obj, media.Video):
            return self.system_error(
                135,
                'Mark video as bookmarked request failed sanity check',
            )

        elif not bookmark_flag:

            # Mark video as not bookmarked
            if not video_obj.bookmark_flag:

                # Already marked
                return

            else:

                # Update the video object's IVs
                video_obj.set_bookmark_flag(False)
                # Update the parent object
                video_obj.parent_obj.dec_bookmark_count()

                # Remove this video from the private 'Bookmarks' folder (the
                #   folder's count IVs are automatically updated)
                self.fixed_bookmark_folder.del_child(video_obj)
                # Update the Video Catalogue, if that folder is the visible one
                #    (deleting the row, if the 'Bookmarks' folder is visible)
                if not no_update_catalogue_flag:

                    if self.main_win_obj.video_index_current is not None \
                    and self.main_win_obj.video_index_current \
                    == self.fixed_bookmark_folder.name:
                        self.main_win_obj.video_catalogue_delete_row(video_obj)

                    else:
                        self.main_win_obj.video_catalogue_update_row(video_obj)

                # Update other private folders
                self.fixed_all_folder.dec_bookmark_count()
                self.fixed_bookmark_folder.dec_bookmark_count()
                if video_obj.fav_flag:
                    self.fixed_fav_folder.dec_bookmark_count()
                if video_obj.live_mode:
                    self.fixed_live_folder.dec_bookmark_count()
                if video_obj.missing_flag:
                    self.fixed_missing_folder.dec_bookmark_count()
                if video_obj.new_flag:
                    self.fixed_new_folder.dec_bookmark_count()
                if video_obj.waiting_flag:
                    self.fixed_waiting_folder.dec_bookmark_count()

        else:

            # Mark video as bookmarked
            if video_obj.bookmark_flag:

                # Already marked
                return

            else:

                # Update the video object's IVs
                video_obj.set_bookmark_flag(True)
                # Update the parent object
                video_obj.parent_obj.inc_bookmark_count()

                # Add this video to the private 'Bookmarks' folder
                self.fixed_bookmark_folder.add_child(video_obj, no_sort_flag)
                self.fixed_bookmark_folder.inc_bookmark_count()
                if video_obj.dl_flag:
                    self.fixed_bookmark_folder.inc_dl_count()
                if video_obj.fav_flag:
                    self.fixed_bookmark_folder.inc_fav_count()
                if video_obj.live_mode:
                    self.fixed_bookmark_folder.inc_live_count()
                if video_obj.missing_flag:
                    self.fixed_bookmark_folder.inc_missing_count()
                if video_obj.new_flag:
                    self.fixed_bookmark_folder.inc_new_count()
                if video_obj.waiting_flag:
                    self.fixed_bookmark_folder.inc_waiting_count()

                # Update the Video Catalogue, if that folder is the visible one
                if not no_update_catalogue_flag:
                    self.main_win_obj.video_catalogue_update_row(video_obj)

                # Update other private folders
                self.fixed_all_folder.inc_bookmark_count()
                if video_obj.fav_flag:
                    self.fixed_fav_folder.inc_bookmark_count()
                if video_obj.live_mode:
                    self.fixed_live_folder.inc_bookmark_count()
                if video_obj.missing_flag:
                    self.fixed_missing_folder.inc_bookmark_count()
                if video_obj.new_flag:
                    self.fixed_new_folder.inc_bookmark_count()
                if video_obj.waiting_flag:
                    self.fixed_waiting_folder.inc_bookmark_count()

        # Update rows in the Video Index
        for container_obj in update_list:
            self.main_win_obj.video_index_update_row_text(container_obj)


    def mark_video_downloaded(self, video_obj, dl_flag, not_new_flag=False):

        """Can be called by anything.

        Marks a video object as downloaded (i.e. the video file exists on the
        user's filesystem) or not downloaded.

        The video object's .dl_flag IV is updated.

        Args:

            video_obj (media.Video): The media.Video object to mark.

            dl_flag (bool): True to mark the video as downloaded, False to mark
                it as not downloaded.

            not_new_flag (bool): Set to True when called by
                downloads.confirm_old_video(). The video is downloaded, but not
                new

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 10018 mark_video_downloaded')

        # (List of Video Index rows to update, at the end of this function)
        update_list = [video_obj.parent_obj, self.fixed_all_folder]

        # Mark the video as downloaded or not downloaded
        if not isinstance(video_obj, media.Video):
            return self.system_error(
                136,
                'Mark video as downloaded request failed sanity check',
            )

        elif not dl_flag:

            # Mark video as not downloaded
            if not video_obj.dl_flag:

                # Already marked
                return

            else:

                # Update the video object's IVs
                video_obj.set_dl_flag(False)
                # (A video that is not downloaded cannot be marked archived)
                video_obj.set_archive_flag(False)
                # Update the parent container object
                video_obj.parent_obj.dec_dl_count()
                # Update private folders
                self.fixed_all_folder.dec_dl_count()
                self.fixed_new_folder.dec_dl_count()
                if video_obj.bookmark_flag:
                    self.fixed_bookmark_folder.dec_dl_count()
                    update_list.append(self.fixed_bookmark_folder)
                if video_obj.fav_flag:
                    self.fixed_fav_folder.dec_dl_count()
                    update_list.append(self.fixed_fav_folder)
                if video_obj.live_mode:
                    self.fixed_live_folder.dec_dl_count()
                    update_list.append(self.fixed_live_folder)
                if video_obj.missing_flag:
                    self.fixed_missing_folder.dec_dl_count()
                    update_list.append(self.fixed_missing_folder)
                if video_obj.waiting_flag:
                    self.fixed_waiting_folder.dec_dl_count()
                    update_list.append(self.fixed_waiting_folder)

                # Also mark the video as not new (if required)...
                if not not_new_flag:
                    self.mark_video_new(video_obj, False, True)
                # ...and not missing (in all circumstances)
                self.mark_video_missing(video_obj, False, True)

        else:

            # Mark video as downloaded
            if video_obj.dl_flag:

                # Already marked
                return

            else:

                # If any ancestor channels, playlists or folders are marked as
                #   favourite, the video must be marked favourite as well
                if video_obj.ancestor_is_favourite():
                    self.mark_video_favourite(video_obj, True, True)

                # Update the video object's IVs
                video_obj.set_dl_flag(True)
                # Update the parent container object
                video_obj.parent_obj.inc_dl_count()
                # Update private folders
                self.fixed_all_folder.inc_dl_count()
                self.fixed_new_folder.inc_dl_count()
                if video_obj.bookmark_flag:
                    self.fixed_bookmark_folder.inc_dl_count()
                    update_list.append(self.fixed_bookmark_folder)
                if video_obj.fav_flag:
                    self.fixed_fav_folder.inc_dl_count()
                    update_list.append(self.fixed_fav_folder)
                if video_obj.live_mode:
                    self.fixed_live_folder.inc_dl_count()
                    update_list.append(self.fixed_live_folder)
                if video_obj.missing_flag:
                    self.fixed_missing_folder.inc_dl_count()
                    update_list.append(self.fixed_missing_folder)
                if video_obj.waiting_flag:
                    self.fixed_waiting_folder.inc_dl_count()
                    update_list.append(self.fixed_waiting_folder)

                # Also mark the video as new
                if not not_new_flag:
                    self.mark_video_new(video_obj, True, True)

        # Update rows in the Video Index
        for container_obj in update_list:
            self.main_win_obj.video_index_update_row_text(container_obj)


    def mark_video_favourite(self, video_obj, fav_flag, \
    no_update_index_flag=False, no_update_catalogue_flag=False,
    no_sort_flag=False):

        """Can be called by anything.

        Marks a video object as favourite or not favourite.

        The video object's .fav_flag IV is updated.

        Args:

            video_obj (media.Video): The media.Video object to mark

            fav_flag (bool): True to mark the video as favourite, False to mark
                it as not favourite

            no_update_index_flag (bool): True if the Video Index should not be
                updated (except for the system 'Favourite Videos' folder),
                because the calling function wants to do that itself

            no_update_catalogue_flag (bool): True if rows in the Video
                Catalogue should not be updated, because the calling function
                wants to redraw the whole catalogue itself

            no_sort_flag (bool): True if the parent container's .child_list
                should not be sorted, because the calling function wants to do
                that itself

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 10142 mark_video_favourite')

        # (List of Video Index rows to update, at the end of this function)
        update_list = [self.fixed_fav_folder]
        if not no_update_index_flag:
            update_list.append(video_obj.parent_obj)
            update_list.append(self.fixed_all_folder)
            if video_obj.bookmark_flag:
                update_list.append(self.fixed_bookmark_folder)
            if video_obj.live_mode:
                update_list.append(self.fixed_live_folder)
            if video_obj.missing_flag:
                update_list.append(self.fixed_missing_folder)
            if video_obj.new_flag:
                update_list.append(self.fixed_new_folder)
            if video_obj.waiting_flag:
                update_list.append(self.fixed_waiting_folder)

        # Mark the video as favourite or not favourite
        if not isinstance(video_obj, media.Video):
            return self.system_error(
                137,
                'Mark video as favourite request failed sanity check',
            )

        elif not fav_flag:

            # Mark video as not favourite
            if not video_obj.fav_flag:

                # Already marked
                return

            else:

                # Update the video object's IVs
                video_obj.set_fav_flag(False)
                # Update the parent object
                video_obj.parent_obj.dec_fav_count()

                # Remove this video from the private 'Favourite Videos' folder
                #   (the folder's count IVs are automatically updated)
                self.fixed_fav_folder.del_child(video_obj)
                # Update the Video Catalogue, if that folder is the visible one
                #    (deleting the row, if the 'Favourite Videos' folder is
                #   visible)
                if not no_update_catalogue_flag:

                    if self.main_win_obj.video_index_current is not None \
                    and self.main_win_obj.video_index_current \
                    == self.fixed_fav_folder.name:
                        self.main_win_obj.video_catalogue_delete_row(video_obj)

                    else:
                        self.main_win_obj.video_catalogue_update_row(video_obj)

                # Update other private folders
                self.fixed_all_folder.dec_fav_count()
                self.fixed_fav_folder.dec_fav_count()
                if video_obj.bookmark_flag:
                    self.fixed_bookmark_folder.dec_fav_count()
                if video_obj.live_mode:
                    self.fixed_live_folder.dec_fav_count()
                if video_obj.missing_flag:
                    self.fixed_missing_folder.dec_fav_count()
                if video_obj.new_flag:
                    self.fixed_new_folder.dec_fav_count()
                if video_obj.waiting_flag:
                    self.fixed_waiting_folder.dec_fav_count()

        else:

            # Mark video as favourite
            if video_obj.fav_flag:

                # Already marked
                return

            else:

                # Update the video object's IVs
                video_obj.set_fav_flag(True)
                # Update the parent object
                video_obj.parent_obj.inc_fav_count()

                # Add this video to the private 'Favourite Videos' folder
                self.fixed_fav_folder.add_child(video_obj, no_sort_flag)
                self.fixed_fav_folder.inc_fav_count()
                if video_obj.bookmark_flag:
                    self.fixed_fav_folder.inc_bookmark_count()
                if video_obj.dl_flag:
                    self.fixed_fav_folder.inc_dl_count()
                if video_obj.live_mode:
                    self.fixed_fav_folder.inc_live_count()
                if video_obj.missing_flag:
                    self.fixed_fav_folder.inc_missing_count()
                if video_obj.new_flag:
                    self.fixed_fav_folder.inc_new_count()
                if video_obj.waiting_flag:
                    self.fixed_fav_folder.inc_waiting_count()

                # Update the Video Catalogue, if that folder is the visible one
                if not no_update_catalogue_flag:
                    self.main_win_obj.video_catalogue_update_row(video_obj)

                # Update other private folders
                self.fixed_all_folder.inc_fav_count()
                if video_obj.bookmark_flag:
                    self.fixed_bookmark_folder.inc_fav_count()
                if video_obj.live_mode:
                    self.fixed_live_folder.inc_fav_count()
                if video_obj.missing_flag:
                    self.fixed_missing_folder.inc_fav_count()
                if video_obj.new_flag:
                    self.fixed_new_folder.inc_fav_count()
                if video_obj.waiting_flag:
                    self.fixed_waiting_folder.inc_fav_count()

        # Update rows in the Video Index
        for container_obj in update_list:
            self.main_win_obj.video_index_update_row_text(container_obj)


    def mark_video_live(self, video_obj, live_mode, \
    no_update_index_flag=False, no_update_catalogue_flag=False, \
    no_sort_flag=False):

        """Can be called by anything.

        Marks a video object as a livestream.

        The video object's .live_mode IV is updated.

        Args:

            video_obj (media.Video): The media.Video object to mark

            live_mode (int): 0 if the video is not a livestream (or if it was a
                livestream which has now finished, and behaves like a normal
                uploaded video), 1 if the livestream has not started, 2 if the
                livestream is currently being broadcast

            no_update_index_flag (bool): True if the Video Index should not be
                updated (except for the system 'Livestreams' folder), because
                the calling function wants to do that itself

            no_update_catalogue_flag (bool): True if rows in the Video
                Catalogue should not be updated, because the calling function
                wants to redraw the whole catalogue itself

            no_sort_flag (bool): True if the parent container's .child_list
                should not be sorted, because the calling function wants to do
                that itself

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 10291 mark_video_live')

        # (List of Video Index rows to update, at the end of this function)
        update_list = [self.fixed_live_folder]
        if not no_update_index_flag:
            update_list.append(video_obj.parent_obj)
            update_list.append(self.fixed_all_folder)
            if video_obj.bookmark_flag:
                update_list.append(self.fixed_bookmark_folder)
            if video_obj.fav_flag:
                update_list.append(self.fixed_fav_folder)
            if video_obj.missing_flag:
                update_list.append(self.fixed_missing_folder)
            if video_obj.new_flag:
                update_list.append(self.fixed_new_folder)
            if video_obj.waiting_flag:
                update_list.append(self.fixed_waiting_folder)

        # Mark the video as a livestream or not a livestream
        if not isinstance(video_obj, media.Video):
            return self.system_error(
                138,
                'Mark video as livestream request failed sanity check',
            )

        elif live_mode == 0:

            # Mark video as not a livestream
            if video_obj.live_mode == 0:

                # Already marked
                return

            else:

                # Update the main registries
                if video_obj.dbid in self.media_reg_live_dict:
                    del self.media_reg_live_dict[video_obj.dbid]
                if video_obj.dbid in self.media_reg_auto_alarm_dict:
                    del self.media_reg_auto_alarm_dict[video_obj.dbid]
                if video_obj.dbid in self.media_reg_auto_open_dict:
                    del self.media_reg_auto_open_dict[video_obj.dbid]
                if video_obj.dbid in self.media_reg_auto_dl_start_dict:
                    del self.media_reg_auto_dl_start_dict[video_obj.dbid]
                if video_obj.dbid in self.media_reg_auto_dl_stop_dict:
                    del self.media_reg_auto_dl_stop_dict[video_obj.dbid]

                # Update the video object's IVs
                video_obj.set_live_mode(live_mode)
                video_obj.set_was_live_flag(True)
                # Update the parent object
                video_obj.parent_obj.dec_live_count()

                # Remove this video from the private 'Livestreams' folder
                #   (the folder's count IVs are automatically updated)
                self.fixed_live_folder.del_child(video_obj)
                # Update the Video Catalogue, if that folder is the visible one
                #    (deleting the row, if the 'Livestreams' folder is visible)
                if not no_update_catalogue_flag:

                    if self.main_win_obj.video_index_current is not None \
                    and self.main_win_obj.video_index_current \
                    == self.fixed_live_folder.name:
                        self.main_win_obj.video_catalogue_delete_row(video_obj)

                    else:
                        self.main_win_obj.video_catalogue_update_row(video_obj)

                # Update other private folders
                self.fixed_all_folder.dec_live_count()
                self.fixed_live_folder.dec_live_count()
                if video_obj.bookmark_flag:
                    self.fixed_bookmark_folder.dec_live_count()
                if video_obj.fav_flag:
                    self.fixed_fav_folder.dec_live_count()
                if video_obj.missing_flag:
                    self.fixed_missing_folder.dec_live_count()
                if video_obj.new_flag:
                    self.fixed_new_folder.dec_live_count()
                if video_obj.waiting_flag:
                    self.fixed_waiting_folder.dec_waiting_count()

        else:

            # Mark video as a livestream
            if video_obj.live_mode == live_mode:

                # Already marked as either a 'waiting' or a 'live' livestream
                return

            elif video_obj.was_live_flag:

                # A livestream video which has been marked as a normal video
                #   can never be marked as a livestream video again
                # (This prevents any problems in reading the RSS feeds from
                #   continually marking an old video as a livestream again)
                return

            else:

                if video_obj.live_mode == 0:
                    # Video was not a livestream, but now is
                    convert_flag = False
                else:
                    # Video was a 'waiting' livestream, and is now 'live' (or
                    #   vice-versa)
                    convert_flag = True

                # Update the main registry
                self.media_reg_live_dict[video_obj.dbid] = video_obj
                if self.livestream_auto_notify_flag:
                    self.media_reg_auto_notify_dict[video_obj.dbid] = video_obj
                if HAVE_PLAYSOUND_FLAG \
                and self.livestream_auto_alarm_flag:
                    self.media_reg_auto_alarm_dict[video_obj.dbid] = video_obj
                if self.livestream_auto_open_flag:
                    self.media_reg_auto_open_dict[video_obj.dbid] = video_obj
                if self.livestream_auto_dl_start_flag:
                    self.media_reg_auto_dl_start_dict[video_obj.dbid] \
                    = video_obj
                if self.livestream_auto_dl_stop_flag:
                    self.media_reg_auto_dl_stop_dict[video_obj.dbid] \
                    = video_obj

                # Update the video object's IVs
                video_obj.set_live_mode(live_mode)
                # Update the parent object
                if not convert_flag:
                    video_obj.parent_obj.inc_waiting_count()

                # Add this video to the private 'Livestreams' folder
                if not convert_flag:
                    self.fixed_live_folder.add_child(video_obj, no_sort_flag)
                    self.fixed_live_folder.inc_live_count()
                    if video_obj.bookmark_flag:
                        self.fixed_live_folder.inc_bookmark_count()
                    if video_obj.dl_flag:
                        self.fixed_live_folder.inc_dl_count()
                    if video_obj.fav_flag:
                        self.fixed_live_folder.inc_fav_count()
                    if video_obj.missing_flag:
                        self.fixed_live_folder.inc_missing_count()
                    if video_obj.new_flag:
                        self.fixed_live_folder.inc_new_count()
                    if video_obj.waiting_flag:
                        self.fixed_live_folder.inc_waiting_count()

                # Update the Video Catalogue, if that folder is the visible one
                if not no_update_catalogue_flag:
                    self.main_win_obj.video_catalogue_update_row(video_obj)

                # Update other private folders
                if not convert_flag:
                    self.fixed_all_folder.inc_live_count()
                    if video_obj.bookmark_flag:
                        self.fixed_bookmark_folder.inc_live_count()
                    if video_obj.fav_flag:
                        self.fixed_fav_folder.inc_live_count()
                    if video_obj.missing_flag:
                        self.fixed_missing_folder.inc_live_count()
                    if video_obj.new_flag:
                        self.fixed_new_folder.inc_live_count()
                    if video_obj.waiting_flag:
                        self.fixed_waiting_folder.inc_live_count()

        # Update rows in the Video Index
        for container_obj in update_list:
            self.main_win_obj.video_index_update_row_text(container_obj)


    def mark_video_missing(self, video_obj, missing_flag, \
    no_update_index_flag=False, no_update_catalogue_flag=False, \
    no_sort_flag=False):

        """Can be called by anything.

        Marks a video object as missing or not missing. (A video is missing if
        it has been downloaded from a channel/playlist by the user, but has
        since been removed from that channel/playlist by its creator).

        The video object's .missing_flag IV is updated.

        Args:

            video_obj (media.Video): The media.Video object to mark

            missing_flag (bool): True to mark the video as missing, False to
                mark it as not missing

            no_update_index_flag (bool): True if the Video Index should not be
                updated, because the calling function wants to do that itself

            no_update_catalogue_flag (bool): True if rows in the Video
                Catalogue should not be updated, because the calling function
                wants to redraw the whole catalogue itself

            no_sort_flag (bool): True if the parent container's .child_list
                should not be sorted, because the calling function wants to do
                that itself

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 10292 mark_video_missing')

        # (List of Video Index rows to update, at the end of this function)
        update_list = [self.fixed_missing_folder]
        if not no_update_index_flag:
            update_list.append(video_obj.parent_obj)
            update_list.append(self.fixed_all_folder)
            if video_obj.bookmark_flag:
                update_list.append(self.fixed_bookmark_folder)
            if video_obj.fav_flag:
                update_list.append(self.fixed_fav_folder)
            if video_obj.live_mode:
                update_list.append(self.fixed_live_folder)
            if video_obj.new_flag:
                update_list.append(self.fixed_new_folder)
            if video_obj.waiting_flag:
                update_list.append(self.fixed_waiting_folder)

        # Mark the video as missing or not missing
        if not isinstance(video_obj, media.Video):
            return self.system_error(
                162,
                'Mark video as missing request failed sanity check',
            )

        elif not missing_flag:

            # Mark video as not missing
            if not video_obj.missing_flag:

                # Already marked
                return

            else:

                # Update the video object's IVs
                video_obj.set_missing_flag(False)
                # Update the parent object
                video_obj.parent_obj.dec_missing_count()

                # Remove this video from the private 'Missing Videos' folder
                #   (the folder's count IVs are automatically updated)
                self.fixed_missing_folder.del_child(video_obj)
                # Update the Video Catalogue, if that folder is the visible one
                #    (deleting the row, if the 'Missing Videos' folder is
                #   visible)
                if not no_update_catalogue_flag:

                    if self.main_win_obj.video_index_current is not None \
                    and self.main_win_obj.video_index_current \
                    == self.fixed_missing_folder.name:
                        self.main_win_obj.video_catalogue_delete_row(video_obj)

                    else:
                        self.main_win_obj.video_catalogue_update_row(video_obj)

                # Update other private folders
                self.fixed_all_folder.dec_missing_count()
                self.fixed_missing_folder.dec_missing_count()
                if video_obj.bookmark_flag:
                    self.fixed_bookmark_folder.dec_missing_count()
                if video_obj.fav_flag:
                    self.fixed_fav_folder.dec_missing_count()
                if video_obj.live_mode:
                    self.fixed_live_folder.dec_missing_count()
                if video_obj.missing_flag:
                    self.fixed_missing_folder.dec_missing_count()
                if video_obj.new_flag:
                    self.fixed_new_folder.dec_missing_count()
                if video_obj.waiting_flag:
                    self.fixed_waiting_folder.dec_missing_count()

        else:

            # Mark video as missing (but not if the video is not marked as
            #   downloaded)
            if video_obj.missing_flag or not video_obj.dl_flag:

                # Already marked, or not elligible
                return

            else:

                # Update the video object's IVs
                video_obj.set_missing_flag(True)
                # Update the parent object
                video_obj.parent_obj.inc_missing_count()

                # Add this video to the private 'Missing Videos' folder
                self.fixed_missing_folder.add_child(video_obj, no_sort_flag)
                self.fixed_missing_folder.inc_missing_count()
                if video_obj.bookmark_flag:
                    self.fixed_missing_folder.inc_bookmark_count()
                if video_obj.dl_flag:
                    self.fixed_missing_folder.inc_dl_count()
                if video_obj.fav_flag:
                    self.fixed_missing_folder.inc_fav_count()
                if video_obj.live_mode:
                    self.fixed_missing_folder.inc_live_count()
                if video_obj.missing_flag:
                    self.fixed_missing_folder.inc_missing_count()
                if video_obj.new_flag:
                    self.fixed_missing_folder.inc_new_count()
                if video_obj.waiting_flag:
                    self.fixed_missing_folder.inc_waiting_count()

                # Update the Video Catalogue, if that folder is the visible one
                if not no_update_catalogue_flag:
                    self.main_win_obj.video_catalogue_update_row(video_obj)

                # Update other private folders
                self.fixed_all_folder.inc_missing_count()
                if video_obj.bookmark_flag:
                    self.fixed_bookmark_folder.inc_missing_count()
                if video_obj.fav_flag:
                    self.fixed_fav_folder.inc_missing_count()
                if video_obj.live_mode:
                    self.fixed_live_folder.inc_missing_count()
                if video_obj.missing_flag:
                    self.fixed_missing_folder.inc_missing_count()
                if video_obj.new_flag:
                    self.fixed_new_folder.inc_missing_count()
                if video_obj.waiting_flag:
                    self.fixed_waiting_folder.inc_missing_count()

        # Update rows in the Video Index
        for container_obj in update_list:
            self.main_win_obj.video_index_update_row_text(container_obj)


    def mark_video_new(self, video_obj, new_flag, no_update_index_flag=False,
    no_update_catalogue_flag=False, no_sort_flag=False):

        """Can be called by anything.

        Marks a video object as new (i.e. unwatched by the user), or as not
        new (already watched by the user).

        The video object's .new_flag IV is updated.

        Args:

            video_obj (media.Video): The media.Video object to mark

            new_flag (bool): True to mark the video as new, False to mark it as
                not new

            no_update_index_flag (bool): True if the Video Index should not be
                updated (except for the system 'New Videos' folder), because
                the calling function wants to do that itself

            no_update_catalogue_flag (bool): True if rows in the Video
                Catalogue should not be updated, because the calling function
                wants to redraw the whole catalogue itself

            no_sort_flag (bool): True if the parent container's .child_list
                should not be sorted, because the calling function wants to do
                that itself

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 10476 mark_video_new')

        # (List of Video Index rows to update, at the end of this function)
        update_list = [self.fixed_new_folder]
        if not no_update_index_flag:
            update_list.append(video_obj.parent_obj)
            update_list.append(self.fixed_all_folder)
            if video_obj.bookmark_flag:
                update_list.append(self.fixed_bookmark_folder)
            if video_obj.fav_flag:
                update_list.append(self.fixed_fav_folder)
            if video_obj.live_mode:
                update_list.append(self.fixed_live_folder)
            if video_obj.missing_flag:
                update_list.append(self.fixed_missing_folder)
            if video_obj.waiting_flag:
                update_list.append(self.fixed_waiting_folder)

        # Mark the video as new or not new
        if not isinstance(video_obj, media.Video):
            return self.system_error(
                139,
                'Mark video as new request failed sanity check',
            )

        elif not new_flag:

            # Mark video as not new
            if not video_obj.new_flag:

                # Already marked
                return

            else:

                # Update the video object's IVs
                video_obj.set_new_flag(False)
                # Update the parent object
                video_obj.parent_obj.dec_new_count()

                # Remove this video from the private 'New Videos' folder
                #   (the folder's count IVs are automatically updated)
                self.fixed_new_folder.del_child(video_obj)
                self.fixed_new_folder.dec_new_count()
                # Update the Video Catalogue, if that folder is the visible one
                #    (deleting the row, if the 'New Videos' folder is visible)
                if not no_update_catalogue_flag:

                    if self.main_win_obj.video_index_current is not None \
                    and self.main_win_obj.video_index_current \
                    == self.fixed_new_folder.name:
                        self.main_win_obj.video_catalogue_delete_row(video_obj)

                    else:
                        self.main_win_obj.video_catalogue_update_row(video_obj)

                # Update other private folders
                self.fixed_all_folder.dec_new_count()
                if video_obj.bookmark_flag:
                    self.fixed_bookmark_folder.dec_new_count()
                if video_obj.fav_flag:
                    self.fixed_fav_folder.dec_new_count()
                if video_obj.live_mode:
                    self.fixed_live_folder.dec_new_count()
                if video_obj.missing_flag:
                    self.fixed_missing_folder.dec_new_count()
                if video_obj.waiting_flag:
                    self.fixed_waiting_folder.dec_new_count()

        else:

            # Mark video as new
            if video_obj.new_flag:

                # Already marked
                return

            else:

                # Update the video object's IVs
                video_obj.set_new_flag(True)
                # Update the parent object
                video_obj.parent_obj.inc_new_count()

                # Add this video to the private 'New Videos' folder
                self.fixed_new_folder.add_child(video_obj, no_sort_flag)
                self.fixed_new_folder.inc_new_count()
                if video_obj.bookmark_flag:
                    self.fixed_new_folder.inc_bookmark_count()
                if video_obj.fav_flag:
                    self.fixed_new_folder.inc_fav_count()
                if video_obj.live_mode:
                    self.fixed_new_folder.inc_live_count()
                if video_obj.missing_flag:
                    self.fixed_new_folder.inc_missing_count()
                if video_obj.waiting_flag:
                    self.fixed_new_folder.inc_waiting_count()
                # Update the Video Catalogue, if that folder is the visible one
                if not no_update_catalogue_flag:
                    self.main_win_obj.video_catalogue_update_row(video_obj)

                # Update other private folders
                self.fixed_all_folder.inc_new_count()
                if video_obj.bookmark_flag:
                    self.fixed_bookmark_folder.inc_new_count()
                if video_obj.fav_flag:
                    self.fixed_fav_folder.inc_new_count()
                if video_obj.live_mode:
                    self.fixed_live_folder.inc_new_count()
                if video_obj.missing_flag:
                    self.fixed_missing_folder.inc_new_count()
                if video_obj.waiting_flag:
                    self.fixed_waiting_folder.inc_new_count()

        # Update rows in the Video Index
        for container_obj in update_list:
            self.main_win_obj.video_index_update_row_text(container_obj)


    def mark_video_waiting(self, video_obj, waiting_flag, \
    no_update_index_flag=False, no_update_catalogue_flag=False, \
    no_sort_flag=False):

        """Can be called by anything.

        Marks a video object as in the waiting list or not in the waiting list.

        The video object's .waiting_flag IV is updated.

        Args:

            video_obj (media.Video): The media.Video object to mark

            waiting_flag (bool): True to mark the video as in the waiting list,
                False to mark it as not in the waiting list

            no_update_index_flag (bool): True if the Video Index should not be
                updated (except for the system 'Waiting Videos' folder),
                because the calling function wants to do that itself

            no_update_catalogue_flag (bool): True if rows in the Video
                Catalogue should not be updated, because the calling function
                wants to redraw the whole catalogue itself

            no_sort_flag (bool): True if the parent container's .child_list
                should not be sorted, because the calling function wants to do
                that itself

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 10619 mark_video_waiting')

        # (List of Video Index rows to update, at the end of this function)
        update_list = [self.fixed_waiting_folder]
        if not no_update_index_flag:
            update_list.append(video_obj.parent_obj)
            update_list.append(self.fixed_all_folder)
            if video_obj.bookmark_flag:
                update_list.append(self.fixed_bookmark_folder)
            if video_obj.fav_flag:
                update_list.append(self.fixed_fav_folder)
            if video_obj.live_mode:
                update_list.append(self.fixed_live_folder)
            if video_obj.missing_flag:
                update_list.append(self.fixed_missing_folder)
            if video_obj.new_flag:
                update_list.append(self.fixed_new_folder)

        # Mark the video as in the waiting list or not in the waiting list
        if not isinstance(video_obj, media.Video):
            return self.system_error(
                140,
                'Mark video as in waiting list request failed sanity check',
            )

        elif not waiting_flag:

            # Mark video as not in the waiting list
            if not video_obj.waiting_flag:

                # Already marked
                return

            else:

                # Update the video object's IVs
                video_obj.set_waiting_flag(False)
                # Update the parent object
                video_obj.parent_obj.dec_waiting_count()

                # Remove this video from the private 'Waiting Videos' folder
                #   (the folder's count IVs are automatically updated)
                self.fixed_waiting_folder.del_child(video_obj)
                # Update the Video Catalogue, if that folder is the visible one
                #    (deleting the row, if the 'Waiting Videos' folder is
                #   visible)
                if not no_update_catalogue_flag:

                    if self.main_win_obj.video_index_current is not None \
                    and self.main_win_obj.video_index_current \
                    == self.fixed_waiting_folder.name:
                        self.main_win_obj.video_catalogue_delete_row(video_obj)

                    else:
                        self.main_win_obj.video_catalogue_update_row(video_obj)

                # Update other private folders
                self.fixed_all_folder.dec_waiting_count()
                self.fixed_waiting_folder.dec_waiting_count()
                if video_obj.bookmark_flag:
                    self.fixed_bookmark_folder.dec_waiting_count()
                if video_obj.fav_flag:
                    self.fixed_fav_folder.dec_waiting_count()
                if video_obj.live_mode:
                    self.fixed_live_folder.dec_waiting_count()
                if video_obj.missing_flag:
                    self.fixed_missing_folder.dec_waiting_count()
                if video_obj.new_flag:
                    self.fixed_new_folder.dec_waiting_count()

        else:

            # Mark video as in the waiting list
            if video_obj.waiting_flag:

                # Already marked
                return

            else:

                # Update the video object's IVs
                video_obj.set_waiting_flag(True)
                # Update the parent object
                video_obj.parent_obj.inc_waiting_count()

                # Add this video to the private 'Waiting Videos' folder
                self.fixed_waiting_folder.add_child(video_obj, no_sort_flag)
                self.fixed_waiting_folder.inc_waiting_count()
                if video_obj.bookmark_flag:
                    self.fixed_waiting_folder.inc_bookmark_count()
                if video_obj.dl_flag:
                    self.fixed_waiting_folder.inc_dl_count()
                if video_obj.fav_flag:
                    self.fixed_waiting_folder.inc_fav_count()
                if video_obj.live_mode:
                    self.fixed_waiting_folder.inc_live_count()
                if video_obj.missing_flag:
                    self.fixed_waiting_folder.inc_missing_count()
                if video_obj.new_flag:
                    self.fixed_waiting_folder.inc_new_count()

                # Update the Video Catalogue, if that folder is the visible one
                if not no_update_catalogue_flag:
                    self.main_win_obj.video_catalogue_update_row(video_obj)

                # Update other private folders
                self.fixed_all_folder.inc_waiting_count()
                if video_obj.bookmark_flag:
                    self.fixed_bookmark_folder.inc_waiting_count()
                if video_obj.fav_flag:
                    self.fixed_fav_folder.inc_waiting_count()
                if video_obj.live_mode:
                    self.fixed_live_folder.inc_waiting_count()
                if video_obj.missing_flag:
                    self.fixed_missing_folder.inc_waiting_count()
                if video_obj.new_flag:
                    self.fixed_new_folder.inc_waiting_count()

        # Update rows in the Video Index
        for container_obj in update_list:
            self.main_win_obj.video_index_update_row_text(container_obj)


    def mark_folder_hidden(self, folder_obj, flag):

        """Called by callbacks in self.on_menu_show_hidden() and
        mainwin.MainWin.on_video_index_hide_folder().

        Marks a folder as hidden (not visible in the Video Index) or not
        hidden (visible in the Video Index, although the user might be
        required to expand the tree to see it).

        Args:

            folder_obj (media.Folder): The folder object to mark

            flag (bool): True to mark the folder as hidden, False to mark it as
                not hidden

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 10756 mark_folder_hidden')

        if not isinstance(folder_obj, media.Folder):
            return self.system_error(
                141,
                'Mark folder as hidden request failed sanity check',
            )

        if not flag:

            # Mark folder as not hidden
            if not folder_obj.hidden_flag:

                # Already marked
                return

            else:

                # Update the folder object's IVs
                folder_obj.set_hidden_flag(False)
                # Update the Video Index
                self.main_win_obj.video_index_add_row(folder_obj)

        else:

            # Mark video as hidden
            if folder_obj.hidden_flag:

                # Already marked
                return

            else:

                # Update the folder object's IVs
                folder_obj.set_hidden_flag(True)
                # Update the Video Index
                self.main_win_obj.video_index_delete_row(folder_obj)


    def mark_container_archived(self, media_data_obj, archive_flag,
    only_child_videos_flag):

        """Called by mainwin.MainWin.on_video_index_mark_archived() and
        .on_video_index_mark_not_archived().

        Marks any descendant videos as archived.

        Args:

            media_data_obj (media.Channel, media.Playlist or media.Folder):
                The container object to update

            archive_flag (bool): True to mark as archived, False to mark as not
                archived

            only_child_videos_flag (bool): Set to True if only child video
                objects should be marked; False if the container object and all
                its descendants should be marked

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 10815 mark_container_archived')

        if isinstance(media_data_obj, media.Video):
            return self.system_error(
                142,
                'Mark container as archived request failed sanity check',
            )

        # Special arrangements for private folders
        if media_data_obj == self.fixed_all_folder:

            # Check every video
            for other_obj in list(self.media_reg_dict.values()):

                if isinstance(other_obj, media.Video) and other_obj.dl_flag:
                    other_obj.set_archive_flag(archive_flag)

        elif not archive_flag and media_data_obj == self.fixed_bookmark_folder:

            # Check videos in this folder
            for other_obj in self.fixed_bookmark_folder.child_list:

                if isinstance(other_obj, media.Video) and other_obj.dl_flag \
                and other_obj.bookmark_flag:
                    other_obj.set_archive_flag(archive_flag)

        elif not archive_flag and media_data_obj == self.fixed_fav_folder:

            # Check videos in this folder
            for other_obj in self.fixed_fav_folder.child_list:

                if isinstance(other_obj, media.Video) and other_obj.dl_flag \
                and other_obj.fav_flag:
                    other_obj.set_archive_flag(archive_flag)

        elif not archive_flag and media_data_obj == self.fixed_live_folder:

            # Check videos in this folder
            for other_obj in self.fixed_live_folder.child_list:

                if isinstance(other_obj, media.Video) and other_obj.dl_flag \
                and other_obj.live_mode:
                    other_obj.set_archive_flag(archive_flag)

        elif media_data_obj == self.fixed_missing_folder:

            # Check videos in this folder
            for other_obj in self.fixed_missing_folder.child_list:

                if isinstance(other_obj, media.Video) and other_obj.dl_flag \
                and other_obj.missing_flag:
                    other_obj.set_archive_flag(archive_flag)

        elif media_data_obj == self.fixed_new_folder:

            # Check videos in this folder
            for other_obj in self.fixed_new_folder.child_list:

                if isinstance(other_obj, media.Video) and other_obj.dl_flag \
                and other_obj.new_flag:
                    other_obj.set_archive_flag(archive_flag)

        elif not archive_flag and media_data_obj == self.fixed_waiting_folder:

            # Check videos in this folder
            for other_obj in self.fixed_waiting_folder.child_list:

                if isinstance(other_obj, media.Video) and other_obj.dl_flag \
                and other_obj.waiting_flag:
                    other_obj.set_archive_flag(archive_flag)

        elif only_child_videos_flag:

            # Check videos in this channel/playlist/folder
            for other_obj in media_data_obj.child_list:

                if isinstance(other_obj, media.Video):
                    other_obj.set_archive_flag(archive_flag)

        else:

            # Check videos in this channel/playlist/folder, and in any
            #   descendant channels/playlists/folders
            for other_obj in media_data_obj.compile_all_videos( [] ):

                if isinstance(other_obj, media.Video) and other_obj.dl_flag:
                    other_obj.set_archive_flag(archive_flag)

        # In all cases, update the row on the Video Index
        self.main_win_obj.video_index_update_row_icon(media_data_obj)
        self.main_win_obj.video_index_update_row_text(media_data_obj)
        # If this container is the one visible in the Video Catalogue, redraw
        #   the Video Catalogue
        if self.main_win_obj.video_index_current == media_data_obj.name:
            self.main_win_obj.video_catalogue_redraw_all(
                self.main_win_obj.video_index_current,
            )


    def mark_container_favourite(self, media_data_obj, fav_flag,
    only_child_videos_flag):

        """Called by mainwin.MainWin.on_video_index_mark_favourite() and
        .on_video_index_mark_not_favourite().

        Marks this channel, playlist or folder as favourite (or not favourite).
        Also marks any descendant videos as (not) favourite (but not descendent
        channels, playlists or folders).

        Args:

            media_data_obj (media.Channel, media.Playlist or media.Folder):
                The container object to update

            fav_flag (bool): True to mark as favourite, False to mark as not
                favourite

            only_child_videos_flag (bool): Set to True if only child video
                objects should be marked; False if the container object and all
                its descendants should be marked

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 10930 mark_container_favourite')

        if isinstance(media_data_obj, media.Video):
            return self.system_error(
                143,
                'Mark container as favourite request failed sanity check',
            )

        # Special arrangements for private folders. Mark the videos as
        #   favourite, but don't modify their parent channels, playlists and
        #   folders
        # (For the private 'Favourite Videos' folder, don't need to do anything
        #   if 'fav_flag' is True, because the popup menu item is desensitised)
        video_list = []

        if media_data_obj == self.fixed_all_folder:

            # Check every video
            for other_obj in list(self.media_reg_dict.values()):

                if isinstance(other_obj, media.Video):
                    video_list.append(other_obj)

        elif media_data_obj == self.fixed_bookmark_folder:

            # Check videos in this folder
            for other_obj in self.fixed_bookmark_folder.child_list:

                if isinstance(other_obj, media.Video) \
                and other_obj.bookmark_flag:
                    video_list.append(other_obj)

        elif not flag and media_data_obj == self.fixed_fav_folder:

            # Check videos in this folder
            for other_obj in self.fixed_fav_folder.child_list:

                if isinstance(other_obj, media.Video) \
                and other_obj.fav_flag:
                    video_list.append(other_obj)

        elif media_data_obj == self.fixed_live_folder:

            # Check videos in this folder
            for other_obj in self.fixed_live_folder.child_list:

                if isinstance(other_obj, media.Video) \
                and other_obj.live_mode:
                    video_list.append(other_obj)

        elif media_data_obj == self.fixed_missing_folder:

            # Check videos in this folder
            for other_obj in self.fixed_missing_folder.child_list:

                if isinstance(other_obj, media.Video) \
                and other_obj.missing_flag:
                    video_list.append(other_obj)

        elif media_data_obj == self.fixed_new_folder:

            # Check videos in this folder
            for other_obj in self.fixed_new_folder.child_list:

                if isinstance(other_obj, media.Video) \
                and other_obj.new_flag:
                    video_list.append(other_obj)

        elif media_data_obj == self.fixed_waiting_folder:

            # Check videos in this folder
            for other_obj in self.fixed_waiting_folder.child_list:

                if isinstance(other_obj, media.Video) \
                and other_obj.waiting_flag:
                    video_list.append(other_obj)

        elif only_child_videos_flag:

            # Check only videos that are children of the specified media data
            #   object
            for other_obj in media_data_obj.child_list:

                if isinstance(other_obj, media.Video):
                    video_list.append(other_obj)

        else:

            # Check only video objects that are descendants of the specified
            #   media data object
            for other_obj in media_data_obj.compile_all_videos( [] ):

                if isinstance(other_obj, media.Video):
                    video_list.append(other_obj)
                else:
                    # For channels, playlists and folders, we can set the IV
                    #   directly
                    other_obj.set_fav_flag(fav_flag)

            # The channel, playlist or folder itself is also marked as
            #   favourite (obviously, we don't do that for private folders)
            media_data_obj.set_fav_flag(fav_flag)

        # Take action, depending on how many videos there are
        count = len(video_list)

        if not count:

            # Just update the row on the Video Index
            self.main_win_obj.video_index_update_row_icon(media_data_obj)
            self.main_win_obj.video_index_update_row_text(media_data_obj)

        elif count < self.main_win_obj.mark_video_lower_limit:

            # The operation should be quick
            for child_obj in video_list:
                self.mark_video_favourite(child_obj, fav_flag)

        elif count < self.main_win_obj.mark_video_higher_limit:

            # This will take a few seconds, so don't prompt the user
            self.prepare_mark_video(
                ['favourite', fav_flag, media_data_obj, video_list],
            )

        else:

            # This might take a few tens of seconds, so prompt the user for
            #   confirmation first
            media_type = media_data_obj.get_type()
            if media_type == 'channel':
                msg = _(
                    'The channel contains {0} item(s), so this action may' \
                    + ' take a while',
                ).format(str(count))

            elif media_type == 'playlist':
                msg = _(
                    'The playlist contains {0} item(s), so this action may' \
                    + ' take a while',
                ).format(str(count))

            else:
                msg = _(
                    'The folder contains {0} item(s), so this action may' \
                    + ' take a while',
                ).format(str(count))

            msg += '\n\n' + _('Are you sure you want to continue?')

            self.dialogue_manager_obj.show_msg_dialogue(
                msg,
                'question',
                'yes-no',
                None,                   # Parent window is main window
                {
                    'yes': 'prepare_mark_video',
                    # Specified options
                    'data': \
                    ['favourite', fav_flag, media_data_obj, video_list],
                },
            )


    def mark_container_missing(self, media_data_obj, missing_flag):

        """Called by mainwin.MainWin.on_video_index_mark_missing() and
        .on_video_index_mark_not_missing().

        Marks this channel or playlist as missing (or not missing). Note that
        this function can't be called for folders (except for the fixed
        'Missing Videos' folder).

        Args:

            media_data_obj (media.Channel, media.Playlist or media.Folder):
                The container object to update

            missing_flag (bool): True to mark as missing, False to mark as not
                missing

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 10931 mark_container_missing')

        if isinstance(media_data_obj, media.Video) \
        or (
            isinstance(media_data_obj, media.Folder) \
            and media_data_obj != self.fixed_missing_folder
        ):
            return self.system_error(
                163,
                'Mark container as missing request failed sanity check',
            )

        # Special arrangements for the 'Missing Videos'f older. Mark the
        #   videos as missing, but don't modify their parent channels,
        #   playlists and folders
        video_list = []

        if media_data_obj == self.fixed_missing_folder:

            # Check videos in this folder
            for other_obj in self.fixed_missing_folder.child_list:

                if isinstance(other_obj, media.Video) \
                and other_obj.missing_flag:
                    video_list.append(other_obj)

        else:

            # Check only videos that are children of the specified media data
            #   object
            for other_obj in media_data_obj.child_list:

                if isinstance(other_obj, media.Video):
                    video_list.append(other_obj)

        # Take action, depending on how many videos there are
        count = len(video_list)

        if not count:

            # Just update the row on the Video Index
            self.main_win_obj.video_index_update_row_icon(media_data_obj)
            self.main_win_obj.video_index_update_row_text(media_data_obj)

        elif count < self.main_win_obj.mark_video_lower_limit:

            # The operation should be quick
            for child_obj in video_list:
                self.mark_video_missing(child_obj, missing_flag)

        elif count < self.main_win_obj.mark_video_higher_limit:

            # This will take a few seconds, so don't prompt the user
            self.prepare_mark_video(
                ['missing', missing_flag, media_data_obj, video_list],
            )

        else:

            # This might take a few tens of seconds, so prompt the user for
            #   confirmation first
            media_type = media_data_obj.get_type()
            if media_type == 'channel':
                msg = _(
                    'The channel contains {0} item(s), so this action may' \
                    + ' take a while',
                ).format(str(count))

            elif media_type == 'playlist':
                msg = _(
                    'The playlist contains {0} item(s), so this action may' \
                    + ' take a while',
                ).format(str(count))

            else:
                msg = _(
                    'The folder contains {0} item(s), so this action may' \
                    + ' take a while',
                ).format(str(count))

            msg += '\n\n' + _('Are you sure you want to continue?')

            self.dialogue_manager_obj.show_msg_dialogue(
                msg,
                'question',
                'yes-no',
                None,                   # Parent window is main window
                {
                    'yes': 'prepare_mark_video',
                    # Specified options
                    'data': \
                    ['missing', missing_flag, media_data_obj, video_list],
                },
            )


    def mark_container_new(self, media_data_obj, new_flag,
    only_child_videos_flag):

        """Called by mainwin.MainWin.on_video_index_mark_new() and
        .on_video_index_mark_not_new().

        Marks videos in this channel, playlist or folder as new (or not new).
        Also marks any descendant videos as (not) new (but not descendent
        channels, playlists or folders).

        Unlike self.mark_container_favourite, the container itself is not
        marked as new.

        Args:

            media_data_obj (media.Channel, media.Playlist or media.Folder):
                The container object to update

            new_flag (bool): True to mark as new, False to mark as not
                new

            only_child_videos_flag (bool): Set to True if only child video
                objects should be marked; False if the container object and all
                its descendants should be marked

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 11113 mark_container_new')

        if isinstance(media_data_obj, media.Video):
            return self.system_error(
                144,
                'Mark container as new request failed sanity check',
            )

        # Special arrangements for private folders
        # (For the private 'Favourite Videos' folder, don't need to do anything
        #   if 'new_flag' is True, because the popup menu item is desensitised)
        video_list = []

        if media_data_obj == self.fixed_all_folder:

            # Check every video
            for other_obj in list(self.media_reg_dict.values()):

                if isinstance(other_obj, media.Video):
                    video_list.append(other_obj)

        elif media_data_obj == self.fixed_bookmark_folder:

            # Check videos in this folder
            for other_obj in self.fixed_bookmark_folder.child_list:

                if isinstance(other_obj, media.Video) \
                and other_obj.bookmark_flag:
                    video_list.append(other_obj)

        elif not flag and media_data_obj == self.fixed_fav_folder:

            # Check videos in this folder
            for other_obj in self.fixed_fav_folder.child_list:

                if isinstance(other_obj, media.Video) \
                and other_obj.fav_flag:
                    video_list.append(other_obj)

        elif media_data_obj == self.fixed_live_folder:

            # Check videos in this folder
            for other_obj in self.fixed_live_folder.child_list:

                if isinstance(other_obj, media.Video) \
                and other_obj.live_mode:
                    video_list.append(other_obj)

        elif media_data_obj == self.fixed_missing_folder:

            # Check videos in this folder
            for other_obj in self.fixed_missing_folder.child_list:

                if isinstance(other_obj, media.Video) \
                and other_obj.missing_flag:
                    video_list.append(other_obj)

        elif media_data_obj == self.fixed_waiting_folder:

            # Check videos in this folder
            for other_obj in self.fixed_waiting_folder.child_list:

                if isinstance(other_obj, media.Video) \
                and other_obj.waiting_flag:
                    video_list.append(other_obj)

        elif only_child_videos_flag:

            # Check only videos that are children of the specified media data
            #   object
            for other_obj in media_data_obj.child_list:

                if isinstance(other_obj, media.Video):
                    video_list.append(other_obj)

        else:

            # Check only video objects that are descendants of the specified
            #   media data object
            for other_obj in media_data_obj.compile_all_videos( [] ):

                # (Only downloaded videos can be marked as new)
                if not new_flag or other_obj.dl_flag:
                    video_list.append(other_obj)

        # Take action, depending on how many videos there are
        count = len(video_list)

        if not count:

            # Just update the row on the Video Index
            self.main_win_obj.video_index_update_row_icon(media_data_obj)
            self.main_win_obj.video_index_update_row_text(media_data_obj)

        elif count < self.main_win_obj.mark_video_lower_limit:

            # The operation should be quick
            for child_obj in video_list:
                self.mark_video_new(child_obj, new_flag)

        elif count < self.main_win_obj.mark_video_higher_limit:

            # This will take a few seconds, so don't prompt the user
            self.prepare_mark_video(
                ['new', new_flag, media_data_obj, video_list],
            )

        else:

            # This might take a few tens of seconds, so prompt the user for
            #   confirmation first
            media_type = media_data_obj.get_type()
            if media_type == 'channel':
                msg = _(
                    'The channel contains {0} item(s), so this action may' \
                    + ' take a while',
                ).format(str(count))

            elif media_type == 'playlist':
                msg = _(
                    'The playlist contains {0} item(s), so this action may' \
                    + ' take a while',
                ).format(str(count))

            else:
                msg = _(
                    'The folder contains {0} item(s), so this action may' \
                    + ' take a while',
                ).format(str(count))

            msg += '\n\n' + _('Are you sure you want to continue?')

            self.dialogue_manager_obj.show_msg_dialogue(
                msg,
                'question',
                'yes-no',
                None,                   # Parent window is main window
                {
                    'yes': 'prepare_mark_video',
                    # Specified options
                    'data': ['new', new_flag, media_data_obj, video_list],
                },
            )


    def rename_container(self, media_data_obj):

        """Called by mainwin.MainWin.on_video_index_rename_location().

        Renames a channel, playlist or folder. Also renames the corresponding
        directory in Tartube's data directory.

        Args:

            media_data_obj (media.Channel, media.Playlist, media.Folder): The
                media data object to be renamed

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 11264 rename_container')

        # Do some basic checks
        if media_data_obj is None or isinstance(media_data_obj, media.Video) \
        or self.current_manager_obj or self.main_win_obj.config_win_list \
        or (
            isinstance(media_data_obj, media.Folder) \
            and media_data_obj.fixed_flag
        ):
            return self.system_error(
                145,
                'Rename container request failed sanity check',
            )

        # Prompt the user for a new name
        dialogue_win = mainwin.RenameContainerDialogue(
            self.main_win_obj,
            media_data_obj,
        )

        response = dialogue_win.run()

        # Retrieve user choices from the dialogue window, before destroying it
        new_name = dialogue_win.entry.get_text()
        dialogue_win.destroy()

        if response == Gtk.ResponseType.OK and new_name != '' \
        and new_name != media_data_obj.name:

            # Check that the name is legal
            if new_name is None \
            or re.match('\s*$', new_name) \
            or not self.check_container_name_is_legal(new_name):
                return self.dialogue_manager_obj.show_msg_dialogue(
                    _('The name \'{0}\' is not allowed').format(new_name),
                    'error',
                    'ok',
                )

            # Check that an existing channel/playlist/folder isn't already
            #   using this name
            if new_name in self.media_name_dict:
                return self.dialogue_manager_obj.show_msg_dialogue(
                    _('The name \'{0}\' is already in use').format(new_name),
                    'error',
                    'ok',
                )

            # Attempt to rename the sub-directory itself
            old_dir = media_data_obj.get_default_dir(self)
            new_dir = media_data_obj.get_default_dir(self, new_name)
            try:
                shutil.move(old_dir, new_dir)

            except:
                return self.dialogue_manager_obj.show_msg_dialogue(
                    _('Failed to rename \'{0}\'').format(media_data_obj.name),
                    'error',
                    'ok',
                )

            # Filesystem updated, so now update the media data object itself.
            #   This call also updates the object's .nickname IV
            old_name = media_data_obj.name
            media_data_obj.set_name(new_name)
            # Update the media data registry
            del self.media_name_dict[old_name]
            self.media_name_dict[new_name] = media_data_obj.dbid

            # Reset the Video Index and the Video Catalogue (this prevents a
            #   lot of problems)
            self.main_win_obj.video_index_catalogue_reset()

            # Save the database file (since the filesystem itself has changed)
            self.save_db()


    def rename_container_silently(self, media_data_obj, new_name):

        """Called by self.load_db() and .rename_fixed_folder().

        A modified form of self.rename_container. No dialogue windows are used,
        no widgets are updated or desensitised, and the Tartube database file
        is not saved.

        No checks are carried out; it's up to the calling function to check
        this function's return value, and respond appropriately.

        Renames a channel, playlist or folder. Also renames the corresponding
        directory in Tartube's data directory.


        Args:

            media_data_obj (media.Channel, media.Playlist, media.Folder): The
                media data object to be renamed

            new_name (str): The object's new name

        Returns:

            True on success, False on failure

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 11370 rename_container_silently')

        # Nothing in the Tartube code should be capable of calling this
        #   function with an illegal name, but we'll still check
        if not self.check_container_name_is_legal(new_name):
            self.system_error(
                146,
                'Illegal container name',
            )

            return False

        # Attempt to rename the sub-directory itself
        # (Private folders don't have a sub-directory to rename, so check for
        #   that)
        if not media_data_obj.priv_flag:
            old_dir = media_data_obj.get_default_dir(self)
            new_dir = media_data_obj.get_default_dir(self, new_name)
            try:
                shutil.move(old_dir, new_dir)

            except:
                return False

        # Filesystem updated, so now update the media data object itself. This
        #   call also updates the object's .nickname IV
        old_name = media_data_obj.name
        media_data_obj.set_name(new_name)
        # Update the media data registry
        del self.media_name_dict[old_name]
        self.media_name_dict[new_name] = media_data_obj.dbid

        return True


    def apply_download_options(self, media_data_obj):

        """Called by mainwin.MainWin.on_video_index_apply_options() and
        config.GenericEditWin.on_button_apply_options_clicked().

        Applies a download options object (options.OptionsManager) to a media
        data object, and also to any of its descendants (unless they too have
        an applied download options object).

        The download options are passed to youtube-dl during a download
        operation.

        Args:

            media_data_obj (media.Video, media.Channel, media.Playlist or
                media.Folder): The media data object to which the download
                options are applied.

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 11426 apply_download_options')

        if self.current_manager_obj \
        or media_data_obj.options_obj\
        or (
            isinstance(media_data_obj, media.Folder)
            and media_data_obj.priv_flag
        ):
            return self.system_error(
                147,
                'Apply download options request failed sanity check',
            )

        # Apply download options to the media data object
        media_data_obj.set_options_obj(options.OptionsManager())
        # If required, clone download options from the General Options Manager
        #   into the new download options manager
        if self.auto_clone_options_flag:
            media_data_obj.options_obj.clone_options(
                self.general_options_obj,
            )

        # Update the row in the Video Index
        self.main_win_obj.video_index_update_row_icon(media_data_obj)


    def remove_download_options(self, media_data_obj):

        """Called by callbacks in
        mainwin.MainWin.on_video_index_remove_options() and
        GenericEditWin.on_button_remove_clicked().

        Removes a download options object (options.OptionsManager) from a media
        data object, an action which also affects its descendants (unless they
        too have an applied download options object).

        Args:

            media_data_obj (media.Video, media.Channel, media.Playlist or
                media.Folder): The media data object from which the download
                options are removed.

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 11471 remove_download_options')

        if self.current_manager_obj or not media_data_obj.options_obj:
            return self.system_error(
                148,
                'Remove download options request failed sanity check',
            )

        # Remove download options from the media data object
        media_data_obj.set_options_obj(None)
        # Update the row in the Video Index
        self.main_win_obj.video_index_update_row_icon(media_data_obj)


    def apply_classic_downoad_options(self):

        """Called by mainwin.MainWin.on_classic_menu_apply_options().

        Also called by self.start().

        A modified version of self.apply_download_options.

        Creates a download options object (options.OptionsManager) for use only
        in the Classic Mode Tab.

        The download options are passed to youtube-dl during a download
        operation.

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 11472 apply_classic_downoad_options')

        if self.current_manager_obj or self.classic_options_obj:
            return self.system_error(
                159,
                'Apply download options request failed sanity check',
            )

        # Apply download options
        self.classic_options_obj = options.OptionsManager()
        # If required, clone download options from the General Options Manager
        #   into the new download options manager
        if self.auto_clone_options_flag:
            self.classic_options_obj.clone_options(
                self.general_options_obj,
            )

        # Disable downloading the description, annotations (etc) files
        self.classic_options_obj.set_classic_mode_options()


    def remove_classic_downoad_options(self):

        """Called by mainwin.MainWin.on_classic_menu_remove_options().

        A modified version of self.remove_download_options().

        Removes the download options object (options.OptionsManager) used only
        in the Classic Mode Tab.

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 11473 remove_classic_downoad_options')

        if self.current_manager_obj or not self.classic_options_obj:
            return self.system_error(
                160,
                'Remove download options request failed sanity check',
            )

        # Remove download options
        self.classic_options_obj = None


    def check_container_name_is_legal(self, name):

        """Can be called by anything.

        Checks that the name of a channel, playlist or folder is legal, i.e.
        that it doesn't match one of the regexes in
        self.illegal_name_regex_list.

        Does not check whether an existing container is already using the name;
        that's the responsibility of the calling code.

        Args:

            name (str): A proposed name for a media.Channel, media.Playlist or
                media.Folder object

        Returns:

            True if the name is legal, False if it is illegal

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 11508 check_container_name_is_legal')

        for regex in self.illegal_name_regex_list:
            if re.search(regex, name, re.IGNORECASE):
                # Illegal name
                return False

        # Legal name
        return True


    # (Export/import data to/from the Tartube database)

    def export_from_db(self, media_list):

        """Called by self.on_menu_export_db() and
        mainwin.MainWin.on_video_index_export().

        Exports a summary of the Tartube database to an export file - either a
        structured JSON file, or a plain text file, at the user's option.

        The export file typically contains a list of videos, channels,
        playlists and folders, but not any downloaded files (videos,
        thumbnails, etc).

        The export file is not the same as a Tartube database file (usually
        tartube.db) and cannot be loaded as a database file. However, the
        export file can be imported into an existing database.

        Args:

            media_list (list): A list of media data objects. If specified, only
                those objects (and any media data objects they contain) are
                included in the export. If an empty list is passed, the whole
                database is included.

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 11547 export_from_db')

        # If the specified list is empty, a summary of the whole database is
        #   exported
        if not media_list:
            whole_flag = True
        else:
            whole_flag = False

        # Prompt the user for which kinds of media data object should be
        #   included in the export, and which type of file (JSON or plain text)
        #   should be created
        dialogue_win = mainwin.ExportDialogue(self.main_win_obj, whole_flag)
        response = dialogue_win.run()

        # Retrieve user choices from the dialogue window...
        include_video_flag = dialogue_win.checkbutton.get_active()
        include_channel_flag = dialogue_win.checkbutton2.get_active()
        include_playlist_flag = dialogue_win.checkbutton3.get_active()
        preserve_folder_flag = dialogue_win.checkbutton4.get_active()
        plain_text_flag = dialogue_win.checkbutton5.get_active()
        # ...before destroying the dialogue window
        dialogue_win.destroy()

        if response != Gtk.ResponseType.OK:
            return

        # Prompt the user for the file path to use
        file_chooser_win = Gtk.FileChooserDialog(
            _('Select where to save the database export'),
            self.main_win_obj,
            Gtk.FileChooserAction.SAVE,
            (
                Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                Gtk.STOCK_OPEN, Gtk.ResponseType.OK,
            ),
        )

        if not plain_text_flag:
            file_chooser_win.set_current_name(self.export_json_file_name)
        else:
            file_chooser_win.set_current_name(self.export_text_file_name)

        response = file_chooser_win.run()
        if response != Gtk.ResponseType.OK:
            file_chooser_win.destroy()
            return

        file_path = file_chooser_win.get_filename()
        file_chooser_win.destroy()
        if not file_path:
            return

        # Compile a dictionary of data to export, representing the contents of
        #   the database (in whole or in part)
        # Throughout the export/import code, dictionaries in this form are
        #   called 'db_dict'
        # Depending on the user's choices, the dictionary preserves the folder
        #   structure of the database (or not)
        #
        # Key-value pairs in the dictionary are in the form
        #
        #       dbid: mini_dict
        #
        # 'dbid' is each media data object's .dbid
        # 'mini_dict' is a dictionary of values representing a media data
        #   object
        #
        # The same 'mini_dict' structure is used during export and
        #   import procedures. Its keys are:
        #
        #       type        - set to 'video', 'channel', 'playlist' or 'folder'
        #       dbid        - set to the media data object's .dbid
        #       name        - set to the media data object's .name IV
        #       nickname    - set to the media data object's .nickname IV (or
        #                       None for videos)
        #       source      - set to the media data object's .source IV (or
        #                       None for folders)
        #       db_dict     - the children of this media data object, stored in
        #                       the form described above
        #
        # The import process adds some extra keys to a 'mini_dict' while
        #   processing it, but only for channels/playlists/folders. The extra
        #   keys are:
        #
        #       display_name
        #               - the media data object's name, indented for display
        #                   in mainwin.ImportDialogueWin
        #       video_count
        #               - the number of videos this media data object contains
        #       import_flag
        #               - True if the user has selected this media data object
        #                   to be imported, False if they have deselected it
        db_dict = {}

        # Compile the contents of the 'db_dict' to export
        # If the media_list argument is empty, use the whole database.
        #   Otherwise, use only the specified media data objects (and any media
        #   data objects they contain)
        if preserve_folder_flag and not plain_text_flag:

            if media_list:

                for media_data_obj in media_list:

                    mini_dict = media_data_obj.prepare_export(
                        include_video_flag,
                        include_channel_flag,
                        include_playlist_flag,
                    )

                    if mini_dict:
                        db_dict[media_data_obj.dbid] = mini_dict

            else:

                for dbid in self.media_top_level_list:

                    media_data_obj = self.media_reg_dict[dbid]

                    mini_dict = media_data_obj.prepare_export(
                        include_video_flag,
                        include_channel_flag,
                        include_playlist_flag,
                    )

                    if mini_dict:
                        db_dict[media_data_obj.dbid] = mini_dict

        else:

            if media_list:

                for media_data_obj in media_list:

                    db_dict = media_data_obj.prepare_flat_export(
                        db_dict,
                        include_video_flag,
                        include_channel_flag,
                        include_playlist_flag,
                    )

            else:

                for dbid in self.media_top_level_list:

                    media_data_obj = self.media_reg_dict[dbid]

                    db_dict = media_data_obj.prepare_flat_export(
                        db_dict,
                        include_video_flag,
                        include_channel_flag,
                        include_playlist_flag,
                    )

        if not db_dict:

            return self.dialogue_manager_obj.show_msg_dialogue(
                _('There is nothing to export!'),
                'error',
                'ok',
            )

        # Export a JSON file
        if not plain_text_flag:

            # The exported JSON file has the same metadata as a config file,
            #   with only the 'file_type' being different

            # Prepare values
            utc = datetime.datetime.utcfromtimestamp(time.time())

            # Prepare a dictionary of data to save as a JSON file
            json_dict = {
                # Metadata
                'script_name': __main__.__packagename__,
                'script_version': __main__.__version__,
                'save_date': str(utc.strftime('%d %b %Y')),
                'save_time': str(utc.strftime('%H:%M:%S')),
                'file_type': 'db_export',
                # Data
                'db_dict': db_dict,
            }

            # Try to save the file
            try:
                with open(file_path, 'w') as outfile:
                    json.dump(json_dict, outfile, indent=4)

            except:
                return self.dialogue_manager_obj.show_msg_dialogue(
                    _('Failed to save the database export file'),
                    'error',
                    'ok',
                )

        # Export a plain text file
        else:

            # The text file contains lines, in groups of three, in the
            #   following format:
            #
            #       @type
            #       <name>
            #       <url>
            #
            # ...where '@type' is one of '@video', '@channel' or '@playlist'
            #   (the folder structure is never preserved in a plain text
            #   export)
            # A video belongs to the channel/playlist above it

            # Prepare the list of lines
            line_list = []

            for dbid in db_dict.keys():

                media_data_obj = self.media_reg_dict[dbid]

                if isinstance(media_data_obj, media.Channel):
                    line_list.append('@channel')
                    line_list.append(media_data_obj.name)
                    line_list.append(media_data_obj.source)

                elif isinstance(media_data_obj, media.Playlist):
                    line_list.append('@playlist')
                    line_list.append(media_data_obj.name)
                    line_list.append(media_data_obj.source)

                else:
                    continue

                if include_video_flag:

                    for child_obj in media_data_obj.child_list:
                        # (Nothing but videos should be in this list, but we'll
                        #   check anyway)
                        if isinstance(child_obj, media.Video):
                            line_list.append('@video')
                            line_list.append(child_obj.name)
                            line_list.append(child_obj.source)

            # Try to save the file
            try:
                with open(file_path, 'w') as outfile:
                    for line in line_list:
                        outfile.write(line + '\n')

            except:
                return self.dialogue_manager_obj.show_msg_dialogue(
                    _('Failed to save the database export file'),
                    'error',
                    'ok',
                )

        # Export was successful
        self.dialogue_manager_obj.show_msg_dialogue(
            _('Database export file saved to:') + '\n\n' + file_path,
            'info',
            'ok',
        )


    def import_into_db(self, json_flag):

        """Called by self.on_menu_import_json() and
        .on_menu_import_plain_text().

        Imports the contents of a JSON export file or a plain text export file
        generated by a call to self.export_from_db().

        After prompting the user, creates new media.Video, media.Channel,
        media.Playlist and/or media.Folder objects. Checks for duplicates and
        handles them appropriately.

        A JSON export file contains a dictionary, 'db_dict', containing further
        dictionaries, 'mini_dict', whose formats are described in the comments
        in self.export_from_db().

        A plain text export file contains lines in groups of three, in the
        format described in the comments in self.export_from_db().

        Args:

            json_flag (bool): True if a JSON export file should be imported,
                False if a plain text export file should be imported

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 11836 import_into_db')

        # Prompt the user for the export file to load
        file_chooser_win = Gtk.FileChooserDialog(
            _('Select the database export'),
            self.main_win_obj,
            Gtk.FileChooserAction.OPEN,
            (
                Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                Gtk.STOCK_OPEN, Gtk.ResponseType.OK,
            ),
        )

        response = file_chooser_win.run()
        if response != Gtk.ResponseType.OK:
            file_chooser_win.destroy()
            return

        file_path = file_chooser_win.get_filename()
        file_chooser_win.destroy()
        if not file_path:
            return

        # Try to load the export file
        if not json_flag:

            text = self.file_manager_obj.load_text(file_path)
            if text is None:
                return self.dialogue_manager_obj.show_msg_dialogue(
                    _('Failed to load the database export file'),
                    'error',
                    'ok',
                )

            # Parse the text file, creating a db_dict in the form described in
            #   the comments in self.export_from_db()
            db_dict = self.parse_text_import(text)

        else:

            json_dict = self.file_manager_obj.load_json(file_path)
            if not json_dict:
                return self.dialogue_manager_obj.show_msg_dialogue(
                    _('Failed to load the database export file'),
                    'error',
                    'ok',
                )

            # Do some basic checks on the loaded data
            # (At the moment, JSON export files are compatible with all
            #   versions of Tartube after v1.0.0; this may change in future)
            if not json_dict \
            or not 'script_name' in json_dict \
            or not 'script_version' in json_dict \
            or not 'save_date' in json_dict \
            or not 'save_time' in json_dict \
            or not 'file_type' in json_dict \
            or json_dict['script_name'] != __main__.__packagename__ \
            or json_dict['file_type'] != 'db_export':
                return self.dialogue_manager_obj.show_msg_dialogue(
                    _('The database export file is invalid'),
                    'error',
                    'ok',
                )

            # Retrieve the database data itself. db_dict is in the form
            #   described in the comments in self.export_from_db()
            db_dict = json_dict['db_dict']

        if not db_dict:
            return self.dialogue_manager_obj.show_msg_dialogue(
                _('The database export file is invalid (or empty)'),
                'error',
                'ok',
            )

        # Prompt the user to allow them to select which videos/channels/
        #   playlists/folders to actually import, and how to deal with
        #   duplicate channels/playlists/folders
        dialogue_win = mainwin.ImportDialogue(self.main_win_obj, db_dict)
        response = dialogue_win.run()

        # Retrieve user choices from the dialogue window, before destroying the
        #   dialogue window
        # 'flat_db_dict' is a flattened version of the imported 'db_dict' (i.e.
        #   with its folder structure removed), and with additional key-value
        #   pairs added to each 'mini_dict'. (The new key-value pairs are also
        #   described in the comments in self.export_from_db() )
        import_videos_flag = dialogue_win.checkbutton.get_active()
        merge_duplicates_flag = dialogue_win.checkbutton.get_active()
        flat_db_dict = dialogue_win.flat_db_dict
        dialogue_win.destroy()

        if response != Gtk.ResponseType.OK:
            return

        # Process the imported 'db_dict', creating new videos/channels/
        #   playlists/folders as required, and dealing appropriately with
        #   any duplicates
        (video_count, channel_count, playlist_count, folder_count) \
        = self.process_import(
            db_dict,                # The imported data
            flat_db_dict,           # The flattened version of that dictionary
            None,                   # No parent 'mini_dict' yet
            import_videos_flag,
            merge_duplicates_flag,
            0,                      # video_count
            0,                      # channel_count
            0,                      # playlist count
            0,                      # folder_count
        )

        if not video_count and not channel_count and not playlist_count \
        and not folder_count:
            self.dialogue_manager_obj.show_msg_dialogue(
                _('Nothing was imported from the database export file'),
                'error',
                'ok',
            )

        else:

            # Update the Video Catalogue, in case any new videos have been
            #   imported into it
            self.main_win_obj.video_catalogue_redraw_all(
                self.main_win_obj.video_index_current,
            )

            # Show a confirmation
            msg = _('Imported:') \
                + '\n\n' + _('Videos:') + ' ' + str(video_count) \
                + '\n\n' + _('Channels:') + ' ' + str(channel_count) \
                + '\n\n' + _('Playlists:') + ' ' + str(playlist_count) \
                + '\n\n' + _('Folders:') + ' ' + str(folder_count)

            self.dialogue_manager_obj.show_msg_dialogue(msg, 'info', 'ok')


    def parse_text_import(self, text):

        """Called by self.import_into_db().

        Given the contents of a plain text database export, which has been
        loaded into memory, convert the contents into the db_dict format
        described in the comments in self.export_from_db(), as if a JSON
        database export had been loaded.

        The text file contains lines, in groups of three, in the following
        format:

            @type
            <name>
            <url>

        ...where '@type' is one of '@video', '@channel' or '@playlist' (the
        folder structure is never preserved in a plain text export).

        A video belongs to the channel/playlist above it.

        Args:

            text (str): The contents of the loaded plain text file

        Returns:

            db_dict (dict): The converted data in the form described in the
                comments in self.export_from_db()

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 12007 parse_text_import')

        db_dict = {}
        dbid = 0
        last_container_mini_dict = None

        # Split text into separate lines
        line_list = text.split('\n')

        # Remove all empty lines (including those containing only whitespace)
        mod_list = []
        for line in line_list:
            if re.search('\S', line):
                mod_list.append(line)

        # Extract each group of three lines, and check they are valid
        # If a group of three is invalid (or if we reach the end of the file
        #   in the middle of a group of 3), ignore that group and any
        #   subsequent groups, and just use the data already extracted
        while len(mod_list) > 2:

            media_type = mod_list[0]
            name = mod_list[1]
            source = mod_list[2]

            mod_list = mod_list[3:]

            if media_type is None \
            or (
                media_type != '@video' and media_type != '@channel' \
                and media_type != '@playlist'
            ) \
            or name is None or name == '' \
            or source is None or not utils.check_url(source):
                break

            # A valid group of three; add an entry to db_dict using a fake dbid
            dbid += 1

            mini_dict = {
                'type': None,
                'dbid': dbid,
                'name': name,
                'nickname': name,
                'source': source,
                'db_dict': {},
            }

            if media_type == '@video':
                mini_dict['type'] = 'video'
                # A video belongs to the previous channel or playlist (if any)
                if last_container_mini_dict is not None:
                    last_container_mini_dict['db_dict'][dbid] = mini_dict

            elif media_type == '@channel':
                mini_dict['type'] = 'channel'
                last_container_mini_dict = mini_dict

            else:
                mini_dict['type'] = 'playlist'
                last_container_mini_dict = mini_dict

            db_dict[dbid] = mini_dict

        # Procedure complete
        return db_dict


    def process_import(self, db_dict, flat_db_dict, parent_obj,
    import_videos_flag, merge_duplicates_flag, video_count, channel_count,
    playlist_count, folder_count):

        """Called by self.import_into_db(). Subsequently called by this
        function recursively.

        Process a 'db_dict' (in the format described in the comments in
        self.export_from_db() ).

        Create new videos/channels/playlists/folders as required, and deal
        appropriately with any duplicates.

        Args:

            db_dict (dict): The dictionary described in self.export_from_db();
                if called from self.import_into_db(), the original imported
                dictionary; if called recursively, a dictionary from somewhere
                inside the original imported dictionary

            flat_db_dict (dict): A flattened version of the original imported
                'db_dict' (not necessarily the same 'db_dict' provided by the
                argument above). Flattened means that the folder structure has
                been removed, and additional key-value pairs have been added to
                each 'mini_dict'

            parent_obj (media.Channel, media.Playlist, media.Folder or None):
                The contents of db_dict are all children of this parent media
                data object

            import_videos_flag (bool): If True, any video objects are imported.
                If False, video objects are ignored

            merge_duplicates_flag (bool): If True, imported channels/playlists/
                folders with the same name (and source URL) as an existing
                channel/playlist/folder are merged with them. If False, the
                imported channel/playlist/folder is renamed

            video_count, channel_count, playlist_count, folder_count (int): The
                total number of videos/channels/playlists/folders imported so
                far

        Returns:

            video_count, channel_count, playlist_count, folder_count (int): The
                updated counts after importing videos/channels/playlists/
                folders

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 12126 process_import')

        # To optimise the code below, compile a dictionary for quick lookup,
        #   containing the source URLs for all videos in the parent channel/
        #   playlist/folder
        url_check_dict = {}
        if parent_obj:
            for child_obj in parent_obj.child_list:
                if isinstance(child_obj, media.Video) \
                and child_obj.source is not None:
                    url_check_dict[child_obj.source] = None

        # Deal in turn with each video/channel/playlist/folder stored at the
        #   top level of 'db_dict'
        # The dbid is the one used in the database from which the export file
        #   was generated. Once imported into our database, the new media data
        #   object will be given a different dbid
        # (In other words, we can't compare this dbid with those used in
        #   self.media_reg_dict)
        for dbid in db_dict.keys():

            media_data_obj = None

            # Each 'mini_dict' contains details for a single video/channel/
            #   playlist/folder
            mini_dict = db_dict[dbid]

            # Check whether the user has marked this item to be imported, or
            #   not
            if int(dbid) in flat_db_dict:

                check_dict = flat_db_dict[int(dbid)]
                if not check_dict['import_flag']:

                    # Don't import this one
                    continue

            # This item is marked to be imported
            if mini_dict['type'] == 'video':

                if import_videos_flag:

                    # Check that a video with the same URL doesn't already
                    #   exist in the parent channel/playlist/folder. If so,
                    #   don't import this duplicate video
                    if not mini_dict['source'] in url_check_dict:

                        # This video isn't a duplicate, so we can import it
                        video_obj = self.add_video(
                            parent_obj,
                            mini_dict['source'],
                        )

                        if video_obj:
                            video_count += 1
                            video_obj.set_name(mini_dict['name'])

            else:

                if mini_dict['name'] in self.media_name_dict:

                    old_dbid = self.media_name_dict[mini_dict['name']]
                    old_obj = self.media_reg_dict[old_dbid]

                    # A channel/playlist/folder with the same name already
                    #   exists in our database. Rename it if the user wants
                    #   that, or if the two have different source URLs
                    if not merge_duplicates_flag \
                    or old_obj.source != mini_dict['source']:

                        # Rename the imported channel/playlist/folder
                        mini_dict['name'] = self.rename_imported_container(
                            mini_dict['name'],
                        )

                        mini_dict['nickname'] = self.rename_imported_container(
                            mini_dict['nickname'],
                        )

                    else:

                        # Use the existing channel/playlist/folder of the same
                        #   name, thereby merging the two
                        old_dbid = self.media_name_dict[mini_dict['name']]
                        media_data_obj = self.media_reg_dict[old_dbid]

                # Import the channel/playlist/folder
                if mini_dict['type'] == 'channel':
                    media_data_obj = self.add_channel(
                        mini_dict['name'],
                        parent_obj,
                        mini_dict['source'],
                    )

                    if media_data_obj:
                        channel_count += 1

                elif mini_dict['type'] == 'playlist':
                    media_data_obj = self.add_playlist(
                        mini_dict['name'],
                        parent_obj,
                        mini_dict['source'],
                    )

                    if media_data_obj:
                        playlist_count += 1

                elif mini_dict['type'] == 'folder':
                    media_data_obj = self.add_folder(
                        mini_dict['name'],
                        parent_obj,
                    )

                    if media_data_obj:
                        folder_count += 1

                # If the channel/playlist/folder was successfully imported,
                #   set its nickname, update the Video Index, then deal with
                #   any children by calling this function recursively
                if media_data_obj is not None:

                    media_data_obj.set_nickname(mini_dict['nickname'])

                    self.main_win_obj.video_index_add_row(media_data_obj)

                    if mini_dict['db_dict']:

                        (
                            video_count, channel_count, playlist_count,
                            folder_count,
                        ) = self.process_import(
                            mini_dict['db_dict'],
                            flat_db_dict,
                            media_data_obj,
                            import_videos_flag,
                            merge_duplicates_flag,
                            video_count,
                            channel_count,
                            playlist_count,
                            folder_count,
                        )

        # Procedure complete
        return video_count, channel_count, playlist_count, folder_count


    def rename_imported_container(self, name):

        """Called by self.process_import().

        When importing a channel/playlist/folder whose name is the same as an
        existing channel/playlist/folder, this function is called to rename
        the imported one (when necessary).

        For example, converts 'Comedy' to 'Comedy (2)'.

        Args:

            name (str): The name of the imported channel/playlist/folder

        Returns:

            The converted name

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 12293 rename_imported_container')

        count = 1
        while True:

            count += 1
            new_name = name + ' (' + str(count) + ')'

            if not new_name in self.media_name_dict:
                return new_name


    # (Interact with media data objects)


    def watch_video_in_player(self, video_obj):

        """Can be called by anything.

        Watch a video using the system's default media player, first checking
        that a file actually exists.

        Args:

            video_obj (media.Video): The video to watch

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 12322 watch_video_in_player')

        path = video_obj.get_actual_path(self)

        if not os.path.isfile(path):

            self.dialogue_manager_obj.show_msg_dialogue(
                _(
                'The video file is missing from Tartube\'s data folder' \
                + ' (try downloading the video again!)',
                ),
                'error',
                'ok',
            )

        else:
            utils.open_file(path)


    def download_watch_videos(self, video_list, watch_flag=True):

        """Can be called by anything.

        Download the specified videos and, when they have been downloaded,
        launch them in the system's default media player.

        Args:

            video_list (list): List of media.Video objects to download and
                watch

            watch_flag (bool): If False, the video(s) are not launched in the
                system's default media player after being downloaded

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 12359 download_watch_videos')

        # Sanity check: this function is only for videos
        for video_obj in video_list:
            if not isinstance(video_obj, media.Video):
                return self.system_error(
                    149,
                    'Download and watch video request failed sanity check',
                )

        # Add the video to the list of videos to be launched in the system's
        #   default media player, the next time a download operation finishes
        if watch_flag:
            for video_obj in video_list:
                self.watch_after_dl_list.append(video_obj)

        if self.download_manager_obj:

            # Download operation already in progress. Add these videos to its
            #   list
            for video_obj in video_list:
                download_item_obj \
                = self.download_manager_obj.download_list_obj.create_item(
                    video_obj,
                    'real',
                    True,
                )

                if download_item_obj:

                    # Add a row to the Progress List
                    self.main_win_obj.progress_list_add_row(
                        download_item_obj.item_id,
                        video_obj,
                    )

                    # Update the main window's progress bar
                    self.download_manager_obj.nudge_progress_bar()

        else:

            # Start a new download operation to download this video
            self.download_manager_start('real', False, video_list)


    # (Options manager objects)


    def clone_general_options_manager(self, data_list):

        """Called by config.OptionsEditWin.on_clone_options_clicked().

        (Not called by self.apply_download_options(), which can handle its own
        cloning).

        Clones youtube-dl download options from the General Options manager
        into the specified download options manager.

        Args:

            data_list (list): List of values supplied by the dialogue window.
                The first is the edit window for the download options object
                (which must be reset). The second value is the download options
                manager object, into which new options will be cloned.

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 12426 clone_general_options_manager')

        edit_win_obj = data_list.pop(0)
        options_obj = data_list.pop(0)

        # Clone values from the general download options manager
        options_obj.clone_options(self.general_options_obj)
        # Reset the edit window to display the new (cloned) values
        edit_win_obj.reset_with_new_edit_obj(options_obj)


    def reset_options_manager(self, data_list):

        """Called by config.OptionsEditWin.on_reset_options_clicked().

        Resets the specified download options manager object, setting its
        options to their default values.

        Args:

            data_list (list): List of values supplied by the dialogue window.
                The first is the edit window for the download options object
                (which must be reset). The second optional value is the media
                data object to which the download options object belongs.

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 12454 reset_options_manager')

        edit_win_obj = data_list.pop(0)

        # Replace the old object with a new one, which has the effect of
        #   resetting its download options to the default values
        options_obj = options.OptionsManager()

        if data_list:

            # The Download Options object belongs to the specified media data
            #   object
            media_data_obj = data_list.pop(0)
            media_data_obj.set_options_obj(options_obj)

        else:

            # The General Download Options object
            self.general_options_obj = options_obj

        # Reset the edit window to display the new (default) values
        edit_win_obj.reset_with_new_edit_obj(options_obj)


    # (Sound effects)

    def play_sound(self, sound_name=None):

        """Can be called by anything.

        Plays the specified sound effect.

        Args:

            sound_name (str): The sound effect to play, one of the items in
                self.sound_list. If no sound effect is specified, plays the
                user's chosen sound effect, self.sound_custom

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 12495 play_sound')

        if sound_name is None:
            sound_name = self.sound_custom

        path = os.path.abspath(
            os.path.join(self.sound_dir, sound_name),
        )

        if os.path.isfile(path) and HAVE_PLAYSOUND_FLAG:

            # v2.1.025 - on a system on which the playsound module is not
            #   installed, I'm seeing (very rarely) a 'name 'playsound' is not
            #   defined' error
            # Cannot reproduce the problem, so enclose this code in a try block
            #   to prevent the error
            try:
                playsound.playsound(path)
            except:
                self.system_error(
                    161,
                    'System tried to play sound effect, even though Python' \
                    + ' playsound module was not detected',
                )


    # Callback class methods


    # (Timers)


    def script_slow_timer_callback(self):

        """Called by GObject timer created by self.start().

        A few times every minute, check whether it's time to perform a
        scheduled 'Download all' or 'Check all' download operation and, if so,
        perform it.

        Otherwise, check whether it's time to perform a scheduled livestream
        operation and, if so, perform it.

        Returns:

            1 to keep the timer going, or None to halt it

        """

        if DEBUG_FUNC_FLAG and not DEBUG_NO_TIMER_FUNC_FLAG:
            utils.debug_time('app 12531 script_slow_timer_callback')

        if not self.disable_load_save_flag \
        and not self.current_manager_obj \
        and not self.main_win_obj.config_win_list:

            if self.scheduled_dl_mode == 'scheduled':

                wait_time = self.scheduled_dl_wait_value \
                * formats.TIME_METRIC_DICT[self.scheduled_dl_wait_unit]

                if (self.scheduled_dl_last_time + wait_time) < time.time():

                    self.download_manager_start(
                        'real',     # 'Download all'
                        True,       # This function is the calling function
                    )

                    # Return 1 to keep the timer going
                    return 1

            elif self.scheduled_check_mode == 'scheduled':

                wait_time = self.scheduled_check_wait_value \
                * formats.TIME_METRIC_DICT[self.scheduled_check_wait_unit]

                if (self.scheduled_check_last_time + wait_time) < time.time():

                    self.download_manager_start(
                        'sim',      # 'Check all'
                        True,       # This function is the calling function
                    )

                    # Return 1 to keep the timer going
                    return 1

            # If no download operation was started, we're free to start a
            #   livestream operation instead (but only if there is at least one
            #   media.Video object marked as a livestream)
            if self.media_reg_live_dict:

                wait_time = self.scheduled_livestream_wait_mins * 60
                if (self.scheduled_livestream_last_time + wait_time) \
                < time.time():

                    self.livestream_manager_start()

                    # Return 1 to keep the timer going
                    return 1

        # Return 1 to keep the timer going
        return 1


    def script_fast_timer_callback(self):

        """Called by GObject timer created by self.start().

        Once a second, check whether there are any mainwin.Catalogue objects to
        add to the Video Catalogue and, if so, add them.

        Also checks whether a download operation that was due to beging at
        startup, should begin now. (For aesthetic reasons, we wait a few
        seconds before starting the scheduled operation).

        Returns:

            1 to keep the timer going, or None to halt it

        """

        if DEBUG_FUNC_FLAG and not DEBUG_NO_TIMER_FUNC_FLAG:
            utils.debug_time('app 12599 script_fast_timer_callback')

        # Update the Video Catalogue
        self.main_win_obj.video_catalogue_retry_insert_items()

        # Check scheduled operations
        current_time = time.time()
        if self.scheduled_dl_start_check_time is not None \
        and self.scheduled_dl_start_check_time < current_time:

            self.download_manager_start(
                'real',     # 'Download all'
                True,       # This function is the calling function
            )

        elif self.scheduled_check_start_check_time is not None \
        and self.scheduled_check_start_check_time < current_time:

            self.download_manager_start(
                'sim',      # 'Check all'
                True,       # This function is the calling function
            )

        # Return 1 to keep the timer going
        return 1


    def dl_timer_callback(self):

        """Called by GObject timer created by self.download_manager_continue().

        During a download operation, a GObject timer runs, so that the Progress
        Tab and Output Tab can be updated at regular intervals. (When the
        download operation is launched from the Classic Mode Tab, the
        Classic Progress List and Output Tab are updated.)

        There is also a delay between the instant at which youtube-dl reports a
        video file has been downloaded, and the instant at which it appears in
        the filesystem. The timer checks for newly-existing files at regular
        intervals, too.

        During download operations, youtube-dl output is temporarily stored
        (because Gtk widgets cannot be updated from within a thread). This
        function calls  mainwin.MainWin.output_tab_update_pages()  to display
        that output in the Output Tab.

        If required, this function periodically checks whether the device
        containing self.data_dir is running out of space (and halts the
        operation, if so.)

        Returns:

            1 to keep the timer going, or None to halt it

        """

        if DEBUG_FUNC_FLAG and not DEBUG_NO_TIMER_FUNC_FLAG:
            utils.debug_time('app 12656 dl_timer_callback')

        # This function behaves differently, if the download operation was
        #   launched from the Classic Mode Tab
        if not self.download_manager_obj \
        or self.download_manager_obj.operation_type != 'classic':
            classic_mode_flag = False
        else:
            classic_mode_flag = True

        # Periodically check (if required) whether the device is running out of
        #   disk space
        if self.dl_timer_disk_space_check_time is None:
            # First check occurs 60 seconds after the operation begins
            self.dl_timer_disk_space_check_time \
            = time.time() + self.dl_timer_disk_space_time

        elif self.dl_timer_disk_space_check_time < time.time():

            self.dl_timer_disk_space_check_time \
            = time.time() + self.dl_timer_disk_space_time

            disk_space = utils.disk_get_free_space(self.data_dir)

            if (
                self.disk_space_stop_flag \
                and self.disk_space_stop_limit != 0 \
                and disk_space <= self.disk_space_stop_limit
            ) or disk_space < self.disk_space_abs_limit:

                # Stop the download operation
                self.system_error(
                    150,
                    'Download operation halted because the device is running' \
                    + ' out of space',
                )

                self.download_manager_obj.stop_download_operation()
                # Return 1 to keep the timer going, which allows the operation
                #   to finish naturally
                return 1

        # Disk space check complete, now update main window widgets
        check_time = self.dl_timer_check_time
        if check_time is None or check_time > time.time():

            if not classic_mode_flag:
                self.main_win_obj.progress_list_display_dl_stats()
                self.main_win_obj.results_list_update_row()
            else:
                self.main_win_obj.classic_mode_tab_display_dl_stats()

            self.main_win_obj.output_tab_update_pages()
            if not classic_mode_flag and self.progress_list_hide_flag:
                self.main_win_obj.progress_list_check_hide_rows()

            if check_time is None:

                # Download operation still in progress, return 1 to keep the
                #   timer going
                return 1

            elif self.main_win_obj.results_list_temp_list:

                # Not all downloaded files confirmed to exist yet, so return 1
                #   to keep the timer going a little longer
                return 1

        # The download operation has finished. The call to
        #   self.download_manager_finished() destroys the timer
        self.download_manager_finished()


    def update_timer_callback(self):

        """Called by GObject timer created by self.update_manager_start().

        During an update operation, a GObject timer runs, so that the Output
        Tab can be updated at regular intervals.

        For the benefit of systems with Gtk < 3.24, the timer continues running
        for a few seconds at the end of the update operation.

        During update operations, messages generated by updates.UpdateManager
        are temporarily stored (because Gtk widgets cannot be updated from
        within a thread). This function calls
        mainwin.MainWin.output_tab_update_pages() to display those messages in
        the Output Tab.

        Returns:

            1 to keep the timer going

        """

        if DEBUG_FUNC_FLAG and not DEBUG_NO_TIMER_FUNC_FLAG:
            utils.debug_time('app 12752 update_timer_callback')

        if self.update_timer_check_time is None:

            self.main_win_obj.output_tab_update_pages()
            # Update operation still in progress, return 1 to keep the timer
            #   going
            return 1

        elif self.update_timer_check_time > time.time():

            self.main_win_obj.output_tab_update_pages()
            # Cooldown time not yet finished, return 1 to keep the timer going
            return 1

        else:
            # The update operation has finished. The call to
            #   self.update_manager_finished() destroys the timer
            self.update_manager_finished()


    def refresh_timer_callback(self):

        """Called by GObject timer created by self.refresh_manager_continue().

        During a refresh operation, a GObject timer runs, so that the Output
        Tab can be updated at regular intervals.

        For the benefit of systems with Gtk < 3.24, the timer continues running
        for a few seconds at the end of the refresh operation.

        During refresh operations, messages generated by refresh.RefreshManager
        are temporarily stored (because Gtk widgets cannot be updated from
        within a thread). This function calls
        mainwin.MainWin.output_tab_update_pages() to display those messages in
        the Output Tab.

        Returns:

            1 to keep the timer going

        """

        if DEBUG_FUNC_FLAG and not DEBUG_NO_TIMER_FUNC_FLAG:
            utils.debug_time('app 12796 refresh_timer_callback')

        if self.refresh_timer_check_time is None:

            self.main_win_obj.output_tab_update_pages()
            # Refresh operation still in progress, return 1 to keep the timer
            #   going
            return 1

        elif self.refresh_timer_check_time > time.time():

            self.main_win_obj.output_tab_update_pages()
            # Cooldown time not yet finished, return 1 to keep the timer going
            return 1

        else:
            # The refresh operation has finished. The call to
            #   self.refresh_manager_finished() destroys the timer
            self.refresh_manager_finished()


    def info_timer_callback(self):

        """Called by GObject timer created by self.info_manager_start().

        During an info operation, a GObject timer runs, so that the Output
        Tab can be updated at regular intervals.

        For the benefit of systems with Gtk < 3.24, the timer continues running
        for a few seconds at the end of the info operation.

        During info operations, messages generated by info.InfoManager
        are temporarily stored (because Gtk widgets cannot be updated from
        within a thread). This function calls
        mainwin.MainWin.output_tab_update_pages() to display those messages in
        the Output Tab.

        Returns:

            1 to keep the timer going

        """

        if DEBUG_FUNC_FLAG and not DEBUG_NO_TIMER_FUNC_FLAG:
            utils.debug_time('app 12840 info_timer_callback')

        if self.info_timer_check_time is None:

            self.main_win_obj.output_tab_update_pages()
            # Info operation still in progress, return 1 to keep the timer
            #   going
            return 1

        elif self.info_timer_check_time > time.time():

            self.main_win_obj.output_tab_update_pages()
            # Cooldown time not yet finished, return 1 to keep the timer going
            return 1

        else:
            # The info operation has finished. The call to
            #   self.info_manager_finished() destroys the timer
            self.info_manager_finished()


    def tidy_timer_callback(self):

        """Called by GObject timer created by self.tidy_manager_start().

        During a tidy operation, a GObject timer runs, so that the Output
        Tab can be updated at regular intervals.

        For the benefit of systems with Gtk < 3.24, the timer continues running
        for a few seconds at the end of the tidy operation.

        During tidy operations, messages generated by tidy.TidyManager
        are temporarily stored (because Gtk widgets cannot be updated from
        within a thread). This function calls
        mainwin.MainWin.output_tab_update_pages() to display those messages in
        the Output Tab.

        Returns:

            1 to keep the timer going

        """

        if DEBUG_FUNC_FLAG and not DEBUG_NO_TIMER_FUNC_FLAG:
            utils.debug_time('app 12884 tidy_timer_callback')

        if self.tidy_timer_check_time is None:

            self.main_win_obj.output_tab_update_pages()
            # Tidy operation still in progress, return 1 to keep the timer
            #   going
            return 1

        elif self.tidy_timer_check_time > time.time():

            self.main_win_obj.output_tab_update_pages()
            # Cooldown time not yet finished, return 1 to keep the timer going
            return 1

        else:
            # The tidy operation has finished. The call to
            #   self.tidy_manager_finished() destroys the timer
            self.tidy_manager_finished()


    # (Menu item and toolbar button callbacks)


    def on_button_apply_filter(self, action, par):

        """Called from a callback in self.do_startup().

        Applies a filter to the Video Catalogue, hiding any videos which don't
        match the search text specified by the user.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 12924 on_button_apply_filter')

        # Sanity check
        if not self.main_win_obj.video_catalogue_dict:
            return self.system_error(
                151,
                'Apply filter request failed sanity check',
            )

        # Apply the filter
        self.main_win_obj.video_catalogue_apply_filter()


    def on_button_cancel_filter(self, action, par):

        """Called from a callback in self.do_startup().

        Cancels the filter, restoring all hidden videos in the Video Catalogue.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 12952 on_button_cancel_filter')

        # Sanity check
        if not self.main_win_obj.video_catalogue_dict:
            return self.system_error(
                152,
                'Cancel filter request failed sanity check',
            )

        # Cancel the filter
        self.main_win_obj.video_catalogue_cancel_filter()


    def on_button_classic_add_urls(self, action, par):

        """Called from a callback in self.do_startup().

        In the Classic Mode Tab, transfers URLs in the textview into the
        Classic Progress List, creating a new dummy media.Video object for each
        URL, and updating IVs.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 12982 on_button_classic_add_urls')

        self.main_win_obj.classic_mode_tab_add_urls()


    def on_button_classic_dest_dir(self, action, par):

        """Called from a callback in self.do_startup().

        Opens the file chooser dialogue, so the user can set a new destination
        directory for videos downloaded in the Classic Mode Tab.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 13024 on_button_classic_dest_dir')

        file_chooser_win = Gtk.FileChooserDialog(
            _('Please select a destination folder'),
            self.main_win_obj,
            Gtk.FileChooserAction.SELECT_FOLDER,
            (
                Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                Gtk.STOCK_OPEN, Gtk.ResponseType.OK,
            ),
        )

        response = file_chooser_win.run()
        dest_dir = file_chooser_win.get_filename()
        file_chooser_win.destroy()

        if response == Gtk.ResponseType.OK:

            # Update IVs. Don't add a duplicate directory, but do move a
            #   duplicate to the top (and apply the maximum size, if required)
            mod_list = [dest_dir]
            for item in self.classic_dir_list:

                if item != dest_dir:
                    mod_list.append(item)

                    if len(mod_list) >= self.classic_dir_max:
                        break

            self.classic_dir_list = mod_list.copy()

            # Update the combo in the main window
            self.main_win_obj.classic_mode_tab_add_dest_dir()


    def on_button_classic_dest_dir_open(self, action, par):

        """Called from a callback in self.do_startup().

        Opens the directory for videos downloaded in the Classic Mode Tab.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 13025 on_button_classic_dest_dir_open')

        utils.open_file(self.classic_dir_list[0])


    def on_button_classic_download(self, action, par):

        """Called from a callback in self.do_startup().

        Starts a download operation for the URLs added to the Classic Progress
        List.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 13075 on_button_classic_download')

        # Start the download operation
        self.download_manager_start('classic')


    def on_button_classic_menu(self, action, par):

        """Called from a callback in self.do_startup().

        Opens a popup menu for the Classic Mode Tab.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 13076 on_button_classic_menu')

        # Open the popup menu
        self.main_win_obj.classic_popup_menu()


    def on_button_classic_move_up(self, action, par):

        """Called from a callback in self.do_startup().

        In the Classic Progress List, moves the selected item(s) up.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 13096 on_button_classic_move_up')

        self.main_win_obj.classic_mode_tab_move_row(True)


    def on_button_classic_move_down(self, action, par):

        """Called from a callback in self.do_startup().

        In the Classic Progress List, moves the selected item(s) down.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 13116 on_button_move_down_play')

        self.main_win_obj.classic_mode_tab_move_row(False)


    def on_button_classic_play(self, action, par):

        """Called from a callback in self.do_startup().

        Plays any videos downloaded from the selected rows in the Classic
        Progress List.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 13137 on_button_classic_play')

        selection = self.main_win_obj.classic_progress_treeview.get_selection()
        (model, path_list) = selection.get_selected_rows()
        if not path_list:

            # Nothing selected
            return

        # Get the the dummy media.Video objects for each selected row, and
        #   filter out those for which no video(s) have been downloaded
        video_list = []
        for path in path_list:

            this_iter = model.get_iter(path)
            dbid = model[this_iter][0]
            video_obj = self.main_win_obj.classic_media_dict[dbid]
            if video_obj.dummy_path is not None:
                video_list.append(video_obj.dummy_path)

        if not video_list:

            self.dialogue_manager_obj.show_msg_dialogue(
                _('No video(s) have been downloaded'),
                'error',
                'ok',
            )

        else:

            for video_path in video_list:
                utils.open_file(video_path)


    def on_button_classic_redownload(self, action, par):

        """Called from a callback in self.do_startup().

        Redownloads the selected rows in the Classic Progress List.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 13186 on_button_classic_redownload')

        selection = self.main_win_obj.classic_progress_treeview.get_selection()
        (model, path_list) = selection.get_selected_rows()
        if not path_list:

            # Nothing selected
            return

        # Get the dummy media.Video objects for each selected row
        video_list = []
        for path in path_list:

            this_iter = model.get_iter(path)
            dbid = model[this_iter][0]
            video_obj = self.main_win_obj.classic_media_dict[dbid]
            video_list.append(video_obj)

            # If mainapp.TartubeApp.allow_ytdl_archive_flag is set, youtube-dl
            #   will have created a ytdl_archive.txt, recording every video
            #   ever downloaded in the parent directory
            # This will prevent a successful re-downloading of the video(s).
            #   Change the name of the archive file temporarily; after the
            #   download operation is complete, the file is give its original
            #   name
            self.set_backup_archive(video_obj.dummy_dir)

        # Start the download operation
        self.download_manager_start('classic', False, video_list)


    def on_button_classic_remove(self, action, par):

        """Called from a callback in self.do_startup().

        Removes the selected rows from the Classic Progress List.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 13232 on_button_classic_remove')

        selection = self.main_win_obj.classic_progress_treeview.get_selection()
        (model, path_list) = selection.get_selected_rows()
        if not path_list:

            # Nothing selected
            return

        # Get the .dbid of the dummy media.Video objects for each selected
        #   row
        dbid_list = []
        for path in path_list:

            this_iter = model.get_iter(path)
            dbid_list.append(model[this_iter][0])

        # Prompt for confirmation
        msg = _('Are you sure you want to remove the selected item(s)?')

        self.dialogue_manager_obj.show_msg_dialogue(
            msg,
            'question',
           'yes-no',
            None,                   # Parent window is main window
            {
                'yes': 'main_win_classic_mode_tab_remove_rows',
                # Specified options
                'data': dbid_list,
            },
        )


    def on_button_classic_stop(self, action, par):

        """Called from a callback in self.do_startup().

        If a download operation is in progress, halts downloads for any of
        the selected rows in the Classic Progress List.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 13281 on_button_classic_stop')

        selection = self.main_win_obj.classic_progress_treeview.get_selection()
        (model, path_list) = selection.get_selected_rows()
        if not path_list:

            # Nothing selected
            return

        # Get the .dbid of the dummy media.Video objects for each selected
        #   row
        dbid_dict = {}
        for path in path_list:

            this_iter = model.get_iter(path)
            dbid_dict[model[this_iter][0]] = None

        # Now, if a download operation is in progress, stop any downloads
        #   matching one of these dbids
        if self.download_manager_obj:

            for worker_obj in self.download_manager_obj.worker_list:

                if worker_obj.running_flag \
                and worker_obj.download_item_obj \
                and worker_obj.download_item_obj.media_data_obj.dbid \
                in dbid_dict:
                    worker_obj.video_downloader_obj.stop()


    def on_button_find_date(self, action, par):

        """Called from a callback in self.do_startup().

        Changes the Video Catalogue page to the first one containing a video
        whose upload time is the first one on or after date specified by the
        user.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 13328 on_button_find_date')

        # Sanity check
        if not self.main_win_obj.video_catalogue_dict:
            return self.system_error(
                153,
                'Find videos by date request failed sanity check',
            )

        # Prompt the user for a new calendar date
        dialogue_win = mainwin.CalendarDialogue(self.main_win_obj)
        response = dialogue_win.run()

        # Retrieve user choices from the dialogue window, before destroying it
        if response == Gtk.ResponseType.OK:
            date_tuple = dialogue_win.calendar.get_date()

        dialogue_win.destroy()

        if response == Gtk.ResponseType.OK and date_tuple:

            year = date_tuple[0]            # e.g. 2011
            month = date_tuple[1] + 1       # Values in range 0-11
            day = date_tuple[2]             # Values in range 1-31

            # Convert the specified date into the epoch time at the start of
            #   that day
            epoch_time = datetime.datetime(year, month, day, 0, 0).timestamp()

            # Get the channel, playlist or folder currently visible in the
            #   Video Catalogue
            dbid = self.media_name_dict[self.main_win_obj.video_index_current]
            container_obj = self.media_reg_dict[dbid]

            count = 0
            for child_obj in container_obj.child_list:

                if isinstance(child_obj, media.Video) \
                and child_obj.upload_time is not None \
                and child_obj.upload_time < epoch_time:
                    break

                else:
                    count += 1

            # Find the corresponding page in the Video Catalogue...
            page_num = math.ceil(count / self.catalogue_page_size)
            # ...and make it visible
            self.main_win_obj.video_catalogue_redraw_all(
                self.main_win_obj.video_index_current,
                page_num,
                True,           # Reset scrollbars
                True,           # Don't cancel the filter, if applied
            )


    def on_button_first_page(self, action, par):

        """Called from a callback in self.do_startup().

        Changes the Video Catalogue page to the first one.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 13399 on_button_first_page')

        self.main_win_obj.video_catalogue_redraw_all(
            self.main_win_obj.video_index_current,
            1,
        )


    def on_button_last_page(self, action, par):

        """Called from a callback in self.do_startup().

        Changes the Video Catalogue page to the last one.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 13422 on_button_last_page')

        self.main_win_obj.video_catalogue_redraw_all(
            self.main_win_obj.video_index_current,
            self.main_win_obj.catalogue_toolbar_last_page,
        )


    def on_button_next_page(self, action, par):

        """Called from a callback in self.do_startup().

        Changes the Video Catalogue page to the next one.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 13445 on_button_next_page')

        self.main_win_obj.video_catalogue_redraw_all(
            self.main_win_obj.video_index_current,
            self.main_win_obj.catalogue_toolbar_current_page + 1,
        )


    def on_button_previous_page(self, action, par):

        """Called from a callback in self.do_startup().

        Changes the Video Catalogue page to the previous one.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 13468 on_button_previous_page')

        self.main_win_obj.video_catalogue_redraw_all(
            self.main_win_obj.video_index_current,
            self.main_win_obj.catalogue_toolbar_current_page - 1,
        )


    def on_button_scroll_down(self, action, par):

        """Called from a callback in self.do_startup().

        Scrolls the Video Catalogue page to the bottom.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 13491 on_button_scroll_down')

        adjust = self.main_win_obj.catalogue_scrolled.get_vadjustment()
        adjust.set_value(adjust.get_upper())


    def on_button_scroll_up(self, action, par):

        """Called from a callback in self.do_startup().

        Scrolls the Video Catalogue page to the top.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 13512 on_button_scroll_up')

        self.main_win_obj.catalogue_scrolled.get_vadjustment().set_value(0)


    def on_button_show_filter(self, action, par):

        """Called from a callback in self.do_startup().

        Reveals or hides another toolbar just below the Video Catalogue. The
        additional toolbar contains filter options.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 13533 on_button_show_filter')

        if not self.catalogue_show_filter_flag:
            self.catalogue_show_filter_flag = True
        else:
            self.catalogue_show_filter_flag = False

        # Update the button in the Video Catalogue's toolbar
        self.main_win_obj.update_show_filter_widgets()


    def on_button_sort_type(self, action, par):

        """Called from a callback in self.do_startup().

        Sets the type of sorting applied to the Video Catalogue: alphabetically
        or by date.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 13560 on_button_sort_type')

        # Sanity check
        if not self.main_win_obj.video_catalogue_dict:
            return self.system_error(
                154,
                'Change catalogue sort type request failed sanity check',
            )

        # Toggle the flag, and update the icon on the toolbutton
        if not self.catalogue_alpha_sort_flag:
            self.catalogue_alpha_sort_flag = True
        else:
            self.catalogue_alpha_sort_flag = False

        self.main_win_obj.update_alpha_sort_widgets()

        # Redraw the Video Catalogue, switching to the first page
        self.main_win_obj.video_catalogue_redraw_all(
            self.main_win_obj.video_index_current,
            1,
            True,           # Reset scrollbars
            True,           # Don't cancel the filter, if applied
        )


    def on_button_stop_operation(self, action, par):

        """Called from a callback in self.do_startup().

        Stops the current download/update/refresh/info/tidy operation (but not
        livestream operations, which run in the background and are halted
        immediately, if a different type of operation wants to start).

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 13603 on_button_stop_operation')

        self.operation_halted_flag = True

        # (The livestream operation runs silently in the background, so the
        #   toolbar button is desensitised and can't be used to stop it)
        if self.download_manager_obj:
            self.download_manager_obj.stop_download_operation()
        elif self.update_manager_obj:
            self.update_manager_obj.stop_update_operation()
        elif self.refresh_manager_obj:
            self.refresh_manager_obj.stop_refresh_operation()
        elif self.info_manager_obj:
            self.info_manager_obj.stop_info_operation()
        elif self.tidy_manager_obj:
            self.tidy_manager_obj.stop_tidy_operation()


    def on_button_switch_view(self, action, par):

        """Called from a callback in self.do_startup().

        Toggles between simple and complex views in the Video Catalogue, and
        between showing the names of each video's parent channel/playlist/
        folder

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 13638 on_button_switch_view')

        # There are four modes in a fixed sequence; switch to the next mode in
        #   the sequence
        if self.catalogue_mode == 'simple_hide_parent':
            self.catalogue_mode = 'simple_show_parent'
        elif self.catalogue_mode == 'simple_show_parent':
            self.catalogue_mode = 'complex_hide_parent'
        elif self.catalogue_mode == 'complex_hide_parent':
            self.catalogue_mode = 'complex_hide_parent_ext'
        elif self.catalogue_mode == 'complex_hide_parent_ext':
            self.catalogue_mode = 'complex_show_parent'
        elif self.catalogue_mode == 'complex_show_parent':
            self.catalogue_mode = 'complex_show_parent_ext'
        else:
            self.catalogue_mode = 'simple_hide_parent'

        # Redraw the Video Catalogue, but only if something was already drawn
        #   there (and keep the current page number)
        if self.main_win_obj.video_index_current is not None:
            self.main_win_obj.video_catalogue_redraw_all(
                self.main_win_obj.video_index_current,
                self.main_win_obj.catalogue_toolbar_current_page,
            )


    def on_button_use_regex(self, action, par):

        """Called from a callback in self.do_startup().

        When the user clicks the Regex togglebutton in the toolbar just below
        the Video Catalogue, updates IVs.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 13680 on_button_use_regex')

        # Sanity check
        if not self.main_win_obj.video_catalogue_dict:
            return self.system_error(
                155,
                'Use regex request failed sanity check',
            )

        if not self.main_win_obj.catalogue_regex_togglebutton.get_active():
            self.catologue_use_regex_flag = False
        else:
            self.catologue_use_regex_flag = True


    def on_menu_about(self, action, par):

        """Called from a callback in self.do_startup().

        Show a standard 'about' dialogue window.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 13710 on_menu_about')

        dialogue_win = Gtk.AboutDialog()
        dialogue_win.set_transient_for(self.main_win_obj)
        dialogue_win.set_destroy_with_parent(True)

        dialogue_win.set_program_name(__main__.__packagename__.title())
        dialogue_win.set_version('v' + __main__.__version__)
        dialogue_win.set_copyright(__main__.__copyright__)
        dialogue_win.set_license(__main__.__license__)
        dialogue_win.set_website(__main__.__website__)
        dialogue_win.set_website_label(
            __main__.__packagename__.title() + ' website'
        )
        dialogue_win.set_comments(__main__.__description__)
        dialogue_win.set_logo(
            self.main_win_obj.pixbuf_dict['system_icon'],
        )
        dialogue_win.set_authors(__main__.__author_list__)
        dialogue_win.set_title('')
        dialogue_win.connect('response', self.on_menu_about_close)

        dialogue_win.show()


    def on_menu_about_close(self, action, par):

        """Called from a callback in self.do_startup().

        Close the 'about' dialogue window.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 13750 on_menu_about_close')

        action.destroy()


    def on_menu_add_channel(self, action, par):

        """Called from a callback in self.do_startup().

        Creates a dialogue window to allow the user to specify a new channel.
        If the user specifies a channel, creates a media.Channel object.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 13771 on_menu_add_channel')

        keep_open_flag = True
        dl_sim_flag = False
        monitor_flag = False

        # If a folder (but not a channel/playlist) is selected in the Video
        #   Index, use that as the dialogue window's suggested parent folder
        suggest_parent_name = None
        if self.main_win_obj.video_index_current:
            dbid = self.media_name_dict[self.main_win_obj.video_index_current]
            container_obj = self.media_reg_dict[dbid]
            if isinstance(container_obj, media.Folder) \
            and not container_obj.fixed_flag \
            and not container_obj.restrict_flag:
                suggest_parent_name = container_obj.name

        while keep_open_flag:

            dialogue_win = mainwin.AddChannelDialogue(
                self.main_win_obj,
                suggest_parent_name,
                dl_sim_flag,
                monitor_flag,
            )

            response = dialogue_win.run()

            # Retrieve user choices from the dialogue window...
            name = dialogue_win.entry.get_text()
            source = dialogue_win.entry2.get_text()
            dl_sim_flag = dialogue_win.radiobutton2.get_active()
            monitor_flag = dialogue_win.checkbutton.get_active()

            # ...and find the name of the parent media data object (a
            #   media.Folder), if one was specified...
            parent_name = None
            if hasattr(dialogue_win, 'parent_name'):
                parent_name = dialogue_win.parent_name
            elif suggest_parent_name is not None:
                parent_name = suggest_parent_name

            # ...and halt the timer, if running
            if dialogue_win.clipboard_timer_id:
                GObject.source_remove(dialogue_win.clipboard_timer_id)

            # ...before destroying the dialogue window
            dialogue_win.destroy()

            if response != Gtk.ResponseType.OK:

                keep_open_flag = False

            else:

                if name is None or re.match('\s*$', name):

                    keep_open_flag = False
                    self.dialogue_manager_obj.show_msg_dialogue(
                        _('You must give the channel a name'),
                        'error',
                        'ok',
                    )

                elif not self.check_container_name_is_legal(name):

                    keep_open_flag = False
                    self.dialogue_manager_obj.show_msg_dialogue(
                        _('The name \'{0}\' is not allowed').format(name),
                        'error',
                        'ok',
                    )

                elif not source or not utils.check_url(source):

                    keep_open_flag = False
                    self.dialogue_manager_obj.show_msg_dialogue(
                        _('You must enter a valid URL'),
                        'error',
                        'ok',
                    )

                elif name in self.media_name_dict:

                    # Another channel, playlist or folder is already using this
                    #   name
                    keep_open_flag = False
                    self.reject_container_name(name)

                else:

                    keep_open_flag = self.dialogue_keep_open_flag

                    # Remove leading/trailing whitespace from the name; make
                    #   sure the name is not excessively long
                    name = utils.tidy_up_container_name(
                        name,
                        self.container_name_max_len,
                    )

                    # Find the parent media data object (a media.Folder), if
                    #   specified
                    parent_obj = None
                    if parent_name and parent_name in self.media_name_dict:
                        dbid = self.media_name_dict[parent_name]
                        parent_obj = self.media_reg_dict[dbid]

                        if self.dialogue_keep_open_flag \
                        and self.dialogue_keep_container_flag:
                            suggest_parent_name = parent_name

                    # Create the new channel
                    channel_obj = self.add_channel(
                        name,
                        parent_obj,
                        source,
                        dl_sim_flag,
                    )

                    # Add the channel to Video Index
                    if channel_obj:

                        if suggest_parent_name is not None \
                        and suggest_parent_name \
                        == self.main_win_obj.video_index_current:
                            # The channel has been added to the currently
                            #   selected folder; the True argument tells the
                            #   function not to select the channel
                            self.main_win_obj.video_index_add_row(
                                channel_obj,
                                True,
                            )

                        else:
                            # Do select the new channel
                            self.main_win_obj.video_index_add_row(channel_obj)


    def on_menu_add_folder(self, action, par):

        """Called from a callback in self.do_startup().

        Creates a dialogue window to allow the user to specify a new folder.
        If the user specifies a folder, creates a media.Folder object.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 13925 on_menu_add_folder')

        # If a folder is selected in the Video Index, the dialogue window
        #   should suggest that as the new folder's parent folder
        suggest_parent_name = None
        if self.main_win_obj.video_index_current:
            dbid = self.media_name_dict[self.main_win_obj.video_index_current]
            container_obj = self.media_reg_dict[dbid]
            if isinstance(container_obj, media.Folder) \
            and not container_obj.fixed_flag \
            and not container_obj.restrict_flag:
                suggest_parent_name = container_obj.name

        dialogue_win = mainwin.AddFolderDialogue(
            self.main_win_obj,
            suggest_parent_name,
        )

        response = dialogue_win.run()

        # Retrieve user choices from the dialogue window...
        name = dialogue_win.entry.get_text()
        dl_sim_flag = dialogue_win.radiobutton2.get_active()

        # ...and find the name of the parent media data object (a
        #   media.Folder), if one was specified...
        parent_name = None
        if hasattr(dialogue_win, 'parent_name'):
            parent_name = dialogue_win.parent_name

        # ...before destroying the dialogue window
        dialogue_win.destroy()

        if response == Gtk.ResponseType.OK:

            if name is None or re.match('\s*$', name):

                self.dialogue_manager_obj.show_msg_dialogue(
                    _('You must give the folder a name'),
                    'error',
                    'ok',
                )

            elif not self.check_container_name_is_legal(name):

                self.dialogue_manager_obj.show_msg_dialogue(
                    _('The name \'{0}\' is not allowed').format(name),
                    'error',
                    'ok',
                )

            elif name in self.media_name_dict:

                # Another channel, playlist or folder is already using this
                #   name
                self.reject_container_name(name)

            else:

                # Remove leading/trailing whitespace from the name; make sure
                #   the name is not excessively long
                name = utils.tidy_up_container_name(
                    name,
                    self.container_name_max_len,
                )

                # Find the parent media data object (a media.Folder), if
                #   specified
                parent_obj = None
                if parent_name and parent_name in self.media_name_dict:
                    dbid = self.media_name_dict[parent_name]
                    parent_obj = self.media_reg_dict[dbid]

                # Create the new folder
                folder_obj = self.add_folder(name, parent_obj, dl_sim_flag)

                # Add the folder to the Video Index
                if folder_obj:

                    if self.main_win_obj.video_index_current:
                        # The new folder has been added inside the currently
                        #   selected folder; the True argument tells the
                        #   function not to select the new folder
                        self.main_win_obj.video_index_add_row(
                            folder_obj,
                            True,
                        )

                    else:
                        # Do select the new folder
                        self.main_win_obj.video_index_add_row(folder_obj)


    def on_menu_add_playlist(self, action, par):

        """Called from a callback in self.do_startup().

        Creates a dialogue window to allow the user to specify a new playlist.
        If the user specifies a playlist, creates a media.PLaylist object.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 14034 on_menu_add_playlist')

        keep_open_flag = True
        dl_sim_flag = False
        monitor_flag = False

        # If a folder (but not a channel/playlist) is selected in the Video
        #   Index, use that as the dialogue window's suggested parent folder
        suggest_parent_name = None
        if self.main_win_obj.video_index_current:
            dbid = self.media_name_dict[self.main_win_obj.video_index_current]
            container_obj = self.media_reg_dict[dbid]
            if isinstance(container_obj, media.Folder) \
            and not container_obj.fixed_flag \
            and not container_obj.restrict_flag:
                suggest_parent_name = container_obj.name

        while keep_open_flag:

            dialogue_win = mainwin.AddPlaylistDialogue(
                self.main_win_obj,
                suggest_parent_name,
                dl_sim_flag,
                monitor_flag,
            )

            response = dialogue_win.run()

            # Retrieve user choices from the dialogue window...
            name = dialogue_win.entry.get_text()
            source = dialogue_win.entry2.get_text()
            dl_sim_flag = dialogue_win.radiobutton2.get_active()
            monitor_flag = dialogue_win.checkbutton.get_active()

            # ...and find the name of the parent media data object (a
            #   media.Folder), if one was specified...
            parent_name = None
            if hasattr(dialogue_win, 'parent_name'):
                parent_name = dialogue_win.parent_name
            elif suggest_parent_name is not None:
                parent_name = suggest_parent_name

            # ...and halt the timer, if running
            if dialogue_win.clipboard_timer_id:
                GObject.source_remove(dialogue_win.clipboard_timer_id)

            # ...before destroying the dialogue window
            dialogue_win.destroy()

            if response != Gtk.ResponseType.OK:

                keep_open_flag = False

            else:

                if name is None or re.match('\s*$', name):

                    keep_open_flag = False
                    self.dialogue_manager_obj.show_msg_dialogue(
                        _('You must give the playlist a name'),
                        'error',
                        'ok',
                    )

                elif not self.check_container_name_is_legal(name):

                    keep_open_flag = False
                    self.dialogue_manager_obj.show_msg_dialogue(
                        _('The name \'{0}\' is not allowed').format(name),
                        'error',
                        'ok',
                    )

                elif not source or not utils.check_url(source):

                    keep_open_flag = False
                    self.dialogue_manager_obj.show_msg_dialogue(
                        _('You must enter a valid URL'),
                        'error',
                        'ok',
                    )

                elif name in self.media_name_dict:

                    # Another channel, playlist or folder is already using this
                    #   name
                    keep_open_flag = False
                    self.reject_container_name(name)

                else:

                    keep_open_flag = self.dialogue_keep_open_flag

                    # Remove leading/trailing whitespace from the name; make
                    #   sure the name is not excessively long
                    name = utils.tidy_up_container_name(
                        name,
                        self.container_name_max_len,
                    )

                    # Find the parent media data object (a media.Folder), if
                    #   specified
                    parent_obj = None
                    if parent_name and parent_name in self.media_name_dict:
                        dbid = self.media_name_dict[parent_name]
                        parent_obj = self.media_reg_dict[dbid]

                        if self.dialogue_keep_open_flag \
                        and self.dialogue_keep_container_flag:
                            suggest_parent_name = parent_name

                    # Create the playlist
                    playlist_obj = self.add_playlist(
                        name,
                        parent_obj,
                        source,
                        dl_sim_flag,
                    )

                    # Add the playlist to the Video Index
                    if playlist_obj:

                        if suggest_parent_name is not None \
                        and suggest_parent_name \
                        == self.main_win_obj.video_index_current:
                            # The playlist has been added to the currently
                            #   selected folder; the True argument tells the
                            #   function not to select the playlist
                            self.main_win_obj.video_index_add_row(
                                playlist_obj,
                                True,
                            )

                        else:
                            # Do select the new playlist
                            self.main_win_obj.video_index_add_row(playlist_obj)


    def on_menu_add_video(self, action, par):

        """Called from a callback in self.do_startup().

        Creates a dialogue window to allow the user to specify one or more
        videos. If the user supplies some URLs, creates media.Video objects.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 14188 on_menu_add_video')

        dialogue_win = mainwin.AddVideoDialogue(self.main_win_obj)
        response = dialogue_win.run()

        # Retrieve user choices from the dialogue window...
        text = dialogue_win.textbuffer.get_text(
            dialogue_win.textbuffer.get_start_iter(),
            dialogue_win.textbuffer.get_end_iter(),
            False,
        )

        dl_sim_flag = dialogue_win.radiobutton2.get_active()

        # ...and find the parent media data object (a media.Channel,
        #   media.Playlist or media.Folder)...
        parent_name = self.fixed_misc_folder.name
        if hasattr(dialogue_win, 'parent_name'):
            parent_name = dialogue_win.parent_name

        dbid = self.media_name_dict[parent_name]
        parent_obj = self.media_reg_dict[dbid]

        # ...and halt the timer, if running
        if dialogue_win.clipboard_timer_id:
            GObject.source_remove(dialogue_win.clipboard_timer_id)

        # ...before destroying the dialogue window
        dialogue_win.destroy()

        if response == Gtk.ResponseType.OK:

            # Split text into a list of lines and filter out invalid URLs
            video_list = []
            duplicate_list = []
            for line in text.split('\n'):

                # Remove leading/trailing whitespace
                line = utils.strip_whitespace(line)

                # Perform checks on the URL. If it passes, remove leading/
                #   trailing whitespace
                if utils.check_url(line):
                    video_list.append(utils.strip_whitespace(line))

            # Check everything in the list against other media.Video objects
            #   with the same parent folder
            for line in video_list:
                if parent_obj.check_duplicate_video(line):
                    duplicate_list.append(line)
                else:
                    self.add_video(parent_obj, line, dl_sim_flag)

            # In the Video Index, select the parent media data object, which
            #   updates both the Video Index and the Video Catalogue
            self.main_win_obj.video_index_select_row(parent_obj)

            # If any duplicates were found, inform the user
            if duplicate_list:

                msg = _('The following videos are duplicates:')
                for line in duplicate_list:
                    msg += '\n\n' + line

                self.dialogue_manager_obj.show_msg_dialogue(
                    msg,
                    'warning',
                    'ok',
                )


    def on_menu_cancel_live(self, action, par):

        """Called from a callback in self.do_startup().

        Cancels all livestream actions (auto-notify, auto-open, download at
        start, download at stop).

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 14275 on_menu_cancel_live')

        # The actions are stored in five different dictionaries. Compile a
        #   single dictionary, eliminating duplicates, so we can count how
        #   many media.Video objects are affected (and updte the Video
        #   Catalogue)
        video_dict = {}

        for video_obj in self.media_reg_auto_notify_dict.values():
            video_dict[video_obj.dbid] = video_obj

        for video_obj in self.media_reg_auto_alarm_dict.values():
            video_dict[video_obj.dbid] = video_obj

        for video_obj in self.media_reg_auto_open_dict.values():
            video_dict[video_obj.dbid] = video_obj

        for video_obj in self.media_reg_auto_dl_start_dict.values():
            video_dict[video_obj.dbid] = video_obj

        for video_obj in self.media_reg_auto_dl_stop_dict.values():
            video_dict[video_obj.dbid] = video_obj

        # Cancel livestream actions by emptying the IVs
        self.media_reg_auto_notify_dict = {}
        self.media_reg_auto_alarm_dict = {}
        self.media_reg_auto_open_dict = {}
        self.media_reg_auto_dl_start_dict = {}
        self.media_reg_auto_dl_stop_dict = {}

        # Update the Video Catalogue
        for video_obj in video_dict.values():
            self.main_win_obj.video_catalogue_update_row(video_obj)

        # Show confirmation
        count = len(video_dict)
        if not count:
            msg = _('There were no livestream alerts to cancel')
        elif count == 1:
            msg = _('Livestream alerts for 1 video were cancelled')
        else:
            msg = _(
                'Livestream alerts for {0} videos were cancelled',
            ).format(str(count))

        self.dialogue_manager_obj.show_msg_dialogue(
            msg,
            'info',
            'ok',
             None,                   # Parent window is main window
        )


    def on_menu_change_db(self, action, par):

        """Called from a callback in self.do_startup().

        Opens the preference window at the right tab, so that the user can
        switch databases.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 14344 on_menu_change_db')

        config.SystemPrefWin(self, 'db')


    def on_menu_check_all(self, action, par):

        """Called from a callback in self.do_startup().

        Call a function to start a new download operation (if allowed).

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 14363 on_menu_check_all')

        self.download_manager_start('sim')


    def on_menu_close_tray(self, action, par):

        """Called from a callback in self.do_startup().

        Closes the main window to the system tray.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 14384 on_menu_close_tray')

        self.main_win_obj.toggle_visibility()


    def on_menu_custom_dl_all(self, action, par):

        """Called from a callback in self.do_startup().

        Call a function to start a new (custom) download operation (if
        allowed).

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 14405 on_menu_custom_dl_all')

        self.download_manager_start('custom')


    def on_menu_download_all(self, action, par):

        """Called from a callback in self.do_startup().

        Call a function to start a new download operation (if allowed).

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 14425 on_menu_download_all')

        self.download_manager_start('real')


    def on_menu_export_db(self, action, par):

        """Called from a callback in self.do_startup().

        Exports data from the Tartube database.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 14445 on_menu_export_db')

        self.export_from_db( [] )


    def on_menu_general_options(self, action, par):

        """Called from a callback in self.do_startup().

        Opens an edit window for the General Options Manager.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 14465 on_menu_general_options')

        config.OptionsEditWin(self, self.general_options_obj, None)


    def on_menu_go_website(self, action, par):

        """Called from a callback in self.do_startup().

        Opens the Tartube website.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 14485 on_menu_go_website')

        utils.open_file(__main__.__website__)


    def on_menu_import_json(self, action, par):

        """Called from a callback in self.do_startup().

        Imports data into from a JSON export file into the Tartube database.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 14505 on_menu_import_json')

        self.import_into_db(True)


    def on_menu_import_plain_text(self, action, par):

        """Called from a callback in self.do_startup().

        Imports data into from a plain text export file into the Tartube
        database.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 14526 on_menu_import_plain_text')

        self.import_into_db(False)


    def on_menu_install_ffmpeg(self, action, par):

        """Called from a callback in self.do_startup().

        Start an update operation to install FFmpeg (on MS Windows only).

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 14546 on_menu_install_ffmpeg')

        self.update_manager_start('ffmpeg')


    def on_menu_live_preferences(self, action, par):

        """Called from a callback in self.do_startup().

        Opens a preference window to edit livestream preferences.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 14566 on_menu_live_preferences')

        config.SystemPrefWin(self, 'live')


    def on_menu_refresh_db(self, action, par):

        """Called from a callback in self.do_startup().

        Starts a refresh operation.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 14586 on_menu_refresh_db')

        self.refresh_manager_start()


    def on_menu_save_all(self, action, par):

        """Called from a callback in self.do_startup().

        Save the config file, and then the Tartube database.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 14606 on_menu_save_all')

        if not self.disable_load_save_flag:
            self.save_config()
        if not self.disable_load_save_flag:
            self.save_db()

        # Show a dialogue window for confirmation (unless file load/save has
        #   been disabled, in which case a dialogue has already appeared)
        if not self.disable_load_save_flag:

            self.dialogue_manager_obj.show_msg_dialogue(
                _('Data saved'),
                'info',
                'ok',
            )


    def on_menu_save_db(self, action, par):

        """Called from a callback in self.do_startup().

        Save the Tartube database.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 14639 on_menu_save_db')

        self.save_db()

        # Show a dialogue window for confirmation (unless file load/save has
        #   been disabled, in which case a dialogue has already appeared)
        if not self.disable_load_save_flag:

            self.dialogue_manager_obj.show_msg_dialogue(
                _('Database saved'),
                'info',
                'ok',
            )


    def on_menu_send_feedback(self, action, par):

        """Called from a callback in self.do_startup().

        Opens the Tartube feedback website.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 14669 on_menu_send_feedback')

        utils.open_file(__main__.__website_bugs__)


    def on_menu_show_hidden(self, action, par):

        """Called from a callback in self.do_startup().

        Un-hides all hidden media.Folder objects (and their children)

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 14689 on_menu_show_hidden')

        for name in self.media_name_dict:

            dbid = self.media_name_dict[name]
            media_data_obj = self.media_reg_dict[dbid]

            if isinstance(media_data_obj, media.Folder) \
            and media_data_obj.hidden_flag:
                self.mark_folder_hidden(media_data_obj, False)


    def on_menu_system_preferences(self, action, par):

        """Called from a callback in self.do_startup().

        Opens a preference window to edit system preferences.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 14716 on_menu_system_preferences')

        config.SystemPrefWin(self)


    def on_menu_test(self, action, par):

        """Called from a callback in self.do_startup().

        Add a set of media data objects for testing. This function can only be
        called if the debugging flags are set.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 14737 on_menu_test')

        # Add media data objects for testing: videos, channels, playlists and/
        #   or folders
        testing.add_test_media(self)

        # Clicking the Test button more than once just adds illegal duplicate
        #   channels/playlists/folders (and non-illegal duplicate videos), so
        #   just disable the button and the menu item
        self.main_win_obj.desensitise_test_widgets()

        # Redraw the video catalogue, if a Video Index row is selected
        if self.main_win_obj.video_index_current is not None:
            self.main_win_obj.video_catalogue_redraw_all(
                self.main_win_obj.video_index_current,
            )


    def on_menu_test_ytdl(self, action, par):

        """Called from a callback in self.do_startup().

        Start an info operation to test a youtube-dl command.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 14770 on_menu_test_ytdl')

        # Prompt the user for what should be tested
        dialogue_win = mainwin.TestCmdDialogue(self.main_win_obj)
        response = dialogue_win.run()

        # Retrieve user choices from the dialogue window...
        url_string = dialogue_win.entry.get_text()
        options_string = dialogue_win.textbuffer.get_text(
            dialogue_win.textbuffer.get_start_iter(),
            dialogue_win.textbuffer.get_end_iter(),
            False,
        )

        # ...before destroying it
        dialogue_win.destroy()

        # If the user specified either (or both) a URL and youtube-dl options,
        #   then we can proceed
        if response == Gtk.ResponseType.OK \
        and (url_string != '' or options_string != ''):

            # Start the info operation, which issues the youtube-dl command
            #   with the specified options
            self.info_manager_start(
                'test_ytdl',
                None,                   # No media.Video object in this case
                url_string,             # Use the source, if specified
                options_string,         # Use download options, if specified
            )


    def on_menu_tidy_up(self, action, par):

        """Called from a callback in self.do_startup().

        Start a tidy operation to tidy up Tartube's data directory.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 14817 on_menu_tidy_up')

        # Prompt the user to specify which actions should be applied to
        #   Tartube's data directory
        dialogue_win = mainwin.TidyDialogue(self.main_win_obj)
        response = dialogue_win.run()

        if response == Gtk.ResponseType.OK:

            # Retrieve user choices from the dialogue window
            choices_dict = {
                'media_data_obj': None,
                'corrupt_flag': dialogue_win.checkbutton.get_active(),
                'del_corrupt_flag': dialogue_win.checkbutton2.get_active(),
                'exist_flag': dialogue_win.checkbutton3.get_active(),
                'del_video_flag': dialogue_win.checkbutton4.get_active(),
                'del_others_flag': dialogue_win.checkbutton5.get_active(),
                'del_descrip_flag': dialogue_win.checkbutton6.get_active(),
                'del_json_flag': dialogue_win.checkbutton7.get_active(),
                'del_xml_flag': dialogue_win.checkbutton8.get_active(),
                'del_thumb_flag': dialogue_win.checkbutton9.get_active(),
                'del_webp_flag': dialogue_win.checkbutton10.get_active(),
                'del_archive_flag': dialogue_win.checkbutton11.get_active(),
            }

        # Now destroy the window
        dialogue_win.destroy()

        if response == Gtk.ResponseType.OK:

            # If nothing was selected, then there is nothing to do
            # (Don't need to check 'del_others_flag' here)
            if not choices_dict['corrupt_flag'] \
            and not choices_dict['exist_flag'] \
            and not choices_dict['del_video_flag'] \
            and not choices_dict['del_descrip_flag'] \
            and not choices_dict['del_json_flag'] \
            and not choices_dict['del_xml_flag'] \
            and not choices_dict['del_thumb_flag'] \
            and not choices_dict['del_webp_flag'] \
            and not choices_dict['del_archive_flag']:
                return

            # Prompt the user for confirmation, before deleting any files
            if choices_dict['del_corrupt_flag'] \
            or choices_dict['del_video_flag'] \
            or choices_dict['del_descrip_flag'] \
            or choices_dict['del_json_flag'] \
            or choices_dict['del_xml_flag'] \
            or choices_dict['del_thumb_flag'] \
            or choices_dict['del_webp_flag'] \
            or choices_dict['del_archive_flag']:

                self.dialogue_manager_obj.show_msg_dialogue(
                    _(
                    'Files cannot be recovered, after being deleted. Are you' \
                    + ' sure you want to continue?',
                    ),
                    'question',
                    'yes-no',
                    None,                   # Parent window is main window
                    {
                        'yes': 'tidy_manager_start',
                        # Specified options
                        'data': choices_dict,
                    },
                )

            else:

                # Start the tidy operation now
                self.tidy_manager_start(choices_dict)


    def on_menu_update_live(self, action, par):

        """Called from a callback in self.do_startup().

        Forces the livestream operation to start. Ignored if any operation
        (including an existing livestream operation) is running.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 14904 on_menu_update_live')

        # Because livestream operations run silently in the background, when
        #   the user goes to the trouble of clicking a menu item in the
        #   main window's menu, tell them why nothing is happening
        msg = _('Cannot update existing livestreams because')
        if self.current_manager_obj:
            msg += ' ' + _('there is another operation running')
        elif self.livestream_manager_obj:
            msg += ' ' + _('they are currently being updated')
        elif self.main_win_obj.config_win_list:
            msg += ' ' + _('one or more configuration windows are open')
        elif not self.media_reg_live_dict:
            msg += ' ' + _('there are no livestreams to update')
        else:
            self.livestream_manager_start()
            return

        self.dialogue_manager_obj.show_msg_dialogue(msg, 'error', 'ok')


    def on_menu_update_ytdl(self, action, par):

        """Called from a callback in self.do_startup().

        Start an update operation to update the system's youtube-dl.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 14940 on_menu_update_ytdl')

        self.update_manager_start('ytdl')


    def on_menu_quit(self, action, par):

        """Called from a callback in self.do_startup().

        Terminates the Tartube app.

        Args:

            action (Gio.SimpleAction): Object generated by Gio

            par (None): Ignored

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 14960 on_menu_quit')

        self.stop()


    # (Callback support functions)


    def reject_container_name(self, name):

        """Called by self.on_menu_add_channel(), .on_menu_add_playlist()
        and .on_menu_add_folder().

        If the user specifies a name for a channel, playlist or folder that's
        already in use by a channel, playlist or folder, tell them why they
        can't use it.

        Args:

            name (str): The name specified by the user

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 14984 reject_container_name')

        # Get the existing media data object with this name
        dbid = self.media_name_dict[name]
        media_data_obj = self.media_reg_dict[dbid]
        media_type = media_data_obj.get_type()
        if media_type == 'channel':
            msg = _('There is already a channel with that name')
        elif media_type == 'playlist':
            msg = _('There is already a playlist with that name')
        else:
            msg = _('There is already a folder with that name')

        self.dialogue_manager_obj.show_msg_dialogue(
            msg + ' ' + _('(so please choose a different name)'),
            'error',
            'ok',
        )


    # Set accessors


    def set_allow_ytdl_archive_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15010 set_allow_ytdl_archive_flag')

        if not flag:
            self.allow_ytdl_archive_flag = False
        else:
            self.allow_ytdl_archive_flag = True


    def set_apply_json_timeout_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15021 set_apply_json_timeout_flag')

        if not flag:
            self.apply_json_timeout_flag = False
        else:
            self.apply_json_timeout_flag = True


    def add_auto_alarm_dict(self, video_obj):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15032 add_auto_alarm_dict')

        self.media_reg_auto_alarm_dict[video_obj.dbid] = video_obj


    def del_auto_alarm_dict(self, video_obj):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15040 del_auto_alarm_dict')

        if video_obj.dbid in self.media_reg_auto_alarm_dict:
            del self.media_reg_auto_alarm_dict[video_obj.dbid]


    def set_auto_clone_options_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15049 set_auto_clone_options_flag')

        if not flag:
            self.auto_clone_options_flag = False
        else:
            self.auto_clone_options_flag = True


    def set_auto_delete_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15060 set_auto_delete_flag')

        if not flag:
            self.auto_delete_flag = False
        else:
            self.auto_delete_flag = True


    def set_auto_delete_days(self, days):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15071 set_auto_delete_days')

        self.auto_delete_days = days


    def set_auto_delete_watched_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15079 set_auto_delete_watched_flag')

        if not flag:
            self.auto_delete_watched_flag = False
        else:
            self.auto_delete_watched_flag = True


    def set_auto_expand_video_index_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15090 set_auto_expand_video_index_flag')

        if not flag:
            self.auto_expand_video_index_flag = False
        else:
            self.auto_expand_video_index_flag = True


    def add_auto_dl_start_dict(self, video_obj):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15101 add_auto_dl_start_dict')

        self.media_reg_auto_dl_start_dict[video_obj.dbid] = video_obj


    def del_auto_dl_start_dict(self, video_obj):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15109 del_auto_dl_start_dict')

        if video_obj.dbid in self.media_reg_auto_dl_start_dict:
            del self.media_reg_auto_dl_start_dict[video_obj.dbid]


    def add_auto_dl_stop_dict(self, video_obj):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15118 add_auto_dl_stop_dict')

        self.media_reg_auto_dl_stop_dict[video_obj.dbid] = video_obj


    def del_auto_dl_stop_dict(self, video_obj):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15126 del_auto_dl_stop_dict')

        if video_obj.dbid in self.media_reg_auto_dl_stop_dict:
            del self.media_reg_auto_dl_stop_dict[video_obj.dbid]


    def add_auto_notify_dict(self, video_obj):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15135 add_auto_notify_dict')

        self.media_reg_auto_notify_dict[video_obj.dbid] = video_obj


    def del_auto_notify_dict(self, video_obj):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15143 del_auto_notify_dict')

        if video_obj.dbid in self.media_reg_auto_notify_dict:
            del self.media_reg_auto_notify_dict[video_obj.dbid]


    def add_auto_open_dict(self, video_obj):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15152 add_auto_open_dict')

        self.media_reg_auto_open_dict[video_obj.dbid] = video_obj


    def del_auto_open_dict(self, video_obj):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15160 del_auto_open_dict')

        if video_obj.dbid in self.media_reg_auto_open_dict:
            del self.media_reg_auto_open_dict[video_obj.dbid]


    def set_autostop_size_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15169 set_autostop_size_flag')

        if not flag:
            self.autostop_size_flag = False
        else:
            self.autostop_size_flag = True


    def set_autostop_size_unit(self, value):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15180 set_autostop_size_unit')

        self.autostop_size_unit = value


    def set_autostop_size_value(self, value):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15188 set_autostop_size_value')

        self.autostop_size_value = value


    def set_autostop_time_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15196 set_autostop_time_flag')

        if not flag:
            self.autostop_time_flag = False
        else:
            self.autostop_time_flag = True


    def set_autostop_time_unit(self, value):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15207 set_autostop_time_unit')

        self.autostop_time_unit = value


    def set_autostop_time_value(self, value):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15215 set_autostop_time_value')

        self.autostop_time_value = value


    def set_autostop_videos_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15223 set_autostop_videos_flag')

        if not flag:
            self.autostop_videos_flag = False
        else:
            self.autostop_videos_flag = True


    def set_autostop_videos_value(self, value):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15234 set_autostop_videos_value')

        self.autostop_videos_value = value


    def set_bandwidth_apply_flag(self, flag):

        """Called by mainwin.MainWin.on_bandwidth_checkbutton_changed().

        Applies or releases the bandwidth limit. If a download operation is in
        progress, the new setting is applied to the next download job.
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15248 set_bandwidth_apply_flag')

        if not flag:
            self.bandwidth_apply_flag = False
        else:
            self.bandwidth_apply_flag = True


    def set_bandwidth_default(self, value):

        """Called by mainwin.MainWin.on_bandwidth_spinbutton_changed().

        Sets the new bandwidth limit. If a download operation is in progress,
        the new value is applied to the next download job.
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15265 set_bandwidth_default')

        if value < self.bandwidth_min or value > self.bandwidth_max:
            return self.system_error(
                156,
                'Set bandwidth request failed sanity check',
            )

        self.bandwidth_default = value


    def set_catalogue_page_size(self, size):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15279 set_catalogue_page_size')

        self.catalogue_page_size = size


    def set_classic_dir_previous(self, directory):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15287 set_classic_dir_previous')

        self.classic_dir_previous = directory


    def classic_ytdl_archive_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15288 classic_ytdl_archive_flag')

        if not flag:
            self.classic_ytdl_archive_flag = False
        else:
            self.classic_ytdl_archive_flag = True


    def set_close_to_tray_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15295 set_close_to_tray_flag')

        if not flag:
            self.close_to_tray_flag = False
        else:
            self.close_to_tray_flag = True


    def set_complex_index_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15306 set_complex_index_flag')

        if not flag:
            self.complex_index_flag = False
        else:
            self.complex_index_flag = True


    def set_custom_dl_by_video_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15317 set_custom_dl_by_video_flag')

        if not flag:
            self.custom_dl_by_video_flag = False
        else:
            self.custom_dl_by_video_flag = True


    def set_custom_dl_delay_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15328 set_custom_dl_delay_flag')

        if not flag:
            self.custom_dl_delay_flag = False
        else:
            self.custom_dl_delay_flag = True


    def set_custom_dl_delay_max(self, value):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15339 set_custom_dl_delay_max')

        self.custom_dl_delay_max = value


    def set_custom_dl_delay_min(self, value):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15345 set_custom_dl_delay_min')

        self.custom_dl_delay_min = value


    def set_custom_dl_divert_mode(self, value):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15355 set_custom_dl_divert_mode')

        self.custom_dl_divert_mode = value

        # The Video Catalogue must be redrawn to reset the 'Other' label (but
        #   only when ComplexCatalogueItems are visible)
        if self.catalogue_mode != 'simple_hide_parent' \
        and self.catalogue_mode != 'simple_show_parent':
            self.main_win_obj.video_catalogue_redraw_all(
                self.main_win_obj.video_index_current,
                self.main_win_obj.catalogue_toolbar_current_page,
            )


    def set_custom_dl_divert_website(self, value):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15356 set_custom_dl_divert_website')

        self.custom_dl_divert_website = value

        # The Video Catalogue must be redrawn to reset the 'Other' label (but
        #   only when ComplexCatalogueItems are visible)
        if self.catalogue_mode != 'simple_hide_parent' \
        and self.catalogue_mode != 'simple_show_parent':
            self.main_win_obj.video_catalogue_redraw_all(
                self.main_win_obj.video_index_current,
                self.main_win_obj.catalogue_toolbar_current_page,
            )


    def set_custom_locale(self, value):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15363 set_custom_locale')

        self.custom_locale = value
        self.update_locale_flag = True


    def set_data_dir(self, path):

        """Called by mainwin.MountDriveDialogue.on_button_clicked() only;
        everything else should call self.switch_db().

        The call to this function resets the value of self.data_dir without
        actually loading the database.
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15379 set_data_dir')

        self.data_dir = path


    def reset_data_dir(self):

        """Called by mainwin.MountDriveDialogue.on_button_clicked() only;
        everything else should call self.switch_db().

        The call to this function resets the value of self.data_dir without
        actually loading the database.
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15394 reset_data_dir')

        self.data_dir = self.default_data_dir


    def set_data_dir_add_from_list_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15402 set_data_dir_add_from_list_flag')

        if not flag:
            self.data_dir_add_from_list_flag = False
        else:
            self.data_dir_add_from_list_flag = True


    def set_data_dir_alt_list(self, dir_list):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15413 set_data_dir_add_from_list_flag')

        self.data_dir_alt_list = dir_list.copy()


    def set_data_dir_use_first_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15421 set_data_dir_use_first_flag')

        if not flag:
            self.data_dir_use_first_flag = False
        else:
            self.data_dir_use_first_flag = True


    def set_data_dir_use_list_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15432 set_data_dir_use_list_flag')

        if not flag:
            self.data_dir_use_list_flag = False
        else:
            self.data_dir_use_list_flag = True


    def set_db_backup_mode(self, value):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15443 set_db_backup_mode')

        self.db_backup_mode = value


    def set_delete_on_shutdown_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15451 set_delete_on_shutdown_flag')

        if not flag:
            self.delete_on_shutdown_flag = False
        else:
            self.delete_on_shutdown_flag = True


    def set_dialogue_copy_clipboard_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15462 set_dialogue_copy_clipboard_flag')

        if not flag:
            self.dialogue_copy_clipboard_flag = False
        else:
            self.dialogue_copy_clipboard_flag = True


    def set_dialogue_keep_open_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15473 set_dialogue_keep_open_flag')

        if not flag:
            self.dialogue_keep_open_flag = False
        else:
            self.dialogue_keep_open_flag = True


    def set_disable_dl_all_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15484 set_disable_dl_all_flag')

        if not flag:
            self.disable_dl_all_flag = False
            self.main_win_obj.enable_dl_all_buttons()

        else:
            self.disable_dl_all_flag = True
            self.main_win_obj.disable_dl_all_buttons()


    def set_disk_space_stop_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15498 set_disk_space_stop_flag')

        if not flag:
            self.disk_space_stop_flag = False
        else:
            self.disk_space_stop_flag = True


    def set_disk_space_stop_limit(self, value):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15509 set_disk_space_stop_limit')

        self.disk_space_stop_limit = value


    def set_disk_space_warn_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15517 set_disk_space_warn_flag')

        if not flag:
            self.disk_space_warn_flag = False
        else:
            self.disk_space_warn_flag = True


    def set_disk_space_warn_limit(self, value):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15528 set_disk_space_warn_limit')

        self.disk_space_warn_limit = value


    def set_enable_livestreams_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15536 set_enable_livestreams_flag')

        if not flag:
            self.enable_livestreams_flag = False
        else:
            self.enable_livestreams_flag = True


    def set_ffmpeg_path(self, path):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15547 set_ffmpeg_path')

        self.ffmpeg_path = path


    def set_full_expand_video_index_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15555 set_full_expand_video_index_flag')

        if not flag:
            self.full_expand_video_index_flag = False
        else:
            self.full_expand_video_index_flag = True


    def set_gtk_emulate_broken_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15566 set_gtk_emulate_broken_flag')

        if not flag:
            self.gtk_emulate_broken_flag = False
        else:
            self.gtk_emulate_broken_flag = True


    def set_ignore_child_process_exit_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15577 set_ignore_child_process_exit_flag')

        if not flag:
            self.ignore_child_process_exit_flag = False
        else:
            self.ignore_child_process_exit_flag = True


    def set_ignore_custom_msg_list(self, custom_list):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15588 set_ignore_custom_msg_list')

        self.ignore_custom_msg_list = custom_list.copy()


    def set_ignore_custom_regex_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15596 set_ignore_custom_regex_flag')

        if not flag:
            self.ignore_custom_regex_flag = False
        else:
            self.ignore_custom_regex_flag = True


    def set_ignore_data_block_error_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15607 set_ignore_data_block_error_flag')

        if not flag:
            self.ignore_data_block_error_flag = False
        else:
            self.ignore_data_block_error_flag = True


    def set_ignore_http_404_error_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15618 set_ignore_http_404_error_flag')

        if not flag:
            self.ignore_http_404_error_flag = False
        else:
            self.ignore_http_404_error_flag = True


    def set_ignore_merge_warning_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15629 set_ignore_merge_warning_flag')

        if not flag:
            self.ignore_merge_warning_flag = False
        else:
            self.ignore_merge_warning_flag = True


    def set_ignore_missing_format_error_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15640 set_ignore_missing_format_error_flag')

        if not flag:
            self.ignore_missing_format_error_flag = False
        else:
            self.ignore_missing_format_error_flag = True


    def set_ignore_no_annotations_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15651 set_ignore_no_annotations_flag')

        if not flag:
            self.ignore_no_annotations_flag = False
        else:
            self.ignore_no_annotations_flag = True


    def set_ignore_no_subtitles_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15662 set_ignore_no_subtitles_flag')

        if not flag:
            self.ignore_no_subtitles_flag = False
        else:
            self.ignore_no_subtitles_flag = True


    def set_ignore_yt_age_restrict_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15673 set_ignore_yt_age_restrict_flag')

        if not flag:
            self.ignore_yt_age_restrict_flag = False
        else:
            self.ignore_yt_age_restrict_flag = True


    def set_ignore_yt_copyright_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15684 set_ignore_yt_copyright_flag')

        if not flag:
            self.ignore_yt_copyright_flag = False
        else:
            self.ignore_yt_copyright_flag = True


    def set_ignore_yt_uploader_deleted_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15695 set_ignore_yt_uploader_deleted_flag')

        if not flag:
            self.ignore_yt_uploader_deleted_flag = False
        else:
            self.ignore_yt_uploader_deleted_flag = True


    def set_livestream_max_days(self, value):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15706 set_livestream_max_days')

        self.livestream_max_days = value


    def set_livestream_auto_alarm_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15714 set_livestream_auto_alarm_flag')

        if not flag:
            self.livestream_auto_alarm_flag = False
        else:
            self.livestream_auto_alarm_flag = True


    def set_livestream_auto_dl_start_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15725 set_livestream_auto_dl_start_flag')

        if not flag:
            self.livestream_auto_dl_start_flag = False
        else:
            self.livestream_auto_dl_start_flag = True


    def set_livestream_auto_dl_stop_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15736 set_livestream_auto_dl_stop_flag')

        if not flag:
            self.livestream_auto_dl_stop_flag = False
        else:
            self.livestream_auto_dl_stop_flag = True


    def set_livestream_auto_notify_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15747 set_livestream_auto_notify_flag')

        if not flag:
            self.livestream_auto_notify_flag = False
        else:
            self.livestream_auto_notify_flag = True


    def set_livestream_auto_open_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15758 set_livestream_auto_open_flag')

        if not flag:
            self.livestream_auto_open_flag = False
        else:
            self.livestream_auto_open_flag = True


    def set_livestream_use_colour_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15769 set_livestream_use_colour_flag')

        if not flag:
            self.livestream_use_colour_flag = False
        else:
            self.livestream_use_colour_flag = True


    def set_main_win_save_size_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15780 set_main_win_save_size_flag')

        if not flag:
            self.main_win_save_size_flag = False
            self.main_win_save_width = self.main_win_width
            self.main_win_save_height = self.main_win_height
            self.main_win_save_posn = self.paned_min_size

        else:
            self.main_win_save_size_flag = True


    def set_match_first_chars(self, num_chars):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15795 set_match_first_chars')

        self.match_first_chars = num_chars


    def set_match_ignore_chars(self, num_chars):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15803 set_match_ignore_chars')

        self.match_ignore_chars = num_chars


    def set_match_method(self, method):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15811 set_match_method')

        self.match_method = method


    def set_num_worker_apply_flag(self, flag):

        """Called by mainwin.MainWin.on_num_worker_checkbutton_changed().

        Applies or releases the simultaneous download limit. If a download
        operation is in progress, the new setting is applied to the next
        download job.
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15826 set_num_worker_apply_flag')

        if not flag:
            self.bandwidth_apply_flag = False
        else:
            self.bandwidth_apply_flag = True


    def set_num_worker_default(self, value):

        """Called by mainwin.MainWin.on_num_worker_spinbutton_changed() and
        .on_num_worker_checkbutton_changed().

        Sets the new value for the number of simultaneous downloads allowed. If
        a download operation is in progress, informs the download manager
        object, so the number of download workers can be adjusted. Also
        increases the number of pages in the Output Tab, if necessary.
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15846 set_num_worker_default')

        if value < self.num_worker_min or value > self.num_worker_max:
            return self.system_error(
                157,
                'Set simultaneous downloads request failed sanity check',
            )

        old_value = self.num_worker_default
        self.num_worker_default = value

        if old_value != value and self.download_manager_obj:
            self.download_manager_obj.change_worker_count(value)

        if value > self.main_win_obj.output_page_count:
            self.main_win_obj.output_tab_setup_pages()


    def set_open_temp_on_desktop_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15687 set_open_temp_on_desktop_flag')

        if not flag:
            self.open_temp_on_desktop_flag = False
        else:
            self.open_temp_on_desktop_flag = True


    def set_operation_auto_update_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15878 set_operation_auto_update_flag')

        if not flag:
            self.operation_auto_update_flag = False
        else:
            self.operation_auto_update_flag = True


    def set_operation_check_limit(self, value):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15889 set_operation_check_limit')

        self.operation_check_limit = value


    def set_operation_convert_mode(self, mode):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15897 set_operation_convert_mode')

        if mode == 'disable' or mode == 'multi' or mode == 'channel' \
        or mode == 'playlist':
            self.operation_convert_mode = mode


    def set_operation_dialogue_mode(self, mode):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15907 set_operation_dialogue_mode')

        if mode == 'default' or mode == 'desktop' or mode == 'dialogue':
            self.operation_dialogue_mode = mode


    def set_operation_download_limit(self, value):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15916 set_operation_download_limit')

        self.operation_download_limit = value


    def set_operation_error_show_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15924 set_operation_error_show_flag')

        if not flag:
            self.operation_error_show_flag = False
        else:
            self.operation_error_show_flag = True


    def set_operation_halted_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15935 set_operation_halted_flag')

        if not flag:
            self.operation_halted_flag = False
        else:
            self.operation_halted_flag = True


    def set_operation_limit_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15946 set_operation_limit_flag')

        if not flag:
            self.operation_limit_flag = False
        else:
            self.operation_limit_flag = True


    def set_operation_save_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15957 set_operation_save_flag')

        if not flag:
            self.operation_save_flag = False
        else:
            self.operation_save_flag = True


    def set_operation_sim_shortcut_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15968 set_operation_sim_shortcut_flag')

        if not flag:
            self.operation_sim_shortcut_flag = False
        else:
            self.operation_sim_shortcut_flag = True


    def set_operation_warning_show_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15979 set_operation_warning_show_flag')

        if not flag:
            self.operation_warning_show_flag = False
        else:
            self.operation_warning_show_flag = True


    def set_progress_list_hide_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 15990 set_progress_list_hide_flag')

        if not flag:
            self.progress_list_hide_flag = False
        else:
            self.progress_list_hide_flag = True
            # If a download operation is in progress, hide any hideable rows
            #   immediately
            if self.download_manager_obj:
                self.main_win_obj.progress_list_check_hide_rows(True)


    def set_refresh_moviepy_timeout(self, value):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16005 set_refresh_moviepy_timeout')

        self.refresh_moviepy_timeout = value


    def set_refresh_output_verbose_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16013 set_refresh_output_verbose_flag')

        if not flag:
            self.refresh_output_verbose_flag = False
        else:
            self.refresh_output_verbose_flag = True


    def set_refresh_output_videos_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16024 set_refresh_output_videos_flag')

        if not flag:
            self.refresh_output_videos_flag = False
        else:
            self.refresh_output_videos_flag = True


    def set_results_list_reverse_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16035 set_results_list_reverse_flag')

        if not flag:
            self.results_list_reverse_flag = False
        else:
            self.results_list_reverse_flag = True


    def set_scheduled_check_mode(self, value):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16046 set_scheduled_check_mode')

        self.scheduled_check_mode = value


    def set_scheduled_check_wait_unit(self, value):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16054 set_scheduled_check_wait_unit')

        self.scheduled_check_wait_unit = value


    def set_scheduled_check_wait_value(self, value):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16055 set_scheduled_check_wait_value')

        self.scheduled_check_wait_value = value


    def set_scheduled_dl_mode(self, value):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16062 set_scheduled_dl_mode')

        self.scheduled_dl_mode = value


    def set_scheduled_dl_wait_unit(self, unit):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16070 set_scheduled_dl_wait_unit')

        self.scheduled_dl_wait_unit = unit


    def set_scheduled_dl_wait_value(self, value):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16071 set_scheduled_dl_wait_value')

        self.scheduled_dl_wait_value = value


    def set_scheduled_livestream_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16078 set_scheduled_livestream_flag')

        if not flag:
            self.scheduled_livestream_flag = False
        else:
            self.scheduled_livestream_flag = True


    def set_scheduled_livestream_wait_mins(self, value):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16089 set_scheduled_livestream_wait_mins')

        self.scheduled_livestream_wait_mins = value


    def set_scheduled_shutdown_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16097 set_scheduled_shutdown_flag')

        if not flag:
            self.scheduled_shutdown_flag = False
        else:
            self.scheduled_shutdown_flag = True


    def set_simple_options_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16108 set_simple_options_flag')

        if not flag:
            self.simple_options_flag = False
        else:
            self.simple_options_flag = True


    def set_show_classic_tab_on_startup_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16119 set_show_classic_tab_on_startup_flag')

        if not flag:
            self.show_classic_tab_on_startup_flag = False
        else:
            self.show_classic_tab_on_startup_flag = True


    def set_show_custom_icons_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16120 set_show_custom_icons_flag')

        if not flag:
            self.show_custom_icons_flag = False
        else:
            self.show_custom_icons_flag = True


    def set_show_pretty_dates_flag(self, flag):

        """Called by config.SystemPrefWin.on_pretty_date_button_toggled().

        Shows/hides the status icon in the system tray.
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16135 set_show_pretty_dates_flag')

        if not flag:
            self.show_pretty_dates_flag = False
        else:
            self.show_status_icon_flag = True

        # Redraw the Video Catalogue, but only if something was already drawn
        #   there (and keep the current page number)
        if self.main_win_obj.video_index_current is not None:
            self.main_win_obj.video_catalogue_redraw_all(
                self.main_win_obj.video_index_current,
                self.main_win_obj.catalogue_toolbar_current_page,
            )


    def set_show_small_icons_in_index_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16154 set_show_small_icons_in_index_flag')

        if not flag:
            self.show_small_icons_in_index_flag = False
        else:
            self.show_small_icons_in_index_flag = True

        # Redraw the Video Index and Video Catalogue
        self.main_win_obj.video_index_catalogue_reset()


    def set_show_status_icon_flag(self, flag):

        """Called by config.SystemPrefWin.on_show_status_icon_toggled().

        Shows/hides the status icon in the system tray.
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16173 set_show_status_icon_flag')

        if not flag:
            self.show_status_icon_flag = False
            if self.status_icon_obj:
                self.status_icon_obj.hide_icon()

        else:
            self.show_status_icon_flag = True
            if self.status_icon_obj:
                self.status_icon_obj.show_icon()


    def set_show_tooltips_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16189 set_show_tooltips_flag')

        if not flag:
            self.show_tooltips_flag = False
            # (The True argument forces the Video Catalogue to be redrawn)
            self.main_win_obj.disable_tooltips(True)

        else:
            self.show_tooltips_flag = True
            self.main_win_obj.enable_tooltips(True)


    def set_sound_custom(self, value):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16204 set_sound_custom')

        self.sound_custom = value


    def set_system_error_show_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16212 set_system_error_show_flag')

        if not flag:
            self.system_error_show_flag = False
        else:
            self.system_error_show_flag = True


    def set_system_msg_keep_totals_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16223 set_system_msg_keep_totals_flag')

        if not flag:
            self.system_msg_keep_totals_flag = False
        else:
            self.system_msg_keep_totals_flag = True


    def set_system_warning_show_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16234 set_system_warning_show_flag')

        if not flag:
            self.system_warning_show_flag = False
        else:
            self.system_warning_show_flag = True


    def set_toolbar_hide_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16245 set_toolbar_hide_flag')

        if not flag:
            self.toolbar_hide_flag = False
        else:
            self.toolbar_hide_flag = True


    def set_toolbar_squeeze_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16246 set_toolbar_squeeze_flag')

        if not flag:
            self.toolbar_squeeze_flag = False
        else:
            self.toolbar_squeeze_flag = True

        if self.main_win_obj and self.main_win_obj.main_toolbar \
        and not self.toolbar_hide_flag:
            self.main_win_obj.redraw_main_toolbar()


    def set_track_missing_time_days(self, value):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16247 set_track_missing_time_days')

        self.track_missing_time_days = value


    def set_track_missing_time_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16248 set_track_missing_time_flag')

        if not flag:
            self.track_missing_time_flag = False
        else:
            self.track_missing_time_flag = True


    def set_track_missing_videos_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16249 set_track_missing_videos_flag')

        if not flag:
            self.track_missing_videos_flag = False
        else:
            self.track_missing_videos_flag = True


    def set_use_module_moviepy_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16259 set_use_module_moviepy_flag')

        if not flag:
            self.use_module_moviepy_flag = False
        else:
            self.use_module_moviepy_flag = True


    def set_video_res_apply_flag(self, flag):

        """Called by mainwin.MainWin.on_video_res_checkbutton_changed().

        Applies or releases the video resolution limit. If a download operation
        is in progress, the new setting is applied to the next download job.
        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16276 set_video_res_apply_flag')

        if not flag:
            self.video_res_apply_flag = False
        else:
            self.video_res_apply_flag = True


    def set_video_res_default(self, value):

        """Called by mainwin.MainWin.set_video_res_limit() and
        .on_video_res_combobox_changed()().

        Sets the new video resolution limit. If a download operation is in
        progress, the new value is applied to the next download job.

        Args:

            value (str): The new video resolution limit (a key in
                formats.VIDEO_RESOLUTION_DICT, e.g. '720p')

        """

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16300 set_video_res_default')

        if not value in formats.VIDEO_RESOLUTION_DICT:
            return self.system_error(
                158,
                'Set video resolution request failed sanity check',
            )

        self.video_res_default = value


    def set_ytdl_output_ignore_json_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16314 set_ytdl_output_ignore_json_flag')

        if not flag:
            self.ytdl_output_ignore_json_flag = False
        else:
            self.ytdl_output_ignore_json_flag = True


    def set_ytdl_output_ignore_progress_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16325 set_ytdl_output_ignore_progress_flag')

        if not flag:
            self.ytdl_output_ignore_progress_flag = False
        else:
            self.ytdl_output_ignore_progress_flag = True


    def set_ytdl_output_show_summary_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16336 set_ytdl_output_show_summary_flag')

        if not flag:
            self.ytdl_output_show_summary_flag = False
        else:
            self.ytdl_output_show_summary_flag = True


    def set_ytdl_output_start_empty_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16347 set_ytdl_output_start_empty_flag')

        if not flag:
            self.ytdl_output_start_empty_flag = False
        else:
            self.ytdl_output_start_empty_flag = True


    def set_ytdl_output_stderr_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16358 set_ytdl_output_stderr_flag')

        if not flag:
            self.ytdl_output_stderr_flag = False
        else:
            self.ytdl_output_stderr_flag = True


    def set_ytdl_output_stdout_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16369 set_ytdl_output_stdout_flag')

        if not flag:
            self.ytdl_output_stdout_flag = False
        else:
            self.ytdl_output_stdout_flag = True


    def set_ytdl_output_system_cmd_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16380 set_ytdl_output_system_cmd_flag')

        if not flag:
            self.ytdl_output_system_cmd_flag = False
        else:
            self.ytdl_output_system_cmd_flag = True


    def set_ytdl_path(self, path):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16391 set_ytdl_path')

        self.ytdl_path = path


    def set_ytdl_update_current(self, string):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16399 set_ytdl_update_current')

        self.ytdl_update_current = string


    def set_ytdl_write_ignore_json_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16407 set_ytdl_write_ignore_json_flag')

        if not flag:
            self.ytdl_write_ignore_json_flag = False
        else:
            self.ytdl_write_ignore_json_flag = True


    def set_ytdl_write_ignore_progress_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16418 set_ytdl_write_ignore_progress_flag')

        if not flag:
            self.ytdl_write_ignore_progress_flag = False
        else:
            self.ytdl_write_ignore_progress_flag = True


    def set_ytdl_write_stderr_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16429 set_ytdl_write_stderr_flag')

        if not flag:
            self.ytdl_write_stderr_flag = False
        else:
            self.ytdl_write_stderr_flag = True


    def set_ytdl_write_stdout_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16440 set_ytdl_write_stdout_flag')

        if not flag:
            self.ytdl_write_stdout_flag = False
        else:
            self.ytdl_write_stdout_flag = True


    def set_ytdl_write_system_cmd_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16451 set_ytdl_write_system_cmd_flag')

        if not flag:
            self.ytdl_write_system_cmd_flag = False
        else:
            self.ytdl_write_system_cmd_flag = True


    def set_ytdl_write_verbose_flag(self, flag):

        if DEBUG_FUNC_FLAG:
            utils.debug_time('app 16462 set_ytdl_write_verbose_flag')

        if not flag:
            self.ytdl_write_verbose_flag = False
        else:
            self.ytdl_write_verbose_flag = True
