import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyTCID",
    version="1.0.0",
    author="Ege Ozkan",
    author_email="egeemirozkan24@gmail.com",
    description="Unofficial Python API to verify Turkish National ID Cards.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ambertide/PyTCID",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)