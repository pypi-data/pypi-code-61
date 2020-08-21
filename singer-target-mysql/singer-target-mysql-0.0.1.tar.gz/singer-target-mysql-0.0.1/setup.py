import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="singer-target-mysql",
    version="0.0.1",
    author="Adrien Czerny",
    author_email="adrien@example.com",
    description="A Singer.io target implementation for MySQL",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/czardien/target-mysql",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
