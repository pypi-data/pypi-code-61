from setuptools import setup

long_description = open('README.md').read()


#DEPENDENCIES = ['numpy==1.16.2', 'pandas==0.24.2', 'matplotlib==3.0.3', 'networkx==2.2', 'scipy==1.2.1',
#                'seaborn==0.9.0', 'powerlaw==1.4.6']
DEPENDENCIES = ['numpy', 'pandas', 'matplotlib', 'networkx', 'scipy',
                'seaborn', 'powerlaw']

packages = ["face2face",
            "face2face.imports",
            "face2face.statistics",
            "face2face.visualization",
	    "face2face.compatibility_check"
            ]

setup(name="face2face",
      version="0.1 Alpha",
      packages=packages,
      description="Library with basic social science functions",
      url="https://github.com/gesiscss/face2face",
      license="",
      #python_requires=">=3.6.1",
      long_description=long_description,
      install_requires=DEPENDENCIES,
      package_data = {"face2face": ["data/Synthetic_Data/*.dat"]}
      )