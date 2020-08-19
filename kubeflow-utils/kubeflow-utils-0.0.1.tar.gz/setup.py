import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kubeflow-utils",  # Replace with your own username
    version="0.0.1",
    author="Chao Tzu-Hsien",
    author_email="danny900714@gmail.com",
    description="Kubeflow utils package helping to speed up building ML model.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GalaxyIT/kubeflow-utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
