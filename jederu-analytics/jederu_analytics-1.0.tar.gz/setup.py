from distutils.core import setup
setup(
  name = 'jederu_analytics',         # How you named your package folder (MyLib)
  packages = ['jederu_analytics'],   # Chose the same as "name"
  version = '1.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Python3 library voor Jederu Analytics',   # Give a short description about your library
  author = 'Jens de Ruiter',                   # Type in your name
  author_email = 'jensgamesnl@gmail.com',      # Type in your E-Mail
  url = 'https://jensderuiter.dev',   # Provide either the link to your github or to your website
  install_requires=[            # I get to this in a second
          'requests',
          'beautifulsoup4',
      ],
  classifiers=[
    'Programming Language :: Python :: 3',
  ],
)
