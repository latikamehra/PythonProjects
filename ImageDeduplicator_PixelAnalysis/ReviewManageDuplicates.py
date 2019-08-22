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
    
    def __init__(self, imgDir, pixThreshold=25):
        self.imgDir = imgDir
        self.pixThreshold = pixThreshold
        fileSuffix = str(pixThreshold)

        self.toKeepDir = self.imgDir+"/DuplicatesToKeep"
        self.secDupesDir = self.imgDir+"/DuplicatesToRemove"
        
        curDir = os.path.dirname(os.path.abspath(__file__))
        debugDir = curDir+"/debug/"+fileSuffix+"/"
        logDir = curDir+"/logs/"+fileSuffix+"/"
        opDir = curDir+"/summary/"+fileSuffix+"/"
        
        AppLogger.initiate(logDir, "FindAndHandleDuplicates", consoleFlag=False)
        
        self.log = AppLogger.logger.getChild(__name__)
        self.basicDetsLog = AppLogger.prntr("BasicDetails"+fileSuffix, debugDir, "BasicImageDetails", consoleFlag=False)
        self.dupleListOP = AppLogger.prntr("DupeList"+fileSuffix, logDir, "ListOfPotentialDuplicates", consoleFlag=False)
        self.op_summary = AppLogger.prntr("Summary"+fileSuffix, opDir, "Summary", consoleFlag=True)
        
        self.pp = PrettyPrinter.PrettyPrint()
        self.opWidth = 150
        self.sep1 = "-"*self.opWidth
        self.sep2 = "="*self.opWidth
        
        self.dupeDict = {}
        self.potentialDupeListList = []
        self.reviewedDupeDict = {}
        self.numOfFilesInDir = 0
        self.imgFileList = []
        
        
        prntStr = "\n\n"
        prntStr += self.pp.cat([self.sep2])
        prntStr += self.pp.cat(["Threshold = "+str(threshold)])
        prntStr += self.pp.cat([self.sep2])
        
        self.op_summary.info(prntStr)
        
        
        
    def review(self):
        
        
        self.numOfFilesInDir , self.imgFileList = ImageFileList.fetch(self.imgDir)
        
        self.detDictDict = BasicImageDetails.fetch(self.imgFileList)
        
        df = ImageDetailsDataFrame.construct(self.detDictDict)
        
        self.potentialDupeListList = PotentialDuplicates.fetch(df)
        
        probableDupeListList = ProbableDuplicates.fetch(self.potentialDupeListList, self.pixThreshold)
        
        self.dupeDict = PrimarySecondaryDuplicates.fetchDict(probableDupeListList)
         
        self.printInfo1()
        
        
        
        
    def manage(self, manualReview=True):
        if len(self.dupeDict) >= 1 :
            mng = ManageDuplicates.ManageDuplicates(self.imgDir, self.toKeepDir, self.secDupesDir)
        
            dplct = DuplicatesForReview.Review(mng)
            
            if manualReview == True :
                self.reviewedDupeDict = dplct.reviewDuplicates(self.dupeDict)
            else :
                self.reviewedDupeDict = self.dupeDict
                
            self.printInfo2()
            
            dplct.moveDuplicates(self.reviewedDupeDict, ~manualReview)
            
            clnp = CleanupDuplicates.Cleanup(mng)
            
            clnp.moveDupesToKeepToOriginalDir(~manualReview)
            
            clnp.removeDuplicates(~manualReview)
            
            self.printInfo3()
            
        else :
            print("No probable duplicate files found in the directory.\nSkipping")
            #quit()
        
        

        
        
    def printInfo1(self):
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
                   str(self.numOfDuplicates(self.dupeDict))]
        
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
        
        self.dupleListOP.debug(self.pp.collectionPrnt(self.potentialDupeListList))
        
    
    def printInfo2(self):
        prntStr = ""
        
        prntStr += "\n\n"
        prntStr += self.pp.cat([self.sep1])
        prntStr += self.pp.cat(["List of reviewed duplicates"])
        prntStr += self.pp.cat([self.sep1])
        prntStr += self.pp.cat([self.pp.collectionPrnt(self.reviewedDupeDict)])
        
        
        self.op_summary.info(prntStr)
        
        
    def printInfo3(self):
        prntStr = ""
        
        prntStr += "\n\n"
        prntStr += self.pp.cat([self.sep1])
        prntStr += self.pp.cat(["Number of duplicates removed = "+str(self.numOfDuplicates(self.reviewedDupeDict))])
        prntStr += self.pp.cat([self.sep1])
        
        self.op_summary.info(prntStr)
        
    def numOfDuplicates(self, dupeDict):
        cntr = 0
        for prim, dupeList in dupeDict.items():
            cntr += len(dupeList)
            
        return cntr



if __name__ == "__main__" :

    imgDir = "/Users/latikamehra/Pictures/Jonny2/"
    thresholds = ['overview', 25, 50]
    dupesRemoved = 0
    
    for i, threshold in enumerate(thresholds):
        rmd = ReviewManageDuplicates(imgDir, threshold)
        rmd.review()
        rmd.manage()
        
        dupesRemoved += rmd.numOfDuplicates(rmd.reviewedDupeDict) 
        
    print ("Total number of duplicates removed = "+ str(dupesRemoved))








