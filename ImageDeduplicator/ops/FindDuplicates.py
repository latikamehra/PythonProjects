'''
Created on Aug 15, 2019

@author: latikamehra
'''


import os 
from PIL import Image, ExifTags
from pprint import pprint as pps
from configs import RelevantExifTags as rets
from formatters import AppLogger, PrettyPrinter

class FindDuplicates:
    def __init__(self, dr):
        
        self.log = AppLogger.logger.getChild(__name__)
        opDir = os.path.dirname(os.path.abspath(__file__))+"/../output/"
        
        self.op_exifData = AppLogger.prntr("exifData", opDir, "CapturedExifData", consoleFlag=False)
        self.op_summary = AppLogger.prntr("summary", opDir, "ExecutionSummary", consoleFlag=True)
        
        self.opWidth = 150
        self.sep1 = "-"*self.opWidth
        self.sep2 = "="*self.opWidth
        self.pp = PrettyPrinter.PrettyPrint(self.opWidth)
        self.rootDir = dr
        self.exifHeightTag = 'ExifImageHeight'
        
        self.tagsToCollect = rets.tagList['collect']
        self.reqdTags = rets.tagList['required']
        self.compTags = rets.tagList['compare']
        
        self.imageMetatdataDict = {}
        self.notImgFiles = []
        
        self.dupeLstLst = []
        self.dupeDict = {}
        
        self.numOfDupes = 0
        
    
    def printInfo(self):
        prntStr = ""
        numOfImageFilesScanned = len(self.imageMetatdataDict)
        cntr = 0
        for dupeLst in self.dupeDict.values():
            cntr += len(dupeLst)
        
        headRow = ["Total in the given directory",
                   "Image Files Found & Scanned for Duplicates",
                   "Potential Duplicates Found"]
        dataRow = [str(len(self.allFiles)),
                   str(numOfImageFilesScanned) ,
                   str(cntr)]
        
        prntStr += self.pp.cat([self.sep2])
        prntStr += self.pp.cat_tabluar(["Number of Files"])
        prntStr += self.pp.cat([self.sep2])
        prntStr += self.pp.cat_tabluar(headRow)
        prntStr += self.pp.cat([self.sep1])
        prntStr += self.pp.cat_tabluar(dataRow)
        prntStr += self.pp.cat([self.sep2])
        
        self.op_summary.info(prntStr)
        
        self.op_exifData.info(self.pp.collectionPrnt(self.imageMetatdataDict))

        
    def fetchAllDuplicates(self):
        fls = os.listdir(self.rootDir)
        
        self.allFiles = [self.rootDir + f for f in fls]

        self.constructMetadataDict(self.allFiles)
        
        self.fetchDupeList(self.imageMetatdataDict, self.compareExifs)
        
        self.constructPrimaryAndDuplicateFileLists()
        
        self.printInfo()
        
        return (self.dupeDict)

    
    def constructMetadataDict(self,listOfFilesToBeScanned):
        excpCntr = 0
        for f in listOfFilesToBeScanned :
            try:
                im = Image.open(f)
                exf = im._getexif()
                newexif = {}

                for k,v in exf.items() :
                    tagKey = ExifTags.TAGS[k] # Change integer tag keys to actual values
                    if tagKey in self.tagsToCollect:
                        newexif[tagKey] = v
                
                  
                if set(self.reqdTags).issubset(set(newexif.keys())) :
                    self.imageMetatdataDict[f] = newexif
                else:
                    raise ValueError('Required Exif Parameters not found')
                
            except (AttributeError, OSError, IOError) as a:
                excpCntr += 1
                self.notImgFiles.append(f)
                
                msg = str(excpCntr) +") "+ str(type(a)) +" : "+ str(a)
                msg += "\nThe following file does not appear to be an image file. Ignoring it for the list of consideration\n"
                msg += f
                
                self.log.error (msg)
                
            except ValueError as v:
                excpCntr += 1
                self.notImgFiles.append(f)
                
                msg = str(excpCntr) +") "+ str(type(v)) +" : "+ str(v)
                msg += "\nThe following file does not seem to have the required Exif parameters. Ignoring it for the list of consideration\n"
                msg += f
                
                self.log.error (msg)
                
    
    def compareExifs(self,dict1, dict2):
        ret = self.compTags
        for tg in ret:
            
            if tg in dict1.keys() and tg in dict2.keys():
                if dict1[tg] != dict2[tg] : return (False)
            elif tg not in dict1.keys() and tg not in dict2.keys(): continue
            else : return(False)
        
        return (True)
     
    def constructPrimaryAndDuplicateFileLists(self):
        self.dupeDict = {}
        for flLst in self.dupeLstLst :
            self.dupeDict.update(self.orderByExifHeightWidth(flLst))
            
                
    def orderByExifHeightWidth(self,fileLst):
        fileDict = {}
        maxExfHeight = -1
        
        for fl in fileLst :
            try :
                exifHght = self.imageMetatdataDict[fl][self.exifHeightTag]
            except :
                print ("The following file does not seem to have Exif data for Height :\n"+fl)
                exit
                exifHght = 0
            
            if exifHght>maxExfHeight : 
                fileToKeep = fl
                maxExfHeight = exifHght
        
        fileLst.remove(fileToKeep)    
        fileDict[fileToKeep] = fileLst
        
        return fileDict
    
    
    def orderBySize(self,fileLst):
    
        fileLst.sort(key = os.path.getsize, reverse=True)
        return(fileLst)
                

    def fetchDupeList(self,dataDict, methodToCompareVals):
    
        keyLst = list(dataDict.keys())
        
        self.dupeLstLst = []
        
        for i, key1 in enumerate(keyLst):
            subLst = keyLst[(i+1):]
            
            dupeLst = [key1]
            
            for j, key2 in enumerate(subLst):
                
                val1 = dataDict[key1]
                val2 = dataDict[key2]
                
                eqFlag = methodToCompareVals(val1, val2)
                
                if eqFlag == True :
                    dupeLst.append(key2)
                    
                    keyLst.remove(key2)
                    
            
            if len(dupeLst) > 1 :
                self.dupeLstLst.append(dupeLst)



if __name__ == "__main__" :
    img = FindDuplicates("/Users/latikamehra/Pictures/Jonny_Updated/")
    dupeDict = img.fetchAllDuplicates()
    
    print(dupeDict)
    

    dict1 = (img.imageMetatdataDict['/Users/latikamehra/Pictures/Jonny_Updated/Jonny940.jpg'])
    
    dict2 = (img.imageMetatdataDict['/Users/latikamehra/Pictures/Jonny1/Jonny_ - 2.jpg'])
    
    pps(dict1[img.exifHeightTag])
    pps(dict2[img.exifHeightTag])
    
    print (img.compareExifs(dict1, dict2))
    
    
    
    








