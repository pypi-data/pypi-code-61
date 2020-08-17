import pytest
from threatstack.control import execProgram

# Python2
try:
    FileNotFoundError
except NameError:
    FileNotFoundError = OSError

def test_execProgram_with_empty_args():
    with pytest.raises(SystemExit):
        execProgram.execProgram([])

def test_execProgram_with_bad_args():
    with pytest.raises(FileNotFoundError):
        execProgram.execProgram(['ls .'])