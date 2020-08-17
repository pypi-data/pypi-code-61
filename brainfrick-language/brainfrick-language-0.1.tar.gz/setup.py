from setuptools import setup, find_packages

setup(
    name='brainfrick-language',
    packages=find_packages(),
    version='0.1',
    description='An Interpreter for the BrainFuck language.',
    author='Chris Oliver',
    author_email='chrisoliver345@gmail.com',
    url='',
    download_url='',
    keywords=['brainfuck', 'pypi', 'package', 'brainfrick', 'interpreter'],  # arbitrary keywords
    install_requires=[
        'pytest==2.9.2',
        'ply==3.11'
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    entry_points={
        'console_scripts': [
            'brainfuck = brainfuck.brainfuck:run'
        ]},
)
