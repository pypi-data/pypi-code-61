import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="BottleRoutes",
    version="2020.08.20",
    author="Afonso Medeiros",
    author_email="afonso.b.medeiros@gmail.com",
    description="Plugin to use OO to create routes in bottle.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/afonsomedeiros/BottleRoutes",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    license='MIT',
)
