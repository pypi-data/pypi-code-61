"""
pyJsConsole wrapper.

© Anime no Sekai - 2020
"""

from .internal.javascript import classes as JSClass

console = JSClass._Console()
document = JSClass._Document()
history = JSClass._History()
Math = JSClass._Math()
navigator = JSClass._Navigator()
screen = JSClass._Screen()
window = JSClass._Window()
browser = JSClass.BrowserObject

'''
import threading
from lifeeasy import sleep

def reloadElements():
    global document
    global window
    lastURL = 'data:,'
    while True:
        sleep(0.1)
        try:
            if JSClass.evaluate('window.location.href') != lastURL:
                document = JSClass._Document()
                window = JSClass._Window()
                lastURL = JSClass.evaluate('window.location.href')
        except:
            break

thread = threading.Thread(target=reloadElements)
thread.daemon = True
thread.start()
'''

def newDocument():
    return JSClass._Document()

def newWindow():
    return JSClass._Window()

def newHistory():
    return JSClass._History()

def fresh():
    return (JSClass._Document(), JSClass._Window(), JSClass._History())

def clearInterval(intervalID):
    JSClass.clearInterval(intervalID)

def clearTimeout(timeoutID):
    JSClass.clearTimeout(timeoutID)

def evaluate(code_to_execute, return_value=False):
    return JSClass.evaluate(code_to_execute, return_value=return_value)

def setInterval(function, milliseconds):
    return JSClass.setInterval(function, milliseconds)

def setTimeout(function, milliseconds):
    return JSClass.setTimeout(function, milliseconds)
