import setuptools

with open("README.md", 'r') as f:
    long_description = f.read()

setuptools.setup(
    name = "gomaps",
    version = "0.1.1",
    author = "David J. Morfe",
    author_email = "jakemorfe@gmail.com",
    license = "MIT",
    description = "A package that queries google maps & scrapes its data",
    long_description=long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/jakeee51/gmapi",
    packages = setuptools.find_packages(),
    py_modules = ["gmapss", "busytimes"],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"]
)
