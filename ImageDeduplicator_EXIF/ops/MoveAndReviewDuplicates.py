'''
Created on Aug 16, 2019

@author: latikamehra
'''
from formatters import AppLogger
import os 
from send2trash import send2trash

class MoveAndReview:
    
    def __init__(self, origDir, toKeepDir, dupeDir):
        curDir = os.path.dirname(os.path.abspath(__file__))
        self.log = AppLogger.logger.getChild(__name__)
        
        self.bckdir = curDir+"/../configs/"
        self.filemapFilename = "OriginalAndDummyFileNameMapsBackup.txt"
        self.bckupFile = AppLogger.prntr("FilenameMaps", self.bckdir, self.filemapFilename, consoleFlag=False)
        self.origDir = origDir
        self.toKeepDir = toKeepDir
        self.dupeDir = dupeDir
        
        self.origAndDummyNameDict = {}
        
        for dr in (toKeepDir,dupeDir) :
            AppLogger.createReqdDirs(dr)
            
    def moveAndReviewDuplicates(self, dupeDict):
        print ("Are you sure you want to move primary and secondary duplicate files to be their respective folders for review?")
        print ("The Primary files will be moved to "+self.toKeepDir)
        print ("The Secondary files will be moved to "+self.dupeDir)
        answr = input()
        
        if answr.lower() in ("y", "yes"):
        
            for i, (prim, dupes) in enumerate(dupeDict.items()):
                primBaseName = os.path.basename(prim)
                dummyPrimeName = "PrimeCopy_"+str(i)+".jpg"
                oldLoc = prim 
                newLoc = self.toKeepDir + "/" + dummyPrimeName
                
                self.origAndDummyNameDict[dummyPrimeName] = primBaseName
                
                
                os.rename(oldLoc, newLoc)
                
                for j, d in enumerate(dupes):
                    secBaseName = os.path.basename(d)
                    dummysecName = "SecondaryCopy_"+str(i)+"_"+str(j)+".jpg"
                    oldLoc = d 
                    newLoc = self.dupeDir + "/" + dummysecName
                    
                    self.origAndDummyNameDict[dummysecName] = secBaseName
                    
                    os.rename(oldLoc, newLoc)
                    
        self.bckupFile.info(str(self.origAndDummyNameDict))
        
      
                
    
    def moveDupesToKeepToOriginalDir(self):
        print ("Have you reviewed the duplicate files and their copies to be kept?")
        print ("Are you sure you want to move the files to keep back to their original location?")
        answr = input()
        
        if answr.lower() in ("y", "yes"):
            listOfFilesToKeep = os.listdir(self.toKeepDir)
            
            for fn in listOfFilesToKeep:
                oldLoc = self.toKeepDir + "/" + fn
                if fn == ".DS_Store" : newLoc = self.origDir + "/" + fn
                
                else: newLoc = self.origDir + "/" + self.origAndDummyNameDict[fn]
                
                os.rename(oldLoc, newLoc)
             
            send2trash(self.toKeepDir)   
            
        else :
            print ("Skipping the move of files to keep back to their original location")    
            
            
    
    def removeDuplicates(self): 
        print ("Have you reviewed the duplicate files and their copies to be kept?")
        print ("Are you sure you want to permanently delete the secondary duplicate files?")
        print ("This action cannot be reverted and all the files from the following location would be permanently deleted : \n"+ self.dupeDir)
        answr = input()
        
        if answr.lower() in ("y", "yes"):
            listOfFilesToDelete = os.listdir(self.dupeDir)
            
            for fn in listOfFilesToDelete:
                fileToDel = self.dupeDir + "/" + fn
                send2trash(fileToDel)
            send2trash(self.dupeDir)    
            
        else :
            print ("Skipping deletion of duplicate files")
    
             
                     
            
