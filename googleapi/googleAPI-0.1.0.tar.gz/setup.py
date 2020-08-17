import setuptools
import versioneer

with open("README.md", "r") as fh:
    long_description = fh.read()
with open("requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh]

setuptools.setup(
    name="googleAPI",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Zeyu Yang",
    author_email="zy2327@columbia.edu",
    description="A high-level python interface to Google APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zy2327/googleAPI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
)
