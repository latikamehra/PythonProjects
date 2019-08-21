'''
Created on Aug 20, 2019

@author: latikamehra
'''

import imageio
from imageanalysis import ExifData
from config.BasicDetails import detDict as paramsDict


def fetch(imgFileList):
    if len(imgFileList) < 1 : 
        print("No image files found in the directory.\nExiting")
        quit()
        
    print ("Fetching basic image details of all the image files ...")
    detDictDict = {}
    for imgFile in imgFileList:
        detDictDict[imgFile] = {}
        pic = imageio.imread(imgFile)
        
        exifData = ExifData.fetch(imgFile)
        
        for paramName, paramMethod in paramsDict['imgio'].items():
            detDictDict[imgFile][paramName] = paramMethod(pic)
            
        for paramName, paramMethod in paramsDict['exif'].items():
            try :
                detDictDict[imgFile][paramName] = paramMethod(exifData)
            except:
                detDictDict[imgFile][paramName] = ''
            
        
    
    return detDictDict