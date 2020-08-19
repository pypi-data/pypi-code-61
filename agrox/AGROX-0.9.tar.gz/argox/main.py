from argo import Argo
from cprint import *

agro = Argo("http://localhost:9000")

data = agro.scanport()
cprint.info(data)