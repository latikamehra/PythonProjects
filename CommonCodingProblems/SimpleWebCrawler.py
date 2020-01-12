'''
Created on Jan 6, 2020

@author: latikamehra
'''

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def web(page,WebUrl):
    if(page>0):
        url = WebUrl
        domain = urlparse(url).scheme + "://" + urlparse(url).netloc
        code = requests.get(url)
        plain = code.text
        #print (code.status_code)
        #print (code.url)
        s = BeautifulSoup(plain, "html.parser")
        
        
        for link in s.findAll('a', href=True, title=True)[0:5] :
            ttl = link.get('title')
            href = link.get('href')
            if href[0] == "/" :
                href = domain + href
            print(ttl, " : " ,href)
            web(page-1,href)



url = "https://upload.wikimedia.org/wikipedia/commons/c/ce/Jonny_Greenwood.jpg"
web(2, url)


