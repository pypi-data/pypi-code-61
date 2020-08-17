"""
"""

try:
    from setuptools import setup, Extension, find_packages
    from setuptools.command.install import install
    from setuptools import Command
except ImportError:
    from distutils.core import setup, Extension
    from distutils.command.install import install
    from distutils import Command

from distutils.command.build import build
from subprocess import call    
import os

# read the contents of your README file
with open("README.md", "r") as fh:
    long_description = fh.read()

class ThreatstackBuild(build):
    """Custom build command"""
    def run(self):
        cmd = [
            'make',
            'V=' + str(self.verbose),
        ]

        call(cmd)

        # run original build code
        build.run(self)      
        
class ThreatstackInstall(install):
    """Custom install command"""
    def run(self):
        print("running custom install command")
        cmd = [
            'make',
            'V=' + str(self.verbose),
        ]

        call(cmd)
        print("end custom install command")

        # run original install code
        install.run(self)   
        print("end original install")

        # install.do_egg_install(self)

class ThreatstackClean(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info _libinjection.so')    

MODULE = Extension(
    '_libinjection', [
        'libinjection/libinjection_wrap.c',
        'libinjection/libinjection_sqli.c',
        'libinjection/libinjection_html5.c',
        'libinjection/libinjection_xss.c'
    ],
    swig_opts=['-Wextra', '-builtin', '-py3'],
    define_macros=[],
    include_dirs=[],
    libraries=[],
    library_dirs=[],
    )

setup (
    name='threatstack-agent-python',
    version='0.1.1',
    description='Application Security Monitoring by Threat Stack',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Threat Stack Inc.',
    author_email='support@threatstack.com',
    url='https://www.threatstack.com',
    license='PROPRIETARY',
    ext_modules=[MODULE],
    packages=find_packages(),
    entry_points={
        'console_scripts': ['threatstackctl=threatstack.control:main'],
    },    
    cmdclass={
        'build': ThreatstackBuild,
        'install': ThreatstackInstall,
        'clean': ThreatstackClean
    },
    install_requires=[
        'colorlog==4.2.1',
        'requests==2.23.0',
        'simplejson==3.17.0',
        'six==1.15.0',
        'wrapt==1.12.1',
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ]    
)
