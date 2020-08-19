# -*- coding: utf-8 -*-
"""
Module for reading change detection result files.
"""

import logging
import sys
import re
import os

import numpy

from sarpy.compliance import int_func, string_types
from sarpy.io.general.utils import parse_xml_from_string
from sarpy.io.general.nitf import NITFReader, NITFWriter, ImageDetails, DESDetails, \
    image_segmentation, get_npp_block, interpolate_corner_points_string
from sarpy.io.general.nitf import NITFDetails, MemMap
from sarpy.io.general.nitf_elements.des import DataExtensionHeader, XMLDESSubheader
from sarpy.io.general.nitf_elements.security import NITFSecurityTags
from sarpy.io.general.nitf_elements.image import ImageSegmentHeader, ImageBands, ImageBand
from sarpy.io.product.sidd2_elements.SIDD import SIDDType
from sarpy.io.product.sidd1_elements.SIDD import SIDDType as SIDDType1
from sarpy.io.complex.sicd_elements.SICD import SICDType
from sarpy.io.complex.sicd import MultiSegmentChipper, extract_clas as extract_clas_sicd


__classification__ = "UNCLASSIFIED"
__author__ = "Thomas McCullough"


if __name__ == '__main__':
    root_dir = os.path.expanduser('~/Downloads/AnamolousChangeDetection')
    the_file_stem = os.path.join(
        root_dir, '01MAY19RS021000100_03JUL16RS021000100_20200617T211636_OBS_XACD')
    file_r = the_file_stem + '_R.ntf'
    file_m = the_file_stem + '_M.ntf'
    file_c = the_file_stem + '_C.ntf'

    details_r = NITFDetails(file_r)
    details_m = NITFDetails(file_m)
    details_c = NITFDetails(file_c)
    im_r = details_r.img_headers
    im_m = details_m.img_headers
    im_c = details_c.img_headers
    print(details_r)

    from PIL import Image
    # let's do a direct memmap test...
    image_offset = details_c.img_segment_offsets[0]
    image_size = details_c.nitf_header.ImageSegments.item_sizes[0]
    our_memmap = MemMap(file_c, image_size, image_offset)
    img = Image.open(our_memmap)  # this is a lazy operation
    img2 = img.crop((0, 0, 1000, 1000))  # this may be lazy too

    # img2.load()
    img2.show()
    poo = numpy.asarray(img2)
    print(img2)

    # img.load()
    print(img)
