import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="commditycategory", 
    version="0.9.4",
    author="Xinmin Su",
    author_email="xinmin.su@hotmail.com",
    description="Get the commdity's category",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xinminsu/commditycategory",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)