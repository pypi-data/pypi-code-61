from setuptools import setup, find_packages

setup(name='sqgtool',
      version='0.0.5.dev5',
      description='Classification of stars, quasars, and galaxies in S-PLUS',
      url='http://github.com/marixko/sqgtool',
      author='Lilianne Nakazono',
      author_email='lilianne.nakazono@usp.br',
      license='MIT',
      packages=find_packages(),
      classifiers=['Development Status :: 3 - Alpha',
                   'Programming Language :: Python :: 3',
                   'Intended Audience :: Science/Research',
                  'Topic :: Scientific/Engineering :: Astronomy'
                   ],
      python_requires='>=3',
      include_package_data=True,
      zip_safe=False,
      install_requires=['numpy', 'pandas', 'scikit-learn', 'astropy', 'tqdm'])