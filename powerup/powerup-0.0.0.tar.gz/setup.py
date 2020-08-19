import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="powerup",
    version="0.0.0",
    author="ambientnuance",
    author_email="ambientnuance@gmail.com",
    description="An ensemble of upcoming power packages.",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
