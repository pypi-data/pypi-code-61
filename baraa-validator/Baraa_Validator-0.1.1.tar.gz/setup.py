from setuptools import setup, find_packages
setup(
    name='Baraa_Validator',
    packages=find_packages(include=['BaraaValidator','BaraaValidator.gRPC']),
    version= '0.1.1',
    description='A simple library that provide multiple useful validation methods.',
    author='Baraa Abu-Alrub',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner','xmltodict'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)