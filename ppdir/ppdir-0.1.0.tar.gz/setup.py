import setuptools


with open("README.md", "r") as file:
    long_description = file.read()


setuptools.setup(
    name="ppdir",
    version="0.1.0",
    author="Emanuel Claesson",
    author_email="emanuel.claesson@gmail.com",
    description="Pretty print a directory structure as a tree",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EClaesson/ppdir",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires=[
        'colorama>=0.4.3'
    ],
    entry_points={
        'console_scripts': ['ppdir=ppdir:main'],
    },
)
