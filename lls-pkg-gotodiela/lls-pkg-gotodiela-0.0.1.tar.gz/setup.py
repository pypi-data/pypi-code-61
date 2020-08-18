import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="lls-pkg-gotodiela",
  version="0.0.1",
  author="lls",
  author_email="null@null.com",
  description="A package for localization",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/pypa/sampleproject", #是項目主頁的URL。指向GitHub，GitLab，Bitbucket
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)