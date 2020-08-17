import pytest
from wrapt import FunctionWrapper
from threatstack.util import common, wrapper, platform_info, injection

import six
if six.PY2:
    _builtins_module = '__builtin__'
elif six.PY3:
    _builtins_module = 'builtins'

class C:
    def method(self):
        pass

def test_module_name():
    m = common._module_name(C.method)
    assert type(m) == str
    assert m == 'test.unit.test_util'

def test_module_name_given_none():
    m = common._module_name(None)
    assert type(m) == str
    assert m == _builtins_module

def test_object_context():
    c = common.object_context(C)
    assert type(c) == tuple

def test_object_context_p3():
    c = common._object_context_py3(C)
    assert type(c) == tuple

def test_object_context_with_method():
    c = common.object_context(str)
    assert type(c) == tuple

def test_callable_name():
    n = common.callable_name(C)
    assert type(n) == str

def test_get_pid_cmdline():
    assert type(common.get_pid_cmdline(123)) == str

def test_get_process_cmdline():
    assert type(common.get_process_cmdline()) == str

def test_get_parent_cmdline():
    assert type(common.get_parent_cmdline()) == str

def test_is_py3_method():
    m = common._is_py3_method(C.method)
    assert m == False

def test_post_function():
    w = wrapper.post_function(C.method)
    assert type(w) == FunctionWrapper

def test_post_function_with_none():
    w = wrapper.post_function(None)
    assert type(w) == FunctionWrapper

def test_PostFunctionWrapper():
    w = wrapper.post_function(C.method)
    wr = wrapper.PostFunctionWrapper(w, C.method)
    assert type(wr) == FunctionWrapper

def test_pre_function():
    w = wrapper.pre_function(C.method)
    assert type(w) == FunctionWrapper

def test_PreFunctionWrapper():
    w = wrapper.pre_function(C.method)
    wr = wrapper.PreFunctionWrapper(w, C.method)
    assert type(wr) == FunctionWrapper

def test_check_sqli():
    assert injection.check_sqli('safe') == 0

def test_check_sqli_with_injection():
    assert injection.check_sqli('name=123%29%3BDROP%20TABLE%20users') == 1

def test_check_xss():
    assert injection.check_xss('safe') == 0

def test_check_css_with_injection():
    assert injection.check_xss('name=<script>alert(-1)</script>') == 1