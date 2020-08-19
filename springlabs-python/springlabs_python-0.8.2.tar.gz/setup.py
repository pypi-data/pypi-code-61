import setuptools
from springlabs_pypi import __version__ as version
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='springlabs_python',
    version=version,
    packages=setuptools.find_packages(),
    include_package_data=True,
    author="Alejandro Barcenas",
    author_email="barcenas.r.2510@gmail.com",
    description="Springlabs Projects Python Standard",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/AlejandroBarcenas/springlabs-python-cli",
    install_requires=['Click', "requests==2.24.0"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points='''
        [console_scripts]
        springlabs_python=springlabs_pypi.scripts.springlabs_python:cli
    ''',
)
