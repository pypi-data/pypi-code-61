from urllib import parse
import urllib,pygame,os
import contextlib
import wave
import urllib.request
import requests,json
import time
from os import path
from urllib.request import urlopen
from urllib.parse import urlencode
from urllib.parse import quote_plus
import hashlib
import random
import base64
import json,time
from alsolib.alsoapi import*
def AI_chat(text,is_speak=False,mode=5):
    def getReqSign(params, key):
        dict_kl = sorted(params)
        s = ''
        for k in dict_kl:
            v = params[k]
            if v != '':
                v0 = str(quote_plus(str(v)))
                s = s + k + '=' + v0 + '&'
        s = s + 'app_key=' + key;
        m = hashlib.md5()
        m.update(s.encode("utf8"))
        sign = m.hexdigest()
        sign = sign.upper()
        return sign

    appid = '2155982863'
    appkey = 'l5Q4dvIXbdfoKE31'
    url = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat'
    time_s = int(time.time())
    m = hashlib.md5()
    m.update(str(time_s).encode("utf8"))
    nonce_s = m.hexdigest()
    nonce_s = nonce_s[0:random.randint(1, 31)]
    params = {'app_id': appid,
              'time_stamp': time_s,
              'nonce_str': nonce_s,
              'session': '0',
              'sign': '',
              'question': text
              }
    params['sign'] = getReqSign(params, appkey)
    s = urlencode(params)
    res = urlopen(url, s.encode())  # 网络请求
    res_str = res.read().decode()
    res_dict = eval(res_str)
    if res_dict['ret']==0:
        if is_speak==True:
            if speak(res_dict['data']['answer'],mode)!=0:
                return -1
            else:
                return 0
        else:
            return 0,res_dict['data']['answer']
    else:
        if res_dict['ret'] == 16394:
            return 404