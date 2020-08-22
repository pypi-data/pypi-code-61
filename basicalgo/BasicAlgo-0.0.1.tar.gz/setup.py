import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BasicAlgo",
    version="0.0.1",
    author="Harsh Chaplot, Kandarp Kakkad",
    author_email="17bit026@nirmauni.ac.in, 17bit034@nirmauni.ac.in",
    description="Using basic algorithms via c++",
    long_description=long_description,
    license="MIT",
    long_description_content_type="text/markdown",
    url="https://github.com/kandarpkakkad/BasicAlgo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
