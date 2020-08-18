import setuptools
with open("README.md", "r") as fh:
	long_description=fh.read()
	
setuptools.setup(
    name="elkAnalyzer", # Replace with your own username
    version="0.0.2",
    author="Elizabeth Pogue",
    author_email="epogue1@jhu.edu",
    description="A small package for analyzing Elk outputs",
	keywords="elk, dft",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/euclidmenot2/elkAnalyzer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)