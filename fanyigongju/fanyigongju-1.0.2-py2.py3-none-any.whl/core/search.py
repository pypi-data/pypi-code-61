#!/bin/env python
# -*- coding:utf-8 -*-
# _author:ken

import requests
import urllib.parse
import time
import random
import hashlib
import json


class Search(object):
    def __init__(self):
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    def getData(self,search_name):
        # salt =i = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10)
        salt = ((time.time() * 1000) + random.randint(1,10))
        # sign = n.md5("fanyideskweb" + t + i + "ebSeFb%=XZ%T[KZ)c(sy!")
        sign_text = "fanyideskweb" + search_name + str(salt) + "ebSeFb%=XZ%T[KZ)c(sy!"
        sign = hashlib.md5((sign_text.encode('utf-8'))).hexdigest()
        lts = ((time.time() * 1000) + random.randint(1,10))
        paydata = {
            'i': search_name,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': '15977312676319',
            'sign': '2ea78ef767f0d46ba88313218b07a66c',
            'lts':'1597731267631',
            'bv':'b286f0a34340b928819a6f64492585e8',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_CLICKBUTTION',
            'typoResult': 'false'
        }
        return paydata

    def getHeader(self):
        header = {
            'Host': 'fanyi.youdao.com',
            'Referer': 'http://fanyi.youdao.com/',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=407488725@10.108.160.17;OUTFOX_SEARCH_USER_ID_NCOO=945369711.9764354;_ga=GA1.2.25015490.1588042186;P_INFO=axiaomixiaomi;JSESSIONID=aaaK2XH4j_1_6asLanaqx;___rl__test__cookies=1597731267623'
        }
        return header

    def getRequest(self,paydata,header):
        _data = urllib.parse.urlencode(paydata).encode('utf-8')
        _header = header
        response = requests.post(self.url,data=_data,headers=_header)
        return response.text

    def getResult(self,response):
        result_text = json.loads(response)
        print(result_text)
        #src = result_text['translateResult'][0][0]['src']
        tgt = result_text['translateResult'][0][0]['tgt']
        return tgt

    def main(self,search_name):
        app = search()
        paydata = app.getData(search_name)
        header = app.getHeader()
        response = app.getRequest(paydata, header)
        tgt = app.getResult(response)
        return tgt
