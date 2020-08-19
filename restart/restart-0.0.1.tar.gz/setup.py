import setuptools

with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Restart Partners",
    author_email="admin@restart.us",
    name='restart',
    version='v0.0.1',
    long_description=README,
    url='https://github.com/restartus/covid-projection',
    packages=setuptools.find_packages(),
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
    ]
)


