'''
Created on Aug 20, 2019

@author: latikamehra
'''

import pandas as pd
from config.BasicDetails import detDict as paramDict

def fetch(df):
    
    colsForGrpBy = list(paramDict['fetch'].keys())

    grps = df.groupby(colsForGrpBy)
    
    dupeListList = []
    
    for detailSet, fileGrp in grps :
        if len(fileGrp)>1 :
            fls = []
            fileGrp['Image'].apply(lambda f : fls.append(f))
            
            dupeListList.append(fls)
            
    return dupeListList