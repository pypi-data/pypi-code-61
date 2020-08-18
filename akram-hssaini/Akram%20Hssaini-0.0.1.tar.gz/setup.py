import setuptools

with open("README.txt", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Akram Hssaini",
    version="0.0.1",
    author="Akram Hssaini",
    author_email="iakram240904@gmail.com",
    description="A decision tree algorithm",
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='ml,ai,decision tree',
    install_requires=['time','random','pathlib']
)