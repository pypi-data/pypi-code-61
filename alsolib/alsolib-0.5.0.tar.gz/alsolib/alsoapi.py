from urllib import parse
import urllib,pygame
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
import json
speaker=1
ak=urllib.request.urlopen("http://www.asunc.cn/ak.txt").read().decode("utf-8")
ak=json.loads(ak)['ak']
def setvoicemode(gender):
    if gender != "boy" and gender != "girl":
        raise Exception("参数必须为boy(男人)或者girl(女人)")
    if gender=='boy':
        speaker=1
    if gender=='girl':
        speaker=5
    global g_gender
    g_gender = gender
def get_ipaddress(ip, getpoint=False):
    if ip.count(".") != 3:
        return -1
    else:
        url = 'http://api.map.baidu.com/location/ip?ak=' + ak + '&ip=' + urllib.parse.quote(ip) + '&coor=bd09ll'
        address = urllib.request.urlopen(url).read().decode("utf-8")
        if 0:
            return -1
        else:
            address = json.loads(address)
            if address['status'] == 0:
                if getpoint==True:
                    content = address['content']
                    addrpoint = content['point']
                    return content['address'], addrpoint['x'], addrpoint['y']
                else:
                    content = address['content']
                    return content['address']

            else:
                return -1
def get_traffic(road,city):
    url='http://api.map.baidu.com/traffic/v1/road?road_name='+urllib.parse.quote(road)+'&city='+urllib.parse.quote(city)+'&ak='+ak
    address = urllib.request.urlopen(url).read().decode("utf-8")
    address = json.loads(address)
    if address['status']==0:
        return address['description']
    else:
        return -1
def makevoice(text, filename):
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
    app=json.loads(urlopen("http://www.asunc.cn/ten.txt").read().decode("utf-8"))
    appid = app['appid']
    appkey = app['appkey']
    url = 'https://api.ai.qq.com/fcgi-bin/aai/aai_tts'
    time_s = int(time.time())
    m = hashlib.md5()
    m.update(str(time_s).encode("utf8"))
    nonce_s = m.hexdigest()
    nonce_s = nonce_s[0:random.randint(1, 31)]
    vmv='1'
    if filename[len(filename)-4]=='.':
        if filename[len(filename)-3]=='p' or filename[len(filename)-3]=='P':
            wmv='1'
        elif filename[len(filename)-3]=='w' or filename[len(filename)-3]=='W':
            wmv='2'
        elif filename[len(filename)-3]=='m' or filename[len(filename)-3]=='M':
            wmv='3'


    params = {'app_id': appid,
              'speaker': speaker,
              'format': wmv,
              'volume': '0',
              'speed': '100',
              'text': text,
              'aht': '0',
              'apc': '58',
              'time_stamp': time_s,
              'nonce_str': nonce_s,
              'sign': ''
              }
    params['sign'] = getReqSign(params, appkey)
    s = urlencode(params)
    res = urlopen(url, s.encode())  # 网络请求
    res_str = res.read().decode()
    res_dict = eval(res_str)

    if res_dict['ret'] == 0:
        res_data = res_dict['data']
        res_data_format = res_data['format']
        res_data_speech = res_data['speech']
        res_data_md5sum = res_data['md5sum']
        filepath = path.dirname(__file__)  # 目录
        file = '/wav01.wav'
        base64_data = res_data_speech
        ori_image_data = base64.b64decode(base64_data)
        fout = open(filename, 'wb')
        fout.write(ori_image_data)
        fout.close()
        return res_dict['ret']
    else:
        return res_dict['ret']
def speak(text):
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
    app=json.loads(urlopen("http://www.asunc.cn/ten.txt").read().decode("utf-8"))
    appid = app['appid']
    appkey = app['appkey']
    url = 'https://api.ai.qq.com/fcgi-bin/aai/aai_tts'
    time_s = int(time.time())
    m = hashlib.md5()
    m.update(str(time_s).encode("utf8"))
    nonce_s = m.hexdigest()
    nonce_s = nonce_s[0:random.randint(1, 31)]


    params = {'app_id': appid,
              'speaker': speaker,
              'format': '3',
              'volume': '0',
              'speed': '100',
              'text': text,
              'aht': '0',
              'apc': '58',
              'time_stamp': time_s,
              'nonce_str': nonce_s,
              'sign': ''
              }
    params['sign'] = getReqSign(params, appkey)
    s = urlencode(params)
    res = urlopen(url, s.encode())  # 网络请求
    res_str = res.read().decode()
    res_dict = eval(res_str)

    if res_dict['ret'] == 0:
        res_data = res_dict['data']
        res_data_format = res_data['format']
        res_data_speech = res_data['speech']
        res_data_md5sum = res_data['md5sum']
        filepath = path.dirname(__file__)  # 目录
        file = '/wav01.wav'
        base64_data = res_data_speech
        ori_image_data = base64.b64decode(base64_data)
        fout = open("alsovoice.mp3", 'wb')
        fout.write(ori_image_data)
        fout.close()
        pygame.mixer.init()
        pygame.mixer.music.load('alsovoice.mp3')
        pygame.mixer.music.play()
        return res_dict['ret']
    else:
        return res_dict['ret']
print(speak('你好'))
