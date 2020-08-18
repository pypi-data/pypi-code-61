#coding: utf-8
import os
import json

from .coloring_utils  import toBLUE
from .generic_utils import now_str

__all__ = [
    "UTILS_DIR", "MODULE_DIR", "REPO_DIR", "AUTOFILL_ENV_DIR",
]

UTILS_DIR         = os.path.dirname(os.path.abspath(__file__))  # path/to/atuofill/utils
MODULE_DIR        = os.path.dirname(UTILS_DIR)                  # path/to/atuofill
REPO_DIR          = os.path.dirname(MODULE_DIR)                 # path/to/Auto-Fill-In
AUTOFILL_ENV_DIR  = os.path.join(os.path.expanduser('~'), '.autofill') # /Users/<username>/.autofill
# Check whether uid/gid has the write access to DATADIR_BASE
if os.path.exists(AUTOFILL_ENV_DIR) and not os.access(AUTOFILL_ENV_DIR, os.W_OK):
    AUTOFILL_ENV_DIR = os.path.join('/tmp', '.autofill')
if not os.path.exists(AUTOFILL_ENV_DIR):
    os.mkdir(AUTOFILL_ENV_DIR)
    print(f"{toBLUE(AUTOFILL_ENV_DIR)} is created. Environment variables (.json) should be stored here.")
SAMPLE_JOSN_PATH = os.path.join(AUTOFILL_ENV_DIR, "_sample.json")
if not os.path.exists(SAMPLE_JOSN_PATH):
    with open(file=SAMPLE_JOSN_PATH, mode="w", encoding="utf8") as fp:
        json.dump(obj={
            "name": "SAMPLE FORMS",
            "URL": "https://forms.office.com/Pages/ResponsePage.aspx?id=XXX",
            "form": "office",
            "last_date" : now_str(),
            "login": {},
            "answer": {},
        }, fp=fp, ensure_ascii=False, indent=2)
    print(f"Saved sample environment file at {toBLUE(SAMPLE_JOSN_PATH)}")