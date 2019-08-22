'''
Created on Aug 20, 2019

@author: latikamehra
'''

from imageanalysis import PixelData

def fetch(potentialDupeListList, pixThreshold = 25):
    if len(potentialDupeListList) < 1 : 
        print("No potential duplicate files found in the directory.\Skipping")
        #quit()
    else:
        print ("Building a list of probable duplicate image files based on their pixel data comparison ...")
    
    probableListList = []
    
    for dupeList in potentialDupeListList :
        
        for i, file1 in enumerate(dupeList):
            probableLst = [file1]
            subLst = dupeList[(i+1):]
            
            for j, file2 in enumerate(subLst):
                
                pd = PixelData.PixelData(pixThreshold)
                eqFlag = pd.compare(file1, file2)
                
                if eqFlag == True :
                    probableLst.append(file2)
                    
                    dupeList.remove(file2)
                    
            
            if len(probableLst) > 1 :
                probableListList.append(probableLst)
                
    
    return (probableListList)
        