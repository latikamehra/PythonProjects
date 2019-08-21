'''
Created on Aug 20, 2019

@author: latikamehra
'''
import os
from manageDuplicates import DisplayDuplicates as dd


class Review():
    
    def __init__(self, manage):
        self.manage = manage
        
        
    def reviewDuplicates(self, dupeDict):
        print ("Starting manual review of duplicates for confirmation ...")
        reviewedDict = {}
        
        for i, (prim, dupes) in enumerate(dupeDict.items()): 
            for dupe in dupes :
                answr = dd.disp(prim, dupe)

                if answr.lower() in ("y", "yes"):
                    reviewedDict.setdefault(prim, [])
                    reviewedDict[prim].append(dupe)
                
        return reviewedDict
        
        
        
    def moveDuplicates(self, dupeDict, confirmFlag = True):
        print ("Moving Primary & Secondary duplicates to their review folders for final confirmation ...")
        
        msg = "Are you sure you want to move primary and secondary duplicate files to be their respective folders for review?"
        msg += "\nThe Primary files will be moved to "+self.manage.toKeepDir
        msg += "\nThe Secondary files will be moved to "+self.manage.dupeDir
        
        answr = self.manage.manualConfirmation(confirmFlag, msg)
        
        if answr.lower() in ("y", "yes"):
        
            for i, (prim, dupes) in enumerate(dupeDict.items()):
                
                primBaseName = os.path.basename(prim)
                dummyPrimeName = "PrimeCopy_"+str(i)+".jpg"
                oldLoc = prim 
                newLoc = self.manage.toKeepDir + "/" + dummyPrimeName
                
                self.manage.origAndDummyNameDict[dummyPrimeName] = primBaseName
                
                
                os.rename(oldLoc, newLoc)
                
                for j, d in enumerate(dupes):
                    secBaseName = os.path.basename(d)
                    dummysecName = "SecondaryCopy_"+str(i)+"_"+str(j)+".jpg"
                    oldLoc = d 
                    newLoc = self.manage.dupeDir + "/" + dummysecName
                    
                    self.manage.origAndDummyNameDict[dummysecName] = secBaseName
                    
                    os.rename(oldLoc, newLoc)
                    
        self.manage.bckupFile.info(str(self.manage.origAndDummyNameDict))