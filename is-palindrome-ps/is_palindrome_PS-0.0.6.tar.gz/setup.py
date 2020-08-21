from setuptools import setup, find_packages

setup(
    name = 'is_palindrome_PS',# while insdtalling pacakge
    version = '0.0.6',
    description = 'This is a palindrome checking function.',
    long_description = open('Readme.txt').read(),
    url = 'https://balajibetadur.github.io',
    author = 'Prakash Shelar',
    keywords = ['palindrome','python palindrome','palindrome evaluator'],
    license = 'MIT',
    packages = ['is_palindrome_PS'],# while impoerting package install_require
)