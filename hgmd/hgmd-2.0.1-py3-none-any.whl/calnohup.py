import os
import sys
import time

import autocalculation as ac

pwd = os.getcwd()

struc = ac.load_structure(path)

ac.CheckCal(pwd, path=path, method1=method, cs=mode, struc=struc, ds=ds, orbit=orbit, running=running[0])