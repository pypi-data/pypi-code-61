from setuptools import setup, find_packages
import io
import os
current = os.path.realpath(os.path.dirname(__file__))
with io.open(os.path.join(current, 'README.md'), encoding="utf-8") as f:
    long_description = f.read()
setup(
    name='climailsystem',
    version='0.11',
    author = 'Akshit Ahuja',
    author_email = "techsyapa@gmail.com",
    description = "A small Package for sending  mails from cli",
    url = "https://github.com/aksh45/climailsystem",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['sendmail'],
    include_package_data=True,
    install_requires=[
        'Click','pybase64','google-api-python-client','google-auth-httplib2','google-auth-oauthlib'
    ],
    entry_points='''
        [console_scripts]
        sendmail=sendmail.__main__:main
    ''',
)
