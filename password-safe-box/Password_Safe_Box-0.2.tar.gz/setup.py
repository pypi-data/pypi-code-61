import setuptools

with open("README.md","r") as fh:
    ldesc = fh.read()

setuptools.setup(
    name = 'Password_Safe_Box',
    version = '0.2',
    author = 'Jim',
    author_email = 'TheDarkProgrammers@gmail.com',
    description = 'Store any password you want with the most secure way',
    long_description = ldesc,
    long_description_content_type="text/markdown",
    url = 'https://github.com/Vbrawl/Password_Safe_Box',
    packages = setuptools.find_packages(),
    classifiers = [
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.x',
)
