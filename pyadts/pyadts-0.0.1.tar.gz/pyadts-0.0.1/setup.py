import os
import atexit
import glob
import shutil
import platform
import subprocess
import warnings

import matplotlib
from setuptools import setup
from setuptools.command.install import install


# Get description from README
root = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(root, 'README.md'), 'r', encoding='utf-8') as f:
    long_description = f.read()


# def __pytorch_cpu():
#     return 'torch>=1.2.0+cpu'
#
# def __pytorch_gpu(cuda_version):
#     if cuda_version == '10.2':
#         return 'torch>=1.2.0'
#     elif cuda_version == '10.1':
#         return 'torch>=1.2.0+cu101'
#     elif cuda_version == '9.2':
#         return 'torch>=1.2.0+cu92'
#     else:
#         raise ValueError('')

# def __check_pytorch():
#     system = platform.system()
#     cuda_file = '/usr/local/cuda/version.txt'
#     if system == 'Linux':
#         if os.path.exists(cuda_file):
#             res = str(subprocess.check_output(['cat', f'{cuda_file}'])).split(' ')[-1]
#             if res.startswith('10.2'):
#                 return __pytorch_gpu('10.2')
#             elif res.startswith('10.1'):
#                 return __pytorch_gpu('10.1')
#             elif res.startswith('9.2'):
#                 return __pytorch_gpu('9.2')
#             else:
#                 warnings.warn()
#                 return __pytorch_cpu()
#         else:
#             warnings.warn()
#             return __pytorch_cpu()
#     else:
#         warnings.warn()
#         return __pytorch_cpu()


def __parse_requirements(file_name):
    with open(file_name, 'r') as f:
        line_striped = (line.strip() for line in f.readlines())
    requirements = [line for line in line_striped if line and not line.startswith('#')]
    # requirements.append(__check_pytorch())
    return requirements


# def install_styles():
#     # Find all style files
#     stylefiles = glob.glob('style/*.mplstyle', recursive=True)
#
#     # Find stylelib directory (where the *.mplstyle files go)
#     mpl_stylelib_dir = os.path.join(matplotlib.get_configdir(), "stylelib")
#     if not os.path.exists(mpl_stylelib_dir):
#         os.makedirs(mpl_stylelib_dir)
#
#     # Copy files over
#     print("Installing styles into", mpl_stylelib_dir)
#     for stylefile in stylefiles:
#         print(os.path.basename(stylefile))
#         shutil.copy(
#             stylefile,
#             os.path.join(mpl_stylelib_dir, os.path.basename(stylefile)))


# class __PostInstallMoveFile(install):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         atexit.register(install_styles)


setup(
    name='pyadts',
    author='Xiao Qinfeng',
    description='A python package for time series anomaly detection',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.0.1',
    packages=[],
    scripts=[],
    install_requirements=__parse_requirements('requirements.txt'),
    # cmdclass={'install': __PostInstallMoveFile},
    url='https://github.com/larryshaw0079/PyADT',
    python_requires=">=3.5",
    license='GPL-3.0 License'
)
