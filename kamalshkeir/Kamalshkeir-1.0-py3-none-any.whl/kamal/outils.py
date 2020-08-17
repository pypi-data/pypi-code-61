


#################################  One Time TOKEN  ##################################################
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type

class OneTimeToken(PasswordResetTokenGenerator):
    def __make_hash_value(self, user, timestamp):
        return (text_type(user.is_active)+text_type(user.pk)+text_type(timestamp))

one_time_token = OneTimeToken()
#one_time_token_generator.make_token(user)
#one_time_token_generator.check_token(user, token)
####################################################################################################



####################################### AES TOKEN #############################################
from decouple import config
import secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import json
import base64

class AES_Token:
    def __init__(self):
        self.key = config("AES_KEY").encode()
        self.my_aes_pass = config("AES_PASS").encode()

    def AESencrypt(self,python_dict):
        nonce = secrets.token_bytes(12)
        #dict to str 
        message_obj_to_str = json.dumps(python_dict)
        #str to bytes
        message_bytes = message_obj_to_str.encode("utf-8")
        #AES encrypt
        cipherbytes = nonce + AESGCM(self.key).encrypt(nonce,message_bytes,self.my_aes_pass)
        #decode to url safe base64 and return it
        ciphertext = base64.urlsafe_b64encode(cipherbytes)
        return ciphertext.decode()

    def AESdecrypt(self,token):
        print('token = ', token)
        #decode b64 
        message_bytes = base64.urlsafe_b64decode(token)
        #decrypt
        message_bytes_decrypted =AESGCM(self.key).decrypt(message_bytes[:12], message_bytes[12:], self.my_aes_pass)
        #bytes to str
        message_str = message_bytes_decrypted.decode("utf-8")
        #str to dict
        message_obj = json.loads(message_str)
        return message_obj
aes_token = AES_Token()
#####################################################################################################



################################## TOTP TOKEN ####################################################
import pyotp
import qrcode
from qrcode.image.svg import SvgImage
from io import BytesIO
from django.http import JsonResponse



class TOTP_Token:
    def __get_qrcode_svg(self,uri):
        stream = BytesIO()
        img = qrcode.make(uri, image_factory = SvgImage)
        img.save(stream)
        return stream.getvalue().decode()

    def create_totp_token(self,user):
        key = user.profile.otp_key
        #create token
        totp = pyotp.totp.TOTP(key)
        #create uri
        totp_uri = pyotp.totp.TOTP(key).provisioning_uri(user.username,issuer_name="Souk Baalbeck")
        svg = __get_qrcode_svg(totp_uri)
        return svg

    def verify_totp_token(self,user, token):
        user_key = user.profile.otp_key
        #create token
        totp = pyotp.totp.TOTP(user_key)
        #verify if token and user match
        if token == totp.now():
            return True
        else:
            return False
totp_token = TOTP_Token()
#######################################################################################################



############################ Send an activation url to user   ##############################
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.core.mail import EmailMessage

def sendActivationUrl(request, user):
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    domain=get_current_site(request).domain
    the_aes_token = aes_token.AESencrypt({'user_id':user.pk})
    link = reverse('authentification:activate', kwargs={'token':one_time_token.make_token(user),'aes_token':the_aes_token})
    activate_url = 'http://'+domain+link

    email_subject = "Validate Your Email"
    email_body = "Hi " + user.username + ". Please use this link to verify your account\n"+activate_url
    email = EmailMessage(
        email_subject,
        email_body,
        'noreply@bookmarker.com',
        [user.email]
    )
    email.send(fail_silently=False)
#############################################################################################




################################# SMS to phone number #########################################
from twilio.rest import Client

account_sid = config('TWILIO_ACCOUNT_SID')
auth_token = config('TWILIO_AUTH_TOKEN')

def sendSMS(message_body, to_phone):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message_body,
        from_='+12085372084',
        to=to_phone
    )
    #print('-----twilio :',message.sid)
###############################################################################################





################################# Cookies ################################################
import datetime
from django.conf import settings

def set_cookie(response, key, value, days_expire = 1):
    if days_expire is None:
        #default
        max_age = 15 * 24 * 60 * 60  # 15 day
    else:
        max_age = days_expire * 24 * 60 * 60 
  
    expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
    response.set_cookie(key, value, max_age=max_age, expires=expires, domain=settings.SESSION_COOKIE_DOMAIN, secure=settings.SESSION_COOKIE_SECURE or None)
    return response
###############################################################################################




####################################### Slugify ###############################################
import re
from unicodedata import normalize

def slugify(text, delim='-'):
    result = []

    re_obj = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.:]+')
    for word in re_obj.split(text):
        word = normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8')
        word = word.replace('/', '')
        if word:
            result.append(word)
    return delim.join(result)
#############################################################################################

################################# benchmark function decorator ##############################

import cProfile, pstats, io

def benchmark(fnc):
    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        original_fnc = fnc(*args,**kwargs)
        pr.disable()
        s = io.StringIO()
        ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
        ps.print_stats()
        print('benchmark result = ', s.getvalue())
        return original_fnc
    return inner

#Utilisation : put @benchmark at any function

#############################################################################################