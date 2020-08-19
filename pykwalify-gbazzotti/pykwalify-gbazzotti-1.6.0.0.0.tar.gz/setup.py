import setuptools

setuptools.setup(
  name = 'pykwalify-gbazzotti',
  packages=setuptools.find_packages(),
  version = '1.6.0.0.0',
  license='MIT',
  description = 'Copy of bfabio.pykwalify',
  install_requires=[
          'docopt',
          'python-dateutil',
          'ruamel.yaml',
          'pyyaml',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  ],
  python_requires='>=3.4',
)
