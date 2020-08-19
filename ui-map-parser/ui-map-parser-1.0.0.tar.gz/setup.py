# -*- coding: utf-8 -*-

__author__ = 'f1ashhimself@gmail.com'


from os import path

from setuptools import setup


def package_env(file_name, strict=False):
    file_path = path.join(path.dirname(__file__), file_name)
    if path.exists(file_path) or strict:
        return open(file_path).read()
    else:
        return ''


if __name__ == '__main__':
    setup(
        name='ui-map-parser',
        version='1.0.0',
        description='UI map parser.',
        long_description=package_env('README.md'),
        long_description_content_type='text/markdown',
        author='Max Biloborodko',
        author_email='f1ashhimself@gmail.com',
        packages=['ui_map_parser'],
        include_package_data=True,
        zip_safe=False
    )
