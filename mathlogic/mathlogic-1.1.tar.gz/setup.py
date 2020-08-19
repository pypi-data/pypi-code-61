from setuptools import setup

setup(name='mathlogic',
      version='1.1',
      description='Python Utilities from MathLogic',
      url='https://github.com/vermanurag/mathlogic-mathlogic',
      author='Anurag Verma',
      author_email='anurag.verma@fnmathlogic.com',
      license='All Rights Reserved',
      packages=['mathlogic'],
      install_requires=[            # I get to this in a second
          'pandas',
          'jinja2',
          'numpy',
          'mysql-python',
          'Ipython'
      ],
      zip_safe=False)
