'''
Created on Aug 20, 2019

@author: latikamehra
'''

import imageio
import os
from config.BasicDetails import detDict as paramDict
from formatters import AppLogger as al
from yellowbrick.classifier import threshold
from imageanalysis import BasicImageDetails as bid

class PixelData :
    
    def __init__(self, threshold=25):
        logDir = os.path.dirname(os.path.abspath(__file__))+"/../debug/"
        logName = "PixelDataComparison_"+str(threshold)
        self.threshold = threshold
        self.debugLog = al.prntr(logName, logDir , logName, consoleFlag=False)
        self.avgDiff = 20

        
        
    def compare(self, img1, img2): # Assuming height & width of the two images are same
        compFlag = True
        
        if type(self.threshold) == int :
            if self.threshold >= 0 :
                compFlag = self.deepCompare(img1, img2)
        elif self.threshold == 'date' :
            compFlag = self.compareDate(img1, img2)
        elif self.threshold == 'avgOfLayers' :
            compFlag = self.compareAvgOfLayers(img1, img2)
        elif self.threshold == 'overview' :
            compFlag = (self.compareAvgOfLayers(img1, img2) and self.compareDate(img1, img2))
        else : # Default to full comparison with threshold = 10
            compFlag = self.deepCompare(img1, img2)
                
        return compFlag
    

        
    def forceGrayScaleToRGB(self, pix):
        if pix.size == 1 :
            pix = [pix]*3
            
        return pix
            
    
    def comparePixel(self, pix1, pix2):
        pix1 = self.forceGrayScaleToRGB(pix1)
        pix2 = self.forceGrayScaleToRGB(pix2)
            
        for i in range(3) :
            dfrnc = abs(int(pix1[i]) - int(pix2[i]))
            if dfrnc > int(self.threshold) :
                self.debugLog.debug (str(pix1[i])  +"\t\t"+  str(pix2[i])  +"\t\t"+ str(dfrnc))
                return False
            
        return True
     
    def compareDate(self, img1, img2):   
        fn = lambda img : bid.singFileFetch(img)['DateTimeOriginal'] or bid.singFileFetch(img)['DateTime']
        
        try :
            if fn(img1) == fn(img2) : return True
            else : return False
        except :
            return False

     
    def compareAvgOfLayers(self, img1, img2):     
        readImg = lambda img : imageio.imread(img)
        
        pic1 = readImg(img1)
        pic2 = readImg(img2)
        
        if pic1.ndim < 3 or pic2.ndim < 3:
            return False
        else :
            for c in range(3) :
                avg1 = pic1[:,:,c].mean()
                avg2 = pic2[:,:,c].mean()
                diff = abs(avg1 - avg2)
                if diff > self.avgDiff : 
                    return False
            
        return True
        
    def deepCompare(self, img1, img2): 
        
        self.debugLog.debug(img1+"\t::\t"+img2)
        
        pic1 = imageio.imread(img1)
        pic2 = imageio.imread(img2)
        
        height =  paramDict['imgio']['Height'](pic1)
        width = paramDict['imgio']['Width'](pic1)
        
        for row in range(height) :
            for col in range(width) :
                pix1 = pic1[row, col]
                pix2 = pic2[row, col]
                comp = self.comparePixel(pix1, pix2)
                if comp == False : 
                    self.debugLog.debug("Row : "+str(row) +"\t\t"+ "Column : "+str(col)+"\n\n")
                    return False
        
        return True
    
