# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['emu']

package_data = \
{'': ['*']}

install_requires = \
['oletools>=0.55.1,<0.56.0',
 'prettytable>=0.7.2,<0.8.0',
 'pyparsing>=2.4.7,<3.0.0',
 'python-magic>=0.4.18,<0.5.0']

entry_points = \
{'console_scripts': ['emu = emu.__main__:main']}

setup_kwargs = {
    'name': 'spurious-emu',
    'version': '0.1.0',
    'description': 'VBA static and dynamic analysis tool for malware analysts',
    'long_description': "# SpuriousEmu\n\nVisual Basic for Applications tools allowing to parse VBA files, interpret them and extract behaviour information for malware analysis purpose.\n\n## Usage\n\nSpuriousEmu can work with VBA source files, or directly with Office documents. For the later case, it relies on olevba to extract macros from the files. For each of the commands, use the `-i` flag to specify the input file to work with, whatever its format.\n\nIf you work with VBA source files, the following convention is used:\n    - procedural modules have `.bas` extension\n    - class modules have `.cls` extension\n    - standalone script files have `.vbs` extension\n\nSpuriousEmu uses different subcommands for its different operating modes.\n\n### Static analysis\n\nStatic analysis is performed using the `static` subcommand.\n\nUsually, the first step is to determine the different functions and classes defined, in order to understand the structure of the program. You can for example use it to determine the entry point prior to dynamic analysis. It is the default behaviour when using no other flag than `-i`:\n\n```bash\n./emu.py static -i document.xlsm\n```\n\nAdditionally, for large files, you can use the `-o` flag to serialize the information compiled during static analysis into a binary file that you will be able to use later with the `-i` flag:\n\n```bash\n./emu.py static -i document.xlsm -o document.spurious-com\n```\n\nYou can also de-obfuscate a file by using the `-d` flag, which specifies the de-obfuscation level. You can output the whole file, or a single function or module using the `-e` flag. The result can be sent to standard output or written to a file specified with the `-o` file:\n\n```bash\n./emu.py static -i document.xlsm -d3 -e VBAEnv.Default.Main -o Main.bas\n```\n\n### Dynamic analysis\n\nYou can trigger dynamic analysis with the `dynamic` subcommand.\n\nOnce you have found the entry-point you want to use with the `static` subcommand, you can execute a file by specifying it with the `-e` flag. For example, to launch the `Main` function found in `doc.xlsm`, use\n\n```bash\n./emu.py dynamic -i doc.xlsm -e Main\n```\n\nThis will display a report of the execution of the program. Additionally, if you want to save the files created during execution, you can use the `-o` flag: it specifies a directory to save files to. Each created file is then stored in a file with its md5 sum as title, and a `{hash}.filename.txt` file contains its original name.\n\n## Dependencies\n\nPython 3.8 is used, and SpuriousEmu mainly relies on `pyparsing` for VBA grammar parsing, and `oletools` to extract VBA macros from Office documents.\n\n`nose` is used as testing framework, and `mypy` to perform static code analysis. `lxml` and `coverage` are used to produce test reports.\n\n## Tests\n\nTo set a development environment up, use `poetry`:\n\n```bash\npoetry install\n```\n\nThen, use nose to run the test suite:\n\n```bash\npoetry run nosetests\n```\n\nAll test files are in `tests`, including:\n    - Python test scripts, starting with `test_`\n    - VBA scripts used to test the different stages of the tools, with `vbs` extensions, stored in `source`\n    - expected test results, stored as JSON dumps in `result`\n\n\nYou can use mypy to perform code static analysis:\n\n```bash\npoetry run mypy emu/*.py\n```\n\nBoth commands produce HTML reports stored in 'tests/report'.\n",
    'author': 'Louis Dubois',
    'author_email': 'ldbo@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ldbo/SpuriousEmu',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
