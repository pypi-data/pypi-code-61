# -*- coding:utf-8 -*-
import os,platform,subprocess,threading,time,socket,json
import mitmproxy

# 启动mitmproxy服务
def start_wqrfproxy(port='8000',client_certs=''):
    # 判断系统
    if 'arwin' in platform.system() or 'inux' in platform.system():
        now_path = now_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/wqrfproxy'
        if client_certs=='':
            cmd='mitmweb -p %s -s %s/mitm_catch.py >mitm_log.txt'%(port,now_path)
        else:
            cmd='mitmweb -p %s -s %s/mitm_catch.py --set client_certs=%s >mitm_log.txt'%(port,now_path,client_certs)
    else: #windows
        if client_certs == '':
            cmd = ''
        else:
            cmd = ''
    subprocess.Popen(cmd, shell=True)
    print(u"*** 抓包断言服务已启动！mitmserver has been started! ***")
    with open('log.txt','w') as fp:
        pass
    with open('mitm_log.txt','w') as fp:
        pass
    print(u"*** 请把你的设备http代理设置成 %s:%s please configure your device's Http proxy on %s:%s ***" % (get_ip(), port,get_ip(), port))
    print(u"*** 你可以用 assert_proxy(目标url,预期字符串,请求次数) 方法来断言设备发出的请求 you can use assert_proxy(your url,your reuqest content) to assert the http request_body ***")
    print(u"*** 你也可以用 proxy_return(目标url) 方法来返回一个列表，内是所有符合的请求的请求体 you can use proxy_return(your url) to get all request body you want ***")
    print(u"*** url必须像这样 http(s)://xxxxx....，并且只能填入 '?' 之前的部分 the url must like http(s)://xxxxx.... which piece befor '?' ***")
    print(u"*** 这个预期字符串将会在url参数部分和请求体中进行查找 the request content will be found in url's params and request's body ***")
    print(u"*** 抓包过程中的日志文件可能会非常庞大,您可以用clear_log()方法来及时清理,但注意断言是需要该日志文件的,所以请在每条用例结束后调用clear_log(),如uniitest的tearDown方法内 ***")
    print(u"*** The log.txt will be very large in the process,so you can use clear_log() to free it,but it must called after the assert,better after the case,like in unittet's tearDown() ***")
    print(u"*** 你最好在你的脚本结尾写上 stop_wqrfproxy() 函数用来关闭服务 you'd better write stop_wqrfproxy() in your script's end to close the server ***")
    print(u'*** 您可以访问http://....... 来阅读使用教程和demo you can find help in http://....... ***')
    print(u'*** 您也可以发送邮件至1074321997@qq.com来获取帮助 you can also send mail to 1074321997@qq.com for help ***')
    print('*** -------------------------------------------------------------------- ***')
    time.sleep(3)


# 清除释放log.txt
def clear_log():
    with open('log.txt','w') as fp:
        pass

#  获取服务器ip：
def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


# 杀掉mitmproxy服务
def stop_wqrfproxy():
    # 判断系统
    if 'arwin' in platform.system() or 'inux' in platform.system():
        subprocess.call("ps -ef | grep mitm | grep -v grep | awk '{print $2}' | xargs kill -9",shell=True)
    else:  # windows
        ...
    print(u"*** 抓包断言服务已停止！mitmserver has been stoped! ***")

# 存放抓包数据
def catch_api(url,request_body):
    with open('log.txt','a+') as fp:
        fp.write('\n'+url+'w*q*r*f'+request_body)

# 断言-字符串检验
def assert_proxy(url='',content='',counts=1):
    with open('log.txt','r') as fp:
        requests_log = fp.readlines()
    counts_sj = 0
    for i in requests_log:
        if content in i:
            counts_sj += 1
    if counts_sj > counts:
        print(u"*** 成功找到url 但请求数量过多！实际：%s , 预期：%s ***"%(str(counts_sj),str(counts)))
    elif counts_sj < counts:
        print(u"*** 成功找到url 但请求数量过少！实际：%s , 预期：%s ***"%(str(counts_sj),str(counts)))
    else:
        print(u"*** 成功找到url 且数量正常！实际：%s , 预期：%s ***"%(str(counts_sj),str(counts)))

# 返回抓到的所有符合的请求返回体-list
def proxy_return(url=''):
    with open('log.txt','r') as fp:
        requests_log = fp.readlines()
    res = []
    for i in requests_log:
        if i != '':
            if i.split('w*q*r*f')[0] == url:
                res.append(i.split('w*q*r*f')[1])
    return res





