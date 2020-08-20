import os
import setuptools
from _setup import CMakeBuild, Clean, get_cmake_command

# This reads the __version__ variable from _version.py
exec(open('_version.py').read())

# Readme file as long_description:
long_description = open('README.rst').read()

# Readthedocs env value
on_rtd = os.environ.get('READTHEDOCS') == 'True'


def get_install_requires():
    if on_rtd:
        requirements_file = 'docs/requirements_rtd.txt'
    else:
        requirements_file = 'requirements.txt'

    # Read in requirements.txt
    with open(requirements_file, 'r') as f_requirements:
        requirements = f_requirements.readlines()
    requirements = [r.strip() for r in requirements]

    # Add CMake as dependency if we cannot find the command
    if get_cmake_command() is None:
        requirements.append('cmake')

    return requirements


class CMakeExtension(setuptools.Extension):
    def __init__(self, pymod, target=None):
        """
        Constructor

        Args:
            src_dir (string): Path to source directory
            target (string): Name of target
            pymod (string): Name of compiled Python module
        """
        # NB: the main source directory is the one containing the setup.py file
        self.src_dir = os.path.abspath('')
        self.pymod = pymod
        self.target = target if target is not None else pymod.split('.')[-1]

        self.lib_filepath = os.path.join(*pymod.split('.'))
        setuptools.Extension.__init__(self, pymod, sources=[])


ext_modules = [
    CMakeExtension(pymod='projectq.backends._hiqsim._cppsim_mpi'),
    CMakeExtension(pymod='projectq.backends._hiqsim._cppstabsim'),
    CMakeExtension(pymod='projectq.cengines._sched_cpp'),
]

if on_rtd:
    setuptools.setup(
        name='hiq-circuit',
        version=__version__,
        author='hiq',
        author_email='hiqinfo@huawei.com',
        description='A high performance distributed quantum simulator',
        long_description=long_description,
        url="https://github.com/Huawei-HiQ/HiQsimulator",
        install_requires=get_install_requires(),
        zip_safe=False,
        license='Apache 2',
        package_dir={'': 'python'},
        packages=[
            'hiq/noise', 'hiq/libs', 'hiq/mitigation',
            'projectq/backends', 'projectq/backends/_hiqsim',
            'projectq/cengines', 'projectq/ops'
        ])
else:
    setuptools.setup(
        name='hiq-circuit',
        version=__version__,
        author='hiq',
        author_email='hiqinfo@huawei.com',
        description='A high performance distributed quantum simulator',
        long_description=long_description,
        url="https://github.com/Huawei-HiQ/HiQsimulator",
        install_requires=get_install_requires(),
        cmdclass=dict(build_ext=CMakeBuild,
                      clean=Clean),
        zip_safe=False,
        license='Apache 2',
        package_dir={'': 'python'},
        packages=setuptools.find_packages(where='python'),
        ext_modules=ext_modules)
