'''
Created on Aug 20, 2019

@author: latikamehra
'''

import os
from PIL.PcfFontFile import sz

def fetchDict(dupeListList):
    
    dupeDict = {}
    
    for dupeList in dupeListList:

        primFile = ""
        secFiles = []
        
        fl = dupeList[0]
        minSize = os.path.getsize(fl)
        primFile = fl
        
        for i in range(1,len(dupeList)) :
            fl = dupeList[i]
            sz = os.path.getsize(fl)
            if sz < minSize :
                minSize = sz
                primFile = fl
                
        dupeList.remove(primFile)
        
        dupeDict[primFile] = dupeList
    
    return dupeDict
    