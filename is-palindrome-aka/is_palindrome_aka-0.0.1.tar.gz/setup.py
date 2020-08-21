from setuptools import setup,find_packages

setup(
    name='is_palindrome_aka',
    version='0.0.1',
    description='My first python package for checking pallindrome',
    long_description=open('readme.txt').read(),
    author='Akash Mane',
    keywords={'palindrome','python palindrome package'},
    license='MIT',
    packages= ['is_palindrome_aka'],
    install_requires= ['']

)