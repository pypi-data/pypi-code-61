def url2img(url):
    import numpy as np
    import urllib.request
    import cv2
    resp=urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()),dtype="uint8")
    image = cv2.imdecode(image,cv2.IMREAD_COLOR)
    return image

#displaying image
def imshow(img,figsize=(6.4,4.8),flip=True):
    import cv2
    import matplotlib.pyplot as plt
    if len(img.shape) == 3:
        if img.shape[2]==3:
            if flip:
                imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                plt.figure(figsize=figsize)
                plt.imshow(imgrgb)
            else:
                plt.figure(figsize=figsize)
                plt.imshow(img)
    else:
        plt.figure(figsize=figsize)
        plt.imshow(img,cmap='gray')
    plt.show()
    return None

import os
import getpass
import cv2
import skvideo.io
from matplotlib import pyplot as plt
#create directory for user
def getOrCreateUserDirectory():
    homepath="/var/www/html/common/"
    username = getpass.getuser()
    directory = homepath+username
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

#writing video
def vwriter(filename,defaultextn=".ogv"):
    if filename[0]=="/":
        print("File path is not supported. Only specify name. File extension optional. Only Limited file extentions supported.")
    extn = os.path.splitext(filename)[1]
    filename= os.path.splitext(filename)[0]
    if extn == '':
        extn = defaultextn
    if (extn == ".ogv") or (extn == ".mp4"):
        fullpath = os.path.join(getOrCreateUserDirectory(),filename+extn)
        if extn == ".ogv":
            print("Writing to File "+fullpath)
            return skvideo.io.FFmpegWriter(fullpath,outputdict={'-vcodec':'libtheora'})
        else:
            print("Writing to File "+fullpath)
            return skvideo.io.FFmpegWriter(fullpath)
    else:
        print(str(extn) + " is not suppoted")
        return None

import random
import string

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def vshow(file,width=320,height=240,defaultextn=".ogv"):
    from IPython.display import HTML
    import getpass, os, subprocess
    extn= os.path.splitext(file)[1]
    filename= os.path.splitext(file)[0]
    randomfilename = randomString(20)
    a=subprocess.call(["cp",file,"/var/www/html/common/"+randomfilename+extn],shell=True)
    if extn == '':
        extn = defaultextn
    if filename[0]=="/":
        if filename[0:19]=='/data/video/common/':
            serverfile=os.path.join("https://training.fnmathlogic.com/common",randomfilename+extn)
        else:
            serverfile=os.path.join("https://training.fnmathlogic.com/common","randomname.mp4")
    else:
        if (filename[0:7] == "http://")  or (filename[0:8] == 'https://'):
            serverfile = filename+extn
            return HTML('''<iframe src="'''+file+'''">''')
        else:
            serverfile=os.path.join("http://training.fnmathlogic.com/common",getpass.getuser(),filename+extn)
    if (extn == ".ogv") or (extn == ".mp4"):
        p1 = '''<video width='''+str(width)+''' height='''+str(height)+''' controls>'''
        p2 = '''<source src="'''+serverfile
        p3 = '''" type="video/mp4"></video>'''
        return HTML(data=p1+p2+p3)
    else:
        print(str(extn) + " is not suppoted")

