import setuptools

setuptools.setup(
    name='pypi-semantic',
    long_description=open('README.md').read(),
    packages=[
        'pypi_semantic',
        'tests',
    ],
    entry_points={
        'console_scripts': ['mtest=pypi_semantic.app:main'],
    },
)
