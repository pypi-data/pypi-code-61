# coding: utf-8
import sys
import argparse

from . import forms
from .utils.generic_utils import MonoParamProcessor
from .utils.environ_utils import load_envfile, show_envfiles
from .utils.form_utils import whichForms

def form_auto_fill_in(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser(prog="form-auto-fill-in", add_help=True)
    parser.add_argument("path", type=str, help="Path to environment file.")
    parser.add_argument("--remain-unchanged", action="store_true", help="Whether you want to update and memorize your answer. (default=True)")
    parser.add_argument("-Y", "--yes",        action="store_true", help="Automatic yes to prompts.")
    parser.add_argument("--quiet",            action="store_true", help="Whether you want to be quiet or not. (default=False)")
    parser.add_argument("--browser",          action="store_true", help="Whether you want to run Chrome with GUI browser. (default=True)")
    parser.add_argument("-P", "--params", default={}, action=MonoParamProcessor, help="Specify the kwargs. You can specify by -P username=USERNAME -P password=PASSWORD")
    args = parser.parse_args(argv)

    path = args.path
    browser = args.browser
    update = not args.remain_unchanged
    need_check = not args.yes
    verbose = not args.quiet
    params = args.params

    env_data = load_envfile(path, ret_path=False)
    model = forms.get(identifier=whichForms(url=env_data["URL"]), path=path, verbose=verbose)
    model.run(browser=browser, update=update, need_check=need_check, **params)

def show_auto_fill_in_envs():
    show_envfiles()