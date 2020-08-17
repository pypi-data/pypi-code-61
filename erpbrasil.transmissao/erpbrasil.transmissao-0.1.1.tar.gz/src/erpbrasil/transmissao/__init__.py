__version__ = '0.1.1'

import logging

from erpbrasil.transmissao.transmissao import TransmissaoSOAP  # noqa: F401

logging.getLogger('erpbrasil.transmissao').addHandler(logging.NullHandler())
