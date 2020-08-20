import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.1'
PACKAGE_NAME = 'simply_progress'
AUTHOR = 'Jordan Mesches'
AUTHOR_EMAIL = 'jordanmesches@gmail.com'
URL = 'https://github.com/Meschdog18/simply-progress'

LICENSE = 'MIT Licenses'
DESCRIPTION = 'A light and easy to use progress bar for python'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"


setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      packages=find_packages()
      )

