'''
Created on Aug 26, 2019

@author: latikamehra
'''

from manageDuplicates import CleanupDuplicates
import time

class Manage():
    
    def __init__(self, obj):
        self.RvwdBckp = obj.RvwdBckp
        
        self.imgDir, self.toKeepDir, self.secDupesDir = obj.imgDir, obj.toKeepDir, obj.secDupesDir
        
        self.pp = obj.pp
        self.sep1 = obj.sep1
        
        self.op_summary = obj.op_summary
        
        self.getDupeCount = obj.getDupeCount
        
        self.deletedCount = 0
        
    
    def manage(self, manualReview):   
        self.reviewedDupeDict = self.RvwdBckp.readDict()
        
        if len(self.reviewedDupeDict) >= 1 :
            
            clnp = CleanupDuplicates.Cleanup(self.imgDir, self.toKeepDir, self.secDupesDir)
            
            clnp.moveDuplicates(self.reviewedDupeDict, not manualReview)
            
            time.sleep(5)
            
            clnp.moveDupesToKeepToOriginalDir(not manualReview)
            
            time.sleep(5)
            
            self.deletedCount = clnp.removeDuplicates(not manualReview)
            
        else :
            print("No reviewed duplicate files found in the directory.\nSkipping")
            #quit()
        
        self.printSummaryInfo()    
            
    def printSummaryInfo(self):
        prntStr = ""
        
        prntStr += "\n\n"
        prntStr += self.pp.cat([self.sep1])
        prntStr += self.pp.cat(["Number of duplicates removed = "+str(self.deletedCount)])
        prntStr += self.pp.cat([self.sep1])
        
        self.op_summary.info(prntStr)
        
        