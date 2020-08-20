from setuptools import setup, find_packages

setup(
  name='say-hi',
  version='0.0.1',
  description='It wishes the person',
  long_description=open('readme.txt').read(),# + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Balaji Betadur',
  author_email='balajibetadur@gmail.com',
#   classifiers=classifiers,
  keywords=['say hi'],
  license='MIT', 
  packages=['greet'], # find_packages(),
  include_package_data=True,
  install_requires=[] 
) 