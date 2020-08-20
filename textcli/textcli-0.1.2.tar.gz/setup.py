from textcli import __version__

import os
import sys

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup


dependencies = ['docopt', 'termcolor', 'brotli']


def publish():
	os.system("python3 setup.py sdist upload")



if sys.argv[-1] == "publish":
	publish()
	sys.exit()


setup(
	name='textcli',
	version='.'.join(str(i) for i in __version__),
	description='Textvn quick save text CLI',
	long_description="Textvn quick save text CLI, save your text quickly",
	author='Le Song Vi',
	author_email='lesongvi@gmail.com',
	url="https://github.com/lesongvi/textcli",
	license="GPLv3+",
	install_requires=dependencies,
	packages=['textcli'],
    py_modules=['textcli'],
	entry_points={
		'console_scripts': [
			'texcl=textcli.cli:start'
		]
	},
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'Natural Language :: English',
		'Programming Language :: Python',
	]
	) 


