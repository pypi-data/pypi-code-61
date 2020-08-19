import pytest
import tempfile
from mesonbuild import mesonmain
from lyncs_cppyy import Lib, cppdef, gbl


def build_meson(sourcedir):
    builddir = tempfile.mkdtemp()
    assert (
        mesonmain.run(
            [
                "setup",
                "--prefix",
                builddir,
                "--libdir",
                builddir + "/lib",
                builddir,
                sourcedir,
            ],
            "meson",
        )
        == 0
    )
    assert mesonmain.run(["compile", "-C", builddir], "meson") == 0
    assert mesonmain.run(["install", "-C", builddir], "meson") == 0
    return builddir


def test_cnumbers():
    path = build_meson("test/cnumbers")
    cnumbers = Lib(
        header="numbers.h",
        library="libnumbers.so",
        c_include=True,
        check=["zero", "one"],
        path=path,
    )
    assert cnumbers.zero() == 0
    assert cnumbers.one() == 1
    assert cnumbers.ZERO == 0
    assert cnumbers.ONE == 1

    # Cppyy cannot access macros.
    with pytest.raises(AttributeError):
        gbl.ZERO

    with pytest.raises(AttributeError):
        cnumbers.TWO
