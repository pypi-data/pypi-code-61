#   Copyright 2019 <Huawei Technologies Co., Ltd>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ==============================================================================
#
#   Part of the code below (as indicated by the comments) is taken from
#   PyTorch
#
#   All rights reserved.
#
#   Redistribution and use in source and binary forms, with or without
#   modification, are permitted provided that the following conditions are
#   met:
#
#   1. Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#
#   2. Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#
#   3. Neither the names of Facebook, Deepmind Technologies, NYU, NEC
#      Laboratories America and IDIAP Research Institute nor the names of its
#      contributors may be used to endorse or promote products derived from
#      this software without specific prior written permission.
#
#   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
#   IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
#   THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#   PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
#   CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#   EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#   PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#   PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#   LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#   NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#   SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import ctypes
import glob
import os
import sys

from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

# ==============================================================================
# Taken from PyTorch torch/__init__.py
if sys.platform == 'win32':
    py_dll_path = os.path.join(sys.exec_prefix, 'Library', 'bin')
    hiqsim_dll_path = os.path.join(os.path.dirname(__file__))

    # When users create a virtualenv that inherits the base environment, we
    # will need to add the corresponding library directory into DLL search
    # directories. Otherwise, it will rely on `PATH` which is dependent on
    # user settings.
    if sys.exec_prefix != sys.base_exec_prefix:
        base_py_dll_path = os.path.join(sys.base_exec_prefix, 'Library', 'bin')
    else:
        base_py_dll_path = ''

    dll_paths = list(
        filter(os.path.exists,
               [hiqsim_dll_path, py_dll_path, base_py_dll_path]))

    kernel32 = ctypes.WinDLL('kernel32.dll', use_last_error=True)
    with_load_library_flags = hasattr(kernel32, 'AddDllDirectory')
    prev_error_mode = kernel32.SetErrorMode(0x0001)

    kernel32.LoadLibraryW.restype = ctypes.c_void_p
    if with_load_library_flags:
        kernel32.AddDllDirectory.restype = ctypes.c_void_p
        kernel32.LoadLibraryExW.restype = ctypes.c_void_p

    for dll_path in dll_paths:
        if sys.version_info >= (3, 8):
            os.add_dll_directory(dll_path)
        elif with_load_library_flags:
            res = kernel32.AddDllDirectory(dll_path)
            if res is None:
                err = ctypes.WinError(ctypes.get_last_error())
                err.strerror += (' Error adding "{}" to the DLL '
                                 'directories.').format(dll_path)
                raise err

    try:
        ctypes.CDLL('vcruntime140.dll')
        ctypes.CDLL('msvcp140.dll')
    except OSError:
        print('Microsoft Visual C++ Redistributable is not installed, this '
              'may lead to the DLL load failure.\nIt can be downloaded at '
              'https://aka.ms/vs/16/release/vc_redist.x64.exe')

    dlls = glob.glob(os.path.join(hiqsim_dll_path, '*.pyd'))
    path_patched = False
    for dll in dlls:
        is_loaded = False
        if with_load_library_flags:
            res = kernel32.LoadLibraryExW(dll, None, 0x00001100)
            last_error = ctypes.get_last_error()
            if res is None and last_error != 126:
                err = ctypes.WinError(last_error)
                err.strerror += (' Error loading "{}" or one of its '
                                 'dependencies.').format(dll)
                raise err
            if res is not None:
                is_loaded = True
        if not is_loaded:
            if not path_patched:
                os.environ['PATH'] = ';'.join(dll_paths + [os.environ['PATH']])
                path_patched = True
            res = kernel32.LoadLibraryW(dll)
            if res is None:
                err = ctypes.WinError(ctypes.get_last_error())
                err.strerror += (' Error loading "{}" or one of its '
                                 'dependencies.').format(dll)
                raise err

    kernel32.SetErrorMode(prev_error_mode)
# ==============================================================================

from ._simulator_mpi import SimulatorMPI
from ._stabilizer_simulator import StabilizerSimulator
