'''
Created on Aug 20, 2019

@author: latikamehra
'''

import imageio
from config.BasicDetails import detDict as paramDict

threshold = 25

def comparePixel(pix1, pix2):
    sz = pix1.size
    #print (sz)
    if sz == 1 : # Image is a grayscale
        dfrnc = abs(int(pix1) - int(pix2))
        if dfrnc > threshold : 
            #print (pix1, pix2, dfrnc)
            return False
        else : return True
    
    else :
        for i in range(sz) :
            dfrnc = abs(int(pix1[i]) - int(pix2[i]))
            if dfrnc > threshold :
                #print (pix1[i], pix2[i], dfrnc)
                return False
        
        return True
            
        
    

def compare(img1, img2): # Assuming shapes of the two images are same
    frmt = 'TIFF'
    pic1 = imageio.imread(img1)
    pic2 = imageio.imread(img2)
    
    dims = getattr(pic1, paramDict['all']['Shape'])
    
    for row in range(dims[0]) :
        for col in range(dims[1]) :
            comp = comparePixel(pic1[row, col], pic2[row, col])
            if comp == False : 
                #print ("Row : "+str(row), "Column : "+str(col))
                return False
            
    return True

