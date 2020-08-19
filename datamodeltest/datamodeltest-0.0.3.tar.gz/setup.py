import setuptools
import tests_pkg

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="datamodeltest",
    version=tests_pkg.version,
    author="Me",
    author_email="me@example.com",
    packages=['tests_pkg'],
    entry_points={
        'console_scripts':['data-models = tests_pkg.cli:entry_point'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
