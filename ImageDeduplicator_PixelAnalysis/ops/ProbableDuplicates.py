'''
Created on Aug 20, 2019

@author: latikamehra
'''

from imageanalysis import PixelData

def fetch(potentialDupeListList):
    
    probableListList = []
    
    for dupeList in potentialDupeListList :
        
        for i, file1 in enumerate(dupeList):
            probableLst = [file1]
            subLst = dupeList[(i+1):]
            
            for j, file2 in enumerate(subLst):
                
                print (file1, file2)
                
                eqFlag = PixelData.compare(file1, file2)
                
                print (eqFlag)
                
                
                
                if eqFlag == True :
                    probableLst.append(file2)
                    
                    dupeList.remove(file2)
                    
            
            if len(probableLst) > 1 :
                probableListList.append(probableLst)
                
    
    return (probableListList)
        