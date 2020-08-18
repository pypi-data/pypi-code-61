from setuptools import find_packages, setup

setup(
    name="sgtree",
    version="0.0.10",
    packages=find_packages(),
    license="Modified BSD",
    description="Computational pipeline for fast and easy construction of phylogenetic trees.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "importlib-metadata>=0.12; python_version<'3.8'",
        "setuptools",
        "numpy",
        "pandas",
        "setuptools"
    ],
    python_requires=">=3.7",
    entry_points={"console_scripts": ["sgtree=sgtree_final:main"]},
    url="https://bitbucket.org/ewanjameswhittakerwalker/sgtree",
    keywords=["bioinformatics", "genomics", "metagenomics", "phylogenetics"],
    author="Frederik Schulz, Ewan Whittaker Walker, Sean Jungbluth",
    classifiers=[
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
    ],
)
