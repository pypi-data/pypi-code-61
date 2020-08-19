# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['osuplaylist']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['osuplaylist = osuplaylist:main']}

setup_kwargs = {
    'name': 'osuplaylist',
    'version': '3.1.0',
    'description': 'Export audio from osu to directory/to ingame collection/to steam music  or create m3u8 playlist',
    'long_description': '# osuplaylist\n[![PyPI](https://img.shields.io/pypi/v/osuplaylist?style=for-the-badge)](https://pypi.org/project/osuplaylist) \n- Extract all osu songs, collection,run a regex search in .osu tag line , apply daterange \n- Export audio to directory/to ingame collection/to steam queue or create m3u8 playlist\n- Import your songs in .mp3 format to osu\n- Use as a module  \n![screenshot_export_to_steam_from_osu](https://raw.githubusercontent.com/upgradeQ/osuplaylist/master/export.jpg)\n# Installation \nPython version >= 3.6  \n`pip install osuplaylist`  \nupdate `pip install osuplaylist -U`\n# Limitations\n- refresh `<F5>` if beatmap library is not correct\n- creation of ingame collection requires to restart client\n- importing your mp3 requires restart & refresh `F5` & ascii name\n## Commands\n### export all songs as .m3u8 playlist, may take a while\n  `osuplaylist`\n### apply daterange (optional)\n  `osuplaylist --date_range "daterange"`,daterange format:Year.month.day\n  example: >2020.1.1 older than, 2020.1.1:2020.1.24 in this range \n  this will include last played beatmaps in that timeframe.\n### export collection. Name might be case insensitive or with typos \n `osuplaylist --collection "name of collection"`\n### export to ingame collection. Name will be with current timestamp. (optional)\n `osuplaylist --update_db "name of collection"` \n### run a regex search on tags provided from .osu file \n`osuplaylist --regtag "regex"`\n### run an inversed regex search on tags (optional)\n  `osuplaylist -r "regex" -i ` \n###  provide path to export audio.(optional) if used without arg - all songs\n  `osuplaylist --to_dir "path"`\n### export to steam queue.m3u8 \n `osuplaylist -r "step" -s` close steam first, this will overwrite queue.m3u8 from _database of steam, you will be asked just one time to provide full path \n### import mp3s \n   `osuplaylist -m "E:Installation\\music" -n "in_game_collection_name"`, name _ascii only_  and you need manually click all mp3s, search mp3 in osu,and click,otherwise collections will not work\n### info\n `osuplaylist --help` \n\n## Examples \n### Example  with [mpv](https://mpv.io/):\n  `mpv --playlist=playlist.m3u8 --shuffle --volume 35` \n### Example regex search + inverse + to directory:\n `osuplaylist -r "(azer|step)" -i -d "E:/music/osuplaylist"`\n`-r "(azer|step)"` will match all songs which contain azer or step\n\n`-i` (optional) return an inverted result , all songs which NOT contain azer or step\n\n`-d` (optional) export .mp3 to directory E:/music/osuplaylist\n### Example combine regex + daterange + to steam\n`osuplaylist -r "step" -t ">2020.1.1" -s`\n# Using osuplaylist.py as module\nSee [tests](/tests)\n# Contribute\nContributions are welcome!\n# See also \n- https://github.com/osufiles/osu-bgchanger - A simple tool for automatically changing all your osu! beatmap backgrounds to a custom one .\n- https://github.com/upgradeQ/OSU-STREAM-DETECTOR - osu standard stream map identifier & exporter to ingame collection .\n- https://github.com/Piotrekol/CollectionManager - gui collections creator & manager for osu\n- https://gitlab.com/esrh/osu-cplayer - tui (urwid) osu player based on mpv\n',
    'author': 'upgradeq',
    'author_email': 'noreply@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/upgradeQ/osuplaylist',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
