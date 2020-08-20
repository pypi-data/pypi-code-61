import sys
sys.path.append("../gdsm/bin")
import gdsm
import pydicom
pydicom.config.image_handlers = ['gdcm_handler']
