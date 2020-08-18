#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/11/20
# Desc: 

import os
from urllib.parse import urlparse

from zxutils.pyencrypt import base64_to_bytes, bytes_to_base64
from zxutils.pyurl import get_page


def img_to_base64(filename):
    """
    Convert binary files to base64 format
    :return:
    """
    with open(filename, "rb") as f:
        return bytes_to_base64(f.read())


def base64_to_img(b64_data, filename):
    """

    :param b64_data:
    :param filename
    :return:
    """
    bytes_data = base64_to_bytes(b64_data)
    with open(filename, "wb") as f:
        f.write(bytes_data)


def download_img(img_url, filename=""):
    """
    Download web pictures
    :param img_url:
    :param filename: Specify the file name, if not specified, the file name on the url will be obtained
    :return:
    """
    if not filename:
        up = urlparse(img_url)
        filename = os.path.basename(up.path)

    resp = get_page(img_url)

    with open(filename, "wb") as f:
        f.write(resp)

    return filename, "success"
