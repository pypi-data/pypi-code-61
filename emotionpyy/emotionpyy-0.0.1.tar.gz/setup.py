from setuptools import setup
import setuptools

def readme():
    with open('README.md', encoding="utf8") as f:
        README = f.read()
    return README


setup(
    name="emotionpyy",
    version="0.0.1",
    description="Detecting emotions behind the text, pyemotionpyy package will help you to understand the emotions in textual meassages.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/aman2656/pyemotion_library",
    author="Pyemotion Team",
    author_email="pyemotionteam@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ],
    packages= setuptools.find_packages(),
    include_package_data=True,
    install_requires=["nltk>=3.5", "numpy>=1.19.1", "emoji>=0.6.0", "pandas>=1.1.0"],
    python_requires='>=3.6'
)