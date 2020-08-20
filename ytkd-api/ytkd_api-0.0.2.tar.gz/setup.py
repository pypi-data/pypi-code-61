import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ytkd_api",
    version="0.0.2",
    author="Ali Haider",
    author_email="alinisarhaider@gmail.com",
    description="A Python wrapper for YouTube Key word detection API. ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["ytkd_api"],
    package_dir={'': 'src'},
    url="https://github.com/alinisarhaider/ytkd_api",
    # packages=setuptools.find_packages(),
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
