'''
Created on Aug 20, 2019

@author: latikamehra
'''

import pandas as pd
from config.BasicDetails import detDict as paramDict

def construct(detDictDict):
    cols=paramDict['all'].keys()
    
    df = pd.DataFrame(columns = cols)
    
    for fileName, dets in detDictDict.items():
        rowDict = {}
        rowDict['Image'] = fileName
        
        for k, v in dets.items():
            rowDict[k] = v
            
        df = df.append(rowDict, ignore_index=True)
        
    return df
    
    