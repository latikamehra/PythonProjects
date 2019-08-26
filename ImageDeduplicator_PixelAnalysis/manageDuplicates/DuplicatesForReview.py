'''
Created on Aug 20, 2019

@author: latikamehra
'''
import os
from manageDuplicates import DisplayDuplicates as dd


class Review():
    
    def __init__(self):
        self.flchk = lambda f : True if os.path.exists(f) else False
        
        self.reviewedDict = {}
        
    def reviewDuplicates(self, dupeDict):
        print ("Starting manual review of duplicates for confirmation ...")
        
        for i, (prim, dupes) in enumerate(dupeDict.items()): 
            for dupe in dupes :
                if self.flchk(prim) and self.flchk(dupe) : self.review(prim, dupe)
                
        return self.reviewedDict
    
    
    def review(self, prim, dupe, pauseTimeFactor=1):
        answr = dd.disp(prim, dupe, pauseTimeFactor)

        if answr.lower() in ("y", "yes"):
            self.reviewedDict.setdefault(prim, [])
            self.reviewedDict[prim].append(dupe)
        elif answr.lower() in ("r", "repeat"):
            self.review(prim, dupe, pauseTimeFactor=(pauseTimeFactor+1))
    
        
    