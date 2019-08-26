'''
Created on Aug 20, 2019

@author: latikamehra
'''

from fileHandlers import ReadWriteDictionary
from formatters import AppLogger, PrettyPrinter
import os
import logging
from execs import FindDuplicates, ReviewDuplicates, ManageDuplicates


class FindReviewManageDuplicates():
    
    def __init__(self, imgDir, pixThreshold=25):

        self.imgDir = imgDir
        self.pixThreshold = pixThreshold
        fileSuffix = "threshold_"+str(pixThreshold)

        self.toKeepDir = self.imgDir+"/DuplicatesToKeep/"
        self.secDupesDir = self.imgDir+"/DuplicatesToRemove/"
        
        curDir = os.path.dirname(os.path.abspath(__file__))
        opDir = curDir+"/logsAndOutput/"
        logDir = opDir+"/logs/"
        debugDir = opDir+"/debug/"
        #debugDir = opDir+"/"+fileSuffix+"/debug/"
        #logDir = opDir+"/"+fileSuffix+"/logs/"
        resDir = opDir+"/"+fileSuffix+"/results/"
        sumDir = opDir+"/"+fileSuffix+"/summary/"
        
        AppLogger.initiate(logDir, "FindAndHandleDuplicates", consoleFlag=False, lvl=logging.DEBUG)
        
        self.basicDetsLog = AppLogger.prntr("BasicDetails"+fileSuffix, debugDir, "BasicImageDetails", consoleFlag=False)
        self.potentialDupleListOP = AppLogger.prntr("PotentialDupeList"+fileSuffix, debugDir, "PotentialDuplicates", consoleFlag=False)
        self.op_summary = AppLogger.prntr("Summary"+fileSuffix, sumDir, "Summary", consoleFlag=True)
        
        opWidth = 150
        self.pp = PrettyPrinter.PrettyPrint(opWidth=opWidth)
        self.sep1 = "-"*opWidth
        self.sep2 = "="*opWidth
        
        
        probableDupleListOP = resDir+"ProbableDuplicates"+".json"
        reviewedDupeDictOP = resDir+"ReviewedDuplicates"+".json"
        
        self.DictBckp = ReadWriteDictionary.ReadWrite(probableDupleListOP)
        self.RvwdBckp = ReadWriteDictionary.ReadWrite(reviewedDupeDictOP)

        
        prntStr = "\n\n"
        prntStr += self.pp.cat([self.sep2])
        prntStr += self.pp.cat(["Threshold = "+str(threshold)])
        prntStr += self.pp.cat([self.sep2])
        
        self.op_summary.info(prntStr)
        
    
    def exec(self, actionList=['find', 'review', 'manage']):
        if 'find' in actionList : 
            fnd = FindDuplicates.Find(self)
            fnd.findDuplicates()
            
        if 'review' in actionList : 
            rvw = ReviewDuplicates.Review(self)
            rvw.review(manualReview=True)
            
        if 'manage' in actionList : 
            mng = ManageDuplicates.Manage(self)
            mng.manage(manualReview=True)
            
            
    def getDupeCount(self, dupeDict):
        cntr = 0
        for dupeList in dupeDict.values():
            cntr += len(dupeList)
            
        return cntr
    


'''
    def findDuplicates(self):
        
        self.numOfFilesInDir , self.imgFileList = ImageFileList.fetch(self.imgDir)
        
        self.detDictDict = BasicImageDetails.fetch(self.imgFileList)
        
        df = ImageDetailsDataFrame.construct(self.detDictDict)
        
        self.potentialDupeListList = PotentialDuplicates.fetch(df)
        
        probableDupeListList = ProbableDuplicates.fetch(self.potentialDupeListList, self.pixThreshold)
        
        self.dupeDict = PrimarySecondaryDuplicates.fetchDict(probableDupeListList)
         
        self.printDupeInfo()
        
               
        
    def review(self, manualReview):
        probDict = self.DictBckp.readDict()
        
        if len(probDict) >= 1 :
        
            dplct = DuplicatesForReview.Review()
            
            if manualReview == True :
                self.reviewedDupeDict = dplct.reviewDuplicates(probDict)
            else :
                self.reviewedDupeDict = probDict
                
            self.printReviewInfo()
            
        else :
            print("No probable duplicate files found in the directory.\nSkipping")
            #quit()
     
    
    def manage(self, mng, manualReview):   
        rvwdDict = self.RvwdBckp.readDict()
        
        if len(rvwdDict) >= 1 :
            
            clnp = CleanupDuplicates.Cleanup(self.imgDir, self.toKeepDir, self.secDupesDir)
            
            clnp.moveDuplicates(self.reviewedDupeDict, ~manualReview)
            
            clnp.moveDupesToKeepToOriginalDir(~manualReview)
            
            clnp.removeDuplicates(~manualReview)
            
            self.printSummaryInfo()
            
        else :
            print("No reviewed duplicate files found in the directory.\nSkipping")
            #quit()
        
        
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
        
        self.potentialDupleListOP.debug(self.pp.collectionPrnt(self.potentialDupeListList))
        
        self.DictBckp.writeDict(self.dupeDict)
        
    
    def printReviewInfo(self):
        prntStr = ""
        
        prntStr += "\n\n"
        prntStr += self.pp.cat([self.sep1])
        prntStr += self.pp.cat(["List of reviewed duplicates"])
        prntStr += self.pp.cat([self.sep1])
        prntStr += self.pp.cat([self.pp.collectionPrnt(self.reviewedDupeDict)])
        
        
        self.op_summary.info(prntStr)
        self.RvwdBckp.writeDict(self.reviewedDupeDict)
        
        
    def printSummaryInfo(self):
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

'''

if __name__ == "__main__" :

    imgDir = "/Users/latikamehra/Pictures/Jonny2/"
    thresholds = ['overview', 25, 50]
    dupesRemoved = 0
    rmd = [None]*len(thresholds)
    
    actionList = ['find', 'review']
    
    try :
        for i, threshold in enumerate(thresholds):
            rmd[i] = FindReviewManageDuplicates(imgDir, threshold)
            rmd[i].exec(actionList)
    except Exception as e:
        print (str(e))
        #rd = input()
        quit()
        








