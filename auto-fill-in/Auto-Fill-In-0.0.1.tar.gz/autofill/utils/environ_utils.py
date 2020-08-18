#coding: utf-8
import os
import re
import json
from pathlib import Path

from ._path import AUTOFILL_ENV_DIR
from .coloring_utils  import toBLUE, toGREEN, toRED
from .generic_utils import now_str

def where_is_envfile():
    return AUTOFILL_ENV_DIR

def load_and_update_envfile(path, update=True, indent=2):
    with open(path, mode="r", encoding="utf8") as fr:
        data = json.load(fr)
    if update:
        save_envfile(path=path, data=data, indent=indent, update=update)
    return data

def load_envfile(path, update=True, ret_path=False):
    msg = ""
    if not path.endswith(".json"):
        msg += f"\t* Since the argument '{toBLUE('path')}' does not seem to be json, added the extension '{toGREEN('.json')}'\n"
        path = path + ".json"
    if not os.path.exists(path):
        msg += f"\t* No such file or directory: '{toBLUE(path)}'\n"
        path = os.path.join(AUTOFILL_ENV_DIR, path)
    try:
        data = load_and_update_envfile(path, update=update)
    except Exception as e:
        msg += f"\t* No such file or directory: '{toBLUE(path)}'"
        print(f"{toRED(e)}\n{msg}")
        data = {}

    if ret_path:
        return (path, data)
    else:
        return data

def save_envfile(path, data, indent=2, update=True):
    if update:
        data["last_date"] = now_str()
    with open(path, mode="w", encoding="utf8") as fw:
        json.dump(obj=data, fp=fw, ensure_ascii=False, indent=indent)

def show_envfiles():
    p = Path(AUTOFILL_ENV_DIR)
    for path in p.glob("*.json"):
        with path.open(mode="r") as f:
            data = json.load(f)
        name = data.pop("name", "")
        URL = data.pop("URL", "")
        last_date = data.pop("last_date", "")
        print(f"""* PATH: {toBLUE(path)}
        - name      : {toGREEN(name)}
        - URL       : {URL}
        - last_date : {last_date}
        - other keys: {list(data.keys())}
        """)
