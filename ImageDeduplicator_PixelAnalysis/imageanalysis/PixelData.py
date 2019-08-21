'''
Created on Aug 20, 2019

@author: latikamehra
'''

import imageio
import os
from config.BasicDetails import detDict as paramDict
from formatters import AppLogger as al

debugLog = al.prntr("PixelData", os.path.dirname(os.path.abspath(__file__))+"/../debug/", "PixelDataComparison", consoleFlag=False)

def forceGrayScaleToRGB(pix):
    
    if pix.size == 1 :
        pix = [pix]*3
        
    return pix
        
        

def comparePixel(pix1, pix2, threshold):
    pix1 = forceGrayScaleToRGB(pix1)
    pix2 = forceGrayScaleToRGB(pix2)
        
    for i in range(3) :
        dfrnc = abs(int(pix1[i]) - int(pix2[i]))
        if dfrnc > threshold :
            debugLog.debug (str(pix1[i])  +"\t\t"+  str(pix2[i])  +"\t\t"+ str(dfrnc))
            return False
        
    return True
            
        
    

def compare(img1, img2, threshold = 25): # Assuming height & width of the two images are same
    frmt = 'JPEG'
    
    debugLog.debug(img1+"\t::\t"+img2)
    
    pic1 = imageio.imread(img1, frmt)
    pic2 = imageio.imread(img2, frmt)
    
    height = paramDict['imgio']['Height'](pic1)
    width = paramDict['imgio']['Width'](pic1)
    
    for row in range(height) :
        for col in range(width) :
            pix1 = pic1[row, col]
            pix2 = pic2[row, col]
            comp = comparePixel(pix1, pix2 , threshold)
            if comp == False : 
                debugLog.debug("Row : "+str(row) +"\t\t"+ "Column : "+str(col))
                return False
            
    return True

