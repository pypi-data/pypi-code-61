#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/11/20
# Desc: 

from zxutils.pyimg import download_img, img_to_base64


def test_download_img():
    test_img_url = "https://file.cibfintech.com/file/M00/00/5C/CiADdV0S6BiAGT-bAAKutEZzfC8967.jpg"
    filename, status = download_img(test_img_url)
    assert status == "success"


def test_img_to_base64():
    test_img_filename = "CiADdV0S6BiAGT-bAAKutEZzfC8967.jpg"
    img_to_base64(test_img_filename)
