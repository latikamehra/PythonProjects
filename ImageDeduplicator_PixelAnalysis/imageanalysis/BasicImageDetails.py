'''
Created on Aug 20, 2019

@author: latikamehra
'''

import imageio
from imageanalysis import ExifData
from config.BasicDetails import detDict as paramsDict


def singFileFetch(imgFile):
    detDict = {}
    pic = imageio.imread(imgFile)
    
    exifData = ExifData.fetch(imgFile)
    
    for paramName, paramMethod in paramsDict['imgio'].items():
        detDict[paramName] = paramMethod(pic)
        
    for paramName, paramMethod in paramsDict['exif'].items():
        try :
            detDict[paramName] = paramMethod(exifData)
        except:
            detDict[paramName] = None
    
    return detDict


def fetch(imgFileList):
    if len(imgFileList) < 1 : 
        print("No image files found in the directory.\Skipping")
        #return None
    else:
        print ("Fetching basic image details of all the image files ...")
        
    detDictDict = {}
    for imgFile in imgFileList:
        detDictDict[imgFile] = singFileFetch(imgFile)
            
            
    return detDictDict