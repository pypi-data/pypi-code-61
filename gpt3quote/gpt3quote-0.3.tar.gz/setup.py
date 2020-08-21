from distutils.core import setup
setup(
  name = 'gpt3quote',
  packages = ['gpt3quote'],
  version = '0.3',
  license='MIT',
  description = 'GPT-3 generated quote library for python',
  author = 'Ethan Goodhart',
  author_email = 'edg.programmer@gmail.com',
  url = 'https://github.com/ethandgoodhart/GPT3-Quote',
  download_url = 'https://github.com/ethandgoodhart/GPT3-Quote/archive/v_03.tar.gz',
  keywords = ['generation', 'quote', 'gpt3', 'random'],
  install_requires=[
          'requests',
          'bs4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)