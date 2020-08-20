from setuptools import setup

setup(name='test_packaging',
      version='0.1.2',
      description='test of packaging',
      url='http://github.com/hector-mao-net/test_packaging',
      author='Hector Mao',
      author_email='hectormao1025@gmail.com',
      license='MIT',
      packages=['test_packaging'],
      install_requires=[
          'numpy',
      ],
      zip_safe=False)
