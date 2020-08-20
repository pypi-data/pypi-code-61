from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
]

setup(
    name="Simple_Calculator",
    version="0.0.1",
    description="A basic calculator which add, subtracts, multiplies and divides",
    Long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author="Punyashlok",
    author_email="itsmathsmagic18@gmail.com",
    license="MIT",
    classifiers=classifiers,
    keywords='calculator',
    packages=find_packages(),
    install_requires=['']
)