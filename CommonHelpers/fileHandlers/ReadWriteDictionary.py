'''
Created on Aug 23, 2019

@author: latikamehra
'''
import json
import os
from formatters import AppLogger

class ReadWrite :

    def __init__(self, fileName):
        self.log = AppLogger.logger.getChild(__name__)
        self.fileName = fileName
        fdir = os.path.dirname(fileName)
        
        if not os.path.exists(fdir) : os.makedirs(fdir)
        
        
    def writeDict(self, datadict):
        fl = open(self.fileName, mode='w')
        
        dataJson = json.dumps(datadict, indent=4)
        
        fl.write(dataJson)
        
        fl.close()
        
        
    def readDict(self):
        try :
            fl = open(self.fileName, mode='r')
            dataJson = fl.read()
            
            dataDict = json.loads(dataJson)
            
            return dataDict
            
        except Exception as e:
            msg = "Failed to open the file "+fl+" for reading :\n"
            msg += str(type(e))+"\t:\t"+str(e)
            self.log.error()
            