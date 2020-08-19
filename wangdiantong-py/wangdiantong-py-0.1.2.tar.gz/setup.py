# -*- coding: utf-8 -*-
import wangdiantong as wdt
from os.path import dirname, abspath, join

from setuptools import setup, find_packages

LIB_DIR = dirname(abspath(__file__))


def long_description():
    with open(join(LIB_DIR, 'README.md')) as readme_file:
        readme = readme_file.read()

    # with open(join(LIB_DIR, 'HISTORY.md')) as history_file:
    #     history = history_file.read()
    # return readme + '\n\n' + history


requirements = ['certifi', 'chardet', 'idna', 'requests', 'urllib3']

test_requirements = ['appnope==0.1.0', 'atomicwrites==1.1.5', 'attrs==18.1.0', 'backports.shutil-get-terminal-size==1.0.0', 'bumpversion==0.5.3', 'cov-core==1.15.0', 'coverage==4.5.1', 'decorator==4.3.0', 'enum34==1.1.6', 'funcsigs==1.0.2', 'ipython-genutils==0.2.0', 'ipython==5.7.0', 'lxml==4.2.1', 'more-itertools==4.2.0', 'namedlist==1.7',
                     'nose-allure-plugin==1.0.5', 'nose-cov==1.6', 'nose==1.3.7', 'pathlib2==2.3.2', 'pexpect==4.5.0', 'pickleshare==0.7.4', 'pluggy==0.6.0', 'prompt-toolkit==1.0.15', 'ptyprocess==0.5.2', 'py==1.5.3', 'pygments==2.2.0', 'pytest-allure-adaptor==1.7.10', 'pytest==3.6.0', 'scandir==1.7', 'simplegeneric==0.8.1', 'six==1.11.0', 'traitlets==4.3.2', 'wcwidth==0.1.7']


setup(
    name='wangdiantong-py',
    packages=find_packages(exclude=['wangdiantong.tests']),
    version=wdt.__version__,
    description="wangdiantong python openapi",
    long_description_content_type="text/markdown",
    long_description=long_description(),
    author=wdt.__author__,
    author_email=wdt.__email__,
    url='https://github.com/AoAoStudio/wangdiantong-py',
    entry_points={
        'console_scripts': [
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='wangdiantong',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='nose.collector',
    tests_require=test_requirements
)
