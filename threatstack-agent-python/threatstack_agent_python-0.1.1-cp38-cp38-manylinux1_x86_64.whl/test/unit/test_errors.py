import pytest
from threatstack import errors

def test_threatstackerror():
    e = errors.ThreatstackError()
    assert type(e) is errors.ThreatstackError

def test_requestblockederror():
    e = errors.RequestBlockedError()
    assert type(e) is errors.RequestBlockedError

def test_threatstackstackerror():
    e = errors.ThreatstackStackError()
    assert type(e) is errors.ThreatstackStackError