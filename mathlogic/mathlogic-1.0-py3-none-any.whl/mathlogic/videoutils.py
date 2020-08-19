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

