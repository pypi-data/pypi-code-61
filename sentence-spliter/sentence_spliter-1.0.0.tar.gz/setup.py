from setuptools import setup, find_packages

setup(
    name="sentence_spliter",
    version="1.0.0",
    description="This is a sentence cutting tool that supports long sentence segmentation and short sentence merging.",
    author="Li Wang",
    author_email="wangli6@yy.com",
    # package_dir={"":"sentence_spliter"},
    packages=['sentence_spliter'],

    lassifiers=[
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
    REQUIRES_PYTHON='>=2.6.0',
    install_requires=['attrdict>=2.0.1']
)
