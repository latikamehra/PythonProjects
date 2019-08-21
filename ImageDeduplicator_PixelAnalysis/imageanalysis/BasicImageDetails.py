'''
Created on Aug 20, 2019

@author: latikamehra
'''

import imageio
from config.BasicDetails import detDict as paramsDict

def fetch(imgFileList):
    print ("Fetching basic image details of all the image files ...")
    detDictDict = {}
    for imgFile in imgFileList:
        detDictDict[imgFile] = {}
        pic = imageio.imread(imgFile)
        
        for paramName, paramMethod in paramsDict['fetch'].items():
            detDictDict[imgFile][paramName] = getattr(pic, paramMethod)
    
    return detDictDict