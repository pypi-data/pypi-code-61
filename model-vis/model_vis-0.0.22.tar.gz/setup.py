"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

import pathlib

# Always prefer setuptools over distutils
from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')
# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(name='model_vis',
      version='0.0.22',
      python_requires='>3.0.0',
      description=
      'An easy and interactive graph visualization tool for ML models!!!',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author_email='amipro@gmail.com',
      install_requires=[
          'onnx==1.6', 'tensorflow==1.14', 'isort', 'flask', 'networkx',
          'flake8', 'flake8-quotes', 'deprecated', 'sklearn', 'yapf', 'Flask',
          'protobuf', 'absl-py', 'gast', 'astor', 'termcolor',
          'keras_applications', 'keras_preprocessing', 'plotly', 'onnxruntime',
          'Pillow'
      ],
      keywords='ML, visualization, visualize, model, graph',
      packages=find_packages(),
      include_package_data=True,
      entry_points={
          'console_scripts': [
              'plot=graph_visualization.plot_graph:main',
          ],
      })
