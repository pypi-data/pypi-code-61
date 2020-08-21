# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dapodix']

package_data = \
{'': ['*']}

install_requires = \
['dapodik>=0.2.1,<0.3.0', 'openpyxl>=3.0.5,<4.0.0']

setup_kwargs = {
    'name': 'dapodix',
    'version': '0.1.0',
    'description': 'Alat bantu aplikasi Dapodik',
    'long_description': '# dapodix\n\n[![dapodix - PyPi](https://img.shields.io/pypi/v/dapodix)](https://pypi.org/project/dapodix/)\n[![Group Telegram](https://img.shields.io/badge/Telegram-Group-blue.svg)](https://t.me/dapodik_2021)\n[![Donate DANA](https://img.shields.io/badge/Donasi-DANA-blue)](https://link.dana.id/qr/1lw2r12r)\n[![Download](https://img.shields.io/badge/Download-Unduh-brightgreen)](https://github.com/hexatester/dapodix/archive/master.zip)\n[![Tutorial](https://img.shields.io/badge/Tutorial-Penggunaan-informational)](https://github.com/hexatester/dapodix/wiki)\n[![LISENSI](https://img.shields.io/github/license/hexatester/dapodix)](https://github.com/hexatester/dapodix/blob/master/LISENSI)\n\nAlat bantu aplikasi dapodik.\n\n## Release\n\nPerkiraan release versi 1 akhir bulan September 2020,\n\n## Fitur yang akan datang\n\n- Download data ke Excel\n- Petunjuk validasi\n- Bulk update dari Excel\n\n## Legal / Hukum\n\nKode ini sama sekali tidak berafiliasi dengan, diizinkan, dipelihara, disponsori atau didukung oleh [Kemdikbud](https://kemdikbud.go.id/) atau afiliasi atau anak organisasinya. Ini adalah perangkat lunak yang independen dan tidak resmi. _Gunakan dengan risiko Anda sendiri._\n',
    'author': 'hexatester',
    'author_email': 'revolusi147id@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/hexatester/dapodix',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
