import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="UR_TCP_RTDE",
    version="0.0.1",
    author="scoard",
    author_email="mwangbuaa@126.com",
    description="UR manipulator communiaction packge.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=" https://github.com/scoard/UR_RTDE",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
