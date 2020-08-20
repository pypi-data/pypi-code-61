#!/usr/bin/env python
# encoding: utf-8


import pytest
import os
from pathlib import Path
from shutil import copyfile
from bopytex.bopytex import produce_and_compile, subject_metadatas

SNIPPETS_PATH = Path("snippets/")
TEST_PATH = Path("test")
TEST_TEMPLATE_PATH = TEST_PATH / "templates/"


@pytest.fixture
def prepare_test_template(tmp_path):
    """ Create a tmp directory, copy snippets inside

    return tmp directory name
    """
    tmp = tmp_path
    snippets = TEST_TEMPLATE_PATH.glob("tpl_*.tex")
    for s in snippets:
        copyfile(s, tmp / s.name)
    csvs = TEST_PATH.glob("*.csv")
    for s in csvs:
        copyfile(s, tmp / s.name)

    prev_dir = Path.cwd()
    os.chdir(tmp)
    yield tmp
    os.chdir(prev_dir)


@pytest.fixture
def prepare_snippets(tmp_path):
    """ Create a tmp directory, copy snippets inside

    return tmp directory name
    """
    tmp = tmp_path
    snippets = SNIPPETS_PATH.glob("tpl_*.tex")
    for s in snippets:
        copyfile(s, tmp / s.name)

    prev_dir = Path.cwd()
    os.chdir(tmp)
    yield tmp
    os.chdir(prev_dir)


def test_produce_and_compile_base(prepare_test_template):
    test_tpl = list(Path(".").glob("tpl_*.tex"))
    assert [tpl.name for tpl in test_tpl] == ["tpl_test.tex"]
    for tpl in test_tpl:
        produce_and_compile(
            {
                "template": tpl,
                "working_dir": None,
                "only_corr": False,
                "students_csv": None,
                "number_subjects": 1,
                "dirty": False,
                "no_compile": False,
                "no_join": False,
                "corr": False,
                "crazy": False,
            }
        )


def test_produce_and_compile_csv(prepare_test_template):
    test_tpl = Path(".").glob("tpl_*.tex")
    for tpl in test_tpl:
        options = {
            "template": tpl,
            "working_dir": None,
            "only_corr": False,
            "students_csv": "students.csv",
            "number_subjects": 1,
            "dirty": False,
            "no_compile": False,
            "no_join": False,
            "corr": False,
            "crazy": False,
        }
        # produce_and_compile(options)


def test_metadatas(prepare_test_template):
    test_tpl = Path(".").glob("tpl_*.tex")
    for tpl in test_tpl:
        options = {
            "template": tpl,
            "working_dir": None,
            "only_corr": False,
            "students_csv": "students.csv",
            "number_subjects": 1,
            "dirty": False,
            "no_compile": False,
            "no_join": False,
            "corr": False,
            "crazy": False,
        }
        metadatas = subject_metadatas(options)
        meta = [
            {
                "num": "01",
                "nom": "Bob",
                "classe": "1ST",
                "elo": "1000",
                "texfile": "01_test.tex",
                "template": "tpl_test.tex",
                "directory": ".",
            },
            {
                "num": "02",
                "nom": "Pipo",
                "classe": "1ST",
                "elo": "1300",
                "texfile": "02_test.tex",
                "template": "tpl_test.tex",
                "directory": ".",
            },
            {
                "num": "03",
                "nom": "Popi",
                "classe": "1ST",
                "elo": "100",
                "texfile": "03_test.tex",
                "template": "tpl_test.tex",
                "directory": ".",
            },
            {
                "num": "04",
                "nom": "Boule",
                "classe": "1ST",
                "elo": "4000",
                "texfile": "04_test.tex",
                "template": "tpl_test.tex",
                "directory": ".",
            },
            {
                "num": "05",
                "nom": "Bill",
                "classe": "1ST",
                "elo": "1300",
                "texfile": "05_test.tex",
                "template": "tpl_test.tex",
                "directory": ".",
            },
        ]
        assert metadatas == meta


def test_pdfjoin_current_directory(prepare_test_template):
    wdir = prepare_test_template
    pass


def test_pdfjoin_deep_directory():
    pass


def test_pdfjoin_dont_remove():
    pass


def test_subject_names():
    pass


def test_feed_texfiles():
    pass


def test_tex2pdf_current_directory():
    pass


def test_tex2pdf_deep_directory():
    pass


def test_activate_solution():
    pass


# def test_snippets(prepare_snippets):
#    snippets = list(Path(".").glob("tpl_*.tex"))
#    for tpl in snippets:
#        produce_and_compile(
#            {
#                "template": tpl,
#                "working_dir": None,
#                "only_corr": False,
#                "students_csv": None,
#                "number_subjects": 1,
#                "dirty": False,
#                "no_compile": False,
#                "no_join": False,
#                "corr": False,
#                "crazy": False,
#            }
#        )


# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del
