'''
Created on Jan 7, 2020

@author: latikamehra
'''

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def webCrawl(urlLink, keywrd, maxLevels, level=0):
    if level < maxLevels :
        try :
            print (urlLink)
            sch = urlparse(urlLink).scheme
            dom = urlparse(urlLink).netloc
            baseDomain = sch + "://" + dom
            
            resp = requests.get(urlLink)
            
            respText = resp.text
            
            htmlResp = BeautifulSoup(respText, "html.parser")
            
            if keywrd.lower() in respText.lower() : 
                msg = "<SUCCESS> Keyword "+ keywrd + " found on webpage : '"+urlLink+"'"
                return (True, msg)
            
            else :
            
                for linkTag in htmlResp.findAll('a', href=True, title=True) :
                    link = linkTag.get("href")
                    
                    if link[0] == "/" :
                        link =  baseDomain + link
                        
                    suc, msg = webCrawl(link, keywrd, maxLevels, level+1)
                    if suc :
                        return (suc, msg)
                    
            
            msg = "<FAILED> Keyword "+ keywrd + " not found under webpage : '"+urlLink+"'"    
            return (False, msg)
        
        except Exception as e :
            msg = "<FAILED> urlLink '"+ urlLink + "' could not be accessed and gave the following error : "+str(e)    
            return (False, msg)
    else :        
        msg = "<FAILED> Keyword "+ keywrd + " not found yet"    
        return (False, msg)   
        
        
        
urlLink =  "https://en.wikipedia.org/wiki/Jonny_Greenwood" 
#urlLink = "https://en.wikipedia.org/wiki/BBC_Concert_Orchestra"
keywrd = "camden"   
print ("Crawling the following web pages looking for keyword '"+keywrd+"'")

flag, msg = webCrawl(urlLink, keywrd, 2)

print (msg)
                  
                    
                    
                    
            
            
            
            
    
    
