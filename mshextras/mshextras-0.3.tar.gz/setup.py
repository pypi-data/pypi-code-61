from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'mshextras',         # How you named your package folder (MyLib)
    version = '0.3',      # Start with a small number and increase it with every change you make
    license='gpl-3.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description = 'Extra fields for Marshmallow', 
    author = 'BK Shrinandhan',
    author_email = 'python.access.server@gmail.com',
    url="https://github.com/bnnk/marshmallow-extras",
    packages=["mshextras"],
    install_requires=[
        "numpy","pandas","pyotp","requests","furl"
    ],
    project_urls={
        'Documentation': 'https://github.com/bnnk/marshmallow-extras/blob/master/README.md/',
        'Say Thanks!': 'https://saythanks.io/to/bk.shrinandhan%40gmail.com/',
        'Source': 'https://github.com/bnnk/marshmallow-extras/',
        'Tracker': 'https://github.com/bnnk/marshmallow-extras/issues',
    },
    classifiers=[
    	'Development Status :: 4 - Beta',      
    	'Intended Audience :: Developers',      
    	'Programming Language :: Python :: 3',      
    	'Programming Language :: Python :: 3.4',
    	'Programming Language :: Python :: 3.5',
    	'Programming Language :: Python :: 3.6',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
