import hashlib

def Password(password,salt="",method=1,hash=""):
    Password=str(password)
    Salt=str(salt)
    Hash=str(hash)
    if isinstance(method,str):
        if method=="Most_Secure":
            method=1
        else:
            method=1
    if str(salt)!="":
        Password=(Salt+Password+Salt).encode()
    if method<=1:
        sha1=hashlib.sha1(Password).hexdigest()
        sha256=hashlib.sha256(Password).hexdigest()
        sha224=hashlib.sha224(Password).hexdigest()
        sha512=hashlib.sha512(Password).hexdigest()
        End1=0
        End2=0
        End3=0
        End4=0
        AtNum=0
        New_Password=""
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
            if End1==1 and End2==1 and End3==1 and End4==1:
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
        else:
            Last_Password=New_Password
        return Last_Password
