'''
Created on Aug 26, 2019

@author: latikamehra
'''

from imageanalysis import ImageFileList, BasicImageDetails
from ops import ImageDetailsDataFrame, PotentialDuplicates, PrimarySecondaryDuplicates, ProbableDuplicates


class Find():
    
    def __init__(self, obj):
        self.imgDir = obj.imgDir
        self.pixThreshold = obj.pixThreshold
        
        self.getDupeCount = obj.getDupeCount
        
        self.pp = obj.pp
        self.sep1 = obj.sep1
        self.sep2 = obj.sep2
        
        self.op_summary = obj.op_summary
        self.basicDetsLog = obj.basicDetsLog
        self.potentialDupleListOP = obj.potentialDupleListOP
        
        self.DictBckp = obj.DictBckp


    def findDuplicates(self):
        
        self.numOfFilesInDir , self.imgFileList = ImageFileList.fetch(self.imgDir)
        
        self.detDictDict = BasicImageDetails.fetch(self.imgFileList)
        
        df = ImageDetailsDataFrame.construct(self.detDictDict)
        
        self.potentialDupeListList = PotentialDuplicates.fetch(df)
        
        print(self.potentialDupeListList)
        
        probableDupeListList = ProbableDuplicates.fetch(self.potentialDupeListList, self.pixThreshold)
        
        print(self.potentialDupeListList)
        
        self.probDupeDict = PrimarySecondaryDuplicates.fetchDict(probableDupeListList)
         
        self.printDupeInfo()
        
        
    def printDupeInfo(self):
        prntStr = ""
        numOfImageFilesScanned = len(self.imgFileList)
        cntr = 0
        for dupeLst in self.potentialDupeListList:
            cntr += len(dupeLst) - 1
        
        headRow = ["Total in the given directory",
                   "Image Files Scanned for Duplicates",
                   "Potential Duplicates Found",
                   "Probable Duplicates Found"]
        dataRow = [str(self.numOfFilesInDir),
                   str(numOfImageFilesScanned) ,
                   str(cntr), 
                   str(self.getDupeCount(self.probDupeDict))]
        
        prntStr += self.pp.cat([self.sep2])
        prntStr += self.pp.cat_tabluar(["Number of Files"])
        prntStr += self.pp.cat([self.sep2])
        prntStr += self.pp.cat_tabluar(headRow)
        prntStr += self.pp.cat([self.sep1])
        prntStr += self.pp.cat_tabluar(dataRow)
        prntStr += self.pp.cat([self.sep2])
        
        '''
        prntStr += "\n\n"
        prntStr += self.pp.cat([self.sep1])
        prntStr += self.pp.cat(["List of probable duplicates"])
        prntStr += self.pp.cat([self.sep1])
        prntStr += self.pp.cat([self.pp.collectionPrnt(self.probDupeDict)])
        '''
        
        self.op_summary.info(prntStr)

        self.basicDetsLog.debug(self.pp.collectionPrnt(self.detDictDict))

        self.potentialDupleListOP.debug(self.pp.collectionPrnt(self.potentialDupeListList))
        
        self.DictBckp.writeDict(self.probDupeDict)
        
    
    