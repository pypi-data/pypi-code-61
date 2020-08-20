import re

from urllib import request
from urllib.request import Request
from urllib.parse import urlencode
import json
import hashlib
import random
from multiprocessing.dummy import Pool as ThreadPool

from brotli import decompress

from textcli.utils import is_url, make_url



class Spider:

    def __init__(self,url, token, verbose = False):
        self.url = url
        self.token = token
        self.domain = 'https://textvn.com/'
        self.response = ''
        self.verbose = verbose
        self.user_agents = [
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
            'Opera/9.25 (Windows NT 5.1; U; en)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
            'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.142 Safari/535.19',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:8.0.1) Gecko/20100101 Firefox/8.0.1',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.151 Safari/535.19'
        ]
        self.content = ''

        self.hspass = False

        self.get_domain()

        self.save_url = 'https://api.rqn9.com/data/1.0/textvn/'

        self.url_key = ""

        self.pad_key = ""
        self.visit()

        if(self.url_key != "" and self.pad_key != ""):
            self.hit(self.url_key)

    
    def get_domain(self):

        pattern = r'(http[s]?://[a-zA-Z0-9]+?\.?[a-zA-Z0-9\-]+\.[a-z]{2,})'
        result = re.findall(pattern, self.url)

        if(result):
            self.domain = result[0]


    def visit(self):
            
            if(self.verbose):
                print("Visiting {}".format("textvn / " + self.url))
            
            try:
                request_obj = Request(self.domain + self.url)
                request_obj.add_header('User-Agent', self.user_agents[random.randint(0,7)])
                response_obj = request.urlopen(request_obj)

                self.headers = response_obj.getheaders()
                self.cookies = response_obj.getheader('Set-Cookie')
                self.response = response_obj.read().decode('utf-8')
                
                self.get_pad_key(self.response)
                self.get_url_key(self.response)

            except Exception as e: 
                print('Something wrong!')


    def add_headers(self, request_obj):

        request_obj.add_header('User-Agent', self.user_agents[random.randint(0,7)])
        request_obj.add_header('referer', 'https://api.rqn9.com/'+self.url_key)
        request_obj.add_header('x-requested-with', 'XMLHttpRequest')
        request_obj.add_header('accept-encoding', 'gzip, deflate, br')
        
        return request_obj


    def hit(self, url):
        data = urlencode({ "token": self.token, "slug": url })

        request_obj = Request(self.save_url, data = data.encode('utf-8'), headers = {'User-Agent': self.user_agents[random.randint(0,7)]})
        response_obj = request.urlopen(request_obj)

        try:
            check = json.loads(response_obj.read().decode('utf-8'))
            if 'message' in check:
                print("Authentication fails")
            else:
                check = check['response']

            if check is None:
                self.content = ''
            elif 'status' in check:
                self.content = ''
                if check['status'] == 'success':
                    self.content = check['message']
                elif check['status'] == 'wrong_password':
                    self.hspass = True
        except Exception as e:
            print("Something wrong!")

        return


    def get_pad_key(self, response):

        pad_key_pattern = r'(?<=pad_key = \')[a-z0-9]+'
        results = re.findall(pad_key_pattern, response)

        if(results):

            for pad_key in results:
                self.pad_key = pad_key


    def get_url_key(self, response):

        url_key_pattern = r'(?<=url_key = \')[a-z0-9]+'
        results = re.findall(url_key_pattern, response)

        if(results):

            for url_key in results:
                if(url_key):
                    self.url_key = url_key


    def save(self, dataz, password = False):
        
        data = { "token": self.token, "slug": self.url, "data": dataz }

        if password != False:
            setattr(current, 'password', password)
        data = urlencode(data)

        request_obj = Request(self.save_url, data = data.encode('utf-8'), headers = {})
        request_obj = self.add_headers(request_obj)
        response_obj = request.urlopen(request_obj)


    def unlock_pad(self, password):
        if self.hspass:
            pdata = urlencode({ "token": self.token, "slug": self.url, "password": password })

            request_obj = Request(self.save_url, data = pdata.encode('utf-8'), headers = {})
            request_obj = self.add_headers(request_obj)
            response_obj = request.urlopen(request_obj)

            return True
        else:
            return False


    def detech_change(self):
        data = urlencode({ "token": self.token, "slug": self.url })

        request_obj = Request(self.save_url, data = data.encode('utf-8'), headers = {'User-agent': self.user_agents[random.randint(0,7)]})
        response_obj = request.urlopen(request_obj)
        
        try:
            check = json.loads(response_obj.read().decode('utf-8'))['response']

            if check is None:
                self.content = ''
            elif 'status' in check:
                if check['status'] == 'success':
                    return hashlib.sha224(check['message'].encode('utf-8')).hexdigest()
                else:
                    return False
        except Exception as inst:
            return False




