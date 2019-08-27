'''
Created on Aug 20, 2019

@author: latikamehra
'''

import pandas as pd
from config.BasicDetails import detDict as paramDict

def fetch(df):
    
    print ("Constructing a list of all potential duplicate image files based on their basic details ...")
    
    colsForGrpBy = paramDict['compare']

    grps = df.groupby(colsForGrpBy)
    
    dupeListList = []
    
    for detailSet, fileGrp in grps :
        if len(fileGrp)>1 :
            fls = []
            fileGrp['Image'].apply(lambda f : fls.append(f))
            
            dupeListList.append(fls)

    return dupeListList