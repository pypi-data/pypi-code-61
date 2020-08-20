from setuptools import setup


setup(name='test_packaging',
      version='0.1.5',
      description='Test of packaging.',
      long_description='Test of packaging math, etc.',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6',
          'Topic :: Text Processing :: General',
      ],
      url='http://github.com/hector-mao-net/test_packaging',
      author='Hector Mao',
      author_email='hectormao1025@gmail.com',
      license='MIT',
      packages=['test_packaging'],
      install_requires=[
          'numpy',
      ],
      include_package_data=True,
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'])
