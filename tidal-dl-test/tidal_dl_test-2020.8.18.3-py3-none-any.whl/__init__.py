#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2020/08/15
@Author  :   Yaronzz
@Version :   1.0
@Contact :   yaronhuang@foxmail.com
@Desc    :   
'''
import requests
import prettytable
from aigpy.stringHelper import isNull
from aigpy.pathHelper import mkdirs
from tidal_dl.tidal import TidalAPI
from tidal_dl.settings import Settings, UserSettings
from tidal_dl.printf import Printf
from tidal_dl.download import start
from tidal_dl.enum import AudioQuality, VideoQuality

api = TidalAPI()
user = UserSettings.read()
conf = Settings.read()


def login(username="", password=""):
    while True:
        if isNull(username) or isNull(password):
            print("----------------LogIn------------------")
            username = Printf.enter("username:")
            password = Printf.enter("password:")
        msg, check = api.login(username, password, "wc8j_yBJd20zOmx0")
        if check == False:
            Printf.err(msg)
            username = ""
            password = ""
            continue
        api2 = TidalAPI()
        msg, check = api2.login(username, password, "_DSTon1kC8pABnTw")
        break
    
    user.username = username
    user.password = password
    user.userid = api.key.userId
    user.countryCode = api.key.countryCode
    user.sessionid1 = api.key.sessionId
    user.sessionid2 = api2.key.sessionId
    UserSettings.save(user)



def setAccessToken():
    while True:
        print("-------------AccessToken---------------")
        token = Printf.enter("accessToken('0' go back):")
        if token == '0':
            return
        msg, check = api.loginByAccessToken(token)
        if check == False:
            Printf.err(msg)
            continue
        if user.userid != api.key.userId:
            Printf.err("User mismatch! Please use your own accesstoken.")
            continue
        break

    user.assesstoken = token
    UserSettings.save(user)



def checkLogin():
    if not isNull(user.assesstoken):
        mag, check = api.loginByAccessToken(user.assesstoken)
        if check == False:
            Printf.err("Invaild AccessToken!Please reset.")
    if not isNull(user.sessionid1) and not api.isValidSessionID(user.userid, user.sessionid1):
        user.sessionid1 = ""
    if not isNull(user.sessionid2) and api.isValidSessionID(user.userid, user.sessionid2):
        user.sessionid2 = ""
    if isNull(user.sessionid1) or isNull(user.sessionid2):
        login(user.username, user.password)



def changeSettings():
    Printf.settings(conf)
    while True:
        choice = Printf.enter("Download path('0' not modify):")
        if choice == '0':
            choice = conf.downloadPath
        elif not mkdirs(choice):
            Printf.err('Path is error!')
            continue
        conf.downloadPath = choice
        break
    while True:
        choice = Printf.enter("Audio quailty('0'-Normal,'1'-High,'2'-HiFi,'3'-Master):")
        if choice != '1' and choice != '2' and choice != '3' and choice != '0':
            Printf.err('Input error!')
            continue
        if choice == '0':
            conf.audioQuality = AudioQuality.Normal
        if choice == '1':
            conf.audioQuality = AudioQuality.High
        if choice == '2':
            conf.audioQuality = AudioQuality.HiFi
        if choice == '3':
            conf.audioQuality = AudioQuality.Master
        break
    while True:
        choice = Printf.enter("Video quailty('0'-1080,'1'-720,'2'-480,'3'-360):")
        if choice != '1' and choice != '2' and choice != '3' and choice != '0':
            Printf.err('Input error!')
            continue
        if choice == '0':
            conf.videoQuality = VideoQuality.P1080
        if choice == '1':
            conf.videoQuality = VideoQuality.P720
        if choice == '2':
            conf.videoQuality = VideoQuality.P480
        if choice == '3':
            conf.videoQuality = VideoQuality.P360
        break
    conf.onlyM4a = Printf.enter("Convert mp4 to m4a('0'-No,'1'-Yes):") == '1'
    conf.addExplicitTag = Printf.enter("Add explicit tag to file names('0'-No,'1'-Yes):") == '1'
    conf.addHyphen = Printf.enter("Use hyphens instead of spaces in file names('0'-No,'1'-Yes):") == '1'
    conf.addYear = Printf.enter("Add year to album folder names('0'-No,'1'-Yes):") == '1'
    conf.useTrackNumber = Printf.enter("Add track number before file names('0'-No,'1'-Yes):") == '1'
    conf.checkExist = Printf.enter("Check exist file befor download track('0'-No,'1'-Yes):") == '1'
    conf.artistBeforeTitle = Printf.enter("Add artistName before track title('0'-No,'1'-Yes):") == '1'
    conf.includeEP = Printf.enter("Include singles and EPs when downloading an artist's albums('0'-No,'1'-Yes):") == '1'
    conf.addAlbumIDBeforeFolder = Printf.enter("Add id before album folder('0'-No,'1'-Yes):") == '1'
    conf.saveCovers = Printf.enter("Save covers('0'-No,'1'-Yes):") == '1'
    Settings.save(conf)


def main():
    Printf.logo()
    Printf.settings(conf)

    checkLogin()

    while True:
        Printf.choices()
        choice = Printf.enter("Enter Choice:")
        if choice == "0":
            return
        elif choice == "1":
            login()
        elif choice == "2":
            changeSettings()
        elif choice == "3":
            setAccessToken()
        else:
            start(user, conf, choice)

if __name__ == "__main__":
    main()



