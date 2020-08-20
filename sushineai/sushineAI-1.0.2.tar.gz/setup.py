"""
@author: zhangX
@license: (C) Copyright 1999-2019, NJ_LUCULENT Corporation Limited.
@contact: 494677221@qq.com
@file: setup.py.py
@time: 2019/12/17 10:38
@desc:
"""

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='sushineAI',
    version='1.0.2',
    description='SuShine DataIntelligencePlatform Helper',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='sushine',
    packages=setuptools.find_packages(),
    author='Xiang zhang',
    author_email='zhangx@luculent.net',
    url='https://www.sushine.net/pages/web/industrialBrain.html',
    classifiers=[
        'Development Status :: 5 - Production/Stable',  # 当前开发进度等级（测试版，正式版等）
        'Intended Audience :: Developers',  # 模块适用人群
        'Topic :: Software Development :: Code Generators',  # 给模块加话题标签
        'License :: OSI Approved :: MIT License',  # 模块的license

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    project_urls={  # 项目相关的额外链接
        'official website': 'https://www.sushine.net',
    },
)