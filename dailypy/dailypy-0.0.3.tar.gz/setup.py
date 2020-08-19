from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='dailypy',
  version='0.0.3',
  description='A useful library used everyday',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Jack Huang',
  author_email='jackhuang.wz@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Tools', 
  packages=find_packages(),
  install_requires=['numpy'] 
)

