'''
Created on Aug 20, 2019

@author: latikamehra
'''

from imageanalysis import PixelData

def fetch(potentialDupeListList, pixThreshold = 5, confirmLevelCount=3):
    pd = PixelData.PixelData(pixThreshold, confirmLevelCount)
    if len(potentialDupeListList) < 1 : 
        print("No potential duplicate files found in the directory.\Skipping")
        #quit()
    else:
        print ("Building a list of probable duplicate image files based on their pixel data comparison ...")
    
    probableListList = []
    
    #potDupeLstLst = potentialDupeListList.copy() # Make a copy of the original list so as not to change it inadvertently
    
    for dupeList in potentialDupeListList :
        
        dplst = dupeList.copy() # Make a copy of the original list so as not to change it inadvertently
        
        for i, file1 in enumerate(dplst):
            probableLst = [file1]
            subLst = dplst[(i+1):]
            
            for j, file2 in enumerate(subLst):
                
                
                eqFlag = pd.compare(file1, file2)
                
                if eqFlag == True :
                    probableLst.append(file2)
                    
                    dplst.remove(file2)
                    
            
            if len(probableLst) > 1 :
                probableListList.append(probableLst)
                
    
    return (probableListList)
        