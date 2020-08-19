import setuptools

setuptools.setup(
     name='genevpkg',  
     version='1.0',
     author="Pavan Kumar",
     author_email="pawan.veeramraju@gmail.com",
     description="Package for performing validation tasks for data of genevare",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     install_requires=[
          'pandas','numpy','openpyxl','argparse','xlsxwriter'
      ]
 )