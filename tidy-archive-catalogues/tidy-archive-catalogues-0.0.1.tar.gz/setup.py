import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tidy-archive-catalogues",
    version="0.0.1",
    author="Natalie Thurlby",
    author_email="natalie.thurlby@bristol.ac.uk",
    description="Code to tidy archivist catalogues into human- and computer-readable formats.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NatalieThurlby/tidy-archive-catalogues",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)