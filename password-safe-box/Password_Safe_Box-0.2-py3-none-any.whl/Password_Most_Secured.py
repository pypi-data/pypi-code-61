import hashlib

def Password_Most_Secured(password,salt="",hash=""):
    Password=str(password)
    Salt=str(salt)
    Hash=str(hash).lower()
    New_Password=""
    if Salt!="":
        Password=(Salt+Password+Salt).encode()
    else:
        Password=Password.encode()
    sha1=hashlib.sha1(Password).hexdigest()
    sha256=hashlib.sha256(Password).hexdigest()
    sha224=hashlib.sha224(Password).hexdigest()
    sha512=hashlib.sha512(Password).hexdigest()
    md5=hashlib.md5(Password).hexdigest()
    sha384=hashlib.sha384(Password).hexdigest()
    End1=0
    End2=0
    End3=0
    End4=0
    End5=0
    End6=0
    AtNum=0
    while True:
        if AtNum<len(sha1):
            New_Password+=sha1[AtNum]
        else:
            End1=1
        if AtNum<len(sha256):
            New_Password+=sha256[AtNum]
        else:
            End2=1
        if AtNum<len(sha224):
            New_Password+=sha224[AtNum]
        else:
            End3=1
        if AtNum<len(sha512):
            New_Password+=sha512[AtNum]
        else:
            End4=1
        if AtNum<len(md5):
            New_Password+=md5[AtNum]
        else:
            End5=1
        if AtNum<len(sha384):
            New_Password+=sha384[AtNum]
        else:
            End6=1
        if End1==1 and End2==1 and End3==1 and End4==1 and End5==1 and End6==1:
            break
        AtNum+=1
    if Hash=="sha1":
        Last_Password=hashlib.sha1(New_Password.encode()).hexdigest()
    elif Hash=="sha256":
        Last_Password=hashlib.sha256(New_Password.encode()).hexdigest()
    elif Hash=="sha224":
        Last_Password=hashlib.sha224(New_Password.encode()).hexdigest()
    elif Hash=="sha512":
        Last_Password=hashlib.sha512(New_Password.encode()).hexdigest()
    elif Hash=="md5":
        Last_Password=hashlib.md5(New_Password.encode()).hexdigest()
    elif Hash=="sha384":
        Last_Password=hashlib.sha384(New_Password.encode()).hexdigest()
    else:
        Last_Password=New_Password
    return Last_Password
