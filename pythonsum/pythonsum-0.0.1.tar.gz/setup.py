import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pythonsum", # Replace with your own username
    version="0.0.1",
    author="Rajesh Berwal",
    author_email="irajeshberwal@gmail.com",
    description="A package to get sum of given numbers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rajeshberwal/pythonsum",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)