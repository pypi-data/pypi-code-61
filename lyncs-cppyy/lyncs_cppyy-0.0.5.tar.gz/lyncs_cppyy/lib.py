"""
A Lib class for managing shared libraries
"""
# pylint: disable=C0303,C0330

import os
import cppyy

__all__ = ["Lib"]


class Lib:
    """
    Lib can be used for managing shared libraries.
    
    Lib returns a variable that represents the library.
    The library is loaded at the first usage of the variable.
    In most of the cases, accessing attributes of the variable 
    is like accessing attributed of `cppyy.gbl`.
    Exceptions are made for the attributes in __slots__
    or for macros defined in the loaded header.
    This latter feature is not supported by cppyy.gbl.
    
    Example
    -------
    
    >>> from lyncs_cppyy import Lib
    >>> zlib = Lib(header='zlib.h', library='libz', check='zlibVersion') 
    >>> zlib.zlibVersion()
     '1.2.11'
    
    The above is the equivalent of the following with cppyy

    >>> import cppyy
    >>> cppyy.include('zlib.h')        # bring in C++ definitions
    >>> cppyy.load_library('libz')     # load linker symbols
    >>> cppyy.gbl.zlibVersion()        # use a zlib API
     '1.2.11'
    """

    __slots__ = [
        "_cwd",
        "path",
        "include",
        "header",
        "library",
        "check",
        "c_include",
        "namespace",
        "redefined",
    ]

    def __init__(
        self,
        header=None,
        library=None,
        check=None,
        include=None,
        path=".",
        c_include=False,
        namespace=None,
        redefined=None,
    ):
        """
        Initializes a library class that can be pickled.

        Parameters
        ----------
        header: str or list
          Header(s) file to include.
        library: str or list
          Library(s) file to include. Also absolute paths are accepted.
        check: str or list
          Check function(s) to look for in the library to test if it has been loaded.
        include: str or list
          Path(s) to be included. Equivalent to `-I` used at compile time. 
        path: str or list
          Path(s) where to look for headers and libraries.
          Headers are searched in path+"/include" and libraries in path+"/lib".
        c_include: bool
          Whether the library is a c library (False means it is a c++ library).
        namespace: str or list
          Namespace used across the library. Directly access object inside namespace.
          Similar to `using namespace ...` in c++.
        redefined: dict
          List of symbols that have been redefined
        """
        assert check, "No checks given."
        assert header, "No header given."
        self._cwd = os.getcwd()
        self.path = [path] if isinstance(path, str) else path
        self.header = [header] if isinstance(header, str) else header
        self.library = [library] if isinstance(library, str) else library or []
        self.check = [check] if isinstance(check, str) else check
        self.include = [include] if isinstance(include, str) else include or []
        self.c_include = c_include
        self.namespace = [namespace] if isinstance(namespace, str) else namespace or []
        self.redefined = redefined or {}

        if self.redefined:
            self.check = [self.redefined.get(check, check) for check in self.check]

    @property
    def lib(self):
        """
        It checks if the library is already loaded, or it loads it.
        """
        if all((hasattr(cppyy.gbl, check) for check in self.check)):
            return cppyy.gbl

        for include in self.include:
            cppyy.add_include_path(include)

        for library in self.library:
            if isinstance(library, Lib):
                library.lib

        self.define()
        for header in self.header:
            for path in self.path:
                if not path.startswith(os.sep):
                    path = self._cwd + "/" + path
                if os.path.isfile(path + "/include/" + header):
                    cppyy.add_include_path(path + "/include")
                    break
            if self.c_include:
                cppyy.c_include(header)
            else:
                cppyy.include(header)
        self.undef()

        for library in self.library:
            if not isinstance(library, str):
                continue
            try:
                cppyy.load_library(library)
                continue
            except RuntimeError:
                pass
            tmp = library
            if not tmp.startswith(os.sep):
                tmp = self._cwd + "/" + tmp
            if not os.path.isfile(tmp):
                for path in self.path:
                    if not path.startswith(os.sep):
                        path = self._cwd + "/" + path
                    tmp = path + "/lib/" + library
                    if os.path.isfile(tmp):
                        break
            if not os.path.isfile(tmp):
                raise ImportError(
                    "Library %s not found in paths %s" % (library, self.path)
                )
            cppyy.load_library(tmp)

        assert all(
            (hasattr(cppyy.gbl, check) for check in self.check)
        ), "Given checks not found."
        return self.lib

    def define(self):
        "Defines the list of values in redefined"
        cpp = ""
        for key, val in self.redefined.items():
            cpp += f"#define {key} {val}\n"
        if cpp:
            cppyy.cppdef(cpp)

    def undef(self):
        "Undefines the list of values in redefined"
        cpp = ""
        for key in self.redefined:
            cpp += f"#undef {key}\n"
        if cpp:
            cppyy.cppdef(cpp)

    def __getattr__(self, key):
        try:
            if self.redefined:
                key = self.redefined.get(key, key)
            if self.namespace:
                for namespace in self.namespace:
                    try:
                        return getattr(getattr(self.lib, namespace), key)
                    except AttributeError:
                        pass
            return getattr(self.lib, key)
        except AttributeError:
            try:
                return self.get_macro(key)
            except BaseException:
                pass
            raise

    def __setattr__(self, key, value):
        try:
            return getattr(type(self), key).__set__(self, value)
        except AttributeError:
            pass

        if self.redefined:
            key = self.redefined.get(key, key)
        if self.namespace:
            for namespace in self.namespace:
                try:
                    getattr(getattr(self.lib, namespace), key)
                    return setattr(getattr(self.lib, namespace), key, value)
                except AttributeError:
                    pass
        setattr(self.lib, key, value)

    def get_macro(self, key):
        "Returns the value of a defined macro by assigning it to a variable"
        try:
            return getattr(self.lib, "_" + key)
        except AttributeError as err:
            try:
                cppyy.cppdef(
                    """
                    auto _%s = %s;
                    """
                    % (key, key)
                )
                return self.get_macro(key)
            except SyntaxError:
                raise err
