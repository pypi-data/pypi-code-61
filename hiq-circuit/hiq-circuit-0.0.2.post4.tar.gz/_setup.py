import os
import re
import platform
import subprocess
import sys

from distutils.command.clean import clean
from distutils.version import LooseVersion

from setuptools.command.build_ext import build_ext
from setuptools.command.develop import develop
from setuptools.command.install import install


def get_python_executable():
    try:
        root_path = os.environ['VIRTUAL_ENV']
        python = os.path.basename(sys.executable)
        python_path = os.path.join(root_path, python)
        if os.path.exists(python_path):
            return python_path
        else:
            return os.path.join(root_path, 'bin', python)
    except KeyError:
        return sys.executable


def get_cmake_command():
    with open(os.devnull, 'w') as devnull:
        try:
            subprocess.check_call(['cmake', '--version'],
                                  stdout=devnull,
                                  stderr=devnull)
            return ['cmake']
        except (OSError, subprocess.CalledProcessError):
            pass

        # CMake not in PATH, should have installed Python CMake module
        # -> try to find out where it is
        try:
            root_path = os.environ['VIRTUAL_ENV']
            python = os.path.basename(sys.executable)
        except KeyError:
            root_path, python = os.path.split(sys.executable)

        search_paths = [
            root_path,
            os.path.join(root_path, 'bin'),
            os.path.join(root_path, 'Scripts')
        ]

        # First try executing CMake directly
        for base_path in search_paths:
            try:
                cmake_cmd = os.path.join(base_path, 'cmake')
                subprocess.check_call([cmake_cmd, '--version'],
                                      stdout=devnull,
                                      stderr=devnull)
                return [cmake_cmd]
            except (OSError, subprocess.CalledProcessError):
                pass

        # That did not work: try calling it through Python
        for base_path in search_paths:
            try:
                cmake_cmd = [python, os.path.join(base_path, 'cmake')]
                subprocess.check_call(cmake_cmd + ['--version'],
                                      stdout=devnull,
                                      stderr=devnull)
                return cmake_cmd
            except (OSError, subprocess.CalledProcessError):
                pass

    # Nothing worked -> give up!
    return None


# ==============================================================================


class CMakeBuild(build_ext):
    user_options = develop.user_options + [
        ('no-arch-native', None, 'Do not use the -march=native flag when '
         'compiling'),
        ('inplace', 'i',
         'ignore build-lib and put compiled extensions into the source ' +
         'directory alongside your pure Python modules'),
    ]

    boolean_options = develop.boolean_options + ['no-arch-native', 'inplace']

    def initialize_options(self):
        build_ext.initialize_options(self)
        self.no_arch_native = None
        self.inplace = False

    def build_extensions(self):
        self.cmake_cmd = get_cmake_command()
        assert self.cmake_cmd is not None
        print('using cmake command:', self.cmake_cmd)
        out = subprocess.check_output(self.cmake_cmd + ['--version'])

        if platform.system() == "Windows":
            cmake_version = LooseVersion(
                re.search(r'version\s*([\d.]+)', out.decode()).group(1))
            if cmake_version < '3.1.0':
                raise RuntimeError("CMake >= 3.1.0 is required on Windows")

        self.cmake_configure_build()
        self.parallel = 2
        build_ext.build_extensions(self)

    def cmake_configure_build(self):
        cfg = 'Debug' if self.debug else 'Release'
        cmake_args = [
            '-DPYTHON_EXECUTABLE=' + get_python_executable(),
            '-DBoost_NO_BOOST_CMAKE=ON',
            '-DBUILD_TESTING=OFF',
            '-DIS_PYTHON_BUILD=ON',
            '-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON'
        ]  # yapf: disable

        if self.no_arch_native:
            cmake_args += ['-DUSE_NATIVE_INTRINSICS=OFF']

        src_dir = self.extensions[0].src_dir
        for ext in self.extensions:
            dest_path = os.path.abspath(
                os.path.dirname(self.get_ext_fullpath(ext.lib_filepath)))
            cmake_args.append('-D{}_LIBRARY_OUTPUT_DIRECTORY={}'.format(
                ext.target.upper(), dest_path))

        self.build_args = ['--config', cfg]

        if platform.system() == "Windows":
            if sys.maxsize > 2**32:
                cmake_args += ['-A', 'x64']
            self.build_args += ['--', '/m']
        else:
            cmake_args += ['-DCMAKE_BUILD_TYPE=' + cfg]
            if platform.system() == "Darwin" and 'TRAVIS' in os.environ:
                self.build_args += ['--']
            else:
                self.build_args += ['--', '-j2']

        env = os.environ.copy()
        env['CXXFLAGS'] = '{} -DVERSION_INFO=\\"{}\\"'.format(
            env.get('CXXFLAGS', ''), self.distribution.get_version())

        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)

        print('CMake command:', self.cmake_cmd + [src_dir] + cmake_args)
        subprocess.check_call(self.cmake_cmd + [src_dir] + cmake_args,
                              cwd=self.build_temp,
                              env=env)

    def build_extension(self, ext):
        print(
            'CMake command:', self.cmake_cmd
            + ['--build', '.', '--target', ext.target] + self.build_args)
        subprocess.check_call(self.cmake_cmd
                              + ['--build', '.', '--target', ext.target]
                              + self.build_args,
                              cwd=self.build_temp)


class Clean(clean):
    def run(self):
        # Execute the classic clean command
        clean.run(self)
        import glob
        from distutils.dir_util import remove_tree
        egg_info = glob.glob('python/*.egg-info')
        if egg_info:
            remove_tree(egg_info[0])
