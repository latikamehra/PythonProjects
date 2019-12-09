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
    
    def __init__(self, imgDir, manualReview=True, pixThreshold=5, confirmLevelCount=3):

        self.imgDir = imgDir
        self.pixThreshold = pixThreshold
        self.confirmLevelCount = confirmLevelCount
        fileSuffix = "threshold_"+str(pixThreshold)
        self.manualReview  = manualReview

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
            rvw.review(self.manualReview)
            
        if 'manage' in actionList : 
            mng = ManageDuplicates.Manage(self)
            mng.manage(self.manualReview)
            
            
    def getDupeCount(self, dupeDict):
        cntr = 0
        for dupeList in dupeDict.values():
            cntr += len(dupeList)
            
        return cntr
    


if __name__ == "__main__" :

    imgDir = "/Users/latikamehra/Pictures/JonnyPics/"
    thresholds = [10]
    confirmLevelCount = 3
    manualReview = False
    dupesRemoved = 0
    rmd = [None]*len(thresholds)
    
    
    actionList = ['manage']
    actionList = ['find', 'review', 'manage']
    
    
       
    try :
        for i, threshold in enumerate(thresholds):
            rmd[i] = FindReviewManageDuplicates(imgDir, manualReview, threshold, confirmLevelCount)
            rmd[i].exec(actionList)
    except Exception as e:
        print (str(e))
        quit()
        








