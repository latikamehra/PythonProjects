'''
Created on Nov 6, 2019

@author: latikamehra
'''

import urllib.request
import nltk
from nltk.corpus import stopwords
import re

response =  urllib.request.urlopen('https://en.wikipedia.org/wiki/Jonny_Greenwood')
html = response.read()
#print(html)

from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'html5lib')
text = soup.get_text(strip = True)

wfl = open("./HTML_Text.txt", "w")

wfl.write(text)

cleanText = text.lower()

charsToBeRemoved = [",", "|", ".", "(", ")"]

for ctbr in charsToBeRemoved :
    cleanText = cleanText.replace(ctbr, "")




#tokens = [t for t in text.split()]

tokens = cleanText.split()

swr= stopwords.words('english')

tokensToBeRemoved = ['-','retrieved']
tokensToBeRemoved = tokensToBeRemoved+swr

print (tokensToBeRemoved)

tokens = [re.sub('retrieved(\d)+', 'retrieved', tkn) for tkn in tokens]
clean_tokens = tokens.copy()

for token in tokens:
    if token in tokensToBeRemoved:
        clean_tokens.remove(token)
        
freq = nltk.FreqDist(clean_tokens)
#print (type(freq))

#for key,val in freq.items():
    #if "retr" in key : print(str(key) + ':' + str(val))
    
freq.plot(20, cumulative=False)