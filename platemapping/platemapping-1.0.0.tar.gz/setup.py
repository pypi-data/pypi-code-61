import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="platemapping", 
    version="1.0.0",
    author="Stuart Warriner, Lawrence Collins",
    author_email="s.l.warriner@leeds.ac.uk, lawrencejordancollins@gmail.com",
    description="Plate map uploading, processing & visualisaion",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lawrencecollins/platemapping",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    setup_requires=['wheel']
)
