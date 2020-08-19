import os
import sys
import tempfile
import platform
import inspect
import ctypes
from pathlib import Path
xtrace_dll_init = False
xtrace_func_ok = False
dll = None

def __check_dll():
    xtrace_dll_folder=""
    xtrace_dll_filepath = ""
    env_dist = os.environ

    if "TMPDIR" in env_dist:
        xtrace_dll_folder=env_dist.get('TMPDIR')
    if "TEMP" in env_dist:
        xtrace_dll_folder=env_dist.get('TEMP')
    if "TMP" in env_dist:
        xtrace_dll_folder=env_dist.get('TMP')

    if len(env_dist.get('TMP')) == 0:
        xtrace_dll_folder=tempfile.gettempdir()
    if platform.architecture()[0] == '64bit':
        xtrace_dll_filepath=xtrace_dll_folder + "\\XTraceDLL64.dll"
    else:
        xtrace_dll_filepath=xtrace_dll_folder + "\\XTraceDLL32.dll"

    if not Path(xtrace_dll_filepath).is_file():
        return

    global dll
    dll = ctypes.cdll.LoadLibrary(xtrace_dll_filepath)

    global xtrace_func_ok
    xtrace_func_ok = True

    #version
    name = ctypes.create_string_buffer(128)
    dll.MagicTraceVersionAnsi(name, 128)
    print("xtrace dll load success, version: ", name.value)

if False == xtrace_dll_init:
    xtrace_dll_init = True
    __check_dll()

def trace(str):
    if xtrace_func_ok:
        xtrace_func_ptr = dll.MagicTraceProc
        dll.MagicTraceProc(ctypes.c_int(11), ctypes.c_int64(0x000000), str, ctypes.c_int64(0), ctypes.c_int64(0))
    return

def ctrace(c, str):
    if xtrace_func_ok:
        xtrace_func_ptr = dll.MagicTraceProc
        dll.MagicTraceProc(ctypes.c_int(11), ctypes.c_int64(c), str, ctypes.c_int64(0), ctypes.c_int64(0))
    return

def count_reset(a,b):
    if xtrace_func_ok:
        xtrace_func_ptr = dll.MagicTraceProc
        dll.MagicTraceProc(ctypes.c_int(21), ctypes.c_int64(a), ctypes.c_int64(b), ctypes.c_int64(0), ctypes.c_int64(0))
    return

def count_inc(a,b):
    if xtrace_func_ok:
        xtrace_func_ptr = dll.MagicTraceProc
        dll.MagicTraceProc(ctypes.c_int(22), ctypes.c_int64(a), ctypes.c_int64(b), ctypes.c_int64(0), ctypes.c_int64(0))
    return

def count_dec(a,b):
    if xtrace_func_ok:
        xtrace_func_ptr = dll.MagicTraceProc
        dll.MagicTraceProc(ctypes.c_int(24), ctypes.c_int64(a), ctypes.c_int64(b), ctypes.c_int64(0), ctypes.c_int64(0))
    return
