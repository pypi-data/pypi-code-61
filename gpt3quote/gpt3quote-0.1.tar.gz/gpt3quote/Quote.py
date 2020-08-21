from bs4 import BeautifulSoup
import requests

class Quote(object):
    def __init__():
        continue

    def get(q):
        url = 'https://thoughts.sushant-kumar.com/' + q
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        return soup.find_all('p')[0].text.replace('”', '').replace('“', '')
