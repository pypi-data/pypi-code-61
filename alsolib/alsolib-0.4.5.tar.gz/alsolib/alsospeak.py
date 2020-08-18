import requests
import time
import pygame
import json,sys
g_gender="female"
g_rate=None
g_pitch=None

#设置语音性别
def setvoicemode(gender):
    if gender != "male" and gender != "female":
        raise Exception("参数必须为male(男人)或者female(女人)")

    global g_gender
    g_gender = gender


#设置语速
def setvoicespeed(rate):
    if not isinstance(rate, int) and not isinstance(rate, float):
        raise Exception("语速设置功能参数范围为0-100")

    if rate < 0 or rate > 100:
        raise Exception("语速设置功能参数范围为0-100")

    global g_rate
    g_rate = rate/50

def gettext():
    cookies = ""
    if len(sys.argv) > 1:
        try:
            cookies = json.loads(sys.argv[1])["cookies"]
        except:
            pass
    return cookies

def jsonLoads(str):
    try:
        return json.loads(str)
    except:
        return None
#设置音高
def sethighvoice():
    global g_pitch
    g_pitch = "high"

def jsonLoads(str):
    try:
        return json.loads(str)
    except:
        return None


def speak(text):
    text = text.strip()
    if text == "":
        raise Exception("文本不能为空")

    print("爱搜语言服务正在加载中，请耐心等待...")

    global g_gender, g_rate, g_pitch
    params = {"text": text, "gender": g_gender, "rate": g_rate, "pitch": g_pitch}
    cookies = gettext()
    headers = {
        "Cookie": cookies}
    rep = requests.get("https://code.xueersi.com/api/ai/python_tts/tts", params=params, headers=headers)
    repDic = jsonLoads(rep.text)
    if repDic is None:
        raise Exception("加载超时，请稍后再试")

    if repDic["stat"] != 1:
        raise Exception(repDic["msg"])

    voiceUrl = repDic["data"]["url"]
    duration = repDic["data"]["duration"]

    # 下载语音文件
    r = requests.get(voiceUrl)
    filename = voiceUrl.split("/")[-1]
    with open(filename, "wb") as f:
        f.write(r.content)
    f.close()

    # 调用pygame播放
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    print("爱搜语言服务处理完毕！")

def makevoice(text,loadfile):
    text = text.strip()
    if text == "":
        return -1
    global g_gender, g_rate, g_pitch
    params = {"text": text, "gender": g_gender, "rate": g_rate, "pitch": g_pitch}
    headers = {"Cookie": gettext()}
    rep = requests.get("https://code.xueersi.com/api/ai/python_tts/tts", params=params, headers=headers)
    repDic = jsonLoads(rep.text)
    if repDic is None:
        return -1

    if repDic["stat"] != 1:
        raise Exception(repDic["msg"])

    voiceUrl = repDic["data"]["url"]
    duration = repDic["data"]["duration"]

    # 下载语音文件
    r = requests.get(voiceUrl)
    filename = voiceUrl.split("/")[-1]
    try:
        with open(loadfile, "wb") as f:
            f.write(r.content)
        f.close()
        return -1
    except:
        return -1