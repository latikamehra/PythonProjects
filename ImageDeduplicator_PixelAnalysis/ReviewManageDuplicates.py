'''
Created on Aug 20, 2019

@author: latikamehra
'''

from formatters import AppLogger, PrettyPrinter
import os
from imageanalysis import ImageFileList, BasicImageDetails
from ops import ImageDetailsDataFrame, PotentialDuplicates, PrimarySecondaryDuplicates, ProbableDuplicates
from manageDuplicates import CleanupDuplicates, ManageDuplicates, DuplicatesForReview


class ReviewManageDuplicates():
    
    def __init__(self, imgDir):

        self.imgDir = imgDir
        
        self.toKeepDir = self.imgDir+"/DuplicatesToKeep"
        self.secDupesDir = self.imgDir+"/DuplicatesToRemove"
        
        curDir = os.path.dirname(os.path.abspath(__file__))
        debugDir = curDir+"/debug/"
        logDir = curDir+"/logs/"
        opDir = curDir+"/output/"
        
        AppLogger.initiate(logDir, "FindAndHandleDuplicates", consoleFlag=False)
        self.log = AppLogger.logger.getChild(__name__)
            
        self.basicDetsLog = AppLogger.prntr("BasicDetails", debugDir, "BasicImageDetails", consoleFlag=False)
        self.dupleListOP = AppLogger.prntr("DupeList", opDir, "ListOfPotentialDuplicates", consoleFlag=False)
        self.op_summary = AppLogger.prntr("Summary", opDir, "Summary", consoleFlag=True)
        
        self.pp = PrettyPrinter.PrettyPrint()
        self.opWidth = 150
        self.sep1 = "-"*self.opWidth
        self.sep2 = "="*self.opWidth
        
        self.dupeDict = {}
        self.reviewedDupeDict = {}
        self.numOfFilesInDir = 0
        self.imgFileList = []
        
        
        
    def review(self):
        
        
        self.numOfFilesInDir , self.imgFileList = ImageFileList.fetch(self.imgDir)
        
        self.detDictDict = BasicImageDetails.fetch(self.imgFileList)
        
        df = ImageDetailsDataFrame.construct(self.detDictDict)
        
        potentialDupeListList = PotentialDuplicates.fetch(df)
        
        probableDupeListList = ProbableDuplicates.fetch(potentialDupeListList)
        
        self.dupeDict = PrimarySecondaryDuplicates.fetchDict(probableDupeListList)
        
        self.printInfo1()
        
        
    def manage(self, manualReview=True):
        
        mng = ManageDuplicates.ManageDuplicates(self.imgDir, self.toKeepDir, self.secDupesDir)
        
        dplct = DuplicatesForReview.Review(mng)
        
        if manualReview == True :
        
            self.reviewedDupeDict = dplct.reviewDuplicates(self.dupeDict)
        else :
            self.reviewedDupeDict = self.dupeDict
            
        self.printInfo2()
        
        dplct.moveDuplicates(self.reviewedDupeDict)
        
        clnp = CleanupDuplicates.Cleanup(mng)
        
        clnp.moveDupesToKeepToOriginalDir()
        
        clnp.removeDuplicates()
        
        

        
        
    def printInfo1(self):
        prntStr = ""
        numOfImageFilesScanned = len(self.imgFileList)
        cntr = 0
        for dupeLst in self.dupeDict.values():
            cntr += len(dupeLst)
        
        headRow = ["Total in the given directory",
                   "Image Files Found & Scanned for Duplicates",
                   "Potential Duplicates Found"]
        dataRow = [str(self.numOfFilesInDir),
                   str(numOfImageFilesScanned) ,
                   str(cntr)]
        
        prntStr += self.pp.cat([self.sep2])
        prntStr += self.pp.cat_tabluar(["Number of Files"])
        prntStr += self.pp.cat([self.sep2])
        prntStr += self.pp.cat_tabluar(headRow)
        prntStr += self.pp.cat([self.sep1])
        prntStr += self.pp.cat_tabluar(dataRow)
        prntStr += self.pp.cat([self.sep2])
        
        prntStr += "\n\n"
        prntStr += self.pp.cat([self.sep1])
        prntStr += self.pp.cat(["List of probable duplicates"])
        prntStr += self.pp.cat([self.sep1])
        prntStr += self.pp.cat([self.pp.collectionPrnt(self.dupeDict)])
        
        self.op_summary.info(prntStr)

        self.basicDetsLog.debug(self.pp.collectionPrnt(self.detDictDict))
        
        self.dupleListOP.debug(self.pp.collectionPrnt(self.dupeDict))
        
    
    def printInfo2(self):
        prntStr = ""
        
        prntStr += "\n\n"
        prntStr += self.pp.cat([self.sep1])
        prntStr += self.pp.cat(["List of reviewed duplicates"])
        prntStr += self.pp.cat([self.sep1])
        prntStr += self.pp.cat([self.pp.collectionPrnt(self.reviewedDupeDict)])
        
        self.op_summary.info(prntStr)
        
    



if __name__ == "__main__" :

    imgDir = "/Users/latikamehra/Pictures/Jonny1/"
    
    rmd = ReviewManageDuplicates(imgDir)
    rmd.review()
    rmd.manage()








