from time import *
from os import *
from webbrowser import *
admin = "用户"
while True:
    r = "雷默机器人:"
    moshi = strftime("%H:%M",localtime())
    if moshi >= "06:00"and moshi < "11:00":
        t = "早上好!"
    elif moshi >= "11:00"and moshi < "13:00":
        t = "中午好!"
    elif moshi >= "13:00" and moshi < "19:00":
        t = "下午好!"
    else:
        t = "晚上好!"
    print(t)
    print("在此键入进行聊天")
    print("------------------------")
    a = input(admin+":")
    if ("你好" in a):
        print(r+"你好，我也给你问个好！")
        print("------------------------")
    if ("hi" in a):
        print(r+"你好，我也给你问个好！")
        print("------------------------")
    if ("hello" in a):
        print(r+"你好，我也给你问个好！")
        print("------------------------")
    if ("nihao" in a):
        print(r+"你好，我也给你问个好！")
        print("------------------------")
    if ("点歌" in a):
        dg = input("歌名:")
        print(r+"歌曲链接:https://www.kugou.com/yy/html/search.html#searchType=song&searchKeyWord="+dg)
        open("https://www.kugou.com/yy/html/search.html#searchType=song&searchKeyWord="+dg)
        print("------------------------")
    if ("diange" in a):
        dg = input("歌名:")
        print(r+"歌曲链接:https://www.kugou.com/yy/html/search.html#searchType=song&searchKeyWord="+dg)
        open("https://www.kugou.com/yy/html/search.html#searchType=song&searchKeyWord="+dg)
        print("------------------------")
    if ("你是谁" in a):
        print(r+"你好，我是雷默机器人~")
        print("------------------------")
    if ("陈浩鑫" in a):
        print(r+"陈浩鑫，雷默公司旗下雷默工作室室长，我的创始人。还研发过雷默浏览器")
        print("------------------------")
    if ("修改" in a):
        c = input(r+"在这里输入你想更改的昵称:")
        admin = c
    if ("百科" in a):
        bk = input("在这里输入你想要搜索的内容:")
        print(r+"百科内容在这里:https://www.baidu.com/s?ie=UTF-8&wd="+bk)
        open("https://www.baidu.com/s?ie=UTF-8&wd="+bk)
    if ("baike" in a):
        bk = input("在这里输入你想要搜索的内容:")
        print(r+"百科内容在这里:https://www.baidu.com/s?ie=UTF-8&wd="+bk)
        open("https://www.baidu.com/s?ie=UTF-8&wd="+bk)
