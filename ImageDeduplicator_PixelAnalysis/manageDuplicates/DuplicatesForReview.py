'''
Created on Aug 20, 2019

@author: latikamehra
'''
import os

class Review():
    
    def __init__(self, manage):
        self.manage = manage
        
    def moveAndReviewDuplicates(self, dupeDict):
        print ("Are you sure you want to move primary and secondary duplicate files to be their respective folders for review?")
        print ("The Primary files will be moved to "+self.manage.toKeepDir)
        print ("The Secondary files will be moved to "+self.manage.dupeDir)
        answr = input()
        
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