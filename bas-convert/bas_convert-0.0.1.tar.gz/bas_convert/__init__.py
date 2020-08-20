import json
import os
from pathlib import Path

EXEC_DIR = Path(os.path.dirname(os.path.realpath(__file__)))

f = EXEC_DIR / "data" / "lookups.json"
lookups = json.loads(f.read_text())
paramlist = lookups["paramlist"]
paramdict = lookups["paramdict"]
