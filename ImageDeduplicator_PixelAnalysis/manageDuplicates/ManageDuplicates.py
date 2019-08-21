'''
Created on Aug 20, 2019

@author: latikamehra
'''

from formatters import AppLogger
import os 

class ManageDuplicates:
    
    def __init__(self, origDir, toKeepDir, dupeDir):
        curDir = os.path.dirname(os.path.abspath(__file__))
        self.log = AppLogger.logger.getChild(__name__)
        
        self.bckdir = curDir+"/../config/"
        self.filemapFilename = "OriginalAndDummyFileNameMapsBackup.txt"
        self.bckupFile = AppLogger.prntr("FilenameMaps", self.bckdir, self.filemapFilename, consoleFlag=False)
        self.origDir = origDir
        self.toKeepDir = toKeepDir
        self.dupeDir = dupeDir
        
        self.origAndDummyNameDict = {}
        
        for dr in (toKeepDir,dupeDir) :
            AppLogger.createReqdDirs(dr)
            
            
    def manualConfirmation(self, confirmFlag, msg):
        if confirmFlag == True :
            print (msg)
            answr = input()
        else:
            answr = "yes"
            
        return answr
    

    