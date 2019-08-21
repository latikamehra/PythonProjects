'''
Created on Aug 20, 2019

@author: latikamehra
'''


import os
from send2trash import send2trash

class Cleanup():
    
    def __init__(self, manage):
        self.manage = manage
    
    
    def moveDupesToKeepToOriginalDir(self, confirmFlag = True):
        print ("Moving Primary duplicates back to the original folder ...")
        
        msg = "Have you reviewed the duplicate files and their copies to be kept?"
        msg += "\nAre you sure you want to move the files to keep back to their original location?"
        
        answr = self.manage.manualConfirmation(confirmFlag, msg)
        
        if answr.lower() in ("y", "yes"):
            listOfFilesToKeep = os.listdir(self.manage.toKeepDir)
            
            for fn in listOfFilesToKeep:
                oldLoc = self.manage.toKeepDir + "/" + fn
                if fn == ".DS_Store" : newLoc = self.manage.origDir + "/" + fn
                
                else: newLoc = self.manage.origDir + "/" + self.manage.origAndDummyNameDict[fn]
                
                os.rename(oldLoc, newLoc)
             
            send2trash(self.manage.toKeepDir)   
            
        else :
            print ("Skipping the move of files to keep back to their original location")    
            
            
    
    def removeDuplicates(self, confirmFlag = True): 
        print ("Moving Secondary duplicates and review directories created to Trash ...")
        
        msg = "Have you reviewed the duplicate files and their copies to be kept?"
        msg += "\nAre you sure you want to permanently delete the secondary duplicate files?"
        msg += "\nThis action cannot be reverted and all the files from the following location would be permanently deleted : \n"+ self.manage.dupeDir
        
        answr = self.manage.manualConfirmation(confirmFlag, msg)
        
        
        if answr.lower() in ("y", "yes"):
            listOfFilesToDelete = os.listdir(self.manage.dupeDir)
            
            for fn in listOfFilesToDelete:
                fileToDel = self.manage.dupeDir + "/" + fn
                send2trash(fileToDel)
            send2trash(self.manage.dupeDir)    
            
        else :
            print ("Skipping deletion of duplicate files")
            
            