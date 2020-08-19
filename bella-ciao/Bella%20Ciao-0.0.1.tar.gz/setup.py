import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Bella Ciao", # Replace with your own username
    version="0.0.1",
    author="Samācāraṁ Śāstravētta",
    author_email="bella.ciao.062020@gmail.com",
    description="Bella Ciao Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BellaCiao2020/BellaCiao",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)