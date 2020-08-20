import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gridfrequency", # Replace with your own username
    version="1.0",
    author="Joakim Argillander",
    author_email="joakim@argillander.se",
    description="Python wrapper for obtaining the current frequency of the Swedish national power grid",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/argillander/GridFrequency",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)