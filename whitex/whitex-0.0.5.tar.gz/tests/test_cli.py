#!/usr/bin/env python

"""Tests for `whitex` package."""

from textwrap import dedent
import os
import pytest

from click.testing import CliRunner

from whitex import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_help_works():
    runner = CliRunner()
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0


def run_and_compare_contents(input_content, expected_content, options=None):
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open('file.tex', 'w') as input_buf:
            input_buf.write(input_content)

        args = ['file.tex']
        if options:
            args.extend(options)
        result = runner.invoke(cli.main, args)
        assert result.exit_code == 0

        with open('file.tex', 'r') as out_buf:
            assert expected_content == out_buf.read()


def test_command_line_interface(tmpdir):
    """Test the CLI."""
    input_content = dedent(
        """\
        Because   of $$a+b=c$$ ({\\it Pythogoras}),
        % @dude, let's go bowling
        and $y=2^ng$ with $n=1,...,10$,
        we have ${\\Gamma \\over 2}=8.$
        """
    )

    expected_content = dedent(
        """\
        Because of
        \\[
        a+b = c
        \\]
        (\\textit{Pythogoras}),
        and $y = 2^n g$ with $n = 1,\\dots,10$,
        we have $\\frac{\\Gamma}{2} = 8$.
        """
    )

    run_and_compare_contents(input_content, expected_content)


def test_keep_comments():
    """Test CLI when keep comments."""
    input_content = dedent(
        """\
        Dude does mind!
        % @dude, let's go bowling
        \\textbf{  this aggression will not stand },
        And this % also.
        """
    )

    expected_content = dedent(
        """\
        Dude does mind!
        % @dude, let's go bowling
        \\textbf{this aggression will not stand},
        And this % also.
        """
    )

    run_and_compare_contents(
        input_content,
        expected_content,
        options=['--keep-comments']
    )


def test_non_tex_file_aborts():
    """Check that click.ClickException is raised for non-tex file."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open('file.dat', 'w') as input_buf:
            input_buf.write('A string')

        result = runner.invoke(cli.main, ['file.dat'])
        assert 'Aborted!' in result.output
        assert result.exit_code == 1  # click.Abort raised


def test_backup_works():
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open('file.tex', 'w') as input_buf:
            input_buf.write('A string')

        result = runner.invoke(cli.main, ['file.tex'])
        assert result.exit_code == 0
        assert os.path.exists('.file_whitex_bkp.tex')
        with open('.file_whitex_bkp.tex', 'r') as bkp:
            assert bkp.read() == 'A string'


def test_no_backup():
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open('file.tex', 'w') as input_buf:
            input_buf.write('A string')

        result = runner.invoke(cli.main, ['file.tex', '--no-backup'])
        assert result.exit_code == 0
        assert not os.path.exists('.file_whitex_bkp.tex')
