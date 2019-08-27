'''
Created on Aug 20, 2019

@author: latikamehra
'''

import imageio
import numpy as np
from config.BasicDetails import detDict as paramDict

class PixelData :
    
    def __init__(self, threshold=0, confirmLevelCount=3):
        self.threshold = threshold
        self.confirmLevelCount = confirmLevelCount

    def compare(self, img1, img2): # Assuming height & width of the two images are same
        pic1 = imageio.imread(img1)
        pic2 = imageio.imread(img2)
        
        height =  paramDict['imgio']['Height'](pic1)
        width = paramDict['imgio']['Width'](pic1)

        pic1 = self.forceGrayScaleToRGB(height, width, pic1)
        pic2 = self.forceGrayScaleToRGB(height,width, pic2)
        
        compFlag = self.compareFullPic(pic1, pic2, itern=0)
        
        return compFlag
    
    

    def forceGrayScaleToRGB(self, height, width, pic):
        lyrs = paramDict['imgio']['Layers'](pic)
        if lyrs == 1 :
            newpic = np.zeros((height,width, 3), dtype=np.int)
            
            newpic[:,:,0] = pic[:,:]
            newpic[:,:,1] = pic[:,:]
            newpic[:,:,2] = pic[:,:]
            
            pic = newpic
            
        return pic
            
   
    def compareFourHalves(self,pic1,pic2,itern=1):
        pic1 = pic1.copy()
        pic2 = pic2.copy()
        
        height =  paramDict['imgio']['Height'](pic1)
        width = paramDict['imgio']['Width'](pic1)
        
        halfHght = height//2
        halfWidth = width//2
        
        rowDict = {0:(halfHght-1), halfHght:height}
        colDict = {0:(halfWidth-1), halfWidth:width}
        
        for stRow, endRow in rowDict.items() :
            for stCol, endCol in colDict.items() :
                #print ("Starting Row = "+str(stRow), "End Row = "+str(endRow))
                #print ("Starting Column = "+str(stCol), "End Column = "+str(endCol))
                
                subpic1 = pic1[stRow:endRow, stCol:endCol]
                subpic2 = pic2[stRow:endRow, stCol:endCol]
                
                compFlag = self.compareFullPic(subpic1, subpic2, itern)
                
                if compFlag == False : return False
                
        
        return True
        
     
    def compareFullPic(self, pic1, pic2, itern=0):  
        itern = itern+1
        #print ("Iteration = "+str(itern))
        pic1 = pic1.copy()
        pic2 = pic2.copy()
        
        for c in range(3) :
            avg1 = pic1[:,:,c].mean()
            avg2 = pic2[:,:,c].mean()
            diff = abs(avg1 - avg2)
            
            #print (diff)
            if diff > self.threshold :  return False
            
        if itern<self.confirmLevelCount :
            compFlag= self.compareFourHalves(pic1, pic2, itern)
            return compFlag        
                
        return True
    
        

    
