import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aimrobot",
    version="0.0.1",
    author="A.L",
    author_email="alha@kadk.dk",
    description="A library to run Robotic Assembly Digital Model (RADM) files directly on Universal Robots.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ALharchi/aimrobot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)