# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dapodik',
 'dapodik.cli',
 'dapodik.customrest',
 'dapodik.peserta_didik',
 'dapodik.ptk',
 'dapodik.rest',
 'dapodik.rombongan_belajar',
 'dapodik.sarpras',
 'dapodik.sekolah',
 'dapodik.tools',
 'dapodik.tools.backup',
 'dapodik.utils']

package_data = \
{'': ['*']}

install_requires = \
['cachetools>=4.1.1,<5.0.0',
 'click>=7.1.2,<8.0.0',
 'dacite>=1.5.1,<2.0.0',
 'openpyxl>=3.0.4,<4.0.0',
 'requests>=2.24.0,<3.0.0']

entry_points = \
{'console_scripts': ['dapodik = dapodik.__main__:main']}

setup_kwargs = {
    'name': 'dapodik',
    'version': '0.1.0',
    'description': 'Client & alat bantu aplikasi Dapodik',
    'long_description': '# dapodik\n\n[![Group Telegram](https://img.shields.io/badge/Telegram-Group-blue.svg)](https://t.me/dapodik_2021)\n[![Donate DANA](https://img.shields.io/badge/Donasi-DANA-blue)](https://link.dana.id/qr/1lw2r12r)\n[![Download](https://img.shields.io/badge/Download-Unduh-brightgreen)](https://github.com/hexatester/dapodik/archive/master.zip)\n[![Tutorial](https://img.shields.io/badge/Tutorial-Penggunaan-informational)](https://github.com/hexatester/dapodik/wiki)\n[![LISENSI](https://img.shields.io/github/license/hexatester/dapodik)](https://github.com/hexatester/dapodik/blob/master/LISENSI)\n\nAlat bantu aplikasi dapodik.\n\n## Release\n\nPerkiraan release versi 1 akhir bulan September 2020,\n\n## Fitur yang akan datang\n\n- Download data ke Excel\n- Petunjuk validasi\n- Bulk update dari Excel\n- Python Client\n\n## Legal / Hukum\n\nKode ini sama sekali tidak berafiliasi dengan, diizinkan, dipelihara, disponsori atau didukung oleh [Kemdikbud](https://kemdikbud.go.id/) atau afiliasi atau anak organisasinya. Ini adalah perangkat lunak yang independen dan tidak resmi. _Gunakan dengan risiko Anda sendiri._\n',
    'author': 'hexatester',
    'author_email': 'habibrohman@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/hexatester/dapodik',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
