# -*- coding:utf-8 -*-

import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='featureview',
    version='1.0.4',
    author='Jiahui Lu',
    author_email='jiahui.lu.external@veoneer.com',
    description='A tool for feature visualization',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    packages=setuptools.find_packages('.'),
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Operating System :: Microsoft :: Windows :: Windows 10'
    ],
    python_requires='>=3.7.4, <=3.8',
    install_requires=[
        'wheel',
        'mdfreader==3.3',
        'numpy==1.17.4',
        'PyQt5==5.13.2',
        'pyqtgraph==0.10.0'
    ],
    package_data={'featureview': [
        'featureview/ui/*.ui',
        'featureview/ui/*.qrc',
        'featureview/ui/images/*.png'
    ]},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'featureview=featureview.featureviewgui: main',
        ],
    },
)
