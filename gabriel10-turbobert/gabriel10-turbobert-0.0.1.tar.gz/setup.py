import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gabriel10-turbobert",
    version="0.0.1",
    author="Robert Degen",
    author_email="os@turbobert.de",
    description="Very Simple PDF TypeWriter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/turbobert/gabriel10",
    packages=setuptools.find_packages(),
    classifiers=[
    ],
    python_requires=">=3.6"
)
