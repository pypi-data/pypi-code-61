import hashlib

def Password_Fastest(password,salt="",hash=""):
    Password=str(password)
    Salt=str(salt)
    Hash=str(hash).lower()
    New_Password=""
    if Salt!="":
        Password=(Salt+Password).encode()
    else:
        Password=Password.encode()
    sha256=hashlib.sha256(Password).hexdigest()
    sha256rev=sha256[::-1]
    AtNum=0
    End1=0
    End2=0
    while True:
        if AtNum<len(sha256):
            New_Password+=sha256[AtNum]
        else:
            End1=1
        if AtNum<len(sha256rev):
            New_Password+=sha256rev[AtNum]
        else:
            End2=1
        if End1==1 and End2==1:
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
